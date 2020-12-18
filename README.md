# scrapping_growth
This single python file will scrap a whole report of different fund and plan through out a particualr range of date that also can be adjusted as per requirements.
It will seperate out lines having word "growth" which signifies planes made a profit or growth .
It will put details from website into MYSQL data base.
As per details from website automatically value will be inserted into table in form of SQL dataset.
used website to scrap : http://portal.amfiindia.com/DownloadNAVHistoryReport_Po.aspx?frmdt=01-Dec-2020
Above link is used to request and get details of every required dates.
Modules used :
* mysql.connector
* datetime
* requests 
* bs4
To run this program :
run xampp and set table name and database names and change the code respectively (only database and table into Query) // checking connection before running will be good.
run python file by python db.py
wait till complete insertion
