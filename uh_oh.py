#!usr/bin/env python
def oops(file_list, hash_list):
    title1 = 'Bad File'
    title2 = 'Hash of Bad File'
    print('Uh-oh! Looks like we found some potentially bad apples in your system, listing them out for you now.')
    print('-' * 228)
    print('-- ' + title1.ljust(92) + '-- ' + title2.ljust(128) + '--')
    for x, y in zip(file_list, hash_list):
        print('-- ' + x.ljust(92) + '-- ' + y.ljust(128) + '--')
    print('-' * 228)
    print()
    print("We've listed all files in your system that match malicious signatures (according to our data), feel free to look up these hashes in VirusTotal or a similar website to learn more about them and what to do.")
    print("Thanks for using PotatoAV, for more information please visit https://github.com/vargasfl/PotatoAV")
    print('Bye-bye!')
def main(file_list, hash_list):
    oops(file_list, hash_list)
if __name__ == '__main__':
    main()
