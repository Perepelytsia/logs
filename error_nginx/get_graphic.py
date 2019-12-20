import pymysql
import datetime
import sys
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

if len(sys.argv) == 4:

	project = sys.argv[1]
	date1    = sys.argv[2]
	dt1 = datetime.datetime(int(date1[:4]), int(date1[4:6]), int(date1[6:]))
	day1 = dt1.strftime("%Y-%m-%d")
	date2    = sys.argv[3]
	dt2 = datetime.datetime(int(date2[:4]), int(date2[4:6]), int(date2[6:]))
	day2 = dt2.strftime("%Y-%m-%d")

	daysPlt = list()
	cntPlt  = list()
	con = pymysql.connect(user='admin', password='admin', db='logs')
	with con:
		cur = con.cursor()
		sql = "SELECT day, count(*) FROM "+project+"_error_nginx WHERE day between %s and %s GROUP BY day"
		cur.execute(sql, (day1, day2))
		rows = cur.fetchall()
		for row in rows:
			daysPlt.append(row[0])
			cntPlt.append(row[1])
	con.close()

	daysPltFloat = mdates.date2num(daysPlt)
	plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
	plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
	plt.style.use('seaborn-whitegrid')
	plt.plot(daysPltFloat, cntPlt)
	plt.gcf().autofmt_xdate()
	plt.title('nginx error of '+project, fontsize=24)
	plt.ylabel('Number',fontsize=14)
	plt.xlabel('Day',fontsize=14)
	plt.show()

else:
	print("The script demands a project, a type and dates. Example: `python3 get_graphic.py {s || o} 20191209 20191211`")
