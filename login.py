from tkinter import*
from tkinter import messagebox


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("File Based Record System")
        self.root.geometry("1350x700+0+0")

        self.username = StringVar()
        self.password = StringVar()

        f1 = Frame(self.root, bd=10, relief=GROOVE)
        f1.place(x=450, y=150, height=350)

        title = Label(f1, text="Login System", font=(
            "times new roman", 30, "bold"))
        title.grid(row=0, columnspan=2, pady=20)

        lusername = Label(f1, text="Username", font=(
            "times new roman", 20, "bold"))
        lusername.grid(row=1, column=0, pady=10, padx=10)

        tusername = Entry(f1, bd=5, relief=GROOVE, width=25,
                          font="arial 14 bold", textvariable=self.username)
        tusername.grid(row=1, column=1, padx=10, pady=10)

        lpassword = Label(f1, text="Password", font=(
            "times new roman", 20, "bold"))
        lpassword.grid(row=2, column=0, pady=10, padx=10)

        tpassword = Entry(f1, bd=5, relief=GROOVE, width=25,
                          font="arial 14 bold", textvariable=self.password, show="*")
        tpassword.grid(row=2, column=1, padx=10, pady=10)

        blogin = Button(f1, text="Login", font="arial 15 bold",
                        bd=5, width=10, command=self.login)
        blogin.place(x=10, y=250)

        breset = Button(f1, text="Reset", font="arial 15 bold",
                        bd=5, width=10, command=self.reset)
        breset.place(x=155, y=250)

        bexit = Button(f1, text="Exit", font="arial 15 bold",
                       bd=5, width=10, command=self.exit_)
        bexit.place(x=300, y=250)

    def login(self):
        # print(self.username.get(), self.password.get())
        if self.username.get() == "komal" and self.password.get() == "1234":
            # messagebox.showinfo(
            #     "Info", f"Welcome {self.username.get()} and your password is :{self.password.get()}")
            self.root.destroy()
            import software
            software.File_App()
        else:
            messagebox.showerror("Error", "Invalid username or password!!")

    def reset(self):
        self.username.set("")
        self.password.set("")

    def exit_(self):
        option = messagebox.askyesno("Exit", "Do you really want to exit??")
        if option > 0:
            self.root.destroy()
        else:
            return


root = Tk()
ob = Login(root)
root.mainloop()
