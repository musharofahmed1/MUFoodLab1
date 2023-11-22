from tkinter import *
from tkinter import ttk

class Customer_Info:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer")
        self.root.geometry("915x440+190+80")

        #==============Title======================
        lbl_title = Label(self.root, text="Customer", font=("times new roman", 16, "bold"), bg="black", fg="gold")
        lbl_title.place(x=0, y=0, width=915, height=30)

        #=============Label Frame=================
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Info",
                                    font=("times new roman", 10, "bold"), bg="light grey", fg="Black")
        labelframeleft.place(x=5, y=35, width=200, height=245)

        #======================polash==============
        # std name
        lab_std_name = Label(labelframeleft, text="Name", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lab_std_name.grid(row=0, column=0)
        entry_name = ttk.Entry(labelframeleft, width=19, font=("times new roman", 10, "bold"))
        entry_name.grid(row=0, column=1, sticky=W)

        # std mobile number
        lab_std_MN = Label(labelframeleft, text="Phone", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lab_std_MN.grid(row=1, column=0)
        entry_MN = ttk.Entry(labelframeleft, width=19, font=("times new roman", 10, "bold"))
        entry_MN.grid(row=1, column=1, sticky=W)

        # std email
        lab_std_email = Label(labelframeleft, text="Email", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lab_std_email.grid(row=2, column=0)
        entry_email = ttk.Entry(labelframeleft, width=19, font=("times new roman", 10, "bold"))
        entry_email.grid(row=2, column=1, sticky=W)

        # std ID
        lab_std_roll = Label(labelframeleft, text="Card No", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lab_std_roll.grid(row=3, column=0)
        entry_roll = ttk.Entry(labelframeleft, width=19, font=("times new roman", 10, "bold"))
        entry_roll.grid(row=3, column=1, sticky=W)

        # gender
        lab_std_gender = Label(labelframeleft, text="Gender ", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lab_std_gender.grid(row=5, column=0)

        combo_gender = ttk.Combobox(labelframeleft, font=("arial", 10, "bold"), width=17, state="readonly")
        combo_gender["value"] = ("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=5, column=1)

        # address
        lab_std_address = Label(labelframeleft, text="Address", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lab_std_address.grid(row=6, column=0)
        entry_ad = ttk.Entry(labelframeleft, width=19, font=("times new roman", 10, "bold"))
        entry_ad.grid(row=6, column=1, sticky=W)

        # buttonframe
        buttonFrame = Frame(labelframeleft, bd=2, relief=RIDGE)
        buttonFrame.place(x=0, y=200, width=200, height=30)
        # addButton
        button_add = Button(buttonFrame, text="Add", font=("arial", 7, "bold"), bg="black", fg="gold", width=6)
        button_add.grid(row=0, column=0, padx=1)

        # updateButton
        button_update = Button(buttonFrame, text="Update", font=("arial", 7, "bold"), bg="black", fg="gold", width=6)
        button_update.grid(row=0, column=1, padx=1)

        # deleteButton
        button_delete = Button(buttonFrame, text="Delete", font=("arial", 7, "bold"), bg="black", fg="gold", width=6)
        button_delete.grid(row=0, column=2, padx=1)

        # SaveButton
        button_save = Button(buttonFrame, text="Save", font=("arial", 7, "bold"), bg="black", fg="gold", width=6)
        button_save.grid(row=0, column=3, padx=1)

        # right frame
        labelframeLright = LabelFrame(self.root, bd=2, relief=RIDGE, text="View details and search system",
                                      font=("times new roman", 15, "bold"), padx=2)
        labelframeLright.place(x=210, y=30, width=865, height=490)

        # address
        lab_search = Label(labelframeLright, text="Search By :", font=("times new roman", 14), padx=2, pady=6,
                           bg="red", fg="white")
        lab_search.grid(row=0, column=0, padx=2)
        # combo box for search
        combo_search = ttk.Combobox(labelframeLright, font=("arial", 12), width=22, state="readonly")
        combo_search["value"] = ("Mobile Number", "Card No")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        entry_ser = ttk.Entry(labelframeLright, width=22, font=("times new roman", 15, "bold"))
        entry_ser.grid(row=0, column=2, sticky=W, padx=2)

        # details frame
        details_frame = LabelFrame(labelframeLright, bd=2, font=("times new roman", 14, "bold"), padx=2)
        details_frame.place(x=0, y=50, width=710, height=355)

        # show data table
        scroll_x = ttk.Scrollbar(details_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_frame, orient=VERTICAL)
        std_details_table = ttk.Treeview(details_frame, column=('Name', 'Phone', 'Email', 'Card No', 'Gender', 'Address'),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=std_details_table.xview)
        scroll_y.config(command=std_details_table.yview)

        std_details_table.heading("Name", text="Name")
        std_details_table.heading("Phone", text="Phone")
        std_details_table.heading("Email", text="Email")
        std_details_table.heading("Card No", text="Card No")
        std_details_table.heading("Gender", text="Gender")
        std_details_table.heading("Address", text="Address")

        std_details_table["show"] = "headings"

        std_details_table.column("Name", width=100)
        std_details_table.column("Phone", width=100)
        std_details_table.column("Email", width=100)
        std_details_table.column("Card No", width=100)
        std_details_table.column("Gender", width=100)
        std_details_table.column("Address", width=100)
        std_details_table.pack(fill=BOTH, expand=1)

if __name__ == "__main__":
    root = Tk()
    object = Customer_Info(root)
    root.mainloop()
