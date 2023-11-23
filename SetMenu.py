from tkinter import *
from PIL import Image, ImageTk

class SetMenu_now:
    def __init__(self, root):
        self.root = root
        self.root.title("Set Menu")
        self.root.geometry("915x440+190+80")

        #==============Title======================
        lbl_title = Label(self.root, text="Set Menu", font=("times new roman", 20, "bold"), bg="black", fg="gold")
        lbl_title.place(x=0, y=0, width=915, height=30)

        #==============Custom Frame 1======================
        self.custom_frame1 = Frame(self.root, bg="light grey", bd=5, relief=GROOVE)
        self.custom_frame1.place(x=30, y=50, width=235, height=300)

        img1 = Image.open(r"set1.jpg")
        img1 = img1.resize((235, 200), Image.ADAPTIVE)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(self.custom_frame1, image=self.photoimg1, bd=0, relief=RIDGE)
        lblimg1.pack(side=TOP, fill=BOTH, expand=True)

        # Text
        text_label1 = Label(self.custom_frame1, text="Set Menu 1", font=("times new roman", 15), bg="light grey")
        text_label1.pack(pady=2)

        # Another Text
        text_label2 = Label(self.custom_frame1, text="1000 BDT", font=("times new roman", 15), bg="light grey")
        text_label2.pack(pady=2)

         

        #==============Custom Frame 2======================
        self.custom_frame2 = Frame(self.root, bg="light grey", bd=5, relief=GROOVE)
        self.custom_frame2.place(x=310, y=50, width=235, height=300)

        img2 = Image.open(r"set2.jpeg")
        img2 = img2.resize((235, 200), Image.ADAPTIVE)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.custom_frame2, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg2.pack(side=TOP, fill=BOTH, expand=True)

        # Text
        text_label3 = Label(self.custom_frame2, text="Set Menu 2", font=("times new roman", 15), bg="light grey")
        text_label3.pack(pady=2)

        # Another Text
        text_label4 = Label(self.custom_frame2, text="1200 BDT", font=("times new roman", 15), bg="light grey")
        text_label4.pack(pady=2)

         

        #==============Custom Frame 3======================
        self.custom_frame3 = Frame(self.root, bg="light grey", bd=5, relief=GROOVE)
        self.custom_frame3.place(x=600, y=50, width=235, height=300)

        img3 = Image.open(r"set4.jpeg")
        img3 = img3.resize((235, 200), Image.ADAPTIVE)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(self.custom_frame3, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg3.pack(side=TOP, fill=BOTH, expand=True)

        # Text
        text_label5 = Label(self.custom_frame3, text="Set Menu 3", font=("times new roman", 15), bg="light grey")
        text_label5.pack(pady=2)

        # Another Text
        text_label6 = Label(self.custom_frame3, text="1500 BDT", font=("times new roman", 15), bg="light grey")
        text_label6.pack(pady=2)

         

        #==============Buttons======================
         
        close_btn = Button(self.root, text="Close", font=("times new roman", 16), bg="blue", fg="white", command=self.root.destroy)
        close_btn.place(x=40, y=370, width=100, height=40)

     

if __name__ == "__main__":
    root = Tk()
    obj = SetMenu_now(root)
    root.mainloop()
