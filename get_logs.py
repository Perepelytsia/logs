import subprocess
import pymysql
import sys
import importlib

settings = importlib.import_module('config')
con = pymysql.connect(user='admin', password='admin', db='logs')
with con:
	cur = con.cursor()
	for table in ['error_nginx', 'slow_php', 'error_yii2', 'error_php']:
		for project in settings.PROJECTS:
			if len(sys.argv) == 2:
				date = sys.argv[1]
				args = ["python3", "./"+table+"/get_log.py", project, date]
				subprocess.call(args)
			else:
				cur.execute("SELECT max(day) FROM "+project+"_"+table)
				row = cur.fetchone()
				print(table +" "+project+" last="+str(row[0]))
con.close()
