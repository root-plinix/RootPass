#!/bin/python3
import os
import sys
import argparse
os.system("clear")
name = input("[ x ] Enter Full Name [ x ] ")
number = input("[ x ] Enter Phone Number [ x ] ")
lnum = ["111","222","333","444","555","666","777","888","999","000","123","1234","12345"]
def extraction(name , index):
  try:
    global frist , middle
    frist = name[:name.index(index)]
    middle = name[name.find(index)+1:]
    global num1 , num2
    num1 = number[:6]
    num2 = number[5:]
  except:
    print("[ x ] Something Occured Happened [ x ]")
def password_saving(num):
  try:
    extraction(name , " ")
    for numbers in num:
      with open(".Result.txt","a") as file_with_name:
        file_with_name.write(frist+numbers+"\n")
        file_with_name.write(middle+numbers+"\n")
        file_with_name.write(num1+"\n"+num2+"\n")
        file_with_name.close()
  except:
    print("[ x ] Something Occured Happened [ x ]")
def compile_run():
  try:
    os.system("sort .Result.txt |" + "uniq > " +frist+".txt")
    if os.path.exists(".Result.txt"):
      os.system("rm .Result.txt")
    if os.path.exists(frist+".txt"):
      print("[ x ] "+frist+".txt saved successfully [ x ]")
  except:
    print ("[ x ] Something Occured Happened [ x ]")
if __name__ == "__main__":
  extraction(name," ")
  password_saving(lnum)
  compile_run()