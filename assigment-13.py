#1.answer='''DIVISION BY ZERO EXCEPTION'''.

#try:                               
#a=3
#if a<4:
#a=a/(a-3)
#print(a)
#except Exception as e:             
#print("exception handled !")
#print(e)


#2.answer='''INDEX ERROR'''

#try: 
#l=[1,2,3]
#print(l[3])
	
#except Exception as e:
#print("exception handled !")
#print (e)



#3.answer=OUTPUT
#An exception


#4.answer=OUTPUT
#-5.0


#5.import error

#try:
#from dilpreet import 
#except Exception:
#print("Import Error")

#value error

#try:
#int("Dilpreet")
#except Exception:
#print("value error")
	
	
#3Index error

#try:
#l=[101,102,103]
#print(l[105])
#except Exception:
#print("Index Error")



#6.class AgeTooSmallError(Exception):
	pass
# try:
# def age():                                 
# num=int(input("Enter your age"))      
# if num<18:
# print("You are too small")
# raise AgeTooSmallError("Age too small exception")            
# else:
# print("HAPPY")
# age()                             
# except AgeTooSmallError as e:
# print(e)                          
# age()           
# else:
# print("No exception")              
#while True:
#try:
#num=int(input("Enter your age"))      
#if num<18:
#print("You are too small")
#raise AgeTooSmallError("Age too small exception")
#break
#except AgeTooSmallError as e:
#print(e)
#print("HAPPY")