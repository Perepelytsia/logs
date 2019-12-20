import pymysql
import sys
import os
import hashlib
import datetime
import importlib

if len(sys.argv) == 3:

	project = sys.argv[1]
	date    = sys.argv[2]
	dt = datetime.datetime(int(date[:4]), int(date[4:6]), int(date[6:]))
	day = dt.strftime("%Y-%m-%d")
	settings = importlib.import_module(project)
	if settings.SCP_CHUNK and settings.PATH:

		os.system(settings.SCP_CHUNK + date + ".gz "+ settings.PATH + ".gz")
		os.system("gunzip -f "+ settings.PATH +".gz")
		data = dict()
		with open(settings.PATH, 'r') as reader:

			lines     = reader.readlines()
			cntLine   = 0
			pieceLine = ''
			for line in lines:

				# fitst time it does not work because len(pieceLine) is zero
				if len(line) == 1 and len(pieceLine):

					objHash = hashlib.md5(pieceLine.encode())
					strHash = objHash.hexdigest()
					if strHash in data.keys():
						data[strHash]['cnt'] += 1
					else:
						data[strHash] = {"stack": pieceLine, "cnt": 1}
					cntLine = 0
					pieceLine = ''

				if cntLine != 1:
					pieceLine = pieceLine + line

				cntLine += 1

		con = pymysql.connect(user='admin', password='admin', db='logs')
		with con:

			cur = con.cursor()
			sql = "DELETE FROM "+project+"_slow_php WHERE day=%s"
			cur.execute(sql, (day))

			for strHash, value in data.items():
				cnt = value['cnt']
				stack = value['stack']
				sql = "INSERT INTO "+project+"_slow_php (`hash`, `stack`, `cnt`, `day`) VALUES (%s, %s, %s, %s)"
				cur.execute(sql, (strHash, stack, cnt, day))

		con.close()

	else:
		print("incorrect params")

else:
	print("The script demands a project and a date. Example: `python3 get_logs.py {s || o} 20191209`")
