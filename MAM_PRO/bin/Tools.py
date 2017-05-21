import xlrd
import os


'''
create a group of tools to analysis the excel file.

'''


'''
to read excel file and create a com_list
'''
def create_com_list(file_name):

	com_list = []
	wb = xlrd.open_workbook(file_name)
	sheet1 = wb.sheet_by_index(0)
	for cow in range(sheet1.nrows):
		com_list.append(cow)
	return com_list


def match(msg, filename, match_level=1):
	match_num = 0
	if len(msg)>=5:
		msg = msg[0:4]
	for item in msg:
		if item in filename:
			match_num += 1
	if match_num >= match_level:
		return True
	else:
		return False

def compare(filename, com_list, flag='F'):
	msg_index = 0						#set index f
	for msg in com_list:				#for msg in 
		if match(msg, filename):		#judge wheat
			return(msg_index, filename)
		else:							#not fix
			msg_index += 1				#next_index
	return (flag,filename)


'''
wheather the rec_list filename in the com_list
return suc_list and return fail_list
'''
def compose_list(rec_list, com_list):

	suc_list = []
	fail_list = []
	for filename in rec_list:			#test filename
		flag, filename = compare(filename, com_list)
		if flag != 'F':
			com_list.pop(flag)
			suc_list.append(filename)
		else:
			fail_list.append(filename)

	for i in range(len(com_list)):		#compose
		com_list[i] = ','.join(com_list[i])
	
	return (com_list,fail_list)


def create_rec_list(path='./'):
	dir_list = os.listdir(path)
	rec_list = [f for f in dir_list if f.split('.')[1]=='pdf']
	return rec_list

