import smtplib

sender = 'harikrisahnasadhineni@gmail.com'
receivers = ['harisadhineni@gmail.com']
message = ''' Hello! harikrishna this mail is regarding for job opertuties '''
content = 'job opertunity'
try:
    obj = smtplib.SMTP('smtp.gmail.com',587)
    obj.starttls()
    obj.login('harikrishnasadhineni@gmail.com','Jyothi@412')
    obj.sendmail(sender,receivers,message,content)
    print("sent succcessfully")

except:
    print("mail not sent plaese check your user id and possword") 
