#1. 
#f=open('new.txt','r',encoding="utf8")
#content=f.readlines()
#n=int(input("enter number of lines you want to read from last"))
#while n>0:
#print(content[-n])
#n=-1
#f.close()


#2.
# f=open('new.txt','r',encoding="utf8")
# w=input('Enter the word you want to search')
# x=f.read()
# c=0
# for w in x:
# if w==x:
#c=c+1
#print(c)
#from collections import Counter
#def word_count(fname,encoding="utf8"):
#with open(fname,encoding="utf8") as f:
#return Counter(f.read().split())
#print("Frequency of words in the file :",word_count("new.txt",encoding="utf8"))


#3.
# with open ('abc.txt','r') as f1:
# with open('cde.txt','w') as f2:
#for line in f1:
#f2.write(line)


#4.

# with open ('abc.txt','r') as f1:
# con1=f1.readlines()
# with open('cde.txt', 'r') as f2:
# con2 =f2.readlines()
# i = 0
# for n in con1:
# print(con1[i]+con2[i])
#i = i + 1


#5.
# import random
# with open ('abc.txt','w') as f1:
# for i in range(10):
# num=random.randint(1,9)
#f1.write(str(num))
#f1.write("\n")
# with open ('abc.txt','r') as f1:
# con=f1.readlines()
#con.sort()
# with open ('cde.txt','w') as f1:
# for i in con:
# f1.write(i)
#f1.write('\n')