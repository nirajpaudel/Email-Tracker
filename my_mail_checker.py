import poplib

mail_server = "pop.gmail.com"
email_id = "akashgoesocial@gmail.com"

email_pass = raw_input("Entert the password for username = Ashutosh:\t")

#open connection to mail server (secured using SSL)
email_connection = poplib.POP3_SSL(mail_server)

#print the response message from server
print email_connection.getwelcome()

#set email address
email_connection.user(email_id)

#set password
email_connection.pass_(email_pass)

#get information about the email address
email_information = email_connection.stat()

print "Total no of new emails: %s (%s bytes)" % email_information

#Reading an email 
print "\n\n==========>READING<===========\n\n"

#Fetch the top mail
latest_email = email_connection.retr(1)

#print the message
print latest_email[1]
