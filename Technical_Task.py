import os

#List all_items
all_items = {
    "Susu": 50000, 
    "Daging" : 20000, 
    "Lampu" : 15000, 
    "Masker" : 25000, 
    "Apel" : 30000
}

#List promotional_items
promotional_items = ["Susu", "Masker"]

def menu_awal():
    print("Selamat datang di toko Indonesia Sejahtera ^^")
    ##Print promotion item
    for i in range (len(promotional_items)):
        print(str(promotional_items[i]) + " : " + str(all_items[promotional_items[i]]))
    print("1. Beli barang diatas \n2. Lihat Barang Lain\n")
    
    while True:
        try:
            inAwal = int(input("Silahkan pilih menu: "))
            if (inAwal == 1 or inAwal == 2):
                break
            else:
                print("Silahkan pilih 1 atau 2")
                continue
        except ValueError:
            print("Silahkan pilih 1 atau 2")
            continue

    match inAwal :
        case 1 :
            os.system('cls') ##Clear terminal
            promotionItem() ##Jump to promotionItem function
        
        case 2 :
            os.system('cls') ##Clear terminal
            allItems() ##Jump to promotionItem function


def promotionItem():
    listItem = {} ##format =>> Jenis Item : Quantity
    for i in range (len(promotional_items)):
        listItem[promotional_items[i]] = 0
    
    while True:
        print("Keranjang kamu:")
        for i in range (len(listItem)):
            print(str(promotional_items[i]) + " = " + str(listItem[promotional_items[i]]))
        
        print("\n----------------------------------------")
        print("Item mana yang anda mau beli?")
        for i in range (len(promotional_items)):
            print(str(i) + ". " + str(promotional_items[i]) + " : " + str(all_items[promotional_items[i]]))
        print("999. Bayar \n")

        while True:
            try :
                inItem = int(input("Pilih item yang mau dibeli: "))
                if inItem in range (len(promotional_items)):
                    a = listItem[promotional_items[inItem]] + quantity()
                    listItem[promotional_items[inItem]] = a
                    break
                elif inItem == 999:
                    total(1 ,list(listItem.keys()), list(listItem.values())) ##Menu, list item, quantity
                else:
                    print("Input Error! Pilih item yang akan dibeli (Angka)")
                continue
            except ValueError:
                print("Input Error! Pilih item yang akan dibeli (Angka)")
                continue


def allItems():
    listItem = {} ##format =>> Jenis Item : Quantity
    for i in range (len(all_items)):
        listItem[list(all_items.keys())[i]] = 0
    
    while True:
        print("Keranjang kamu:")
        for i in range (len(listItem)):
            print(str(list(all_items.keys())[i]) + " = " + str(listItem[list(all_items.keys())[i]]))
        
        print("\n----------------------------------------")
        print("Item mana yang anda mau beli?")
        for i in range (len(list(all_items.keys()))):
            print(str(i) + ". " + str(list(all_items.keys())[i]) + " : " + str(all_items[list(all_items.keys())[i]]))
        print("999. Bayar \n")

        while True:
            try :
                inItem = int(input("Pilih item yang mau dibeli: "))
                if inItem in range (len(list(all_items.keys()))):
                    a = listItem[list(all_items.keys())[inItem]] + quantity()
                    listItem[list(all_items.keys())[inItem]] = a
                    break
                elif inItem == 999:
                    total(2, list(listItem.keys()), list(listItem.values()))  ##Menu, list item, quantity
                else:
                    print("Input Error! Pilih item yang akan dibeli (Angka)")
                continue
            except ValueError:
                print("Input Error! Pilih item yang akan dibeli (Angka)")
                continue

def quantity(): ##Menghitung kuantiti barang
    while True:
        try:
            qnt = int(input("Berapa banyak yang anda mau?\n"))
            if qnt > 0:
                print("Jumlah : " + str(qnt))
                break
            else:
                print("Jumlah tidak bisa nol (0)")
                continue
        except ValueError:
            print("Input Error! Masukan angka integer")
            continue
    os.system('cls') ##Clear terminal
    return qnt

def total(menu, list_item, quantity): ##Menghitung total harga
    os.system('cls') ##Clear terminal
    if (menu == 1): ##User memilih belanja dari menu barang2 promosi
        totalHarga = 0
        for i in range (len(list_item)):
            totalHarga += all_items[promotional_items[i]] * quantity[i]
        totalHarga = "{:,}".format(totalHarga)
        print("Total Harga : Rp. " + str(totalHarga))
        print("\nDetail :")
        for i in range (len(list_item)):
            print(str(quantity[i]) + " " + str(list_item[i]) + " -> Rp. " + "{:,}".format(all_items[list_item[i]]*quantity[i]))


    elif (menu == 2): ##User memilih belanja dari menu all item
        totalHarga = 0
        for i in range (len(list_item)):
            totalHarga += all_items[list_item[i]] * quantity[i]
        totalHarga = "{:,}".format(totalHarga)
        print("Total Harga : Rp. " + str(totalHarga))
        print("\nDetail :")
        for i in range (len(list_item)):
            print(str(quantity[i]) + " " + str(list_item[i]) + " -> Rp. " + "{:,}".format(all_items[list_item[i]]*quantity[i]))
    exit()

menu_awal()