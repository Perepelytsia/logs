import pymysql
import sys
import os
import datetime
import re
from Parser import Parser
import paramiko
import importlib

print("Run " + os.getcwd() +"/"+ sys.argv[0])
try:
	if len(sys.argv) >= 2:
		settings = importlib.import_module(sys.argv[1])

		con = pymysql.connect(user=settings.DB_USER, password=settings.DB_PASS, db=settings.DB_NAME)
		ssh = paramiko.SSHClient()
		ssh.load_system_host_keys()
		ssh.connect(hostname=settings.SSH_HOST, port=settings.SSH_PORT, username=settings.SSH_USER)

		for fileName in ['error-fatal-api', 'error-fatal-game', 'error-fatal-system', 'error-game', 'error-api']:

			remoteFile = settings.R_PATH + fileName + '.log'
			os.system("scp -P "+ settings.SSH_PORT + " " + settings.SSH_USER +"@"+settings.SSH_HOST +":"+ remoteFile +" "+ os.getcwd() + "/error_yii2/" + fileName + ".log")
			ssh.exec_command('echo "">'+remoteFile)

			with open(os.getcwd()+"/error_yii2/" + fileName + ".log", 'r') as reader:
				lines      = reader.readlines()
				pieceStack = None
				item       = None
				data       = list()
				for line in lines:

					day = re.match(r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\]', line)
					if day:
						if item:
							item.addStack(pieceStack)
							# save data from object
							data.append(item.getData())
						# create object
						item = Parser(day.group())
						pieceStack = None

					if item:
						code = re.search(r'\[code\] =>', line)
						if code:
							item.addCode(line[1+code.end():-1])
						message = re.search(r'\[message\] =>', line)
						if message:
							item.addMessage(line[1+message.end():-1])
						trace = re.search(r'\[trace\] =>', line)
						if trace:
							item.addTrace(line[1+trace.end():-1])
						if pieceStack:
							pieceStack += line
						stack = re.search(r'Stack trace:', line)
						if stack and pieceStack == None:
							pieceStack = ':'
			reader.close()
			# save data from last object
			if item:
				item.addStack(pieceStack)
				data.append(item.getData())
			with con:
				cur = con.cursor()
				for value in data:
					sql = "INSERT INTO "+ settings.DB_TBL +" (`day`, `code`, `msg`, `trace`, `stack`, `type`) VALUES (%s, %s, %s, %s, %s, %s)"
					cur.execute(sql, (value[0], value[1], value[2], value[3], value[4], fileName))
		ssh.close()

	else:
		print("The script demands a name of a settings file. Example: `python3 get_logs.py config`")
		print("The setting file should have:")
		print("DB_USER\nDB_PASS\nDB_NAME\nDB_TBL\nSSH_HOST\nSSH_USER\nSSH_PORT\nR_PATH")
except:
	print("Unexpected error:", sys.exc_info()[1])
	print("Unexpected error:", sys.exc_info()[2].tb_lineno)
finally:
	print("Finished " + os.getcwd() +"/"+ sys.argv[0])
