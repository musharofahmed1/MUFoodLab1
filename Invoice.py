from tkinter import *
from PIL import Image, ImageTk

class InvoiceGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Invoice")
        self.root.geometry("400x570+1110+80")

        # Title
        lbl_title = Label(self.root, text="Invoice", font=("times new roman", 20, "bold"), bg="black", fg="gold")
        lbl_title.pack(fill=X)

        # Invoice Details Frame
        frame_invoice = Frame(self.root, bd=5, relief=GROOVE)
        frame_invoice.place(x=10, y=50, width=380, height=450)

        lbl_invoice = Label(frame_invoice, text="Invoice Details", font=("times new roman", 14, "bold"))
        lbl_invoice.grid(row=0, column=0, pady=5, padx=20, sticky="w")

        # Example invoice details
        self.lbl_invoice_no = Label(frame_invoice, text="Invoice No:")
        self.lbl_invoice_no.grid(row=1, column=0, pady=2, padx=20, sticky="w")

        self.lbl_date = Label(frame_invoice, text="Date:")
        self.lbl_date.grid(row=2, column=0, pady=2, padx=20, sticky="w")

        self.lbl_total = Label(frame_invoice, text="Total Amount:")
        self.lbl_total.grid(row=3, column=0, pady=2, padx=20, sticky="w")

        # Close Button
        btn_close = Button(self.root, text="Close", font=("times new roman", 16), bg="blue", fg="white", command=self.root.destroy)
        btn_close.place(x=150, y=520, width=100, height=30)

        # Button to simulate adding an item to the invoice
        btn_add_item = Button(self.root, text="Add Item", font=("times new roman", 16), bg="green", fg="white", command=self.add_item_to_invoice)
        btn_add_item.place(x=10, y=520, width=100, height=30)

    def add_item_to_invoice(self):
        # Simulating adding an item to the invoice
        item_name = "Example Item"
        item_price = 50
        item_quantity = 2

        # Call the update_invoice method to update the invoice details
        self.update_invoice(item_name, item_price, item_quantity)

    def update_invoice(self, item_name, item_price, item_quantity):
        # Update the invoice details
        self.lbl_invoice_no.config(text=f"Invoice No: INV123456")
        self.lbl_date.config(text=f"Date: 2023-01-01")

        # Update the total amount (you need to calculate this based on the items)
        total_amount = item_price * item_quantity
        self.lbl_total.config(text=f"Total Amount: ${total_amount}")

if __name__ == "__main__":
    root = Tk()
    obj = InvoiceGenerator(root)
    root.mainloop()
