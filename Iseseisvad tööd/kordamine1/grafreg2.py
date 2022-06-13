from tkinter import *
import os

# Defineerivad delete funktsioonid
def delete2():
    screen3.destroy()

def delete3():
    screen4.destroy()

def delete4():
    screen5.destroy()

# Defineerib login successi
def login_success():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3, text = "Login Success").pack()
    Button(screen3, text = "OK", command = delete2).pack()
# Defineerib password_not_recognised'i
def password_not_recognised():
    global screen4
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3, text = "Password Error").pack()
    Button(screen3, text = "OK", command = delete3).pack()
#defineerib user_not_found'i
def user_not_found():
    global screen5
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3, text = "User Not Found").pack()
    Button(screen3, text = "OK", command = delete4).pack()

# defineerib register_user'i
def register_user():
    print("working")
    username_info = username.get () #Võtab usernamei info
    password_info = password.get ()#Võtab passwordi info

# SALVESTAB Kasutaja usernamei ja passwordi faili
    file=open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()
    # Kustutab entry'd
    username_entry.delete(0, END)
    password_entry.delete(0, END)
# Näitab ekraanil teksti
    Label(screen1, text = "Registration Success", fg  = "green", font = ("calibri", 11)).pack()
# Defineerib login_verify
def login_verify():

    username1 = username_verify.get()# kui username õige siis verifyitakse username
    password1 = password_verify.get()# kui password õige siis verifyitakse password
    # Entryd kustutatakse
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
# Otsib failide seast ja kontrollib infot
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognised()
    else:
            user_not_found()


def register() :
    global screen1 # defineerib screen1
    screen1 = Toplevel (screen)
    screen1.title("Register") #Register nupu tekst
    screen1.geometry("300x250")#Register nupu suurus
# Defineerib erinevad funktsioonid
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar ()
    password = StringVar ()
# Loob Erinevad nupud, mis registreerimiseks vajalikud
    Label(screen1, text = "Please enter details below").pack ()
    Label(screen1, text = "").pack ()
    Label(screen1, text = "Username * ").pack ()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack ()
    Label(screen1, text = "Password * ").pack ()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack ()
    Label(screen1, text = "").pack ()
    Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack ()
# defineerib login'i
def login() :
    global screen2
    print("Login session started")
    # tekitab screeni ja selleks vajalikud asjad
    screen2 = Toplevel (screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text="Please enter details below to login").pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify
    username_verify = StringVar()# username verify on string
    password_verify = StringVar()# password verify on string

    global username_entry1
    global password_entry1
    # Tekitab vajalikud asjad Login ekraanile nupud ja muud vajalikud asjad
    Label(screen2, text="Username * ").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "Password * ").pack ()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "login", width = 10, height = 1, command = login_verify).pack()
#Kui vajutades login tuleb tekst.

def main_screen() :
   # Loob pealkirja ning erinevad nupud peamenüül.
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Notes 1.0")
    Label (text = "Notes 1.0", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)). pack ()
    Label (text = "") .pack()
    Button (text = "Login", height = "2", width = "30", command = login).pack ()
    Label (text = "").pack ()
    Button (text = "Register", height = "2", width = "30", command = register).pack ()

    screen.mainloop ()

main_screen()