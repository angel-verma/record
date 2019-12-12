from tkinter import*
from tkinter import ttk, messagebox
import time
import os


class File_App:
    def __init__(self):
        self.root = Tk()
        self.root.title("File Based Record System")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="File Based Record System",
                      bd=5, relief=GROOVE, font="arial 35 bold", pady=10)
        title.pack(fill=X)

        student_frame = Frame(self.root, bd=10, relief=GROOVE)
        student_frame.place(x=20, y=100, height=420)

        # ==========All Variables===========
        self.sid = StringVar()
        self.name = StringVar()
        self.course = StringVar()
        self.address = StringVar()
        self.city = StringVar()
        self.contact = StringVar()
        self.date = StringVar()
        self.degree = StringVar()
        self.idproof = StringVar()
        self.payment = StringVar()

        # =============inside student frame===================
        stitle = Label(student_frame, text="STUDENT DETAILS",
                       font="arial 20 bold")
        stitle.grid(row=0, columnspan=4, pady=20)

        lsid = Label(student_frame, text="Student ID", font="arial 16 bold")
        lsid.grid(row=1, column=0, padx=10, sticky=W)
        tsid = Entry(student_frame, bd=5, relief=GROOVE,
                     width=20, font="arial 15 bold", textvariable=self.sid)
        tsid.grid(row=1, column=1, padx=10, pady=10)

        lname = Label(student_frame, text="Name", font="arial 16 bold")
        lname.grid(row=2, column=0, padx=10, sticky=W)
        tname = Entry(student_frame, bd=5, relief=GROOVE,
                      width=20, font="arial 15 bold", textvariable=self.name)
        tname.grid(row=2, column=1, padx=10, pady=10)

        lcontact = Label(student_frame, text="Contact No",
                         font="arial 16 bold")
        lcontact.grid(row=1, column=2, padx=10, sticky=W)
        tcontact = Entry(student_frame, bd=5, relief=GROOVE,
                         width=20, font="arial 15 bold", textvariable=self.contact)
        tcontact.grid(row=1, column=3, padx=10, pady=10)

        ldob = Label(student_frame, text="Date(dd-mm-yyyy)",
                     font="arial 16 bold")
        ldob.grid(row=2, column=2, padx=10, sticky=W)
        tdob = Entry(student_frame, bd=5, relief=GROOVE,
                     width=20, font="arial 15 bold", textvariable=self.date)
        tdob.grid(row=2, column=3, padx=10, pady=10)

        lcourse = Label(student_frame, text="Course", font="arial 16 bold")
        lcourse.grid(row=3, column=0, padx=10, sticky=W)
        tcourse = Entry(student_frame, bd=5, relief=GROOVE,
                        width=20, font="arial 15 bold", textvariable=self.course)
        tcourse.grid(row=3, column=1, padx=10, pady=10)

        ldegree = Label(student_frame, text="Select Degree",
                        font="arial 16 bold")
        ldegree.grid(row=3, column=2, padx=10, sticky=W)
        combodegree = ttk.Combobox(
            student_frame, width=19, state="readonly", font="arial 15 bold", textvariable=self.degree)
        combodegree['values'] = ("BCA", "BBA", "MCA", "MBA", "BTech", "MTech")
        combodegree.grid(row=3, column=3, padx=10, pady=10)

        laddress = Label(student_frame, text="Address", font="arial 16 bold")
        laddress.grid(row=4, column=0, padx=10, sticky=W)
        taddress = Entry(student_frame, bd=5, relief=GROOVE,
                         width=20, font="arial 15 bold", textvariable=self.address)
        taddress.grid(row=4, column=1, padx=10, pady=10)

        lid = Label(student_frame, text="Id Proof", font="arial 16 bold")
        lid.grid(row=4, column=2, padx=10, sticky=W)
        comboid = ttk.Combobox(student_frame, width=19,
                               state="readonly", font="arial 15 bold", textvariable=self.idproof)
        comboid['values'] = ("Voter Id", "Adhar Card",
                             "Student Id", "Pan Card", "Driving Licence")
        comboid.grid(row=4, column=3, padx=10, pady=10)

        lcity = Label(student_frame, text="City", font="arial 16 bold")
        lcity.grid(row=5, column=0, padx=10, sticky=W)
        tcity = Entry(student_frame, bd=5, relief=GROOVE,
                      width=20, font="arial 15 bold", textvariable=self.city)
        tcity.grid(row=5, column=1, padx=10, pady=10)

        lpayment = Label(student_frame, text="Payment Mode",
                         font="arial 16 bold")
        lpayment.grid(row=5, column=2, padx=10, sticky=W)
        combopayment = ttk.Combobox(
            student_frame, width=19, state="readonly", font="arial 15 bold", textvariable=self.payment)
        combopayment['values'] = (
            "Cash", "Phonepe", "Paytm", "Internet Banking", "Credit Card")
        combopayment.grid(row=5, column=3, padx=10, pady=10)

        # ============button frame===========
        bframe = Frame(self.root, bd=5, relief=GROOVE)
        bframe.place(x=18, y=550)

        bsave = Button(bframe, text="Save",
                       font="arial 15 bold", bd=5, width=18, command=self.save)
        bsave.grid(row=0, column=0, padx=10, pady=10)

        bdel = Button(bframe, text="Delete",
                      font="arial 15 bold", bd=5, width=18, command=self.delete)
        bdel.grid(row=0, column=1, padx=10, pady=10)

        bclear = Button(bframe, text="Clear",
                        font="arial 15 bold", bd=5, width=18, command=self.clear)
        bclear.grid(row=0, column=2, padx=10, pady=10)

        blogout = Button(bframe, text="Logout",
                         font="arial 15 bold", bd=5, width=18,command=self.logout)
        blogout.grid(row=0, column=3, padx=10, pady=10)

        bexit = Button(bframe, text="Exit",
                       font="arial 15 bold", bd=5, width=18, command=self.exit_)
        bexit.grid(row=0, column=4, padx=10, pady=10)

        # ==============file frame=====================
        file_frame = Frame(self.root, bd=5, relief=GROOVE)
        file_frame.place(x=900, y=100, width=380, height=420)

        file_title = Label(file_frame, text="ALL FILES",
                           font="arial 20 bold", bd=5, relief=GROOVE)
        file_title.pack(side=TOP, fill=X)

        scroll_y = Scrollbar(file_frame, orient=VERTICAL)
        self.file_list = Listbox(file_frame, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.file_list.yview)
        self.file_list.pack(fill=BOTH, expand=1)
        self.file_list.bind("<ButtonRelease-1>", self.get_data)
        self.show_files()
        self.root.mainloop()

    # file saving and updating
    def save(self):
        present = "no"
        if self.sid.get() == "":
            messagebox.showerror("Error", "Student Id must be required!!!")
        else:
            f = os.listdir("files/")
            if len(f) > 0:
                for i in f:
                    if i.split(".")[0] == self.sid.get():
                        present = "yes"
                if present == "yes":
                    ask = messagebox.askyesno(
                        "Delete", "File already present...\n Do you want to update it???")
                    if ask > 0:
                        self.save_files()
                        messagebox.showinfo(
                            "Update", "Record has been updated successfully!!")
                        self.show_files()
                else:
                    self.save_files()
                    messagebox.showinfo(
                        "Saved", "Record has been saved successfully!!")
                    self.show_files()
            else:
                self.save_files()
                messagebox.showinfo(
                    "Saved", "Record has been saved successfully!!")
                self.show_files()

    def save_files(self):
        f = open("files/"+str(self.sid.get())+".txt", "w")
        f.write(
            str(self.sid.get())+"," +
            str(self.name.get())+"," +
            str(self.course.get())+"," +
            str(self.address.get())+"," +
            str(self.city.get())+"," +
            str(self.contact.get())+"," +
            str(self.date.get())+"," +
            str(self.degree.get())+"," +
            str(self.idproof.get())+"," +
            str(self.payment.get())
        )
        f.close()
        # messagebox.showinfo("Success", "Record has been saved!")
        # self.show_files()

    def show_files(self):
        files = os.listdir("files/")
        self.file_list.delete(0, END)
        if len(files) > 0:
            for file in files:
                self.file_list.insert(END, file)

    def get_data(self, event):
        get_cursor = self.file_list.curselection()
        # print(self.file_list.get(get_cursor))
        f1 = open("files/"+self.file_list.get(get_cursor))
        value = []
        for f in f1:
            value = f.split(",")
        # print(value)
            self.sid.set(value[0])
            self.name.set(value[1])
            self.course.set(value[2])
            self.address.set(value[3])
            self.city.set(value[4])
            self.contact.set(value[5])
            self.date.set(value[6])
            self.degree.set(value[7])
            self.idproof.set(value[8])
            self.payment.set(value[9])

    def clear(self):
        self.sid.set("")
        self.name.set("")
        self.course.set("")
        self.address.set("")
        self.city.set("")
        self.contact.set("")
        self.date.set("")
        self.degree.set("")
        self.idproof.set("")
        self.payment.set("")

    def delete(self):
        present = "no"
        if self.sid.get() == "":
            messagebox.showerror("Error", "Student Id must be required!!!")
        else:
            f = os.listdir("files/")
            if len(f) > 0:
                for i in f:
                    if i.split(".")[0] == self.sid.get():
                        present = "yes"
                if present == "yes":
                    ask = messagebox.askyesno(
                        "Delete", "Do you really want to delete???")
                    if ask > 0:
                        os.remove("files/"+self.sid.get()+".txt")
                        messagebox.showinfo(
                            "Success", "File Deleted Successfully")
                        self.show_files()
                else:
                    messagebox.showerror("Error", "File not found!!")


    def exit_(self):
        ask=messagebox.askyesno("Exit","Do you really want to exit??")
        if ask>0:
            self.root.destroy()

    def logout(self):
        self.root.destroy()
        import login

# root = Tk()
# ob = File_App(root)
# root.mainloop()
