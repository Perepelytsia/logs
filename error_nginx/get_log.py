import pymysql
import sys
import os
import datetime
import importlib
import re

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
		with open(settings.PATH, 'r') as reader:

			lines     = reader.readlines()
			step = 0
			for line in lines:
				data = []
				day = re.match(r'\d{4}\/\d{2}\/\d{2} \d{2}:\d{2}:\d{2}', line)
				if day:
					groupDay  = day.group()
					formatDay = groupDay[0:10]
					formatDay = formatDay.replace('/', '-')
					data.append(formatDay)

					index4LvlBefore = 2 + day.end()
					index4LvlAfter = 5 + index4LvlBefore
					data.append(line[index4LvlBefore:index4LvlAfter])

					pid = re.search(r'\*\d{1,30}', line)
					if pid:
						index4MsgBefore = pid.end()
						index4MsgAfter = len(line)
						data.append(line[index4MsgBefore:index4MsgAfter])
						sql = "INSERT INTO "+project+"_error_nginx (`level`, `msg`, `day`) VALUES (%s, %s, %s)"
						cur.execute(sql, (data[1], data[2], data[0]))
					#print(step)
					step += 1

		reader.close()
	con.close()
else:
	print("The script demands a project and a date. Example: `python3 get_logs.py {s || o} 20191209`")
