from nginx_error_log import parse_lines, parse_lines_merge_multiple
import pymysql
import sys
import os
import datetime
import importlib

if len(sys.argv) == 3:
	project = sys.argv[1]
	date    = sys.argv[2]
	dt = datetime.datetime(int(date[:4]), int(date[4:6]), int(date[6:]))
	day = dt.strftime("%Y-%m-%d")
	settings = importlib.import_module(project)
	os.system(settings.SCP_CHUNK + date + ".gz "+ settings.PATH + ".gz")
	os.system("gunzip -f "+ settings.PATH +".gz")
	con = pymysql.connect(user='admin', password='admin', db='logs')
	with con:
		cur = con.cursor()
		sql = "DELETE FROM "+project+"_error_nginx WHERE day=%s"
		cur.execute(sql, (day))
		with open(settings.PATH, 'r') as reader:
			for log in parse_lines(reader):
				sql = "INSERT INTO "+project+"_error_nginx (`level`, `msg`, `day`) VALUES (%s, %s, %s)"
				lvl = str(log.level)
				cur.execute(sql, (lvl.replace('Level.', ''), log.message, day))
		reader.close()
	con.close()
else:
	print("The script demands a project and a date. Example: `python3 get_logs.py {s || o} 20191209`")
