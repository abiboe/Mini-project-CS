import tkinter as tk
from tkinter import ttk
from tkinter import * 


root = Tk()


root.geometry('826x567')
root.configure(background='#000000')
root.title('Message Encryption and Decryption')



lblInfo=Label(root, text=':::::SECRET MESSAGING::::::::  :::Vigenère cipher:::', bg='white', font=('helvetica', 12, 'normal'),fg='black').place(x=264, y=36)

rand = StringVar() 
Msg = StringVar() 
key = StringVar() 
mode = StringVar() 
Result = StringVar() 
  
def qExit(): 
    root.destroy() 
  
def Reset(): 
    rand.set("") 
    Msg.set("") 
    key.set("") 
    mode.set("") 
    Result.set("") 

lblReference = Label(root,bg="black", font = ('Century', 11, 'bold'),text = "NAME:::",fg="white", bd = 11, anchor = "w").place(x=98, y=197)
txtReference =Entry(root, font = ('Century', 11, 'bold'),textvariable = rand, bd = 10, insertwidth = 4,bg = "white", justify = 'right').place(x=343, y=198) 
lblMsg =Label(root,bg="black", font = ('Century', 11, 'bold'),text = "MESSAGE:::",fg="white", bd = 11, anchor = "w").place(x=98, y=241) 
txtMsg =Entry(root, font = ('Century', 11, 'bold'),textvariable = Msg, bd = 10, insertwidth = 4,bg = "white", justify = 'right').place(x=343, y=241) 
lblkey =Label(root,bg="black", font = ('Century', 11, 'bold'),text = "KEY:::",fg="white", bd = 11, anchor = "w").place(x=98, y=274)
txtkey =Entry(root, font = ('Century', 11, 'bold'),textvariable = key,fg="black", bd = 10, insertwidth = 4,bg = "white", justify = 'right').place(x=343, y=275)
lblmode =Label(root,bg="black", font = ('Century', 11, 'bold'),text = "Mode==",fg="white", bd = 11, anchor = "w").place(x=98, y=316) 
txtmode =Entry(root, font = ('Century', 11, 'bold'),textvariable = mode, bd = 10, insertwidth = 4,bg = "white", justify = 'right').place(x=343, y=316)
lblService = Label(root,bg="black", font = ('Century', 11, 'bold'),text = "The Result--",fg="white", bd = 11, anchor = "w").place(x=98, y=354) 
txtService = Entry(root, font = ('Century', 11, 'bold'),textvariable = Result, bd = 10, insertwidth = 4,bg = "white", justify = 'right').place(x=343, y=354) 



import base64 
  
def encode(key, clear): 
    enc = [] 
      
    for i in range(len(clear)): 
        key_c = key[i % len(key)] 
        enc_c = chr((ord(clear[i]) +
                     ord(key_c)) % 256) 
                       
        enc.append(enc_c) 
          
    return base64.urlsafe_b64encode("".join(enc).encode()).decode() 
  
def decode(key, enc): 
    dec = [] 
      
    enc = base64.urlsafe_b64decode(enc).decode() 
    for i in range(len(enc)): 
        key_c = key[i % len(key)] 
        dec_c = chr((256 + ord(enc[i]) -
                           ord(key_c)) % 256) 
                             
        dec.append(dec_c) 
    return "".join(dec) 
  
def Ref(): 
    print("Message= ", (Msg.get())) 
  
    clear = Msg.get() 
    k = key.get() 
    m = mode.get() 
  
    if (m == 'e'): 
        Result.set(encode(k, clear)) 
    else: 
        Result.set(decode(k, clear))







btnTotal =Button(root, text='Show Message', bg='#7FFF00', font=('verdana', 12, 'normal'), command=Ref).place(x=112, y=444)
btnReset =Button(root, text='Reset', bg='#FF3030', font=('verdana', 12, 'normal'), command=Reset).place(x=250, y=444)
btnExit =Button(root, text='Exit', bg='#A020F0', font=('verdana', 12, 'normal'), command=qExit).place(x=315, y=444)


root.mainloop()
