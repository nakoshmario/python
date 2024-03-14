from tkinter import *

root = Tk()
# root.title('Hello world')
root.geometry('400x300')
root.resizable(0,1)


# count = 0
# def test():
#     global count
#     count += 1
#     entry['text'] = count
#     # print('Hello')

# def save():
#     test = entry.get()
#     print(test)

# lab = tkinter.Label(root,text='This is a label',bg='yellow',fg='red',width=15,height=10,font=("Arial", 25,'bold'),anchor='n')
# lab.pack()


# lbl = tkinter.Label(root,width=30)ed
# lbl.pack()
# btn = tkinter.Button(root,text='кликни',command=test)
# btn.pack()

# entry = tkinter.Entry(root,width=30)
# entry.pack()

# btn2 = tkinter.Button(root,text='кликни',command=save)
# btn2.pack()

# tkinter.mainloop()




   


# def red():
#     lab['text'] = 'красный'
#     entry.delete(0, END)
#     entry.insert(0,'#FF0000')
# def yellow():
#     lab['text'] = 'желтый'
#     entry.delete(0, END)
#     entry.insert(0,'#FFFF00')
# def green():
#     lab['text'] = 'зеленый'
#     entry.delete(0, END)
#     entry.insert(0,'#008000')



# lab = Label(root)
# lab.pack(fill='x')
# entry = Entry(root)
# entry.pack(fill='x')


# btn = Button(root,bg = 'green', command=red)
# btn.pack(fill='x')

# btn2 = Button(root, command=yellow,bg='yellow')
# btn2.pack(fill='x')
# btn3 = Button(root,command=green,bg='red')
# btn3.pack(fill='x')



# mainloop()

# ---------------------


# форма регистрации


def save():
    test = entry.get()
    test2 = entry2.get()
    test3 = entry3.get()
    print(test)
    print(test2)
    print(test3)
    saving()
    

    
def saving():
    # with open ('data.txt', 'r',encoding='utf-8') as file1:
    #     test = file1.readlines()
    #     data = f"{entry.get()}\n{entry2.get()}\n{entry3.get()}" 
    #     file1.write(data)
    with open('data.txt','r',encoding= "utf-8") as file :
        test = file.readlines()
    data = entry.get()
    for i in test:
        if data == i.strip('\n'):
            lab['text'] = 'уже зарегистрирован'
            entry.delete(0,END)
            return
    with open('data.txt','a',encoding='utf-8') as file1:
        file1.write(f'{entry.get()}\n')
        file1.write(f'{entry2.get()}\n')
        file1.write(f'{entry3.get()}\n')
        lab['text'] = 'зарегистрирован'
# проверка на заполненость полей

        
lab = Label(root)
lab.pack()
entry = Entry(root,width=40,)
entry.pack()
entry2 = Entry(root,width=40,)
entry2.pack()
entry3 = Entry(root,width=40,)
entry3.pack()
btn = Button(root,text='регистрация',command=saving)
btn.pack()








mainloop()