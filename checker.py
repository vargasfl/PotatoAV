#!/usr/bin/env/python3


import os
import hashlib

def check_file():
	malicious_check = open('./bad_hashes.txt')
	malicious_list = malicious_check.readlines()
	bad_file_list = []
	gotcha_list = []
	for root,dirs,files in os.walk ('.'):
		for filename in sorted(files):
			full_path = os.path.join(root,filename)
			full_open = open(full_path, 'rb')
			full_read = full_open.read()
			full_open.close()
			mdholder = hashlib.md5(full_read).hexdigest()
			sha256holder = hashlib.sha256(full_read).hexdigest()
			sha512holder = hashlib.sha512(full_read).hexdigest()
			for item in malicious_list:
				if item in [mdholder, sha256holder, sha512holder]:
					bad_file_list.append(full_path)
					if item == mdholder:
						gotcha_list.append(mdholder)
					elif item == sha256holder:
						gotcha_list.append(sha256holder)
					elif item == sha512holder:
						gotcha_list.append(sha512holder)
	if not bad_file_list:
		print('Wow! Your system is completely clean (as far as I can tell).')
		print('Thanks for using PotatoAV, for more information check out https://github.com/vargasfl/PotatoAV')
		print('Bye-bye!')
		exit()
	elif len(bad_file_list) > 0:
		uh_oh.oops(bad_file_list, gotcha_list)
def main():
	check_file()

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
