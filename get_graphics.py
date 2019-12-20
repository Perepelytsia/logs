import subprocess
import pymysql
import importlib

settings = importlib.import_module('config')
con = pymysql.connect(user='admin', password='admin', db='logs')
with con:
	cur = con.cursor()
	for table in ['error_nginx', 'slow_php', 'error_yii2']:
		for project in settings.PROJECTS:
			cur.execute("SELECT min(day), max(day) FROM "+project+"_"+table)
			row = cur.fetchone()
			minDay = str(row[0])
			maxDay = str(row[1])
			args = ["python3", "./"+table+"/get_graphic.py", project]
			if table == 'slow_php':
				args.append('sum')
			args = args + [minDay.replace('-', ''), maxDay.replace('-', '')]
			subprocess.call(args)
con.close()
