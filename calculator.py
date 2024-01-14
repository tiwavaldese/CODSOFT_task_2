#import the entire tkinter library
from tkinter import *

#press button
def button_press(num):
    global equation_text
    
    equation_text= equation_text + str(num)
    
    equation_label.set(equation_text)

#equals to button
def equals():
    global equation_text
        
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
 
 #number divided by zero will throw an error       
    except ZeroDivisionError:
        equation_label.set('Error')
        equation_text=""
#random symbols will throw an error    
    except SyntaxError:
        equation_label.set('Syntaxerror')
        equation_text=""
    
#clean the operation   
def clear():
    global equation_text
    equation_label.set("")
    equation_text=""
#create a window section for the mathematical operation
window = Tk()
window.title("My Calculator Program")
window.geometry("550x550+500+100")
window.resizable(False,False)

equation_text = ""
equation_label = StringVar()

#setting a label within the window
label = Label(window, textvariable= equation_label, font='arial 20',
              fg='#483C32', bg= '#ADD8E6', height=2,width=24)
label.pack()

#setting a frame within the window
frame = Frame(window,bd=3,width=700,height=180,bg="#0096FF")
frame.pack()

#values button
button1= Button(frame,text=7,height=1,width=3,bg='skyblue',fg='white',
                font='arial 35',command=lambda: button_press(7))
button1.grid(row=0,column=0,padx=3,pady=3)

button2= Button(frame,text=8,height=1,width=3,bg='skyblue',fg='white',
                font='arial 35',command=lambda: button_press(8))
button2.grid(row=0,column=1,padx=3,pady=3)

button3= Button(frame,text=9,height=1,width=3,bg='skyblue',fg='white',
                font='arial 35',command=lambda: button_press(9))
button3.grid(row=0,column=2,padx=3,pady=3)

button4= Button(frame,text=4,height=1,width=3,bg='skyblue',fg='white',
                font='arial 35',command=lambda: button_press(4))
button4.grid(row=1,column=0,padx=3,pady=3)

button5= Button(frame,text=5,height=1,width=3,bg='skyblue',fg='white',
                font='arial 35',command=lambda: button_press(5))
button5.grid(row=1,column=1,padx=3,pady=3)

button6= Button(frame,text=6,height=1,width=3,bg='skyblue',fg='white',
                font='arial 35',command=lambda: button_press(6))
button6.grid(row=1,column=2,padx=3,pady=3)

button7= Button(frame,text=1,height=1,width=3,bg='skyblue',fg='white',
                font='arial 35',command=lambda: button_press(1))
button7.grid(row=2,column=0,padx=3,pady=3)

button8= Button(frame,text=2,height=1,width=3,bg='skyblue',fg='white',
                font='arial 35',command=lambda: button_press(2))
button8.grid(row=2,column=1,padx=3,pady=3)

button9= Button(frame,text=3,height=1,width=3,bg='skyblue',fg='white',
                font='arial 35',command=lambda: button_press(3))
button9.grid(row=2,column=2,padx=3,pady=3)

button10= Button(frame,text=0,height=1,width=3,bg='skyblue',fg='white',
                 font='arial 35',command=lambda: button_press(0))
button10.grid(row=3,column=0,padx=3,pady=3)

#decimal button
decimal= Button(frame,text='.',height=1,width=3,bg='#0096FF',
                font='arial 35',command=lambda: button_press('.'))
decimal.grid(row=3,column=1,padx=3,pady=3)

#division button
division= Button(frame,text='/',height=1,width=3,bg='#0096FF',
                 font='arial 35',command=lambda: button_press('/'))
division.grid(row=0,column=3,padx=3,pady=3)

#multiply button
product= Button(frame,text='*',height=1,width=3,bg='#0096FF',
                font='arial 35',command=lambda: button_press('*'))
product.grid(row=1,column=3,padx=3,pady=3)

#minus button
difference= Button(frame,text='-',height=1,width=3,bg='#0096FF',
                   font='arial 35',command=lambda: button_press('-'))
difference.grid(row=2,column=3,padx=3,pady=3)

#addition button
sum= Button(frame,text='+',height=1,width=3,bg='#0096FF',font='arial 35',
            command=lambda: button_press('+'))
sum.grid(row=3,column=3,padx=3,pady=3)

#equals button
equals= Button(frame,text='=',height=1,width=3,bg='#0096FF',
               font='arial 35',command=equals)
equals.grid(row=3,column=2,padx=3,pady=3)

#clear button
clear= Button(window,text='clear',height=1,width=6,bg='skyblue',
              fg='brown',font='arial 35',command=clear)
clear.pack(padx=3,pady=3)


#frame = tk.Frame(master=window,bg="skyblue", padx=10)
#frame.pack()
#entry=tk.Entry(master=frame,relief=SUNKEN,borderwidth=3,width=30)
#entry.grid(row=0,column=0,columnspan=4,ipady=2,pady=2)

#print("Select Operations to perform: ")
#print("1.Addition\n"
      #"2.Substraction\n"
      #"3.Multiplication\n"
      #"4.Division")

#operation = input()
#Addition
#if operation == "1":
    #num1 =input("Input first number: ")
    #num2 = input("Input second number: ")
    #print("sum of "+ str(int(num1) + int(num2)))

#Substraction
#elif operation == "2":
    #num1 =input("Input first number: ")
    #num2 = input("Input second number: ")
    #print("difference of "+ str(int(num1) - int(num2)))

#Multiplication
#elif operation == "3":
    #num1 =input("Input first number: ")
    #num2 = input("Input second number: ")
    #print("product of "+ str(int(num1) * int(num2)))

#Division
#elif operation == "4":
    #num1 =input("Input first number: ")
    #num2 = input("Input second number: ")
    #print("result of "+ str(int(num1) / int(num2)))
    

#else:
    #print("Invalid entry")
    

window.mainloop()


