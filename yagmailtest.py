# yagmail test
import yagmail
yag = yagmail.SMTP('noamhermanse3')
to = 'noamhermanse@gmail.com'
to2 = 'noamhermanse3@gmail.com'
subject = 'This is obviously the subject'
body = 'This is obviously the body'
html = '<h1></h1>'
yag.send(to = to, subject = subject, contents = body)