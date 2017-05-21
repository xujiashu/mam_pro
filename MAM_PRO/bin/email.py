#encoding=utf-8  
import poplib  
import email 
import re 

def cfmat():
	pattern = re.compile(".*[0-9]+.*")
	form = [pattern,'pdf']
	return form

def cmpre(filename, form):
	fname = re.match(form[0], filename)
	if fname:
		ftype = filename.split('.')[1]
		if ftype == form[1]:
			return filename
	return None


#wait for testing...

def get_mail_attach(mail_msg, form):
	for part in mail_msg.walk():
		filname = part.get_filename()
		if cmpre(filename, form):
			data = part.get_payload(decode=True)
			with open('./homework/'+filename, 'wb') as f:
				f.write(data)

def cmail(address, password, form):
	server = address.split('@')[1]
	Mailbox = poplib.POP3_SSL('pop.'+server)
	Mailbox.user(address)
	Mailbox.pass_(password)

	mail_num = len(Mailbox.list()[1])
	mails = (Mailbox.retr(i+1) for i in range(mail_num))
	for mail in mails:
		mail_msg = email.message_from_string('\n'.join(mail[1]))
		get_mail_attach(mail_msg, form)
	
