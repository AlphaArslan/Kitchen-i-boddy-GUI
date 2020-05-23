from time import sleep

def barcode_scan_add_cb():
    for i in range(5):
        print(i)
        sleep(1)

def manual_add_cb():
    sleep(5)

def barcode_scan_remove_cb():
    for i in range(5):
        print(i)
        sleep(1)

def manual_remove_cb():
    sleep(5)
