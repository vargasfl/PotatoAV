#!/usr/bin/env/python3

import os
import hashlib
import uh_oh
import __init__
vt = __init__.VT()
vt.setkey('0a1c6042e479633d58c7123ab825510f9d2fccda16d13c7b553c1dcf047b3425')
import time

def check_file():
    file_list = ['/yo/momma']
    hash_list = ['YOOOoooooooooooo']
    vt_results = {}
    filtered = ['response_code', 'positives']
    for root,dirs,files in os.walk('.'):
        for filename in sorted(files):
            full_p = os.path.join(root,filename)
            full_o = open(full_p, 'rb')
            full_r = full_o.read()
            mdholder = hashlib.md5(full_r).hexdigest()
            vt_results = vt.getfile(mdholder)
            keylist = [vt_results[key] for key in filtered]
            time.sleep(15)
            if keylist [0] == 0:
                print('Virustotal did not like this one.')
            elif keylist[0] == 1:
                if keylist[1] > 0:
                    file_list.append(full_p)
                    hash_list.append(mdholder)
            time.sleep(15)
            full_o.close()
    if len(file_list) == 0:
        print('Wow! Your system is completely clean (as far as VirusTotal can tell).')
        print('Thanks for using PotatoAV, for more information check out https://github.com/vargasfl/PotatoAV')
        print('Bye-bye!')
        exit()
    elif len(file_list) > 0:
        uh_oh.main(file_list, hash_list)
def main():
    check_file()
if __name__ == '__main__':
    main()
    
