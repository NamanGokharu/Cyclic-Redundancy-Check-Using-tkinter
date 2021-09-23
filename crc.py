from tkinter import *
from PyQt5.QtWidgets import * 

def xor(dividend, div):
    result = []
    for i in range(1, len(div)):
        if dividend[i] == div[i]:
            result.append('0')
        else:
            result.append('1') 
    return ''.join(result)

def mod_2_div(dividend,div):
    len_div=len(div)
    len_sel_dividend=len(dividend)
    sel_dividend=dividend[0:len_div]
    while(len_div<len_sel_dividend):
        print(sel_dividend)
        if(sel_dividend[0]=="1" and len(sel_dividend)==len(div)):
            sel_dividend=xor(sel_dividend,div)+dividend[len_div]
            len_div=len_div+1
        else:
            while((sel_dividend[0]!="1" or len(sel_dividend)!=len(div)) and len_div<len_sel_dividend):
                sel_dividend=sel_dividend[1:len(div)]+dividend[len_div]
                len_div=len_div+1
    if sel_dividend[0]=='1':
        sel_dividend=xor(div,sel_dividend)
    else:
        sel_dividend=xor('0'*len_div,sel_dividend)
    checkword = sel_dividend
    return checkword
def pol_calculator(pol,i):
    powe=""
    while(pol[i]!="+" and pol[i]!="-"):
        if(pol[i]!="*"):
            powe=powe+str(pol[i])
        i=i+1
        if(i==len(pol) or i=="+" or i=="-"):
            break
    return powe
def onClick():
    pol=list(e2.get())
    binary_n=e1.get()
    pol_lst=[]
    bin_pol=""
    count=0
    for i in range(len(pol)):
        if(count==2):
            count=0
            pol_lst.append(int(pol_calculator(pol,i-1)))
        if(pol[i]=="*"):
            count=count+1
        else:
            count=0
    if(pol[len(pol)-2]=="+" or pol[len(pol)-2]=="-"):
        if(pol[len(pol)-1]=="1"):
            pol_lst.append(int("0"))
        else:
            pol_lst.append(int("1"))
    else:
        pol.append("+")
    j=max(pol_lst)
    print(type(j))
    i=0;
    while(j>=1):
        try:
            if(j==pol_lst[i]):
                i=i+1;
                bin_pol=bin_pol+"1"
            else:
                bin_pol=bin_pol+"0"
        except:
            bin_pol=bin_pol+"0"
        j=j-1
        print(j)
    if(pol[-1]!="+"):
        if(pol_lst[len(pol_lst)-1]==0):
            bin_pol=bin_pol+"1"
    else:
        bin_pol=bin_pol+"0"
    for i in range(len(bin_pol)-1):
        binary_n=binary_n+str(0)
    crc=mod_2_div(binary_n,bin_pol)
    binary_n=binary_n[0:1-len(bin_pol)]+crc
    text="Bits sent: "+binary_n
    l4=Label(f,text=text,fg="cyan",bg="black",font=('TIMES NEW ROMAN',20))
    l4.place(x=100,y=350)
    
    
    
root=Tk()
f=Frame(root,width=500,height=500,bg="black")
root.title("CRC Finder")
l1=Label(f,text="CRC Finder",fg="lightgreen",bg="black",font=('TIMES NEW ROMAN',35))
l1.place(x=150,y=50)
l2=Label(f,text="Actual bits",fg="white",bg="black",font=('TIMES NEW ROMAN',16))
l2.place(x=50,y=175)
l3=Label(f,text="Polynomial",fg="white",bg="black",font=('TIMES NEW ROMAN',16))
l3.place(x=50,y=210)
l5=Label(f,text="Note: represent x^4 as x**4,\n for every polynomial with power",
         fg="red",bg="black",font=('TIMES NEW ROMAN',15))
l5.place(x=100,y=420)
e1=Entry(f,width=20,bg="white",fg="black",font=('TIMES NEW ROMAN',16))
e1.place(x=180,y=175)
e2=Entry(f,width=20,bg="white",fg="black",font=('TIMES NEW ROMAN',16))
e2.place(x=180,y=210)
b1=Button(f,text="Calculate bits sents",width=20,height=1,fg="black",
          bg="lightgreen",font=('TIMES NEW ROMAN',16),command=lambda:onClick())
b1.place(x=130,y=275)
f.pack()
root.mainloop()
