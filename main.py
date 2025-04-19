#Love Calculator

from tkinter import *
from tkinter import messagebox

loveScore = ''

def calculate_loveScore(own_name, partner_name):
    true = 'true'
    love = 'love'
    
    #takes two names & lowering them
    name1 = own_name.lower()
    name2 = partner_name.lower()
    
    #concatenating both names
    concatenated_name = name1 + name2
    
    #looking for 'true' in concatenated_name
    true_counted = []
    for char in true:
        counted = concatenated_name.count(char)
        true_counted.append(counted)
    #print(true_counted)
    
    #looking for 'love' in concatenated_name
    love_counted = []
    for char in love:
        counted = concatenated_name.count(char)
        love_counted.append(counted)
    #print(love_counted)
    
    true_counts = true_counted[0] + true_counted[1] + true_counted[2] + true_counted[3]
    #print(true_counts)
    
    love_counts = love_counted[0] +  love_counted[1] +  love_counted[2] +  love_counted[3]
    #print(love_counts)
    
    love_score = int(str(true_counts) +str(love_counts))
    #print("love score is: ",love_score)
    
    global loveScore
    
    if love_score < 10 or love_score > 90:
        loveScore = f"Your love score is {love_score} and you go together like coke and mentos."
        
    elif love_score >= 40 and love_score <= 50:
        loveScore = f"Your love score is {love_score} and you are alright together."
        
    else:
        loveScore = f"Your love score is {love_score}."


def display_loveScore():
    own_name = own_name_var.get()
    partner_name = partner_name_var.get()
    
    calculate_loveScore(own_name, partner_name)
    
    #displaying Score
    
    messagebox.showinfo('Love Calculator', f'{loveScore}')
    own_name_var.set('')
    partner_name_var.set('')

def about():
    messagebox.showinfo('About', 'Love Calculator by Hassan Khan.')

if __name__ == '__main__':
    root = Tk()
    root.title('Love Calculator')
    root.geometry('700x380+600+400')
    root.resizable(False,False)
    icon_image = PhotoImage(file='icon.png')
    root.iconphoto(False, icon_image)

    background_image = PhotoImage(file='background.png')
    Label(root,image=background_image).place(x=-2, y=0)
    
    Label(root, text='Love Calculator', font=('Constantia', '42', 'bold'), bg='#B08B83').place(x=245, y=10)
    
    your_name = Label(root, text='Your Name', font=('Constantia', '17'), bg='#B08B83').place(x=360, y=150)
    partner_name = Label(root, text='Partner Name', font=('Constantia', '17'), bg='#B08B83').place(x=336, y=190)
    
    own_name_var = StringVar()
    partner_name_var = StringVar()
    
    own_name_entry = Entry(root, textvariable=own_name_var, font=('Constantia', '15')).place(x=482, y=153, width=200, height=25)
    partner_name_entry = Entry(root, textvariable=partner_name_var, font=('Constantia', '15')).place(x=482, y=193, width=200, height=25)

    
    Button(root, text='Submit', font=('Constantia', '18'), bg='#B08B83', cursor='hand2', command=display_loveScore).place(x=515, y=232, width=130, height=35)
    
    about_image = PhotoImage(file='about.png')
    Button(root, image=about_image, cursor='hand2', bg='#B08B83', activebackground='#B08B83', bd=0, command=about).place(x=640, y=325)
    
    root.mainloop()