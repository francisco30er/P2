import smtplib 

monto= '2250'

smtpUser = 'labdemicros@gmail.com'
smtpPass = 'micros1234'

toAdd= 'freddysalazar95@gmail.com'
fromAdd= smtpUser 

subject = 'Cobro Peaje'
header = 'Para: ' + toAdd + '\n' + 'From: ' + fromAdd + '\n' + 'Subject: ' + subject
body = 'El cobro del peaje MEMO 27 ha sido realizado por un monto de: '+ monto 


s = smtplib.SMTP('smtp.gmail.com',587)

s.ehlo()
s.starttls()
s.ehlo()

s.login(smtpUser, smtpPass)
s.sendmail(fromAdd, toAdd, header + '\n\n' + body)

s.quit()
