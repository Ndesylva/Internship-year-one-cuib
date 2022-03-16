##importing the various  modules

from tkinter import *
import base64

#initialize window
root = Tk() #tk() is used to iniitialize tkinter
root.geometry('500x300') #geometry()used primarily to set the width and height
root.resizable(0, 0)

#title of the window
root.title("Message Encode and Decode")#title()sets the title of the window to be opened



#label widget
#label()func is used to display one or more than one line of text that cant be modified by users
#pack is used to organize the widgets in blocks
Label(root, text ='ENCODE and  DECODE', font = 'arial 20 bold').pack()
Label(root, text ='', font = 'arial 20 bold').pack(side =BOTTOM)


#define variables

Text = StringVar() #text variable stores the message to be encoded
private_key = StringVar()#stores the private key for encoding and decoding
mode = StringVar() #use to make the choice between encoding and decoding
Result = StringVar()#stores the results


##define functions

#function to encode
#ord()funtion bbasically takes a sting value and returns its positional integer value
#chr()takes an integer and returns a string and then stores it to enc
#join() joins each element of a list, string by a string separator and returns the conc string.
#decode()decodes the string while encode()returns utf-8 of the sting .
def Encode(key,message):
    enc=[] #declarirng an empty list
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))

    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

#function to decode, decodes the contents from input and writes the result in binary to the output

def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))

    return "".join(dec)

#function to set mode, user choses the modes either to encode or decode by iputing the required letters
def Mode():
    if(mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')



#Function to exit window

def Exit():
    root.destroy()


#Function to reset
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")


# Label and Buttons
#entry() is used to create an input text field
#button()widget used to display button on the window created

#Message
Label(root, font= 'arial 12 bold', text='MESSAGE').place(x= 60,y=60)
Entry(root, font = 'arial 10', textvariable = Text, bg = 'ghost white').place(x=290, y = 60)

#key
Label(root, font = 'arial 12 bold', text ='KEY').place(x=60, y = 90)
Entry(root, font = 'arial 10', textvariable = private_key , bg ='ghost white').place(x=290, y = 90)

#mode
Label(root, font = 'arial 12 bold', text ='MODE(e-encode, d-decode)').place(x=60, y = 120)
Entry(root, font = 'arial 10', textvariable = mode , bg= 'ghost white').place(x=290, y = 120)

#RESULTS
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='ghost white').place(x=290, y = 150)

##result button
Button(root, font = 'arial 10 bold', text = 'RESULT'  ,padx =2,bg ='LightGray' ,command = Mode).place(x=60, y = 150)


#reset button
Button(root, font = 'arial 10 bold' ,text ='RESET' ,width =6, command = Reset,bg = 'LimeGreen', padx=2).place(x=80, y = 190)

#exit button
Button(root, font = 'arial 10 bold',text= 'EXIT' , width = 6, command = Exit,bg = 'OrangeRed', padx=2, pady=2).place(x=180, y = 190)
root.mainloop()
