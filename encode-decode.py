from tkinter import * # a standard GUI library
import base64 # this module provides a method to encode binary data to ASCII character and decode that vice-versa

# steps that would follow to build the project
'''
1. import module
2. create display window 
3. define function
4. define labels and buttons
'''

# 2. here we will initialize window

root = Tk()  # in this step we have initialized tkinter which will obtain our window
root.geometry('550x400') # set the width and height of window
root.resizable(0, 0) # set fixed size of window
root.title("Security - message Encoder and Decoder") # set the title of window

Label(root, text='ENCODE DECODE', font='arial 20 bold').pack()
Label(root, text='SECURITY', font='arial 20 bold').pack(side=BOTTOM)
# here the label widget is used to show more than one line of text that user can't modify
# root is the window on which we are working
# text depends on your choice which we want to display
# pack forms an organized widget in block

# now we will define variables
Text = StringVar()  # this veriable will store the text to be encoded or decoded
private_key = StringVar() # it will store private key used to encode and decode
mode = StringVar() # whether you want encoding mode or decoding mode
Result = StringVar() # store the result

# function to encode text using vigenere cipher algorithm
def Encode(key, message): # passing to variables as arguements
    enc = [] # empty list

    for i in range(len(message)): # i % len(key) will give remainder of division between i and len(key)
        # and that remainder is used as an index of key
        key_c = key[i % len(key)] # here key_c is storing the value of key at that index
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256)) # here the ord function takes string unicode
        # value and returns integers unicode value
    return base64.urlsafe_b64encode("".join(enc).encode()).decode() # chr function takes an integer arguement and return the string
# ord(message[i] convert the value of message at index i into integer value
# similarly ord(key_c) function key_c value in integer value
# ord(message[i]) + ord(key_c)) % 256 gives the remainder of division of addition of ord(message[i]) + ord(key_c)) with 256 and passes that
# chr() function
# now chr() will convert this integer value into string and store to enc

# base64.urlsafe_b64encode encode a string
# join will give the concatenated output string output obtained from any list, tuple, dictionary
# encode() method returns utf-8 encoded message of the string
# decode() method decode the string

# function to decode text
def Decode(key, message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()

    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
    return "".join(dec)

# function to set mode
def Mode():
    if (mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set("Invalid mode choose between e or d")

# If the mode set by the user is ‘e’ then the Encode() function will be called
# If the mode set to ‘d‘ then the Decode() function will be called
# Else print ‘invalid mode choose between e or d’
# private_key.get() and Text.get() values are pass to the arguments of Encode() and Decode() function


# function to exit window
def Exit():
    root.destroy()
# root.destroy() will quit the program by stopping the mainloop()

# function to rest window
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")
# this function will set all variables to empty string

# labels and buttons
Label(root, font= 'arial 12 bold', text='MESSAGE').place(x= 60,y=60)
Entry(root, font = 'arial 10', textvariable = Text, bg = 'ghost white').place(x=290, y = 60)

Label(root, font = 'arial 12 bold', text ='KEY').place(x=60, y = 90)
Entry(root, font = 'arial 10', textvariable = private_key , bg ='ghost white').place(x=290, y = 90)

Label(root, font = 'arial 12 bold', text ='MODE(e-encode, d-decode)').place(x=60, y = 120)
Entry(root, font = 'arial 10', textvariable = mode , bg= 'ghost white').place(x=290, y = 120)
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='ghost white').place(x=290, y = 150)

Button(root, font = 'arial 10 bold', text = 'RESULT'  ,padx =2,bg ='LightGray' ,command = Mode).place(x=60, y = 150)

Button(root, font = 'arial 10 bold' ,text ='RESET' ,width =6, command = Reset,bg = 'LimeGreen', padx=2).place(x=80, y = 190)

Button(root, font = 'arial 10 bold',text= 'EXIT' , width = 6, command = Exit,bg = 'OrangeRed', padx=2, pady=2).place(x=180, y = 190)

root.mainloop()






