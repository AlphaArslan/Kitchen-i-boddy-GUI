from tkinter import *
from tkinter import ttk

from Callback import *

# main window
window = Tk()
window.title("Kitchen i-boddy")
window.geometry("800x600")

# tab styling (increase font size)
s = ttk.Style()
s.theme_create( "MyStyle", parent="clam", settings={
        "TNotebook": {"configure": {"tabmargins": [20, 5, 2, 0], "background": "white" } },
        "TNotebook.Tab": {"configure": {"padding": [80, 10],
                                        "font" : ('URW Gothic L', '11', 'bold'),
                                        "background" : "#87e5ff" },}})
s.theme_use("MyStyle")
#s.theme_use("winnative")

# tabs
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Add Items')
tab_control.add(tab2, text='Remove Items')
tab_control.add(tab3, text='Show Items')


# tab1 "Add Items" Content
#splitting the tab virtecally
t1_upper_half = Frame(tab1, bg="#329691")
t1_upper_half.pack(expand=1, fill='both')
t1_lower_half = Frame(tab1, bg="#9bd4d1")
t1_lower_half.pack(expand=1, fill='both')

# manually add item
item_name_tb = Text(t1_upper_half, width=20, height= 1,
                                             bg= "#fcffeb",
                                             font= ("Arial", 18),
                                             insertborderwidth= 20)
item_name_tb.insert(END, "Enter Item Name")
#item_name = item_name_tb.get()
item_name_tb.place(relx=0.3, rely=0.4, anchor=CENTER)

Expiration_tb = Text(t1_upper_half, width=15, height= 1,
                                             bg= "#fcffeb",
                                             font= ("Arial", 18),
                                             insertborderwidth= 20)
Expiration_tb.insert(END, "YYYY-MM-DD")
#item_name = item_name_tb.get()
Expiration_tb.place(relx=0.3, rely=0.6, anchor=CENTER)

items_num = IntVar()
items_num_spin = Spinbox(t1_upper_half, from_=1, to=100, width=5,
                                                 bg= "#fcffeb",
                                                 font= ("Arial", 18),
                                                 textvariable=items_num)
items_num_spin.place(relx=0.55, rely=0.5, anchor=CENTER)

manual_add_btn = Button(t1_upper_half, text= "Manual Add",
                                       bg="#5780d9",
                                       font=("Arial Black", 20),
                                       command= manual_add_cb)
manual_add_btn.place(relx=0.75, rely=0.5, anchor=CENTER)

# barcode scan add item
barcode_scan_add_btn = Button(t1_lower_half, text= "Barcode Scan",
                                             bg= "#5780d9",
                                             font= ("Arial Black", 20),
                                             command= barcode_scan_add_cb)
barcode_scan_add_btn.place(relx=0.5, rely=0.5, anchor=CENTER)



# tab2 "remove items"
#splitting the tab virtecally
t1_upper_half = Frame(tab2, bg="#f26f83")
t1_upper_half.pack(expand=1, fill='both')
t1_lower_half = Frame(tab2, bg="#b83246")
t1_lower_half.pack(expand=1, fill='both')

# manually remove item
item_name_tb_r = Text(t1_upper_half, width=20, height= 1,
                                             bg= "#fcffeb",
                                             font= ("Arial", 18),
                                             insertborderwidth= 20)
item_name_tb_r.insert(END, "Enter Item Name")
#item_name_r = item_name_tb_r.get()
item_name_tb_r.place(relx=0.27, rely=0.4, anchor=CENTER)

Expiration_tb_r = Text(t1_upper_half, width=15, height= 1,
                                             bg= "#fcffeb",
                                             font= ("Arial", 18),
                                             insertborderwidth= 20)
Expiration_tb_r.insert(END, "YYYY-MM-DD")
#Expiration_r = Expiration_tb_r.get()
Expiration_tb_r.place(relx=0.27, rely=0.6, anchor=CENTER)

items_num_r = IntVar()
items_num_spin_r = Spinbox(t1_upper_half, from_=1, to=100, width=4,
                                                 bg= "#fcffeb",
                                                 font= ("Arial", 18),
                                                 textvariable=items_num_r)
items_num_spin_r.place(relx=0.52, rely=0.5, anchor=CENTER)

manual_remove_btn = Button(t1_upper_half, text= "Manual Remove",
                                       bg="#910c20",
                                       fg="white",
                                       font=("Arial Black", 20),
                                       command= manual_remove_cb)
manual_remove_btn.place(relx=0.75, rely=0.5, anchor=CENTER)

# barcode scan add item
barcode_scan_remove_btn = Button(t1_lower_half, text= "Barcode Scan",
                                             bg= "#910c20",
                                             fg="white",
                                             font= ("Arial Black", 20),
                                             command= barcode_scan_remove_cb)
barcode_scan_remove_btn.place(relx=0.5, rely=0.5, anchor=CENTER)




# packing the tabs
tab_control.pack(expand=1, fill='both')

window.mainloop()
