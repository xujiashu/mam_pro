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


def match(msg, filename):
	flag = True
	msg = msg[0:4]
	for item in msg:
		if item in filename:
			continue
		else:
			flag = False
	return flag


'''
wheather the rec_list item in com_list
return suc_list and return fail_list
'''
def compare(rec_list, com_list):

	suc_list = []
	fail_list = []
	for filename in rec_list:				#for one filename
		msg_index = 0						#set index from 0
		for msg in com_list:				#for msg in com_list index in msg_index
			if match(msg, filename):		#judge wheather fix the rule
				suc_list.append(filename)	#add it
				com_list.pop(msg_index)		#D it from c_l and keep index
			else:							#not fix
				fail_list.append(filename)	#add to fail_index
				msg_index += 1				#next_index

	remain_list = com_list[:]				#the com_list stay same why?
	for i in range(len(remain_list)):
		remain_list[i] = ','.join(remain_list[i])
	
	return (remain_list,fail_list)


def create_rec_list(path='./'):
	dir_list = os.listdir(path)
	rec_list = [f for f in dir_list if f.split('.')[1]=='pdf']
	return rec_list

