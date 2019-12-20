import pymysql
import datetime
import sys
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

if len(sys.argv) == 5:

	project = sys.argv[1]
	date1    = sys.argv[3]
	dt1 = datetime.datetime(int(date1[:4]), int(date1[4:6]), int(date1[6:]))
	day1 = dt1.strftime("%Y-%m-%d")
	date2    = sys.argv[4]
	dt2 = datetime.datetime(int(date2[:4]), int(date2[4:6]), int(date2[6:]))
	day2 = dt2.strftime("%Y-%m-%d")

	daysPlt = list()
	cntPlt  = list()
	sumPlt  = list()
	con = pymysql.connect(user='admin', password='admin', db='logs')
	with con:
		cur = con.cursor()
		if sys.argv[2] not in ['sum', 'cnt']:
			addSql = sys.argv[2]
			sql = "SELECT day, count(*), sum(cnt) FROM "+project+"_slow_php  WHERE hash='"+sys.argv[2]+"' and day between %s and %s GROUP BY day"
		else:
			sql = "SELECT day, count(*), sum(cnt) FROM "+project+"_slow_php WHERE day between %s and %s GROUP BY day"
		cur.execute(sql, (day1, day2))
		rows = cur.fetchall()
		for row in rows:
			daysPlt.append(row[0])
			cntPlt.append(row[1])
			sumPlt.append(row[2])
	con.close()

	daysPltFloat = mdates.date2num(daysPlt)
	plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
	plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
	plt.style.use('seaborn-whitegrid')
	if sys.argv[2] == 'cnt':
		yData = cntPlt
	else:
		yData = sumPlt
	plt.plot(daysPltFloat, yData)
	plt.gcf().autofmt_xdate()
	plt.title('slow php of '+project, fontsize=24)
	plt.ylabel(sys.argv[2], fontsize=14)
	plt.xlabel('Day', fontsize=14)
	plt.show()

else:
	print("The script demands a project, a type and dates. Example: `python3 get_graphic.py {s || o} {sum || cnt || hash} 20191209 20191211`")
