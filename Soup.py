from tkinter import*

class Soup_on:
    def __init__(self,root):
        self.root = root
        self.root.title("Soup")
        self.root.geometry("915x440+190+80")

        #==============Title======================
        lbl_title = Label(self.root,text="Soup", font=("times new roman",20,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=915,height=30)

         
if __name__ == "__main__":
    root = Tk()
    object = Soup_on(root)
    root.mainloop()