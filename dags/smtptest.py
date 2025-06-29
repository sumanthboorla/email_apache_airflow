import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('sumanthb.freelance@gmail.com', 'yehlkabrdbolaryw')
server.sendmail('sumanthb.freelance@gmail.com', 'sumanthb31@gmail.com', 'Subject: Test\n\nHello123')
server.quit()
