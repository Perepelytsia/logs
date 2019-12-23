import pymysql
import sys
import os
import datetime
import re
from Parser import Parser
import paramiko
import importlib

try:
	if len(sys.argv) >= 2:
		settings = importlib.import_module(sys.argv[1])
		con = pymysql.connect(user=settings.DB_USER, password=settings.DB_PASS, db=settings.DB_NAME)
		ssh = paramiko.SSHClient()
		ssh.load_system_host_keys()
		ssh.connect(hostname=settings.SSH_HOST, port=settings.SSH_PORT, username=settings.SSH_USER)
		os.system("scp -P "+ settings.SSH_PORT + " " + settings.SSH_USER +"@"+settings.SSH_HOST +":"+ settings.R_PATH +" "+os.getcwd()+ "/error_php/phperror.log")
		ssh.exec_command('echo "">'+settings.R_PATH)
		with open(os.getcwd()+"/error_php/phperror.log", 'r') as reader:
			lines      = reader.readlines()
			item       = None
			data       = list()
			savePost   = False;
			saveTrace  = False;
			for line in lines:

				day = re.match(r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\]', line)
				if day:
					if item:
						# save data from object
						data.append(item.getData())
					# create object
					request = re.match(r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\] REQUEST:', line)
					item = Parser(day.group(), line[request.end():])

				if item:
					post = re.search(r'POST: Array', line)
					if saveTrace and len(line) > 5:
						item.addTrace(line)
						saveTrace  = False;
					if savePost:
						if len(line) == 1:
							savePost  = False
							saveTrace = True
						else:
							item.addPost(line)
					if post:
						savePost = True
		reader.close()
		# save data from last object
		if item:
			data.append(item.getData())
		with con:
			cur = con.cursor()
			for value in data:
				sql = "INSERT INTO "+ settings.DB_TBL +" (`day`, `request`, `post`, `trace`) VALUES (%s, %s, %s, %s)"
				cur.execute(sql, (value[0], value[1], value[2], value[3]))
		ssh.close()
	else:
		print("The script demands a name of a settings file. Example: `python3 get_logs.py config`")
		print("The setting file should have:")
		print("DB_USER\nDB_PASS\nDB_NAME\nDB_TBL\nSSH_HOST\nSSH_USER\nSSH_PORT\nR_PATH")
except:
	print("Unexpected error:", sys.exc_info()[1])
	print("Unexpected error:", sys.exc_info()[2].tb_lineno)
