# this program developed by Mohammad Rasoul Azizi


# importing the module
from tkinter import *

# defination the phonebook class
class PhoneBook:

    # add class attributes

    # save the developer information in info variable
    info = """This program developed by
    Mohammad Rasoul Azizi
    azizi.mr1377@gmail.com"""

    # create a empty list for saving the Name contact
    Name_list = []

    # Create a empty list for saving the family contact
    famili_list = []

    # Create a empty list for saving the Phone number contact
    phone_list = []

    # Create a empty list for saving the address contact
    address_list = []

    # Create a empty list for saving the email contact
    email_list = []

    # Create a empty list for saving the cellphone contact
    cellphone_list = []

    # Create a empty list for saving the id contact
    id_list = []

    # defination the initial funtion
    def __init__(self) -> None:
        """This function is used to build the initial personalized page."""
        
        # create a object from tkinter module for create a window
        self.first_window = Tk()

        # give a title to the our screen
        self.first_window.title("PhoneBook")
        
        # give a size for our screen window
        self.first_window.geometry("500x700")

        # removing the changeable size of width and height from your window screen
        self.first_window.resizable(False, False)
        
        # getting the a color for our background
        self.first_window.configure(background="#ffbfff")

        # create a label object for write "Welcome to PhoneBook" as message
        self.welcome_label = Label(self.first_window, text="Welcome to PhoneBook", background="#ffbfff",
                                   foreground="#ff03ff",
                                   font="arial 20 bold")

        # change the position of text label in our screen
        self.welcome_label.place(x=250.0, y=50.0, anchor="center")

        # create a label object for write "Azizi" as message
        self.ronak_biniaz = Label(self.first_window, text="Azizi.MR", background="#ffbfff", foreground="#ff03ff",
                                  font="arial 15 bold")

        # change the position of text label in our screen
        self.ronak_biniaz.place(x=240, y=90, anchor="center")

        # create a label object for write number of contact exist in our phonebook
        self.num_contact = Label(self.first_window, text=f"you have {len(self.Name_list)} contact",
                                 background="#ffbfff",
                                 foreground="#801680", font="arial 17 bold")

        # change the position of text label in our screen
        self.num_contact.place(x=243, y=200, anchor="center")

        # create a Button object for  "add contact" push button
        self.add_button = Button(self.first_window, text="Add Contact", background="#b30eb3",
                                 command=self.make_add_page)

        # change the position of add button in our screen
        self.add_button.place(x=150, y=300, anchor="center")

        # create a Button object for "Search Contact" push button
        self.search_button = Button(self.first_window, text="Search Contact", background="#b30eb3",
                                    command=self.make_search_page)

        # change the position of search button in our screen
        self.search_button.place(x=350, y=300, anchor="center")

        # create a Button object for "Edit Contact" push button
        self.edith_button = Button(self.first_window, text="Edit Contact", background="#b30eb3",
                                   command=self.make_edit_page)

        # change the position of search button in our screen
        self.edith_button.place(x=120, y=350, anchor="center")

        # create a Button object for "Delete Contact" push button
        self.delete_button = Button(self.first_window, text="Delete Contact", background="#b30eb3",
                                    command=self.make_delete_page)

        # change the position of search button in our screen
        self.delete_button.place(x=370, y=350, anchor="center")

        # create a Button object for "Numbers" push button
        self.report_numbers_button = Button(self.first_window, text="Numbers", background="#b30eb3",
                                            command=self.make_show_num)

        # change the position of Numbers button in our screen
        self.report_numbers_button.place(x=320, y=400, anchor="center")

        # create a Button object for "Emails" push button
        self.report_email_button = Button(self.first_window, text="Emails", background="#b30eb3",
                                          command=self.make_show_email)

        # change the position of Emails button in our screen
        self.report_email_button.place(x=242, y=450, anchor="center")

        # create a Button object for "Address" push button
        self.report_address_button = Button(self.first_window, text="Address", background="#b30eb3",
                                            command=self.make_show_address)

        # change the position of Address button in our screen
        self.report_address_button.place(x=170, y=400, anchor="center")

        # create a Button object for "Info" push button
        self.info_button = Button(self.first_window, text="Info", background="#b30eb3", command=self.info_button_func)
        
        # change the position of info button in our screen
        self.info_button.place(x=242, y=330, anchor="center")

        # create a label object for when user calling the info function
        self.info_label = Label(self.first_window, background="#ffbfff",
                                foreground="#7d0a79", font="arial 17 bold")
        # self.aad = self.add_page()

        # running the programm
        self.first_window.mainloop()

    # Define the Add Page Function
    def add_page(self):

        # create a page window with tkinter
        self.add_window = Tk()

        # set title for our window
        self.add_window.title("Add Contact")

        # set size for our window
        self.add_window.geometry("500x700")

        # disable of resizable of our window
        self.add_window.resizable(False, False)

        # set background for our window
        self.add_window.configure(background="#ffbfff")

        # Create a label for message of "Please Enter the information"
        self.add_window_welcome_label = Label(self.add_window, text="Please Enter the information",
                                              background="#ffbfff", foreground="#ff03ff",
                                              font="arial 20 bold")

        # set pozition for the label in add window
        self.add_window_welcome_label.place(x=250, y=50, anchor="center")

        # Create a label for message of "Name :"
        self.name_label = Label(self.add_window, text="Name :",
                                background="#ffbfff", foreground="#ff03ff",
                                font="arial 10 bold")

        # set pozition for the label in add window
        self.name_label.place(x=140, y=100, anchor="center")

        # create the Entry for getting name with textbox
        self.get_name = Entry(self.add_window, width=20)

        # set pozition for the Entery in add window
        self.get_name.place(x=250, y=100, anchor="center")

        self.famili_label = Label(self.add_window, text="family :",
                                  background="#ffbfff", foreground="#ff03ff",
                                  font="arial 10 bold")
        self.famili_label.place(x=140, y=140, anchor="center")
        self.get_family = Entry(self.add_window, width=20)
        self.get_family.place(x=250, y=140, anchor="center")

        self.cellphone_label = Label(self.add_window, text="Cellphone :",
                                     background="#ffbfff", foreground="#ff03ff",
                                     font="arial 10 bold")
        self.cellphone_label.place(x=130, y=180, anchor="center")
        self.get_cellphone = Entry(self.add_window, width=20)
        self.get_cellphone.place(x=250, y=180, anchor="center")

        self.email_label = Label(self.add_window, text="Email :",
                                 background="#ffbfff", foreground="#ff03ff",
                                 font="arial 10 bold")
        self.email_label.place(x=140, y=220, anchor="center")
        self.get_email = Entry(self.add_window, width=20)
        self.get_email.place(x=250, y=220, anchor="center")

        self.id_label = Label(self.add_window, text="Id :",
                              background="#ffbfff", foreground="#ff03ff",
                              font="arial 10 bold")
        self.id_label.place(x=140, y=260, anchor="center")
        self.get_id = Entry(self.add_window, width=20)
        self.get_id.place(x=250, y=260, anchor="center")
        #

        self.phone_label = Label(self.add_window, text="Phone :",
                                 background="#ffbfff", foreground="#ff03ff",
                                 font="arial 10 bold")
        self.phone_label.place(x=140, y=300, anchor="center")
        self.get_phone = Entry(self.add_window, width=20)
        self.get_phone.place(x=250, y=300, anchor="center")
        #

        self.address_label = Label(self.add_window, text="Address :",
                                   background="#ffbfff", foreground="#ff03ff",
                                   font="arial 10 bold")
        self.address_label.place(x=140, y=340, anchor="center")
        self.get_address = Entry(self.add_window, width=20)
        self.get_address.place(x=250, y=340, anchor="center")

        self.save_button = Button(self.add_window, text="Save Contact", background="#b30eb3",
                                  command=self.add_button_func)
        self.save_button.place(x=250, y=390, anchor="center")

        self.status_label = Label(self.add_window, background="#ffbfff", foreground="#ff03ff",
                                  font="arial 20 bold")

        self.add_window.mainloop()

    def search_page(self):
        self.search_window = Tk()
        self.search_window.title("Add Contact")
        self.search_window.geometry("500x700")
        self.search_window.resizable(False, False)
        self.search_window.configure(background="#ffbfff")
        self.search_window_welcome_label = Label(self.search_window, text="Please Enter the id",
                                                 background="#ffbfff", foreground="#ff03ff",
                                                 font="arial 20 bold")
        self.search_window_welcome_label.place(x=250, y=50, anchor="center")

        self.id_search_label = Label(self.search_window, text="id to search : ",
                                     background="#ffbfff", foreground="#ff03ff",
                                     font="arial 10 bold")
        self.id_search_label.place(x=120, y=130, anchor="center")

        self.id_search_entry = Entry(self.search_window, width=20)
        self.id_search_entry.place(x=250, y=130, anchor="center")

        self.status_search = Label(self.search_window, background="#ffbfff", foreground="#ff03ff",
                                   font="arial 20 bold")

        self.search_button = Button(self.search_window, text="Search Contact", background="#b30eb3",
                                    command=self.search_button_func)
        self.search_button.place(x=240, y=180, anchor="center")

        self.name_label = Label(self.search_window, text="Name :",
                                background="#ffbfff", foreground="#ff03ff",
                                font="arial 10 bold")
        self.name_label.place(x=140, y=300, anchor="center")
        self.get_name = Entry(self.search_window, width=20)
        self.get_name.place(x=250, y=300, anchor="center")

        self.famili_label = Label(self.search_window, text="Family :",
                                  background="#ffbfff", foreground="#ff03ff",
                                  font="arial 10 bold")
        self.famili_label.place(x=140, y=340, anchor="center")
        self.get_family = Entry(self.search_window, width=20)
        self.get_family.place(x=250, y=340, anchor="center")

        self.cellphone_label = Label(self.search_window, text="Cellphone :",
                                     background="#ffbfff", foreground="#ff03ff",
                                     font="arial 10 bold")
        self.cellphone_label.place(x=130, y=380, anchor="center")
        self.get_cellphone = Entry(self.search_window, width=20)
        self.get_cellphone.place(x=250, y=380, anchor="center")

        self.email_label = Label(self.search_window, text="Email :",
                                 background="#ffbfff", foreground="#ff03ff",
                                 font="arial 10 bold")
        self.email_label.place(x=140, y=420, anchor="center")
        self.get_email = Entry(self.search_window, width=20)
        self.get_email.place(x=250, y=420, anchor="center")

        self.id_label = Label(self.search_window, text="Id :",
                              background="#ffbfff", foreground="#ff03ff",
                              font="arial 10 bold")
        self.id_label.place(x=140, y=460, anchor="center")
        self.get_id = Entry(self.search_window, width=20)
        self.get_id.place(x=250, y=460, anchor="center")
        #

        self.phone_label = Label(self.search_window, text="Phone :",
                                 background="#ffbfff", foreground="#ff03ff",
                                 font="arial 10 bold")
        self.phone_label.place(x=140, y=500, anchor="center")
        self.get_phone = Entry(self.search_window, width=20)
        self.get_phone.place(x=250, y=500, anchor="center")
        #

        self.address_label = Label(self.search_window, text="Address :",
                                   background="#ffbfff", foreground="#ff03ff",
                                   font="arial 10 bold")
        self.address_label.place(x=140, y=540, anchor="center")
        self.get_address = Entry(self.search_window, width=20)
        self.get_address.place(x=250, y=540, anchor="center")

        # self.save_button = Button(self.search_window, text="Save Contact", background="#b30eb3")
        # self.save_button.place(x=250, y=590, anchor="center")

        self.search_window.mainloop()

    def edit_page(self):
        self.edith_window = Tk()
        self.edith_window.title("Add Contact")
        self.edith_window.geometry("500x700")
        self.edith_window.resizable(False, False)
        self.edith_window.configure(background="#ffbfff")
        self.edith_window_welcome_label = Label(self.edith_window, text="Please Enter the id",
                                                background="#ffbfff", foreground="#ff03ff",
                                                font="arial 20 bold")
        self.edith_window_welcome_label.place(x=250, y=50, anchor="center")

        self.id_search_label = Label(self.edith_window, text="id to search : ",
                                     background="#ffbfff", foreground="#ff03ff",
                                     font="arial 10 bold")
        self.id_search_label.place(x=120, y=130, anchor="center")

        self.id_search_entry = Entry(self.edith_window, width=20)
        self.id_search_entry.place(x=250, y=130, anchor="center")

        self.status_search = Label(self.edith_window, background="#ffbfff", foreground="#ff03ff",
                                   font="arial 20 bold")

        self.status_edit = Label(self.edith_window, background="#ffbfff", foreground="#db0d0d",
                                 font="arial 20 bold")

        self.search_button = Button(self.edith_window, text="Search Contact", background="#b30eb3",
                                    command=self.search_button_func)
        self.search_button.place(x=240, y=180, anchor="center")

        self.name_label = Label(self.edith_window, text="Name :",
                                background="#ffbfff", foreground="#ff03ff",
                                font="arial 10 bold")
        self.name_label.place(x=140, y=300, anchor="center")
        self.get_name = Entry(self.edith_window, width=20)
        self.get_name.place(x=250, y=300, anchor="center")

        self.famili_label = Label(self.edith_window, text="Family :",
                                  background="#ffbfff", foreground="#ff03ff",
                                  font="arial 10 bold")
        self.famili_label.place(x=140, y=340, anchor="center")
        self.get_family = Entry(self.edith_window, width=20)
        self.get_family.place(x=250, y=340, anchor="center")

        self.cellphone_label = Label(self.edith_window, text="Cellphone :",
                                     background="#ffbfff", foreground="#ff03ff",
                                     font="arial 10 bold")
        self.cellphone_label.place(x=130, y=380, anchor="center")
        self.get_cellphone = Entry(self.edith_window, width=20)
        self.get_cellphone.place(x=250, y=380, anchor="center")

        self.email_label = Label(self.edith_window, text="Email :",
                                 background="#ffbfff", foreground="#ff03ff",
                                 font="arial 10 bold")
        self.email_label.place(x=140, y=420, anchor="center")
        self.get_email = Entry(self.edith_window, width=20)
        self.get_email.place(x=250, y=420, anchor="center")

        self.id_label = Label(self.edith_window, text="Id :",
                              background="#ffbfff", foreground="#ff03ff",
                              font="arial 10 bold")
        self.id_label.place(x=140, y=460, anchor="center")
        self.get_id = Entry(self.edith_window, width=20)
        self.get_id.place(x=250, y=460, anchor="center")
        #

        self.phone_label = Label(self.edith_window, text="Phone :",
                                 background="#ffbfff", foreground="#ff03ff",
                                 font="arial 10 bold")
        self.phone_label.place(x=140, y=500, anchor="center")
        self.get_phone = Entry(self.edith_window, width=20)
        self.get_phone.place(x=250, y=500, anchor="center")
        #

        self.address_label = Label(self.edith_window, text="Address :",
                                   background="#ffbfff", foreground="#ff03ff",
                                   font="arial 10 bold")
        self.address_label.place(x=140, y=540, anchor="center")
        self.get_address = Entry(self.edith_window, width=20)
        self.get_address.place(x=250, y=540, anchor="center")

        self.save_changes_button = Button(self.edith_window, text="Save Contact", background="#b30eb3",
                                          command=self.save_change_button_func)
        self.save_changes_button.place(x=250, y=590, anchor="center")
        self.edith_window.mainloop()

    def delete_page(self):
        self.delete_window = Tk()
        self.delete_window.title("Add Contact")
        self.delete_window.geometry("500x700")
        self.delete_window.resizable(False, False)
        self.delete_window.configure(background="#ffbfff")
        self.delete_window_welcome_label = Label(self.delete_window, text="Please Enter the id",
                                                 background="#ffbfff", foreground="#ff03ff",
                                                 font="arial 20 bold")
        self.delete_window_welcome_label.place(x=250, y=50, anchor="center")

        self.id_search_label = Label(self.delete_window, text="id to search : ",
                                     background="#ffbfff", foreground="#ff03ff",
                                     font="arial 10 bold")
        self.id_search_label.place(x=120, y=130, anchor="center")

        self.id_search_entry = Entry(self.delete_window, width=20)
        self.id_search_entry.place(x=250, y=130, anchor="center")
        self.status_search = Label(self.delete_window, background="#ffbfff", foreground="#ff03ff",
                                   font="arial 20 bold")

        self.status_delete = Label(self.delete_window, background="#ffbfff", foreground="#db0d0d",
                                   font="arial 20 bold")

        self.search_button = Button(self.delete_window, text="Search Contact", background="#b30eb3",
                                    command=self.search_button_func)
        self.search_button.place(x=240, y=180, anchor="center")

        self.name_label = Label(self.delete_window, text="Name :",
                                background="#ffbfff", foreground="#ff03ff",
                                font="arial 10 bold")
        self.name_label.place(x=140, y=300, anchor="center")
        self.get_name = Entry(self.delete_window, width=20)
        self.get_name.place(x=250, y=300, anchor="center")

        self.famili_label = Label(self.delete_window, text="Family :",
                                  background="#ffbfff", foreground="#ff03ff",
                                  font="arial 10 bold")
        self.famili_label.place(x=140, y=340, anchor="center")
        self.get_family = Entry(self.delete_window, width=20)
        self.get_family.place(x=250, y=340, anchor="center")

        self.cellphone_label = Label(self.delete_window, text="Cellphone :",
                                     background="#ffbfff", foreground="#ff03ff",
                                     font="arial 10 bold")
        self.cellphone_label.place(x=130, y=380, anchor="center")
        self.get_cellphone = Entry(self.delete_window, width=20)
        self.get_cellphone.place(x=250, y=380, anchor="center")

        self.email_label = Label(self.delete_window, text="Email :",
                                 background="#ffbfff", foreground="#ff03ff",
                                 font="arial 10 bold")
        self.email_label.place(x=140, y=420, anchor="center")
        self.get_email = Entry(self.delete_window, width=20)
        self.get_email.place(x=250, y=420, anchor="center")

        self.id_label = Label(self.delete_window, text="Id :",
                              background="#ffbfff", foreground="#ff03ff",
                              font="arial 10 bold")
        self.id_label.place(x=140, y=460, anchor="center")
        self.get_id = Entry(self.delete_window, width=20)
        self.get_id.place(x=250, y=460, anchor="center")
        #

        self.phone_label = Label(self.delete_window, text="Phone :",
                                 background="#ffbfff", foreground="#ff03ff",
                                 font="arial 10 bold")
        self.phone_label.place(x=140, y=500, anchor="center")
        self.get_phone = Entry(self.delete_window, width=20)
        self.get_phone.place(x=250, y=500, anchor="center")
        #

        self.address_label = Label(self.delete_window, text="Address :",
                                   background="#ffbfff", foreground="#ff03ff",
                                   font="arial 10 bold")
        self.address_label.place(x=140, y=540, anchor="center")
        self.get_address = Entry(self.delete_window, width=20)
        self.get_address.place(x=250, y=540, anchor="center")

        self.delete_button1 = Button(self.delete_window, text="Delete Contact", background="#db0d0d",
                                     command=self.delete_button_func)
        self.delete_button1.place(x=250, y=590, anchor="center")

        self.delete_window.mainloop()

    def make_add_page(self):
        self.add1 = self.add_page()

    def make_search_page(self):
        self.search1 = self.search_page()

    def make_delete_page(self):
        self.delete1 = self.delete_page()

    def make_edit_page(self):
        self.edit1 = self.edit_page()

    def make_show_num(self):
        self.show_num_page = self.show_num()

    def make_show_email(self):
        self.show_email_page = self.show_email()

    def make_show_address(self):
        self.show_adres_page = self.show_adres()

    def add_button_func(self):
        self.Name_list.append(self.get_name.get())
        self.famili_list.append(self.get_family.get())
        self.cellphone_list.append(self.get_cellphone.get())
        self.email_list.append(self.get_email.get())
        self.phone_list.append(self.get_phone.get())
        self.address_list.append(self.get_address.get())
        self.id_list.append(self.get_id.get())

        self.get_name.delete(0, END)
        self.get_family.delete(0, END)
        self.get_id.delete(0, END)
        self.get_phone.delete(0, END)
        self.get_address.delete(0, END)
        self.get_cellphone.delete(0, END)
        self.get_email.delete(0, END)
        self.num_contact["text"] = f"you have {len(self.Name_list)} contact"
        self.status_label["text"] = "Contact Saved"
        self.status_label.place(x=250, y=500, anchor="center")

    def search_button_func(self):
        id_text = self.id_search_entry.get()
        found = 0
        for i in range(len(self.id_list)):
            if self.id_list[i] == id_text:
                self.status_search["text"] = "Contact Found"
                self.status_search.place(x=250, y=220, anchor="center")

                self.get_name.delete(0, END)
                self.get_family.delete(0, END)
                self.get_id.delete(0, END)
                self.get_phone.delete(0, END)
                self.get_address.delete(0, END)
                self.get_cellphone.delete(0, END)
                self.get_email.delete(0, END)

                self.get_id.insert(0, self.id_list[i])
                self.get_family.insert(0, self.famili_list[i])
                self.get_phone.insert(0, self.phone_list[i])
                self.get_name.insert(0, self.Name_list[i])
                self.get_email.insert(0, self.email_list[i])
                self.get_cellphone.insert(0, self.cellphone_list[i])
                self.get_address.insert(0, self.address_list[i])
                found = 1
                break
        if found == 0:
            self.status_search["text"] = "Contact Not Found"
            self.status_search.place(x=250, y=220, anchor="center")

    def delete_button_func(self):
        id_text = self.id_search_entry.get()
        for i in range(len(self.id_list)):
            if self.id_list[i] == id_text:
                del self.Name_list[i]
                del self.famili_list[i]
                del self.phone_list[i]
                del self.cellphone_list[i]
                del self.address_list[i]
                del self.email_list[i]
                del self.id_list[i]

                self.get_id.delete(0, END)
                self.get_phone.delete(0, END)
                self.get_name.delete(0, END)
                self.get_family.delete(0, END)
                self.get_email.delete(0, END)
                self.get_cellphone.delete(0, END)
                self.get_address.delete(0, END)

                self.status_delete["text"] = "Contact Deleted"
                self.status_delete.place(x=250, y=640, anchor="center")
                self.num_contact["text"] = f"you have {len(self.Name_list)} contact"
                break

    def save_change_button_func(self):
        id_text = self.id_search_entry.get()
        for i in range(len(self.id_list)):
            if self.id_list[i] == id_text:
                self.Name_list[i] = self.get_name.get()
                self.famili_list[i] = self.get_family.get()
                self.phone_list[i] = self.get_phone.get()
                self.cellphone_list[i] = self.get_cellphone.get()
                self.address_list[i] = self.get_address.get()
                self.email_list[i] = self.get_email.get()
                self.id_list[i] = self.get_id.get()

                self.get_id.delete(0, END)
                self.get_phone.delete(0, END)
                self.get_name.delete(0, END)
                self.get_family.delete(0, END)
                self.get_email.delete(0, END)
                self.get_cellphone.delete(0, END)
                self.get_address.delete(0, END)

                self.status_edit["text"] = "Change Saved"
                self.status_edit.place(x=250, y=640, anchor="center")
                break

    def info_button_func(self):
        self.info_label["text"] = self.info
        self.info_label.place(x=235, y=570, anchor="center")

    def show_num(self):
        self.show_all = Tk()
        self.show_all.title("Show all")
        self.show_all.configure(background="#ffbfff")
        self.scorll_all = Scrollbar(self.show_all, background="#ff03ff")
        self.show_all.geometry("500x700")
        self.show_all.resizable(False, False)
        self.scorll_all.pack(side=RIGHT, fill=Y)
        my_list = Listbox(self.show_all, yscrollcommand=self.scorll_all.set, background="#ffbfff", width=60)
        for i in range(len(self.cellphone_list)):
            my_list.insert(END, f"#{i + 1}  {self.cellphone_list[i]}")
        my_list.pack(side=LEFT, fill=BOTH)
        self.scorll_all.config(command=my_list.yview)
        self.show_all.mainloop()

    def show_adres(self):
        self.show_all = Tk()
        self.show_all.title("Show Address")
        self.show_all.configure(background="#ffbfff")
        self.scorll_all = Scrollbar(self.show_all, background="#ff03ff")
        self.show_all.geometry("500x700")
        self.show_all.resizable(False, False)
        self.scorll_all.pack(side=RIGHT, fill=Y)
        my_list = Listbox(self.show_all, yscrollcommand=self.scorll_all.set, background="#ffbfff", width=60)
        for i in range(len(self.address_list)):
            my_list.insert(END, f"#{i + 1}  {self.address_list[i]}")
        my_list.pack(side=LEFT, fill=BOTH)
        self.scorll_all.config(command=my_list.yview)
        self.show_all.mainloop()

    def show_email(self):
        self.show_all = Tk()
        self.show_all.title("Show Emails")
        self.show_all.configure(background="#ffbfff")
        self.scorll_all = Scrollbar(self.show_all, background="#ff03ff")
        self.show_all.geometry("500x700")
        self.show_all.resizable(False, False)
        self.scorll_all.pack(side=RIGHT, fill=Y)
        my_list = Listbox(self.show_all, yscrollcommand=self.scorll_all.set, background="#ffbfff", width=60)
        for i in range(len(self.email_list)):
            my_list.insert(END, f"#{i + 1}  {self.email_list[i]}")
        my_list.pack(side=LEFT, fill=BOTH)
        self.scorll_all.config(command=my_list.yview)
        self.show_all.mainloop()


phonebook = PhoneBook()
