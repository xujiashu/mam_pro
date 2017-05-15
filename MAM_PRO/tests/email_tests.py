#-*- coding:utf-8 -*-

from nose.tools import *
from bin.email import *
import re

def test_cfmat():
	pattern = re.compile(".*[0-9]+.*")
	assert_equal(cfmat(), [pattern,'pdf'])
	
def test_cmpre():
	filename1 = '姓名 资源环境学院 201234567520.pdf'
	filename2 = '姓名 资源环境学院 201234567520.word'
	filename3 = '数学建模.pdf'
	
	pattern = re.compile(".*[0-9]+.*")
	assert_equal(cmpre(filename1, [pattern, 'pdf']), filename1) 
	assert_equal(cmpre(filename2, [pattern, 'pdf']), None) 
	assert_equal(cmpre(filename3, [pattern, 'pdf']), None) 
