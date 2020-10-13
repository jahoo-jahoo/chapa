import os 
import sys 
import time 

print("\n\nSelection 2020 auto mate program\n\n\n")
n='''1 >>> update program\n2 >>> open runing Algorithm\n\n'''
print(n)


def select():
  a=int(input("Ente Your selection : "))
  if a==1 :
    name=input("Enter your folder name : ")
    os.system('pkg update')
    os.system('pkg upgrade')
    os.system('rm -rf name')
  elif a==2 :
    os.system('python jahoo4.py')
  else:
    select()
select()