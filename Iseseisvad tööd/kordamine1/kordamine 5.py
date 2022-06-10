from tkinter import * #importdib

def save_info(): #salvestab info
    firstname_info = firstname.get() #võtab kastist infot
    lastname_info = lastname.get()# võtab kastist infot
    age_info = age.get()# võtab kastist infot
    age_info = str(age_info) #võtab kastist infot
    print(firstname_info, lastname_info, age_info) #prindib

    file = open("user.txt", "w") #
    file.write(firstname_info) #kirjtuab faili
    file.write(lastname_info) #kirjutab faili
    file.write(age_info) # kirjutab faili
    file.close() #sulgeb faili #
    print("user", firstname_info, "Has been registered successfully") #prindib et user on edukalt registreerinud

    firstname_entry.delete(0, END) #kustutab kastist info
    lastname_entry.delete(0, END) #kustutab kastist info
    age_entry.delete(0 , END) #kustutab kastist info

screen = Tk() #loob ekraani
screen.geometry("500x500") #ekraani suurus 500x500
screen.title("Python form") #vasakul üleval ääres on kirjsa "python form"
heading = Label(text = "Python form", bg = "grey", fg = "black", width = "500", height = "3") #teeb erkaani üles halliääre
heading.pack() #esitab halli ekraani äärise

firstname_text = Label(text = "Firstname *",) # tekst "firstname"
lastname_text = Label(text = "Lastname *",) #Tekst "lastname"
age_text = Label(text = "age *") #tekst "age
firstname_text.place(x = 15, y = 70) #firstname teksti asukoht
lastname_text.place(x = 15, y = 140) #lastname teksti asukoht
age_text.place(x = 15, y = 210) #age teksti asukoht

firstname = StringVar() #sõne
lastname = StringVar() #sõne
age = IntVar() #muutuja täisnumber

firstname_entry = Entry(textvariable =firstname, width = "30") #lahter kuhu esinimi kirjutada
lastname_entry = Entry(textvariable = lastname, width = "30")   #lahter kuhu perekonna nimi kirjutada
age_entry = Entry(textvariable = age, width = "30") #lahter kuhu vanus kirjutada

firstname_entry.place(x = 15, y = 100) #lahter kuhu esinimi kirjutada
lastname_entry.place(x = 15, y = 180) #lahter kuhu perekonna nimi kirjutada
age_entry.place(x = 15, y = 240) #lahter kuhu vanus kirjutada

register = Button(screen,text = "Register", width = "30", height = "2", command = save_info, bg = "grey") #teeb alla nupu kus on kirjas register
register.place(x = 15, y = 290) #registreerimis nupu asukoht
screen.mainloop() #alustab mainloopi