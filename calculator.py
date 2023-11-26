# Smart Scientific Calculator
# scientific buttons: function sc
# number and mathematical buttons(0-9) & (+,-,*,/,%): function click
# equal button: function evaluate
# backspace button: bksps function
# clear button: clear fun
from tkinter import *
import math
from pygame import mixer
import speech_recognition
# mixer module helps us to play any sound (pip install pygame)
#pip install speechrecognition
#pip install pyaudio
mixer.init()

# To create main window (window variable: root)
root = Tk()
root.title("Scientific Calculator")
root.config(bg='#17161b')
root.geometry('395x628+100+100')

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
def lcm(a,b):
    l=math.lcm(a,b)
    return l
def hcf(a,b):
    h=math.gcd(a,b)
    return h

operations={'ADD':add,'ADDITION':add,'SUM':add,'PLUS':add,'SUMMATION':add,
            'SUBTRACTION':sub,'DIFFERENCE':sub,'MINUS':sub,'SUBTRACT':sub,
            'PRODUCT':mul,'MULTIPLICATION':mul,'MULTIPLY':mul,'INTO':mul,
            'DIVIDE':div,'DIVISION':div,'DIV':div,
            'LCM':lcm,'HCF':hcf,
            'MOD':mod,'MODULUS':mod,'REMAINDER':mod}

def findNumbers(t):
    l=[]
    for num in t:
        try:
            l.append(int(num))
        except ValueError:
            pass
    return l

def audio():
    mixer.music.load('music1.mp3')
    mixer.music.play()
    # to provide voice commands (module to convert audio-> text)
    sr=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as m:
        try:
            # sentence consideration as per duration
            sr.adjust_for_ambient_noise(m,duration=0.2)
            voice=sr.listen(m)
            # converts voice->text
            text=sr.recognize_google(voice)
            mixer.music.load('music2.mp3')
            mixer.music.play()
            text_list=text.split(" ")
            print(text_list)
            for word in text_list:
                if word.upper() in operations.keys():
                    l=findNumbers(text_list)
                    print(l)
                    result=operations[word.upper()](l[0],l[1]) #mul(5.0,6.0)
                    e.delete(0,END)
                    e.insert(END,result)
                else:
                    pass

        except:
            pass

micImage = PhotoImage(file='microphone.png')
# micImage=micImage.zoom(8)
# micImage=micImage.subsample(20)
micButton= Button(root, image=micImage,bd=0,bg="#17161b",activebackground="#17161b",command=audio)
micButton.grid(row=0, column=0)
# relief--> simulated 3d effect around
# outside of widget (sunken,groove,raised,ridge,flat,solid...)
# entry takes everything in string
e = Entry(root, width=16, borderwidth=5, bd=10, relief=RIDGE, fg="white", bg="black", font=('arial', 20, 'bold'))
# better than 'pack' is 'grid' --> allows to take rows and columns
e.grid(row=0, column=1, columnspan=5, padx=10, pady=15)

def click(to_print):
    # whatever is there in entry, get it for me
    old = e.get()
    # everything gets deleted
    e.delete(0, END)
    e.insert(0, old + to_print)
    return

def clear():
    e.delete(0, END)
    return

def bksps():
    current = e.get()
    length = len(current) - 1
    e.delete(length, END)

def evaluate():
    ans = e.get()
    ans = eval(ans)
    e.delete(0, END)
    e.insert(0, ans)

def sc(event):
    key = event.widget
    # now in event format,needs in text
    text = key['text']
    no = e.get()  # no in string, then further to float
    result = ''
    if text == 'deg':
        result = str(math.degrees(float(no)))
    if text == 'sin':
        result = str(math.sin(float(no)))
    if text == "sinh":
        result = str(math.sinh(float(no)))
    if text == 'cos':
        result = str(math.cos(float(no)))
    if text == "cosh":
        result = str(math.cosh(float(no)))
    if text == 'tan':
        result = str(math.tan(float(no)))
    if text == "tanh":
        result = str(math.tanh(float(no)))
    if text == 'log':
        result = str(math.log10(float(no)))
    if text == 'ln':
        result = str(math.log(float(no)))
    if text == 'Sqrt':
        result = str(math.sqrt(float(no)))
    if text == 'rad':
        result = str(math.radians(float(no)))
    if text == 'x!':
        result = str(math.factorial(int(no)))
    if text == '1/x':
        result = str(1 / (float(no)))
    if text == 'x\u02b8':
        result = e.insert(END, '**')
        return
    if text == 'pi':
        if no == "":
            result = str(math.pi)
        if no == "180/":
            result = str(180 / math.pi)
        else:
            result = str(float(no) * math.pi)
    if text == 'e':
        if no == "":
            result = str(math.e)
        else:
            result = str(math.e ** float(no))
    if text== '+/-':
        i=1
        result= str((-1)**i*float(no))
    e.delete(0, END)
    e.insert(0, result)

button_text_list = ["sin","cos","tan","rad","log",
                    "sinh","cosh","tanh","deg","ln",
                    "(",")","+/-","x!","1/x",
                    "//","C","%","Bksp",chr(247),
                    "x\u02b8","7","8","9","*",
                    "sqrt","4","5","6","-",
                    "pi","1","2","3","+",
                    "e","00","0",".","="]
commands = ["","","","","",
            "","","","","",
            lambda: click("("),lambda: click(")"),"","","",
            lambda: click("//"),lambda: clear(),lambda: click("%"),lambda: bksps(),lambda: click("/"),
            "",lambda: click("7"),lambda: click("8"),lambda: click("9"),lambda: click("*"),
            "",lambda: click("4"),lambda: click("5"),lambda: click("6"),lambda: click("-"),
            "",lambda: click("1"),lambda: click("2"),lambda: click("3"),lambda: click("+"),
            "",lambda: click("00"),lambda: click("0"),lambda: click("."),lambda: evaluate()]
rowvalue = 1
columnvalue = 0
for i in range(len(button_text_list)):
    button = Button(root, text=button_text_list[i], padx=28, pady=10, relief=RIDGE, bg="#2a2d36", fg="#fff", width=1,
                    height=1, bd=2, font=('arial', 18, 'bold'), activebackground='grey', command=commands[i])
    if (commands[i] == ""):
        button.bind("<Button-1>", sc)
    button.grid(row=rowvalue, column=columnvalue)
    columnvalue += 1
    if (columnvalue > 4):
        rowvalue += 1
        columnvalue = 0

# the label won't be displayed in window until packed
# l=Label(root,text="Musu",bg="Blue")
# l.pack()
# to keep window stay until we don't exit
root.mainloop()