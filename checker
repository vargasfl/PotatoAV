#!/usr/bin/env/python3


import os
import hashlib

def check_file():
	malicious_check = open(./bad_hashes)
	malicious_list = malicious_check.readlines()

	for root,dirs,files in os.walk ('.'):
		for filename in sorted(files):
			full_path = os.path.join(root,filename)
			full_open = open(full_path, 'rb')
			full_read = full_open.read()
			mdholder = hashlib.md5(full_read).hexdigest()
			sha256holder = hashlib.sha256(full_read).hexdigest()
			sha512holder = hashlib.sha512(full_read).hexdigest()
			for item in malicious_list:
				if item in [mdholder, sha256holder, sha512holder]:
					print(filename)
			full_open.close()

def main():
	check_file()

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
