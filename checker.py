#!/usr/bin/env/python3

import os
import hashlib
import uh_oh
from vt import VT
vt = VT()
vt.setkey('0a1c6042e479633d58c7123ab825510f9d2fccda16d13c7b553c1dcf047b3425')
import time

def check_file():
	file_list = []
	hash_list = []
	vt_results = {}
	for root,dirs,files in os.walk ('.'):
		for filename in sorted(files):
			full_path = os.path.join(root,filename)
			#full_open = open(full_path, 'rb')
			#full_read = full_open.read()
			#mdholder = hashlib.md5(full_read).hexdigest()
			print(filename)
			vt_results = vt.getfile(full_path)
			print(vt_results)
			#print(mdholder)
			time.sleep(30)
	if len(file_list) == 0:
		print('Wow! Your system is completely clean (as far as I can tell).')
		print('Thanks for using PotatoAV, for more information check out https://github.com/vargasfl/PotatoAV')
		print('Bye-bye!')
		exit()
	elif len(file_list) > 0:
		uh_oh.main(file_list, hash_list)
def main():
	check_file()
if __name__ == '__main__':
	main()
