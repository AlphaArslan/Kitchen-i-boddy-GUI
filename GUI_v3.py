from tkinter import *
from tkinter import ttk

from Callback import *

# main window
window = Tk()
window.title("Kitchen i-boddy")
window.geometry("800x480")
window.config(background="#280d69")

####################################################
# a window that pop-up when u click the Add button
def add_window():
    add_win = Toplevel(window)
    add_win.title("Add an item")
    add_win.geometry("800x480")
    add_win.config(background="#280d69")

    add_frame = Frame(add_win, bg="red")
    add_frame.pack(expand=1, fill='both')

    # splitting the window virtecally
    upper_half = Frame(add_frame, bg="#369c5c")
    upper_half.pack(expand=1, fill='both')
    lower_half = Frame(add_frame, bg="#146131")
    lower_half.pack(expand=1, fill='both')

    # manually add item
    item_name_tb = Text(upper_half, width=20,   height= 1,
                                                bg= "#fcffeb",
                                                font= ("Arial", 18),
                                                insertborderwidth= 20)
    item_name_tb.insert(END, "Enter Item Name")
    #item_name = item_name_tb.get()
    item_name_tb.place(relx=0.3, rely=0.4, anchor=CENTER)


    # Expiration 0.3 0.6
    exp_year_combo = ttk.Combobox(upper_half,   width= 5,
                                                background= "#fcffeb",
                                                font= ("Arial", 18))
    exp_year_combo['values'] = (2020, 2021, 2022, 2023, 2024, 2025)
    exp_year_combo.set("Year")
    exp_year_combo.place(relx=0.15, rely=0.56, anchor=CENTER)

    exp_month_combo = ttk.Combobox(upper_half,  width= 9,
                                                background= "#fcffeb",
                                                font= ("Arial", 18))
    exp_month_combo['values'] = (   "January",  "February", "March",
                                    "April",    "May",      "June",
                                    "Julie",    "Ougust",   "September",
                                    "October",  "November", "December")
    exp_month_combo.set("Month")
    exp_month_combo.place(relx=0.31, rely=0.56, anchor=CENTER)

    exp_day_combo = ttk.Combobox(upper_half,    width= 4,
                                                background= "#fcffeb",
                                                font= ("Arial", 18))
    exp_day_combo['values'] =        (  1,  2,  3,  4,  5,  6,
                                        7,  8,  9,  10, 11, 12,
                                        13, 14, 15, 16, 17, 18,
                                        19, 20, 21, 22, 23, 24,
                                        25, 26, 27, 28, 29, 30,
                                        31,)
    exp_day_combo.set("Day")
    exp_day_combo.place(relx=0.45, rely=0.56, anchor=CENTER)

    items_num = IntVar()
    items_num_spin = Spinbox(upper_half, from_=1,    to=100, width=5,
                                                     bg= "#fcffeb",
                                                     font= ("Arial", 18),
                                                     textvariable=items_num)
    items_num_spin.place(relx=0.56, rely=0.5, anchor=CENTER)

    manual_add_btn = Button(upper_half, text= "Manual Add",
                                           bg="#5780d9",
                                           font=("Arial Black", 20),
                                           command= manual_add_cb)
    manual_add_btn.place(relx=0.75, rely=0.5, anchor=CENTER)

    # barcode scan add item
    barcode_scan_add_btn = Button(lower_half, text= "Barcode Scan",
                                                 bg= "#5780d9",
                                                 font= ("Arial Black", 20),
                                                 command= barcode_scan_add_cb)
    barcode_scan_add_btn.place(relx=0.5, rely=0.5, anchor=CENTER)

####################################################
# a window that pop-up when u click the Remove button
def rmv_window():
    rmv_win = Toplevel(window)
    rmv_win.title("Remove an item")
    rmv_win.geometry("800x480")
    rmv_win.config(background="#280d69")

    #splitting the tab virtecally
    upper_half = Frame(rmv_win, bg="#c41854")
    upper_half.pack(expand=1, fill='both')
    lower_half = Frame(rmv_win, bg="#6b1332")
    lower_half.pack(expand=1, fill='both')

    # manually remove item
    manual_remove_btn = Button(upper_half, text= "Remove from Inventory",
                                           bg="#910c20",
                                           fg="white",
                                           font=("Arial Black", 20),
                                           command= invt_window)
    manual_remove_btn.place(relx=0.5, rely=0.5, anchor=CENTER)

    # barcode scan remove item
    barcode_scan_remove_btn = Button(lower_half, text= "Barcode Scan",
                                                 bg= "#910c20",
                                                 fg="white",
                                                 font= ("Arial Black", 20),
                                                 command= barcode_scan_remove_cb)
    barcode_scan_remove_btn.place(relx=0.5, rely=0.5, anchor=CENTER)

####################################################
# a window that pop-up when u click the Inventory button
def invt_window():
    invt_win = Toplevel(window)
    invt_win.title("Inventory")
    invt_win.geometry("800x480")
    invt_win.config(background="#280d69")
    invt_frame = Frame(invt_win, bg="#e0c1c8")
    invt_frame.pack(expand=1, fill='both')

    items = [   "item1 - Expiration Date - number",
                "item2 - Expiration Date - number",
                "item3 - Expiration Date - number",
                "item4 - Expiration Date - number",
                "item5 - Expiration Date - number",
                "item6 - Expiration Date - number",
                "item7 - Expiration Date - number",
                "item8 - Expiration Date - number",
                "item1 - Expiration Date - number",
                "item2 - Expiration Date - number",
                "item3 - Expiration Date - number",
                "item4 - Expiration Date - number",
                "item5 - Expiration Date - number",
                "item6 - Expiration Date - number",
                "item7 - Expiration Date - number",
                "item8 - Expiration Date - number"  ]

    chk_vars_list = []
    for _ in range(len(items)):
        chk_vars_list.append(BooleanVar())

    for i in range(len(items)):
        Checkbutton(        invt_frame,
                            height= 1,
                            width=  26,
                            text= items[i],
                            font= ("Arial Black", 12),
                            var=chk_vars_list[i]
                            ).place(relx= (i//10) / 2.5 + 0.02,
                                    rely= (i%10) / 10 + 0.02,
                                    anchor= NW)

    remove_selected_btn = Button(   invt_frame, text= "Remove Selected",
                                    bg="#910c20",
                                    fg="white",
                                    font= ("Arial Black", 16),
                                    height= 1,
                                    width= 15)
    remove_selected_btn.place(relx= 0.83, rely= 0.92, anchor= CENTER)

####################################################
# a window that pop-up when u click the Settings button
def stng_window():
    stng_win = Toplevel(window)
    stng_win.title("Settings")
    stng_win.geometry("800x480")
    stng_win.config(background="#280d69")
    stng_frame = Frame(stng_win, bg="#5c5355")
    stng_frame.pack(expand=1, fill='both')



####################################################
# adding main window buttons
# main frame
main_frame = Frame(window, bg="#280d69")
main_frame.pack(expand=1, fill='both')
# add
main_add_btn = Button(main_frame,   text= "Add",
                                    bg= "#116339",
                                    font= ("Arial Black", 20),
                                    height= 3,
                                    width= 10,
                                    command= add_window)
main_add_btn.place(relx=0.33, rely=0.33, anchor=CENTER)

#remove
main_remove_btn = Button(main_frame,text= "Remove",
                                    bg= "#91243e",
                                    font= ("Arial Black", 20),
                                    height= 3,
                                    width= 10,
                                    command= rmv_window)
main_remove_btn.place(relx=0.67, rely=0.33, anchor=CENTER)

#inventory
main_inventory_btn = Button(main_frame, text= "Inventory",
                                        bg= "#e0c1c8",
                                        font= ("Arial Black", 20),
                                        height= 3,
                                        width= 10,
                                        command= invt_window)
main_inventory_btn.place(relx=0.33, rely=0.67, anchor=CENTER)

#settings
main_settings_btn = Button(main_frame,  text= "Settings",
                                        bg= "#5c5355",
                                        font= ("Arial Black", 20),
                                        height= 3,
                                        width= 10,
                                        command= stng_window)
main_settings_btn.place(relx=0.67, rely=0.67, anchor=CENTER)

####################################################
window.mainloop()
