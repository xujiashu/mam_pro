import Tools

com_list = []
rec_list = []
suc_list = []
bad_list = []

file_name = raw_input('enter the ss list excel's name:')
com_list = Tools.anal_excel(file_name)
rec_list = Tools.receive()

while rec_list:
	student_data = rec_list.pop()
	if student_data in com_list:
		good_data = com_list.pop(student_data)
		suc_list.append(good_data)
	else:
		bad_list.append(student_data)

file = raw_input('done! enter the filename to save:')

'''
#save filename #ok list #not ok list #remain list
'''
Tool.write(file, suc_list, bad_list, com_list)

