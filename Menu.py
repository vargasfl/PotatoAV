#!/usr/bin/env python3
import checker
import sys
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
      checker.check_file()
  if response == '3':
      print()
      print('Bye-bye!')
      exit()
def main():
    menu()
main()
