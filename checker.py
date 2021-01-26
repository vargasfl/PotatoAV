#!/usr/bin/env/python3

import os
import hashlib
import uh_oh

def check_file():
	malicious_check = open('./bad_hashes.txt')
	malicious_list = malicious_check.read()
	file_list = []
	hash_list = []
	for root,dirs,files in os.walk ('.'):
		for filename in sorted(files):
			full_path = os.path.join(root,filename)
			full_open = open(full_path, 'rb')
			full_read = full_open.read()
			full_open.close()
			mdholder = hashlib.md5(full_read).hexdigest()
			sha256holder = hashlib.sha256(full_read).hexdigest()
			sha512holder = hashlib.sha512(full_read).hexdigest()
			if mdholder in malicious_list:
				file_list.append(full_path)
				hash_list.append(mdholder)
			elif sha256holder in malicious_list:
				file_list.append(full_path)
				hash_list.append(sha256holder)
			elif sha512holder in malicious_list:
				file_list.append(full_path)
				hash_list.append(sha512holder)
	print(file_list)
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
