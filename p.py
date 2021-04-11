from tkinter import Tk
from tkinter import * 

root = Tk()
root.geometry('826x567')
root.configure(background='#000000')
root.title('Message Encryption and Decryption')


lblInfo=Label(root, text=':::::SECRET MESSAGING:::::::: \n :::Vigenère cipher:::', bg='black', font=('helvetica', 22, 'normal'),fg='purple').place(x=264, y=36)

Msg = StringVar() 
key = StringVar() 
mode = StringVar() 
Result = StringVar() 
  
def qExit(): 
    root.destroy() 
  
def Reset(): 
   
    Msg.set("") 
    key.set("") 
    mode.set("") 
    Result.set("") 

 
lblMsg =Label(root,bg="black", font = ('Century', 11, 'bold'),text = "MESSAGE:::",fg="white", bd = 11, anchor = "w").place(x=98, y=241) 
txtMsg =Entry(root, font = ('Century', 11, 'bold'),textvariable = Msg, bd = 10, insertwidth = 4,bg = "white", justify = 'right').place(x=343, y=241) 
lblkey =Label(root,bg="black", font = ('Century', 11, 'bold'),text = "KEY:::",fg="white", bd = 11, anchor = "w").place(x=98, y=274)
txtkey =Entry(root, font = ('Century', 11, 'bold'),textvariable = key,fg="black", bd = 10, insertwidth = 4,bg = "white", justify = 'right').place(x=343, y=275)
lblmode =Label(root,bg="black", font = ('Century', 11, 'bold'),text = "Mode==",fg="white", bd = 11, anchor = "w").place(x=98, y=316) 
txtmode =Entry(root, font = ('Century', 11, 'bold'),textvariable = mode, bd = 10, insertwidth = 4,bg = "white", justify = 'right').place(x=343, y=316)
lblService = Label(root,bg="black", font = ('Century', 11, 'bold'),text = "The Result--",fg="white", bd = 11, anchor = "w").place(x=98, y=354) 
txtService = Entry(root, font = ('Century', 11, 'bold'),textvariable = Result, bd = 10, insertwidth = 4,bg = "white", justify = 'right').place(x=343, y=354)

import base64 

def generateKey(string, key):
	key = list(key)
	if len(string) == len(key):
		return(key)
	else:
		for i in range(len(string) -
					len(key)):
			key.append(key[i % len(key)])
	return("" . join(key))
	

def cipherText(string, key):
	cipher_text = []
	for i in range(len(string)):
		x = (ord(string[i]) +
			ord(key[i])) % 26
		x += ord('A')
		cipher_text.append(chr(x))
	return("" . join(cipher_text))
	

def originalText(cipher_text, key):
	orig_text = []
	for i in range(len(cipher_text)):
		x = (ord(cipher_text[i]) -
			ord(key[i]) ) 
		x += ord('A')
		orig_text.append(chr(x))
	return("" . join(orig_text))
	


def Ref():
	print("Message= ", (Msg.get()))

	string = Msg.get()
	keyword = key.get()
	k = generateKey(string, keyword)
	m = mode.get()

	if (m == 'e'):
		Result.set(cipherText(string, k))
	else:
		Result.set(originalText(string, k))

btnTotal =Button(root, text='Show Message', bg='#7FFF00', font=('verdana', 12, 'normal'), command=Ref).place(x=112, y=444)
btnReset =Button(root, text='Reset', bg='#FF3030', font=('verdana', 12, 'normal'), command=Reset).place(x=250, y=444)
btnExit =Button(root, text='Exit', bg='#A020F0', font=('verdana', 12, 'normal'), command=qExit).place(x=315, y=444)

root.mainloop()
