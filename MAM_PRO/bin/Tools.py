import xlrd
import os


'''
create a group of tools to analysis the excel file.

'''


def create_com_list(file_name):
'''
	to read the excel file and return a com_list
'''
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
		if item in filname:
			continue
		else:
			flag = False
	return flag


def compare(rec_list, com_list):
'''
wheather the rec_list item in com_list
return suc_list and return the remain item in com_list
'''

	suc_list = []
	for filename in rec_list:
		for msg in com_list:
			if match(msg, filename):
				suc_list.append(filename)
				com_list.pop(msg)
	remain_list = com_list
	print('remain students:')
	for i in range(len(remain_list)):
		remain_list[i] = ','.join(remain_list[i])
	
	return remain_list


def create_rec_list(path='./')
	dir_list = os.listdir(path)
	rec_list = [f for f in dir_list if f.split('.')[1]=='pdf']
	return rec_list

