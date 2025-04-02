# Import the modules we'll need
import schedule
import time
from datetime import datetime
from threading import Timer
import pypatent
import smtplib
import re
from email.message import EmailMessage 

gmail_user = 'your.username@gmail.com'
gmail_password = 'your.pw' # move to env variable

#DAILY PATENT CHECK FUNCTION
def DailyPatentCheck():
    now = datetime.now() # current date and time
    IssueDate = "5-19-2020" #now.strftime(" %m-%d-%Y").replace(' 0', '') #create today's date formatted properly

    try:
        res = pypatent.Search('ISD/' + IssueDate, results_limit=2, get_patent_details=False).as_list()# 'ISD/2-11-2020->' + 
        #latest_patents_result = str(res)
        #print (latest_patents_result)
        print (res)
        #result_halfway_trimmed = latest_patents_result.split("\'applicant_name\': \'",1)[1]
        #ApplicantName = result_halfway_trimmed.split("\',",1)[0]

    except AttributeError:
        print("No patents filed on " + IssueDate)
        PatentResults = "No patents filed on " + IssueDate
        pass

##    try:
##        msg = EmailMessage()
##        msg.set_content(PatentResults)
##        msg['Subject'] = "Today's Patents"
##        msg['From'] = your.username@gmail.com'
##        msg['To'] = 'your.username@gmail.com'
##        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
##        server.ehlo()
##        server.login(gmail_user, gmail_password)
##        server.send_message(msg)
##        server.quit()
##        print("email sent")
##    except:
##        print ("something went wrong with connection to Gmail")

    
#DAILY PATENT CHECK FUNCTION

#SET SCHEDULED TIME TO CHECK PATENTS
schedule.every().day.at("22:47").do(DailyPatentCheck)
#SET SCHEDULED TIME TO CHECK PATENTS

#LOOP
while True:
    #PATENT CHECK WILL RUN EVERY DAY AT 7AM
    schedule.run_pending()
    time.sleep(30)
    #PATENT CHECK WILL RUN EVERY DAY AT 7AM
#LOOP


raise SystemExit
