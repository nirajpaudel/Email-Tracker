# Email-Tracker
Simple python code to keep track of your all emails at one place
Usage : just run the code
  It will prompt you to enter your email id and password
  Once set it will fetch you the unread emails.
  
Currently you have to enter your emails 
In later versions this will be handled too :)

While running the program and if you are using Gmail as your email server 
if you come across the following error:
  Traceback (most recent call last):
  File "my_mail_checker.py", line 18, in <module>
    email_connection.pass_(email_pass)
  File "/usr/lib/python2.7/poplib.py", line 197, in pass_
    return self._shortcmd('PASS %s' % pswd)
  File "/usr/lib/python2.7/poplib.py", line 160, in _shortcmd
    return self._getresp()
  File "/usr/lib/python2.7/poplib.py", line 136, in _getresp
    raise error_proto(resp)
  poplib.error_proto: -ERR [AUTH] Web login required: https://support.google.com/mail/answer/78754

To resolve the above issue :
  Go to https://www.google.com/settings/security/lesssecureapps
  
  Do Turn on Access for less secure apps.
  
  It might make your account vulnerable to attacks though.
