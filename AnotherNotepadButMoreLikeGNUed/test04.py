import time
i=0
y=0
z=0
q=0
while q<=35:
    wr='something is happening \n loading ...'
    print(wr[q],end='', flush=True)
    q+=1
    time.sleep(0.1)
time.sleep(5)
print('\n')
while z<=9:
    wer='we are ready'
    print(wer[z],end='', flush=True)
    z+=1
    time.sleep(0.1)
print('\n')
while y<=22:
    werq='enter full name of file'
    print(werq[y],end='', flush=True)
    y+=1
    time.sleep(0.1)
print('\n')
x=input()
book = open(x, 'r')
str=book.read()
text_length = len(str)+1;
while i<=text_length:
    print(str[i],end='', flush=True)
    i+=1
    time.sleep(0.09)