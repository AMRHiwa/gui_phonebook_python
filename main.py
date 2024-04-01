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

        # set position for the label in add window
        self.add_window_welcome_label.place(x=250, y=50, anchor="center")

        # Create a label for message of "Name :"
        self.name_label = Label(self.add_window, text="Name :",
                                background="#ffbfff", foreground="#ff03ff",
                                font="arial 10 bold")

        # set position for the label in add window
        self.name_label.place(x=140, y=100, anchor="center")

        # create the Entry for getting name with textbox
        self.get_name = Entry(self.add_window, width=20)

        # set position for the Entery in add window
        self.get_name.place(x=250, y=100, anchor="center")

        # Create a label for message of "family :"
        self.famili_label = Label(self.add_window, text="family :",
                                  background="#ffbfff", foreground="#ff03ff",
                                  font="arial 10 bold")

        # set position for the label in add window
        self.famili_label.place(x=140, y=140, anchor="center")

        # create the Entry for getting family with textbox
        self.get_family = Entry(self.add_window, width=20)

        # set position for the Entery in add window
        self.get_family.place(x=250, y=140, anchor="center")

        # Create a label for message of "cellphone :"
        self.cellphone_label = Label(self.add_window, text="Cellphone :",
                                     background="#ffbfff", foreground="#ff03ff",
                                     font="arial 10 bold")

        # set position for the label in add window
        self.cellphone_label.place(x=130, y=180, anchor="center")

        # create the Entry for getting cellphone with textbox
        self.get_cellphone = Entry(self.add_window, width=20)

        # set position for the Entery in add window
        self.get_cellphone.place(x=250, y=180, anchor="center")

        # Create a label for message of "Email :"
        self.email_label = Label(self.add_window, text="Email :",
                                 background="#ffbfff", foreground="#ff03ff",
                                 font="arial 10 bold")

        # set position for the label in add window
        self.email_label.place(x=140, y=220, anchor="center")

        # create the Entry for getting Email with textbox
        self.get_email = Entry(self.add_window, width=20)

        # set position for the Entery in add window
        self.get_email.place(x=250, y=220, anchor="center")

        # Create a label for message of "ID :"
        self.id_label = Label(self.add_window, text="Id :",
                              background="#ffbfff", foreground="#ff03ff",
                              font="arial 10 bold")
        
        # set position for the label in add window
        self.id_label.place(x=140, y=260, anchor="center")

        # create the Entry for getting ID with textbox
        self.get_id = Entry(self.add_window, width=20)

        # set position for the Entery in add window
        self.get_id.place(x=250, y=260, anchor="center")

        # Create a label for message of "Phone :"
        self.phone_label = Label(self.add_window, text="Phone :",
                                 background="#ffbfff", foreground="#ff03ff",
                                 font="arial 10 bold")
        
        # set position for the label in add window
        self.phone_label.place(x=140, y=300, anchor="center")

        # create the Entry for getting phone with textbox
        self.get_phone = Entry(self.add_window, width=20)

        # set position for the Entery in add window
        self.get_phone.place(x=250, y=300, anchor="center")
        
        # Create a label for message of "Address :"
        self.address_label = Label(self.add_window, text="Address :",
                                   background="#ffbfff", foreground="#ff03ff",
                                   font="arial 10 bold")

        # set position for the label in add window
        self.address_label.place(x=140, y=340, anchor="center")

        # create the Entry for getting address with textbox
        self.get_address = Entry(self.add_window, width=20)

        # set position for the Entery in add window
        self.get_address.place(x=250, y=340, anchor="center")

        # create a button object for saving information in notebook that names "save contact"
        self.save_button = Button(self.add_window, text="Save Contact", background="#b30eb3",
                                  command=self.add_button_func)
        
        # set position for the button in add window 
        self.save_button.place(x=250, y=390, anchor="center")

        # Create a label for Status
        self.status_label = Label(self.add_window, background="#ffbfff", foreground="#ff03ff",
                                  font="arial 20 bold")

        # running the window
        self.add_window.mainloop()
    
    # define the search page function
    def search_page(self):
        
        # create a window object from tkinter
        self.search_window = Tk()

        # setup the title for page
        self.search_window.title("Add Contact")

        # set size for for page window
        self.search_window.geometry("500x700")

        # disable resizable of window
        self.search_window.resizable(False, False)

        # set background color of window
        self.search_window.configure(background="#ffbfff")

        # create a label for "Please Enter the id" message
        self.search_window_welcome_label = Label(self.search_window, text="Please Enter the id",
                                                 background="#ffbfff", foreground="#ff03ff",
                                                 font="arial 20 bold")
        
        # set position for label in window
        self.search_window_welcome_label.place(x=250, y=50, anchor="center")

        # create a label for "id to search : " message
        self.id_search_label = Label(self.search_window, text="id to search : ",
                                     background="#ffbfff", foreground="#ff03ff",
                                     font="arial 10 bold")

        # set position for label in window
        self.id_search_label.place(x=120, y=130, anchor="center")

        # create a textbox object with Entry to get id
        self.id_search_entry = Entry(self.search_window, width=20)

        # set position for Entry in window
        self.id_search_entry.place(x=250, y=130, anchor="center")

        # create a label for Status
        self.status_search = Label(self.search_window, background="#ffbfff", foreground="#ff03ff",
                                   font="arial 20 bold")

        # create a button for search in window
        self.search_button = Button(self.search_window, text="Search Contact", background="#b30eb3",
                                    command=self.search_button_func)

        # set position for button in window
        self.search_button.place(x=240, y=180, anchor="center")

        # create a label for "Name : " message
        self.name_label = Label(self.search_window, text="Name :",
                                background="#ffbfff", foreground="#ff03ff",
                                font="arial 10 bold")

        # set position for label in window
        self.name_label.place(x=140, y=300, anchor="center")

        # create a textbox object with Entry to get name
        self.get_name = Entry(self.search_window, width=20)

        # set position for Entry in window
        self.get_name.place(x=250, y=300, anchor="center")

        # create a label for "Family : " message
        self.famili_label = Label(self.search_window, text="Family :",
                                  background="#ffbfff", foreground="#ff03ff",
                                  font="arial 10 bold")

        # set position for label in window
        self.famili_label.place(x=140, y=340, anchor="center")

        # create a textbox object with Entry to get family
        self.get_family = Entry(self.search_window, width=20)

        # set position for Entry in window
        self.get_family.place(x=250, y=340, anchor="center")

        # create a label for "Cellphone : " message
        self.cellphone_label = Label(self.search_window, text="Cellphone :",
                                     background="#ffbfff", foreground="#ff03ff",
                                     font="arial 10 bold")
        
        # set position for label in window
        self.cellphone_label.place(x=130, y=380, anchor="center")

        # create a textbox object with Entry to get cellphone
        self.get_cellphone = Entry(self.search_window, width=20)

        # set position for label in window
        self.get_cellphone.place(x=250, y=380, anchor="center")

        # create a label for "Email : " message
        self.email_label = Label(self.search_window, text="Email :",
                                 background="#ffbfff", foreground="#ff03ff",
                                 font="arial 10 bold")

        # set position for label in window
        self.email_label.place(x=140, y=420, anchor="center")

        # create a textbox object with Entry to get email
        self.get_email = Entry(self.search_window, width=20)

        # set position for Entry in window
        self.get_email.place(x=250, y=420, anchor="center")

        # create a label for "Id : " message
        self.id_label = Label(self.search_window, text="Id :",
                              background="#ffbfff", foreground="#ff03ff",
                              font="arial 10 bold")

        # set position for label in window
        self.id_label.place(x=140, y=460, anchor="center")

        # create a textbox object with Entry to get id
        self.get_id = Entry(self.search_window, width=20)

        # set position for Entry in window
        self.get_id.place(x=250, y=460, anchor="center")
        
        # create a label for "Phone : " message
        self.phone_label = Label(self.search_window, text="Phone :",
                                 background="#ffbfff", foreground="#ff03ff",
                                 font="arial 10 bold")

        # set position for label in window
        self.phone_label.place(x=140, y=500, anchor="center")

        # create a textbox object with Entry to get phone
        self.get_phone = Entry(self.search_window, width=20)

        # set position for Entry in window
        self.get_phone.place(x=250, y=500, anchor="center")
        
        # create a label for "Address : " message
        self.address_label = Label(self.search_window, text="Address :",
                                   background="#ffbfff", foreground="#ff03ff",
                                   font="arial 10 bold")

        # set position for Label in window
        self.address_label.place(x=140, y=540, anchor="center")
    
        # create a textbox object with Entry to get address
        self.get_address = Entry(self.search_window, width=20)

        # set position for Entry in window
        self.get_address.place(x=250, y=540, anchor="center")

        # run the window
        self.search_window.mainloop()

    # define the edit page function
    def edit_page(self):

        # create a page of edit with tkinter
        self.edith_window = Tk()

        # set title for our page
        self.edith_window.title("edit Contact")

        # set size of page for our page
        self.edith_window.geometry("500x700")

        # desiable of resizable of window
        self.edith_window.resizable(False, False)

        # set background color for our page
        self.edith_window.configure(background="#ffbfff")

        # create a label for "Please Enter the id" message in page
        self.edith_window_welcome_label = Label(self.edith_window, text="Please Enter the id",
                                                background="#ffbfff", foreground="#ff03ff",
                                                font="arial 20 bold")

        # set position for our label in window
        self.edith_window_welcome_label.place(x=250, y=50, anchor="center")

        # create a label for "id to search : " message
        self.id_search_label = Label(self.edith_window, text="id to search : ",
                                     background="#ffbfff", foreground="#ff03ff",
                                     font="arial 10 bold")

        # set position for label in window
        self.id_search_label.place(x=120, y=130, anchor="center")

        # create a Textbox object to get id with Entry object
        self.id_search_entry = Entry(self.edith_window, width=20)

        # set postion for Entry in window
        self.id_search_entry.place(x=250, y=130, anchor="center")

        # create a label for Status Search in window
        self.status_search = Label(self.edith_window, background="#ffbfff", foreground="#ff03ff",
                                   font="arial 20 bold")

        # create a label for Status Edit in our window
        self.status_edit = Label(self.edith_window, background="#ffbfff", foreground="#db0d0d",
                                 font="arial 20 bold")

        # Create a button for Searching contant  
        self.search_button = Button(self.edith_window, text="Search Contact", background="#b30eb3",
                                    command=self.search_button_func)

        # set position for our button in window
        self.search_button.place(x=240, y=180, anchor="center")

        # create a label for "Name : " message
        self.name_label = Label(self.edith_window, text="Name :",
                                background="#ffbfff", foreground="#ff03ff",
                                font="arial 10 bold")

        # set postion of label in our window
        self.name_label.place(x=140, y=300, anchor="center")

        # create a Textbox object to get name with Entry Object
        self.get_name = Entry(self.edith_window, width=20)

        # set postion for Entry in our window
        self.get_name.place(x=250, y=300, anchor="center")

        # Create label for "Family : " message
        self.famili_label = Label(self.edith_window, text="Family :",
                                  background="#ffbfff", foreground="#ff03ff",
                                  font="arial 10 bold")

        # set postion for label in our window
        self.famili_label.place(x=140, y=340, anchor="center")

        # create a textbox object for get family feature with Entry object
        self.get_family = Entry(self.edith_window, width=20)

        # set postion for Entry in window
        self.get_family.place(x=250, y=340, anchor="center")

        # create a label for "Cellphone : " message
        self.cellphone_label = Label(self.edith_window, text="Cellphone :",
                                     background="#ffbfff", foreground="#ff03ff",
                                     font="arial 10 bold")

        # set position for label in window 
        self.cellphone_label.place(x=130, y=380, anchor="center")
        
        # create a textbox object for getting the cellphone feature with Entry object in tk
        self.get_cellphone = Entry(self.edith_window, width=20)
        
        # set position of cellphone Entry 
        self.get_cellphone.place(x=250, y=380, anchor="center")

        # create a label for "Email : " message
        self.email_label = Label(self.edith_window, text="Email :",
                                 background="#ffbfff", foreground="#ff03ff",
                                 font="arial 10 bold")

        # set position for label in our window
        self.email_label.place(x=140, y=420, anchor="center")

        # create a Entry for getting the email 
        self.get_email = Entry(self.edith_window, width=20)

        # set postion for Entry in our page
        self.get_email.place(x=250, y=420, anchor="center")

        # create a label for 'Id :' message
        self.id_label = Label(self.edith_window, text="Id :",
                              background="#ffbfff", foreground="#ff03ff",
                              font="arial 10 bold")

        # set position for label in window
        self.id_label.place(x=140, y=460, anchor="center")

        # create a Entry object for getting the id
        self.get_id = Entry(self.edith_window, width=20)

        # set position for Entry
        self.get_id.place(x=250, y=460, anchor="center")
        
        # create a label for set 'phone : ' message
        self.phone_label = Label(self.edith_window, text="Phone :",
                                 background="#ffbfff", foreground="#ff03ff",
                                 font="arial 10 bold")

        # set position for label in our label
        self.phone_label.place(x=140, y=500, anchor="center")

        # create a Entry for getting the phone numuber with textbox
        self.get_phone = Entry(self.edith_window, width=20)

        # set position for our Entry in window
        self.get_phone.place(x=250, y=500, anchor="center")
        
        # create a label for set "Address :" message on it
        self.address_label = Label(self.edith_window, text="Address :",
                                   background="#ffbfff", foreground="#ff03ff",
                                   font="arial 10 bold")

        # set position for label in window
        self.address_label.place(x=140, y=540, anchor="center")

        # create a entry for getting the address
        self.get_address = Entry(self.edith_window, width=20)

        # set position for entry in window
        self.get_address.place(x=250, y=540, anchor="center")

        # create a button object names 'save change' for save all chainging inforamtion
        self.save_changes_button = Button(self.edith_window, text="Save Contact", background="#b30eb3",
                                          command=self.save_change_button_func)

        # set position for our button
        self.save_changes_button.place(x=250, y=590, anchor="center")

        # run page
        self.edith_window.mainloop()

    # define the delete_page function
    def delete_page(self):

        # create a window object with Tkinter module
        self.delete_window = Tk()

        # add title for window
        self.delete_window.title("delete Contact")

        # set size of width and height for our label
        self.delete_window.geometry("500x700")

        # disable of resizable window
        self.delete_window.resizable(False, False)

        # set background color for window
        self.delete_window.configure(background="#ffbfff")

        # create a label for set "Please Enter the id" message
        self.delete_window_welcome_label = Label(self.delete_window, text="Please Enter the id",
                                                 background="#ffbfff", foreground="#ff03ff",
                                                 font="arial 20 bold")

        # set position for our label
        self.delete_window_welcome_label.place(x=250, y=50, anchor="center")

        # create a label for setting the "id to search: " message on it
        self.id_search_label = Label(self.delete_window, text="id to search : ",
                                     background="#ffbfff", foreground="#ff03ff",
                                     font="arial 10 bold")

        # set position for label in window
        self.id_search_label.place(x=120, y=130, anchor="center")

        # create a Entry object for getting the id
        self.id_search_entry = Entry(self.delete_window, width=20)

        # set position for our Entry
        self.id_search_entry.place(x=250, y=130, anchor="center")

        # create a label object for setting the status situation
        self.status_search = Label(self.delete_window, background="#ffbfff", foreground="#ff03ff",
                                   font="arial 20 bold")

        # set position for our label
        self.status_delete = Label(self.delete_window, background="#ffbfff", foreground="#db0d0d",
                                   font="arial 20 bold")

        # create a button for search in information with name "Search Contact"
        self.search_button = Button(self.delete_window, text="Search Contact", background="#b30eb3",
                                    command=self.search_button_func)

        # set position for our button
        self.search_button.place(x=240, y=180, anchor="center")

        # create a label for set "Name :" message
        self.name_label = Label(self.delete_window, text="Name :",
                                background="#ffbfff", foreground="#ff03ff",
                                font="arial 10 bold")

        # set position for label
        self.name_label.place(x=140, y=300, anchor="center")
        
        # create a Entry for getting name information
        self.get_name = Entry(self.delete_window, width=20)

        # set position for Entry
        self.get_name.place(x=250, y=300, anchor="center")


        # create a label object for setting "Family :" message
        self.famili_label = Label(self.delete_window, text="Family :",
                                  background="#ffbfff", foreground="#ff03ff",
                                  font="arial 10 bold")

        # set position for our label 
        self.famili_label.place(x=140, y=340, anchor="center")

        # create a Entry object for getting family information
        self.get_family = Entry(self.delete_window, width=20)

        # set position for Entry 
        self.get_family.place(x=250, y=340, anchor="center")

        # create a label for setting "Cellphone :" message
        self.cellphone_label = Label(self.delete_window, text="Cellphone :",
                                     background="#ffbfff", foreground="#ff03ff",
                                     font="arial 10 bold")

        # set position for label object
        self.cellphone_label.place(x=130, y=380, anchor="center")

        # create a Entry object for getting the cellphone number
        self.get_cellphone = Entry(self.delete_window, width=20)

        # set position for Entry object
        self.get_cellphone.place(x=250, y=380, anchor="center")

        # create a label object for setting "Email :" object
        self.email_label = Label(self.delete_window, text="Email :",
                                 background="#ffbfff", foreground="#ff03ff",
                                 font="arial 10 bold")

        # set position for label object
        self.email_label.place(x=140, y=420, anchor="center")

        # create a Entry object for getting the email
        self.get_email = Entry(self.delete_window, width=20)

        # set position for our Entry object
        self.get_email.place(x=250, y=420, anchor="center")

        # create a label object for setting "id" message
        self.id_label = Label(self.delete_window, text="Id :",
                              background="#ffbfff", foreground="#ff03ff",
                              font="arial 10 bold")

        # set position for label object
        self.id_label.place(x=140, y=460, anchor="center")

        # create a Entry object for getting the id information
        self.get_id = Entry(self.delete_window, width=20)

        # set position for Entry object
        self.get_id.place(x=250, y=460, anchor="center")
    
        # create a label object for setting the "Phone :" message
        self.phone_label = Label(self.delete_window, text="Phone :",
                                 background="#ffbfff", foreground="#ff03ff",
                                 font="arial 10 bold")

        # set position for label object
        self.phone_label.place(x=140, y=500, anchor="center")

        # create a Entry object for getting phone number
        self.get_phone = Entry(self.delete_window, width=20)

        # set position for Entry object 
        self.get_phone.place(x=250, y=500, anchor="center")
        
        # create a label object for setting "Address :" message
        self.address_label = Label(self.delete_window, text="Address :",
                                   background="#ffbfff", foreground="#ff03ff",
                                   font="arial 10 bold")
        
        # set position for label object
        self.address_label.place(x=140, y=540, anchor="center")

        # create a Entry object for getting address
        self.get_address = Entry(self.delete_window, width=20)

        # set position for Entry object
        self.get_address.place(x=250, y=540, anchor="center")


        # create a button for delete a contact
        self.delete_button1 = Button(self.delete_window, text="Delete Contact", background="#db0d0d",
                                     command=self.delete_button_func)

        # set postion for Entry object
        self.delete_button1.place(x=250, y=590, anchor="center")

        # run page
        self.delete_window.mainloop()

    # define the make_add_page
    def make_add_page(self):
        ''' this function used for call the add_page function to create a window '''
        
        # create a add_page with calling the add_page method
        self.add1 = self.add_page()

    # define the make_search_page
    def make_search_page(self):
        ''' this function used for call the search_page function to create a window '''

        # create a search_page with calling the search_page 
        self.search1 = self.search_page()

    # define the make_delete_page function
    def make_delete_page(self):
        ''' this function used for call the delete_page function to create a window '''

        # create a delete_page window by calling the delete_page method
        self.delete1 = self.delete_page()

    # define the make_edit_page
    def make_edit_page(self):
        ''' this function use for calling the edit_page function to create own page '''

        # create edit page by calling the edit_page method
        self.edit1 = self.edit_page()

    # define the make_show_num
    def make_show_num(self):
        ''' this function used calling the show_num function to create a own page '''

        # create a show_numb_page object by calling the show_num method
        self.show_num_page = self.show_num()

    # define the show_emails 
    def make_show_email(self):
        '''this function used for create a window to show all storage emails in our phone book'''

        # create a show_email_page by calling the show_email method
        self.show_email_page = self.show_email()

    # define the make_show_address method
    def make_show_address(self):
        '''this function used for create a window that show all storage address in phonebook on it'''

        # create a window to show address with calling the show_adres function
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
