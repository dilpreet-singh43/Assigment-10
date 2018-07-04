#1.import re
#email_1="zuck26@facebook.com"
#email_2="page33@google.com"
#email_3="jeff42@amazon.com"
#p=re.compile(r"([a-zA-Z0-9]+)@([a-zA-Z]+).([a-z]+)")
#def show(email):
   # result=p.match(email)
   print(result[1],end=" ")
    print(result[2],end=" ")
    print(result[3])
show(email_1)
show(email_2)
show(email_3)


2.import re
text='''Betty bought a bit of butter, But the butter was so bitter,So she bought some better butter,
 To make the bitter butter better.'''

p = re.compile(r"\b[bB]\w+")
result=p.findall(text)
print(result)


3.import re
irregular_sentence="A,very very;irregular_sentence"


p = re.compile(r"[^A-Za-z0-9]")
result=p.sub(" ",irregular_sentence)
print(result)



4.import re
tweet = '''Good advice! RT @TheNextWeb:What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''

p=re.sub("!|RT @TheNextWeb:|:|http://t.co/lbwej0pxOd cc: @garybernhardt #rstats","",'''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats''')
print(p)