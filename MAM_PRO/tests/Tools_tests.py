#-*- coding:utf-8 -*-

from nose.tools import *
from bin.Tools import *

def test_match():
	msg = ['1','filename1','xy']
	filename1 = 'filename1.pdf'
	filename2 = 'filename2.pdf'
	assert_equal(match(msg, filename1), True)	
	assert_equal(match(msg, filename2), False)


def test_compare():
	com_list = [['1','filename1','xy'],['2','filename2','学院'],['3','filename3','学院'],
			['5','filename5','xy'],['6','filename6','xy'],['7','filename7','xy']]
	filename1 = 'filename1.pdf'
	filename2 = 'filename2.pdf'
	filename3 = 'filename3.pdf'
	filename4 = 'filename4.pdf'
	filenameF = 'filenameF.pdf'
	assert_equal(compare(filename1, com_list), (0, 'filename1.pdf'))
	assert_equal(compare(filename2, com_list), (1, 'filename2.pdf'))
	assert_equal(compare(filename3, com_list), (2, 'filename3.pdf'))
	assert_equal(compare(filename4, com_list), ('F', 'filename4.pdf'))
	assert_equal(compare(filenameF, com_list), ('F', 'filenameF.pdf'))	
