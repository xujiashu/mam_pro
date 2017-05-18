#-*- coding:utf-8 -*-

from nose.tools import *
from bin.Tools import *

def test_compare():
	com_list = [['1','filename1','xy'],['2','filename2','学院'],['3','filename3','学院'],
			['5','filename5','xy'],['6','filename6','xy'],['7','filename7','xy']]
	rec_list = ['filename1.pdf','filename2.pdf','filename3.pdf','filename4.pdf']
	remain_list = [['5,filename5,xy'],['6,filename6,xy'],['7,filename7,xy']]
	fail_list = ['filename4.pdf']
	remain_list = [['5,filename5,xy'],['6,filename6,xy'],['7,filename7,xy']]
	assert_equal(compare(rec_list, com_list), (remain_list,fail_list))

