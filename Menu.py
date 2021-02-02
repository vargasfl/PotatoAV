#!/usr/bin/env python3
import checker
import sys
import time
def menu():
  art_file = open('./ASCII_potatopic.txt')
  print(art_file.read())
  print('Welcome to PotatoAV')
  print('Please select an option below:')
  print()
  print('[1]: Scan')
  print('[2]: About')
  print('[3]: Quit')

  response = input()
  	
  if response == '2':
      print()
      print(open('./README.md').read())
  if response == '1':
      print('Go get some lunch or something, this is going to take a while')
      checker.check_file()
  if response == '3':
      print()
      print('Bye-bye!')
   
   # incorrect key message and program continuation until system scanned or program quit    
  response_opt = ['1','2','3']
  while response not in response_opt:
  	print('oops..wrong key. please enter option 1,2,or 3...')
  	time.sleep(3)
  	return menu()
  		
  if response != '3':
  	print('please Enter M to return to the main menu !')
  	print(' or enter any key to exit')
  	
  	response2 = input()
  	if response2 == 'M' or response2 == 'm':
  		return menu()
  	if response2 != 'M' or response2 != 'm':
  		print('Bye-bye!')
  		exit()
  	exit()
  	
def main():
    menu()
main()
