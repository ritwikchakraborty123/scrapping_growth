import mysql.connector
import datetime
import requests as rq
import bs4

# connect to scrap databse of MYSQL 
mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="scrap"
)

# starting date from where we have to scrap
start=datetime.date(2016,4,10);

# ending date till where we have to scrap
end=datetime.date(2020,11,28);

# it will be differece to calculate next day
delta=datetime.timedelta(days=1)

month=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

while start<=end :

	# this part will help to split the datetime object to string and use that for getting the link of web site
	dates=str(start).rstrip().split('-')
	final_date=""
	final_date=dates[-1]+'-'+month[int(dates[1])-1]+'-'+dates[0]
	
	if(int(dates[-1])>=10 and int(dates[-1])<=15): # we only have to scrap in between this range 

		# help to insert into scrap table wtih sql query
		sql="INSERT INTO `scrap` (`scheme_code`, `scheme_name`, `isin_growth`, `net_asset_value`) VALUES (%s, %s, %s, %s)"

		# auto generated URL to get the web site
		URL="http://portal.amfiindia.com/DownloadNAVHistoryReport_Po.aspx?frmdt="+final_date
		
		res=rq.get(URL)

		# scrapping the website as html data
		soup=bs4.BeautifulSoup(res.text,'html.parser')
		mycursor = mydb.cursor()

		# it will split every line by newline seperation splitting

		for i in soup:
		  part=i.rstrip().split('\n')

		  #it will help to get different word out of sentence

		  for j in part:
		    line=j.rstrip().split(' ')
		    ok=0

		    # help to seach if it contain growth term inside and it will make ok as true value
		    for k in line:
		      if(k=="Growth"):
		        ok=1
		        break

		     # checking if line is eligible to be inserted into table
		    if(ok):

		        col=j.rstrip().split(';')
		        schemecode="NULL"
		        schemename="NULL"
		        isingrowth="NULL"
		        netassetvalue="NULL"
		        
		        if(len(col)>0):  # helps to check if scheme code is present or not that particular row it will prevent from any array out of bound error
		        	schemecode=col[0]
		        if(len(col)>1):
		        	schemename=col[1] # helps to check if scheme name is present or not that particular row  it will prevent from any array out of bound error
		        if(len(col)>2):
		        	isingrowth=col[2] # helps to check if isin growth field is present or not that particular row  it will prevent from any array out of bound error
		        if(len(col)>4):
		        	netassetvalue=col[4] # helps to check if net asset value is present or not that particular row  it will prevent from any array out of bound error
		    

		        val=(schemecode, schemename, isingrowth, netassetvalue)
		    
		        mycursor.execute(sql,val)
		        mydb.commit()  # refelct the change in database


	start+=delta # it will increase the date by 1 day at the end