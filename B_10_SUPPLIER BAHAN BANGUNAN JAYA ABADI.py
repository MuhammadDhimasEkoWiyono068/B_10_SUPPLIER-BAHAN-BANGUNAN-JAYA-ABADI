import os
import time
from prettytable import PrettyTable
print("LOADING.......PLEASE WAIT")
print()
time.sleep(2)
print("LOADING.......0%")
time.sleep(4)
print("LOADING.......25%")
time.sleep(6)
print("LOADING.......75%")
time.sleep(4)
print("LOADING COMPLETE!!!")
time.sleep(1)
os.system("cls")

class color:
   biru = '\033[94m'
   hijau = '\033[92m'
   kuning = '\033[93m'
   merah = '\033[91m'
   ungu = '\033[95m'
   end = '\033[0m'
   bold = '\033[1m'

username = ["Admin", "User"]
password = ["112233", "123"]
sebagai = ["Admin", "User"]

data_bahanbangunan = [["semen", 100, 50000, "bahan"],
                     ["keramik", 500, 10000, "bahan"],
                     ["kayu gelam", 700, 8000, "bahan"],
                     ["besi pondasi", 800, 20000, "bahan"],
                     ["batu bata", 10000, 1200, "bahan"],
                     ["pasir per pickup", 50, 585000,"bahan"],
                     ["seng", 1000, 72000, "bahan"]]

data_alatmanual = [["sekop", 50, 49000, "alat manual"],
                  ["palu", 30, 35000, "alat manual"],
                  ["gergaji", 25, 73000, "alat manual"],
                  ["meteran", 10, 105000, "alat manual"],
                  ["sendok semen", 40, 20000, "alat manual"],
                  ["roller cat", 70, 20000, "alat manual"]]

data_alatelektronik = [["bor", 15, 359000, "alat elektronik"],
                      ["gergaji mesin", 5, 3500000, "alat elektronik"],
                      ["mesin ketam", 10, 380000, "alat elektronik"],
                      ["mesin paku tembak", 15, 490000, "alat elektronik"],
                      ["pemotong kayu", 7, 1900000, "alat elektronik"],
                      ["mesin las", 6, 1825000, "alat elektronik"]]
              

data_penyewaanjasa = [["tukang kayu per hari", 30, 100000, "penyewaan jasa"],
                     ["tukang cat per meter", 20, 25000, "penyewaan jasa"],
                     ["tukang gali per hari", 30, 80000, "penyewaan jasa"],
                     ["tukang besi beton", 35, 120000, "penyewaan jasa"]]

data_penyewaanalat = [["mesin molen per hari", 10, 65000, "penyewaan alat"],
                     ["genset per hari", 13, 50000, "penyewaan alat"],
                     ["kompressor per hari", 7, 80000, "penyewaan alat"],
                     ["scaffolding per hari", 8, 10000, "penyewaan alat"],
                     ["stamper per hari", 13, 50000, "penyewaan alat"],
                     ["jack hammer per hari", 12, 60000, "penyewaan alat"]]

#def admin
def lihat_stock():
    print(color.biru + "||===========================================||")
    print("||  Silahkan pilih data yang ingin di lihat  ||")
    print("||===========================================||")
    print("||    1. Bahan Bangunan                      ||")
    print("||    2. Alat Bangunan                       ||")
    print("||    3. Penyewaan                           ||")
    print("||===========================================||" + color.end)
    lihat_data = input(color.hijau + "Masukan data yang ingin di lihat : " + color.end)
    if (lihat_data == "Bahan Bangunan" or lihat_data == "bahan bangunan" or lihat_data == "1"):
        table = PrettyTable(["Nama", "Jumlah", "Harga", "Jenis"])
        for x in data_bahanbangunan:
            table.add_row(x)
        table.align = "l"
        print(table)
    elif (lihat_data == "alat bangunan" or lihat_data == "Alat Bangunan" or lihat_data == "2"):
        print(color.biru + "||===========================================||")
        print("||    1. Alat Manual                         ||")
        print("||    2. Alat Elektronik                     ||")
        print("||===========================================||" + color.end)
        menu_alat1 = input(color.hijau + "Masukkan pilihan anda : " + color.end)
        if (menu_alat1 == "Alat Manual" or menu_alat1 == "alat manual" or menu_alat1 == "1"):
            table = PrettyTable(["Nama", "Jumlah", "Harga", "Jenis"])
            for x in data_alatmanual:
                table.add_row(x)
            table.align = "l"
            print(table)
        elif (menu_alat1 == "Alat Elektronik" or menu_alat1 == "alat elektronik" or menu_alat1 == "2"):
            table = PrettyTable(["Nama", "Jumlah", "Harga", "Jenis"])
            for x in data_alatelektronik:
                table.add_row(x)
            table.align = "l"
            print(table)
        else:
            print(color.merah + "Saat ini hanya data diatas yang tersedia" + color.end)
    elif (lihat_data == "penyewaan" or lihat_data == "Penyewaan" or lihat_data == "3"):
        print(color.biru + "||===========================================||")
        print("||    1. Penyewaan Jasa                      ||")
        print("||    2. Penyewaan Alat                      ||")
        print("||===========================================||" + color.end)
        menu_penyewaan1 = input(color.hijau + "Masukkan pilihan anda : " + color.end)
        if (menu_penyewaan1 == "Penyewaan Jasa" or menu_penyewaan1 == "penyewaan jasa" or menu_penyewaan1 == "1"):
            table = PrettyTable(["Nama", "Jumlah", "Harga", "Jenis"])
            for x in data_penyewaanjasa:
                table.add_row(x)
            table.align = "l"
            print(table)
        elif (menu_penyewaan1 == "Penyewaan Alat" or menu_penyewaan1 == "penyewaan alat" or menu_penyewaan1 == "2"):
            table = PrettyTable(["Nama", "Jumlah", "Harga", "Jenis"])
            for bahan in data_penyewaanalat:
                table.add_row(bahan)
            table.align = "l"
            print(table)
        else:
            print(color.merah + "Saat ini hanya data diatas yang tersedia" + color.end)
    else:
        print(color.merah + "Maaf data yang anda pilih tidak tersedia" + color.end)
    time.sleep(10)
    os.system("cls")
    print(color.kuning + "||===========================================||")
    print("||          Kembali ke menu Admin            ||")
    print("||===========================================||" + color.end)

def tambah_stock():
    try:
        nama  = input(color.ungu + "Nama : " + color.end)
        jumlah = int(input(color.ungu + "Jumlah : " + color.end))
        harga = int(input(color.ungu + "Harga : " + color.end))
        jenis = input(color.ungu + "Jenis : " + color.end)
    except ValueError:
        print(color.merah + "Salah satu data yang di inputkan salah" + color.end)
        time.sleep(2)
        print(color.merah + ">Masukkan kembali data dengan benar<" + color.end)
        tambah_stock()
    else:
        if (jumlah and harga <=0):
            print(color.merah + "Data yang di Inputkan tidak valid" + color.end)
        else:
            print(color.biru + "||===========================================||")
            print("||    1. Bahan Bangunan                      ||")
            print("||    2. Alat Bangunan                       ||")
            print("||    3. Penyewaan                           ||")
            print("||===========================================||" + color.end)
            data_toko_b = input(color.hijau + "Masukan data yang ingin diupdate atau di tambahkan : " + color.end)
            if (data_toko_b == "bahan bangunan" or data_toko_b == "Bahan Bangunan" or data_toko_b == "1"):
                data_bahanbangunan.append([nama, jumlah, harga, jenis])
                print(color.kuning + "Berhasil menambahkan!")
                print("Data bahan bangunan berhasil diperbarui" + color.end)       
            elif (data_toko_b == "Alat Bangunan" or data_toko_b == "alat bangunan" or data_toko_b == "2"):
                print(color.biru + "||===========================================||")
                print("||    1. Alat Manual                         ||")
                print("||    2. Alat Elektronik                     ||")
                print("||===========================================||" + color.end)
                menu_alat = input("Masukkan pilihan anda : ")
                if (menu_alat == "Alat Manual" or menu_alat == "alat manual" or menu_alat == "1"):
                    data_alatmanual.append([nama, jumlah, harga, jenis])
                    print(color.kuning + "Berhasil menambahkan!")
                    print("Data alat manual berhasil diperbarui" + color.end)
                elif (menu_alat == "Alat Elektronik" or menu_alat == "alat elektronik" or menu_alat == "2"):
                    data_alatelektronik.append([nama, jumlah, harga, jenis])
                    print(color.kuning + "Berhasil menambahkan!")
                    print("Data alat elektronik berhasil diperbarui" + color.end)
                else:
                    print(color.merah + "Saat ini hanya data diatas yang tersedia" + color.end)                      
            elif (data_toko_b == "penyewaan" or data_toko_b == "Penyewaan" or data_toko_b == "3"):
                print(color.biru + "||==========================================||")
                print("||    1. Penyewaan Jasa                     ||")
                print("||    2. Penyewaan Alat                     ||")
                print("||==========================================||" + color.end)
                menu_penyewaan = input(color.hijau + "Masukkan pilihan anda : " + color.end)
                if (menu_penyewaan == "Penyewaan Jasa" or menu_penyewaan == "penyewaan jasa" or menu_penyewaan == "1"):
                    data_penyewaanjasa.append([nama, jumlah, harga, jenis])
                    print(color.kuning + "berhasil menambahkan!")
                    print("Data penyewaan jasa berhasil diperbarui" + color.end)
                elif (menu_penyewaan == "Penyewaan Alat" or menu_penyewaan == "penyewaan alat" or menu_penyewaan == "2"):
                    data_penyewaanalat.append([nama, jumlah, harga, jenis])
                    print(color.kuning + "Berhasil menambahkan!")
                    print("Data penyewaan alat berhasil diperbarui" + color.end)
                else:
                    print(color.merah + "Saat ini hanya data diatas yang tersedia" + color.end)
            else:
                print(color.merah + "Maaf data yang anda pilih tidak tersedia" + color.end)
        time.sleep(3)
        os.system("cls")
        print(color.kuning + "||===========================================||")
        print("||========= Kembali ke menu Admin ===========||")
        print("||===========================================||" + color.end)

def update_stock():
    def bahan_bangunan():
        table = PrettyTable(["Nama", "Jumlah", "Harga", "Jenis"])
        for x in data_bahanbangunan:
            table.add_row(x)
        table.align = "l"
        print(table)
        cek_barang1 = len(data_bahanbangunan) - 1
        N_barang1 = input(color.hijau + "Masukkan nama bahan bangunan : " + color.end)
        while (cek_barang1 >= 0):
            if (N_barang1 == data_bahanbangunan[cek_barang1][0]):
                break
            else:
                cek_barang1 -= 1
        if (cek_barang1 >= 0):
            print(color.hijau + ">Masukkan data baru : " + color.end)
            try:
                PJ_barang = int(input(color.hijau + "Masukkan jumlah : " + color.end))
                data_bahanbangunan[cek_barang1][1] = PJ_barang
                PJ_barang = int(input(color.hijau + "Masukkan Harga : " + color.end))
                data_bahanbangunan[cek_barang1][2] = PJ_barang
            except ValueError:
                print(color.merah + "Data baru yang di masukkan salah" + color.end)
                time.sleep(2)
                os.system("cls")
                print(color.merah + "Mohon masukkan kembali data yang ingin di update dengan benar" + color.end)
                bahan_bangunan()
            else:                
                print(color.kuning + "Data bahan bangunan berhasil di update" + color.end)
        else:
            print(color.merah + "Maaf bahan bangunan yang dimasukkan tidak ada" + color.end)
    def alat_bangunan():
        print(color.biru + "||===========================================||")
        print("||    1. Alat Manual                         ||")
        print("||    2. Alat Elektronik                     ||")
        print("||===========================================||" + color.end)
        menu_alat2 = input(color.hijau + "Masukkan pilihan anda : " + color.end)
        if (menu_alat2 == "Alat Manual" or menu_alat2 == "alat manual" or menu_alat2 == "1"):
            table = PrettyTable(["Nama", "Jumlah", "Harga", "Jenis"])
            for x in data_alatmanual:
                table.add_row(x)
            table.align = "l"
            print(table)
            cek_barang1 = len(data_alatmanual) - 1
            N_barang1 = input(color.hijau + "Masukkan nama alat manual : " + color.end)
            while (cek_barang1 >= 0):
                if (N_barang1 == data_alatmanual[cek_barang1][0]):
                    break
                else:
                    cek_barang1 -= 1
            if (cek_barang1 >= 0):
                print(color.hijau + ">Masukkan data baru : " + color.end)
                try:
                    PJ_barang = int(input(color.hijau + "Masukkan jumlah alat : " + color.end))
                    data_alatmanual[cek_barang1][1] = PJ_barang
                    PJ_barang = int(input(color.hijau + "Masukkan Harga : " + color.end))
                    data_alatmanual[cek_barang1][2] = PJ_barang
                except ValueError:
                    print(color.merah + "Data baru yang di masukkan salah" + color.end)
                    time.sleep(2)
                    os.system("cls")
                    print(color.merah + "Mohon masukkan kembali data yang ingin di update dengan benar" + color.end)
                    alat_bangunan()
                else:
                    print(color.kuning + "Data alat manual berhasil di update" + color.end)
            else:
                print(color.merah + "Maaf alat manual yang dimasukkan tidak ada" + color.end)
        elif (menu_alat2 == "Alat Elektronik" or menu_alat2 == "alat elektronik" or menu_alat2 == "2"):
            table = PrettyTable(["Nama", "Jumlah", "Harga", "Jenis"])
            for x in data_alatelektronik:
                table.add_row(x)
            table.align = "l"
            print(table)
            cek_barang1 = len(data_alatelektronik) - 1
            N_barang1 = input(color.hijau + "Masukkan nama alat elektronik : " + color.end)
            while (cek_barang1 >= 0):
                if (N_barang1 == data_alatelektronik[cek_barang1][0]):
                    break
                else:
                    cek_barang1 -= 1
            if (cek_barang1 >= 0):
                print(color.hijau + ">Masukkan data baru : " + color.end)
                try:
                    PJ_barang = int(input(color.hijau + "Masukkan jumlah alat : " + color.end))
                    data_alatelektronik[cek_barang1][1] = PJ_barang
                    PJ_barang = int(input(color.hijau + "Masukkan Harga : " + color.end))
                    data_alatelektronik[cek_barang1][2] = PJ_barang
                except ValueError:
                    print(color.merah + "Data baru yang di masukkan salah" + color.end)
                    time.sleep(2)
                    os.system("cls")
                    print(color.merah + "Mohon masukkan kembali data yang ingin di update dengan benar" + color.end)
                    alat_bangunan()
                else:
                    print(color.kuning + "Data alat elektronik berhasil di update" + color.end)
            else:
                print(color.merah + "Maaf alat elektronik yang dimasukkan tidak ada" + color.end)
        else:
            print(color.merah + "Saat ini hanya data diatas yang tersedia" + color.end)
    def penyewaan():
        print(color.biru + "||===========================================||")
        print("||    1. Penyewaan Jasa                      ||")
        print("||    2. Penyewaan Alat                      ||")
        print("||===========================================||" + color.end)
        menu_penyewaan2 = input(color.hijau + "Masukkan pilihan anda : " + color.end)
        if (menu_penyewaan2 == "Penyewaan Jasa" or menu_penyewaan2 == "penyewaan jasa" or menu_penyewaan2 == "1"):
            table = PrettyTable(["Nama", "Jumlah", "Harga", "Jenis"])
            for x in data_penyewaanjasa:
                table.add_row(x)
            table.align = "l"
            print(table)
            cek_barang1 = len(data_penyewaanjasa) - 1
            N_barang1 = input(color.hijau + "Masukkan nama penyewaan jasa : " + color.end)
            while (cek_barang1 >= 0):
                if (N_barang1 == data_penyewaanjasa[cek_barang1][0]):
                    break
                else:
                    cek_barang1 -= 1
            if (cek_barang1 >= 0):
                print(color.hijau + ">Masukkan data baru : " + color.end)
                try:
                    PJ_barang = int(input(color.hijau + "Masukkan jumlah penyewaan : " + color.end))
                    data_penyewaanjasa[cek_barang1][1] = PJ_barang
                    PJ_barang = int(input(color.hijau + "Masukkan Harga : " + color.end))
                    data_penyewaanjasa[cek_barang1][2] = PJ_barang
                except ValueError:
                    print(color.merah + "Data baru yang di masukkan salah" + color.end)
                    time.sleep(2)
                    os.system("cls")
                    print(color.merah + "Mohon masukkan kembali data yang ingin di update dengan benar" + color.end)
                    penyewaan()
                else:
                    print(color.kuning + "Data penyewaan jasa berhasil di update" + color.end)
            else:
                print(color.merah + "Maaf penyewaan jasa yang dimasukkan tidak ada" + color.end)
        elif (menu_penyewaan2 == "Penyewaan Alat" or menu_penyewaan2 == "penyewaan alat" or menu_penyewaan2 == "2"):
            table = PrettyTable(["Nama", "Jumlah", "Harga", "Jenis"])
            for x in data_penyewaanalat:
                table.add_row(x)
            table.align = "l"
            print(table)
            cek_barang1 = len(data_penyewaanalat) - 1
            N_barang1 = input(color.hijau + "Masukkan nama penyewaan alat : " + color.end)
            while (cek_barang1 >= 0):
                if (N_barang1 == data_penyewaanalat[cek_barang1][0]):
                    break
                else:
                    cek_barang1 -= 1
            if (cek_barang1 >= 0):
                print(color.hijau + ">Masukkan data baru : " + color.end)
                try:
                    PJ_barang = int(input(color.hijau + "Masukkan jumlah penyewaan : " + color.end))
                    data_alatmanual[cek_barang1][1] = PJ_barang
                    PJ_barang = int(input(color.hijau + "Masukkan Harga : " + color.end))
                    data_alatmanual[cek_barang1][2] = PJ_barang
                except ValueError:
                    print(color.merah + "Data baru yang di masukkan salah" + color.end)
                    time.sleep(2)
                    os.system("cls")
                    print(color.merah + "Mohon masukkan kembali data yang ingin di update dengan benar" + color.end)
                    penyewaan()
                else:
                    print(color.kuning + "Data penyewaan alat berhasil di update" + color.end)
            else:
                print(color.merah + "Maaf penyewaan alat yang dimasukkan tidak ada" + color.end)
        else:
            print(color.merah + "Saat ini hanya data diatas yang tersedia" + color.end)        
    print(color.biru + "||===========================================||")
    print("||    1. Bahan Bangunan                      ||")
    print("||    2. Alat Bangunan                       ||")
    print("||    3. Penyewaan                           ||")
    print("||===========================================||" + color.end)
    tambah_jumlah = input(color.hijau + "Masukan data yang ingin di update : " + color.end)
    if (tambah_jumlah == "Bahan Bangunan" or tambah_jumlah == "bahan bangunan" or tambah_jumlah == "1"):
        bahan_bangunan()
    elif (tambah_jumlah == "Alat Bangunan" or tambah_jumlah == "alat bangunan" or tambah_jumlah == "2"):
        alat_bangunan()
    elif (tambah_jumlah == "Penyewaan" or tambah_jumlah == "penyewaan" or tambah_jumlah == "3"):
        penyewaan()
    else:
        print(color.merah + "Maaf data yang anda pilih tidak tersedia" + color.end)
    time.sleep(3)
    os.system("cls")
    print(color.kuning + "||===========================================||")
    print("||          Kembali ke menu Admin            ||")
    print("||===========================================||" + color.end)

def hapus_stock():
    print(color.biru + "||===========================================||")
    print("||  Silahkan pilih data yang ingin di hapus  ||")
    print("||===========================================||")
    print("||    1. Bahan Bangunan                      ||")
    print("||    2. Alat Bangunan                       ||")
    print("||    3. Penyewaan                           ||")
    print("||===========================================||" + color.end)
    hapus_data = input(color.hijau + "Masukan nama data yang ingin di hapus : " + color.end)
    if (hapus_data == "Bahan Bangunan" or hapus_data == "bahan bangunan" or hapus_data == "1"):
        table = PrettyTable(["Nama", "Jumlah", "Harga", "Jenis"])
        for x in data_bahanbangunan:
            table.add_row(x)
        table.align = "l"
        print(table)
        cek_barang2 = len(data_bahanbangunan) - 1
        N_barang2 = input(color.hijau + "Masukkan salah satu nama bahan bangunan yang ingin di hapus : " + color.end)
        while (cek_barang2 >= 0):
            if (N_barang2 == data_bahanbangunan[cek_barang2][0]):
                break
            else:
                cek_barang2 -= 1
        if (cek_barang2 >= 0):
            del data_bahanbangunan[cek_barang2]
            print(color.kuning + "Berhasil menghapus bahan bangunan" + color.end)
        else:
            print(color.merah + "Maaf nama bahan bangunan yang anda masukkan tidak ada" + color.end)
    elif (hapus_data == "Alat Bangunan" or hapus_data == "alat bangunan" or hapus_data == "2"):
        print(color.biru + "||===========================================||")
        print("||    1. Alat Manual                         ||")
        print("||    2. Alat Elektronik                     ||")
        print("||===========================================||" + color.end)
        menu_alat3 = input(color.hijau + "Masukkan pilihan anda : " + color.end)
        if (menu_alat3 == "Alat Manual" or menu_alat3 == "alat manual" or menu_alat3 == "1"): 
            table = PrettyTable(["Nama", "Jumlah", "Harga", "Jenis"])
            for x in data_alatmanual:
                table.add_row(x)
            table.align = "l"
            print(table)
            cek_barang2 = len(data_alatmanual) - 1
            N_barang2 = input(color.hijau + "Masukkan salah satu nama alat manual yang ingin di hapus : " + color.end)
            while (cek_barang2 >= 0):
                if (N_barang2 == data_alatmanual[cek_barang2][0]):
                    break
                else:
                    cek_barang2 -= 1
            if (cek_barang2 >= 0):
                del data_alatmanual[cek_barang2]
                print(color.kuning + "Berhasil menghapus alat manual" + color.end)
            else:
                print(color.merah + "Maaf nama alat manual yang anda masukkan tidak ada" + color.end)
        elif (menu_alat3 == "Alat Elektronik" or menu_alat3 == "alat elektronik" or menu_alat3 == "2"):
            table = PrettyTable(["Nama", "Jumlah", "Harga", "Jenis"])
            for x in data_alatelektronik:
                table.add_row(x)
            table.align = "l"
            print(table)
            cek_barang2 = len(data_alatelektronik) - 1
            N_barang2 = input(color.hijau + "Masukkan salah satu nama alat elektronik yang ingin di hapus : " + color.end)
            while (cek_barang2 >= 0):
                if (N_barang2 == data_alatelektronik[cek_barang2][0]):
                    break
                else:
                    cek_barang2 -= 1
            if (cek_barang2 >= 0):
                del data_alatelektronik[cek_barang2]
                print(color.kuning + "Berhasil menghapus alat elektronik" + color.end)
            else:
                print(color.merah + "Maaf nama alat elektronik yang anda masukkan tidak ada" + color.end)
        else:
            print(color.merah + "Saat ini hanya data diatas yang tersedia" + color.end)
    elif (hapus_data == "Penyewaan" or hapus_data == "penyewaan" or hapus_data == "3"):
        print(color.biru + "||===========================================||")
        print("||    1. Penyewaan Jasa                      ||")
        print("||    2. Penyewaan Alat                      ||")
        print("||===========================================||" + color.end)
        menu_penyewaan3 = input(color.hijau + "masukkan pilihan anda : " + color.end)
        if (menu_penyewaan3 == "Penyewaan Jasa" or menu_penyewaan3 == "penyewaan jasa" or menu_penyewaan3 == "1"): 
            table = PrettyTable(["Nama", "Jumlah", "Harga", "Jenis"])
            for x in data_penyewaanjasa:
                table.add_row(x)
            table.align = "l"
            print(table)
            cek_barang2 = len(data_penyewaanjasa) - 1
            N_barang2 = input(color.hijau + "Masukkan salah satu penyewaan jasa yang ingin di hapus : " + color.end)
            while (cek_barang2 >= 0):
                if (N_barang2 == data_penyewaanjasa[cek_barang2][0]):
                    break
                else:
                    cek_barang2 -= 1
            if (cek_barang2 >= 0):
                del data_penyewaanjasa[cek_barang2]
                print(color.kuning + "Berhasil menghapus penyewaan jasa" + color.end)
            else:
                print(color.merah + "Maaf nama penyewaan jasa yang anda masukkan tidak ada" + color.end)
        elif (menu_penyewaan3 == "Penyewaan Alat" or menu_penyewaan3 == "penyewaan alat" or menu_penyewaan3 == "2"):
            table = PrettyTable(["Nama", "Jumlah", "Harga", "Jenis"])
            for x in data_penyewaanalat:
                table.add_row(x)
            table.align = "l"
            print(table)
            cek_barang2 = len(data_penyewaanalat) - 1
            N_barang2 = input(color.hijau + "Masukkan salah satu penyewaan alat yang ingin di hapus : " + color.end)
            while (cek_barang2 >= 0):
                if (N_barang2 == data_penyewaanalat[cek_barang2][0]):
                    break
                else:
                    cek_barang2 -= 1
            if (cek_barang2 >= 0):
                del data_penyewaanalat[cek_barang2]
                print(color.kuning + "Berhasil menghapus penyewaan alat" + color.end)
            else:
                print(color.merah + "Maaf nama penyewaan alat yang anda masukkan tidak ada" + color.end)
        else:
            print(color.merah + "Saat ini hanya data diatas yang tersedia" + color.end)
    else:
        print(color.merah + "Maaf data yang anda pilih tidak tersedia" + color.end)
    time.sleep(3)
    os.system("cls")
    print(color.kuning + "||===========================================||")
    print("||          Kembali ke menu Admin            ||")
    print("||===========================================||" + color.end)  

#def user
def beli_stock():
    def beli_bahanbangunan():
        print(color.ungu + "Ini adalah beberapa bahan bangunan yang dijual" + color.end)
        table = PrettyTable(["Nama", "Jumlah", "Harga", "Jenis"])
        for x in data_bahanbangunan:
            table.add_row(x)
        table.align = "l"
        print(table)
        cek_barang3 = len(data_bahanbangunan) - 1
        B_barang = input(color.hijau + "Masukkkan nama bahan bangunan yang mau anda beli : " + color.end)
        while (cek_barang3 >= 0):
            if (B_barang == data_bahanbangunan[cek_barang3][0]):
                break
            else:
                cek_barang3 -= 1
        if (B_barang == data_bahanbangunan[cek_barang3][0]):
            try:
                JB_barang = int(input(color.hijau + "Masukkan jumlah bahan bangunan yang dibeli : " + color.end))
            except ValueError:
                print(color.merah + "Jumlah yang di masukkan salah" + color.end)
                time.sleep(3)
                os.system("cls")
                print(color.merah + ">Mohon masukkan kembali jumlah bahan bangunan yang ingin dibeli dengan benar<" + color.end)
                beli_bahanbangunan()
            else:
                if (JB_barang <= 0):
                    print(color.merah + "Maaf jumlah pesanan anda tidak valid" + color.merah)
                elif (JB_barang <= data_bahanbangunan[cek_barang3][1]):
                    T_harga = JB_barang * data_bahanbangunan[cek_barang3][2]
                    time.sleep(2)
                    os.system("cls")
                    print(color.kuning + "Pesanan anda sedang di proses..0%")
                    time.sleep(3)
                    print("Pesanan anda sedang di proses..50%")
                    time.sleep(2)
                    print("Pesanan anda sedang di proses..75%")
                    time.sleep(2)
                    print("Pesanan anda sedang di proses..100%!!" + color.end)
                    time.sleep(1)
                    os.system("cls")
                    if (T_harga<=0):
                        print(color.merah + "Terjadi kesalahan pada pembelian ini!!!" + color.end)
                    else:
                        print(color.kuning + "Berikut ini adalah Struk Pembayaran")
                        time.sleep(2)
                        print("||===========================================||")
                        print("||        Toko Bangunan Jaya Abadi           ||")
                        print("||            Struk Pembayaran               ||")
                        print("||Nama stock  :", B_barang)
                        print("||Jumlah stock:", JB_barang)
                        print("||Total harga : Rp.", T_harga)
                        print("||===========================================||" + color.end)
                        time.sleep(7)
                        os.system("cls")
                        print(color.kuning + "||===========================================||")
                        print("||     Silahkan ke kasir untuk pembayaran    ||")
                        print("||        Kembali ke menu Pelanggan          ||")
                        print("||===========================================||" + color.end)
                else:
                    print(color.merah + "Maaf jumlah bahan bangunan yang tersedia tidak cukup" + color.end)
        else:
            print(color.merah + "Maaf nama bahan bangunan yang anda masukkan tidak ada" + color.end)

    def beli_alatbangunan():
        print(color.biru + "||===========================================||")
        print("||       Alat Bangunan yang Tersedia         ||")
        print("||===========================================||")
        print("||    1. Alat Manual                         ||")
        print("||    2. Alat Elektronik                     ||")
        print("||===========================================||" + color.end)
        jual_alatbangunan = input(color.hijau + "masukkan pilihan anda : " + color.end)
        if (jual_alatbangunan == "1" or jual_alatbangunan == "Alat Manual" or jual_alatbangunan == "alat manual"):
            print(color.ungu + "Ini adalah beberapa alat bangunan yang dijual" + color.end)
            table = PrettyTable(["Nama", "Jumlah", "Harga", "Jenis"])
            for x in data_alatmanual:
                table.add_row(x)
            table.align = "l"
            print(table)
            cek_barang3 = len(data_alatmanual) - 1
            B_barang = input(color.hijau + "Masukkkan nama alat bangunan yang mau anda beli: " + color.end)
            while (cek_barang3 >= 0):
                if (B_barang == data_alatmanual[cek_barang3][0]):
                    break
                else:
                    cek_barang3 -= 1
            if (B_barang == data_alatmanual[cek_barang3][0]):
                try:
                    JB_barang = int(input(color.hijau + "Masukkan jumlah alat bangunan yang dibeli: " + color.end))
                except ValueError:
                    print(color.merah + "Jumlah yang di masukkan salah" + color.end)
                    time.sleep(3)
                    os.system("cls")
                    print(color.merah + ">Mohon masukkan kembali jumlah alat bangunan yang ingin dibeli dengan benar<" + color.end)
                    beli_alatbangunan()
                else:
                    if (JB_barang <= 0):
                        print(color.merah + "Maaf jumlah pesanan anda tidak valid" + color.end)
                    elif (JB_barang <= data_alatmanual[cek_barang3][1]):
                        T_harga = JB_barang * data_alatmanual[cek_barang3][2]
                        time.sleep(2)
                        os.system("cls")
                        print(color.kuning + "Pesanan anda sedang di proses..0%")
                        time.sleep(3)
                        print("Pesanan anda sedang di proses..50%")
                        time.sleep(2)
                        print("Pesanan anda sedang di proses..75%")
                        time.sleep(2)
                        print("Pesanan anda sedang di proses..100%!!" + color.end)
                        time.sleep(1)
                        os.system("cls")
                        if (T_harga<=0):
                            print(color.merah + "Terjadi kesalahan pada pembelian ini!!!" + color.end)
                        else:
                            print(color.kuning + "Berikut ini adalah Struk Pembayaran")
                            time.sleep(2)
                            print("||===========================================||")
                            print("||        Toko Bangunan Jaya Abadi           ||")
                            print("||            Struk Pembayaran               ||")
                            print("||Nama stock  :", B_barang)
                            print("||Jumlah stock:", JB_barang)
                            print("||Total harga : Rp.", T_harga)
                            print("||===========================================||" + color.end)
                            time.sleep(7)
                            os.system("cls")
                            print(color.kuning + "||===========================================||")
                            print("||     Silahkan ke kasir untuk pembayaran    ||")
                            print("||        Kembali ke menu Pelanggan          ||")
                            print("||===========================================||" + color.end)
                    else:
                        print(color.merah + "Maaf jumlah alat manual yang tersedia tidak cukup" + color.end)
            else:
                print(color.merah + "Maaf nama alat manual yang anda masukkan tidak ada" + color.end)
        elif (jual_alatbangunan == "2" or jual_alatbangunan == "Alat Elektronik" or jual_alatbangunan == "alat elektronik"):
            print(color.ungu + "ini adalah beberapa alat bangunan yang dijual" + color.end)
            table = PrettyTable(["Nama", "Jumlah", "Harga", "Jenis"])
            for x in data_alatelektronik:
                table.add_row(x)
            table.align = "l"
            print(table)
            cek_barang3 = len(data_alatelektronik) - 1
            B_barang = input(color.hijau + "Masukkkan nama alat bangunan yang mau anda beli : " + color.end)
            while (cek_barang3 >= 0):
                if (B_barang == data_alatelektronik[cek_barang3][0]):
                    break
                else:
                    cek_barang3 -= 1
            if (B_barang == data_alatelektronik[cek_barang3][0]):
                try:
                    JB_barang = int(input(color.hijau + "Masukkan jumlah alat bangunan yang dibeli: " + color.end))
                except ValueError:
                    print(color.merah + "Jumlah yang di masukkan salah" + color.end)
                    time.sleep(3)
                    os.system("cls")
                    print(color.merah + ">Mohon masukkan kembali jumlah alat bangunan yang ingin dibeli dengan benar<" + color.end)
                    beli_alatbangunan()
                else:
                    if (JB_barang <= 0):
                        print(color.merah + "Maaf jumlah pesanan anda tidak valid" + color.end)
                    elif (JB_barang <= data_alatelektronik[cek_barang3][1]):
                        T_harga = JB_barang * data_alatelektronik[cek_barang3][2]
                        time.sleep(2)
                        os.system("cls")
                        print(color.kuning + "Pesanan anda sedang di proses..0%")
                        time.sleep(3)
                        print("Pesanan anda sedang di proses..50%")
                        time.sleep(2)
                        print("Pesanan anda sedang di proses..75%")
                        time.sleep(2)
                        print("Pesanan anda sedang di proses..100%!!" + color.end)
                        time.sleep(1)
                        os.system("cls")
                        if (T_harga<=0):
                            print(color.merah + "Terjadi kesalahan pada pembelian ini!!!" + color.end)
                        else:
                            print(color.kuning + "Berikut ini adalah Struk Pembayaran")
                            time.sleep(2)
                            print("||===========================================||")
                            print("||        Toko Bangunan Jaya Abadi           ||")
                            print("||            Struk Pembayaran               ||")
                            print("||Nama stock  :", B_barang)
                            print("||Jumlah stock:", JB_barang)
                            print("||Total harga : Rp.", T_harga)
                            print("||===========================================||" + color.end)
                            time.sleep(7)
                            os.system("cls")
                            print(color.kuning + "||===========================================||")
                            print("||     Silahkan ke kasir untuk pembayaran    ||")
                            print("||        Kembali ke menu Pelanggan          ||")
                            print("||===========================================||" + color.end)
                    else:
                        print(color.merah + "Maaf jumlah alat elektronik yang tersedia tidak cukup" + color.end)
            else:
                print(color.merah + "Maaf nama alat elektronik yang anda masukkan tidak ada" + color.end)
        else:
            print(color.merah + "Saat ini hanya data diatas yang tersedia" + color.end)
    def pilih_penyewaan():
        print(color.biru + "||===========================================||")
        print("||         Penyewaan yang Tersedia           ||")
        print("||===========================================||")
        print("||    1. Penyewaan Jasa                      ||")
        print("||    2. Penyewaan Alat                      ||")
        print("||===========================================||" + color.end)
        sewa_penyewaan = input(color.hijau + "masukkan pilihan anda :" + color.end)
        if (sewa_penyewaan == "1" or sewa_penyewaan == "Penyewaan Jasa" or sewa_penyewaan == "penyewaan jasa"):
            print(color.ungu + "Ini adalah beberapa penyewaan jasa yang tersedia" + color.end)
            table = PrettyTable(["Nama", "Jumlah", "Harga", "Jenis"])
            for x in data_penyewaanjasa:
                table.add_row(x)
            table.align = "l"
            print(table)
            cek_barang3 = len(data_penyewaanjasa) - 1
            B_barang = input(color.hijau + "Masukkkan nama penyewaan yang mau anda pilih : " + color.end)
            while (cek_barang3 >= 0):
                if (B_barang == data_penyewaanjasa[cek_barang3][0]):
                    break
                else:
                    cek_barang3 -= 1
            if (B_barang == data_penyewaanjasa[cek_barang3][0]):
                try:
                    JB_barang = int(input(color.hijau + "Masukkan jumlah penyewaan jasa yang ingin disewa : " + color.end))
                except ValueError:
                    print(color.merah + "Jumlah yang di masukkan salah" + color.end)
                    time.sleep(3)
                    os.system("cls")
                    print(color.merah + ">Mohon masukkan kembali jumlah penyewaan yang ingin disewa dengan benar<" + color.end)
                    pilih_penyewaan()
                else:
                    if (JB_barang <= 0):
                        print(color.merah + "Maaf jumlah pesanan anda tidak valid" + color.end)
                    elif (JB_barang <= data_penyewaanjasa[cek_barang3][1]):
                        T_harga = JB_barang * data_penyewaanjasa[cek_barang3][2]
                        time.sleep(2)
                        os.system("cls")
                        print(color.kuning + "Pesanan anda sedang di proses..0%")
                        time.sleep(3)
                        print("Pesanan anda sedang di proses..50%")
                        time.sleep(2)
                        print("Pesanan anda sedang di proses..75%")
                        time.sleep(2)
                        print("Pesanan anda sedang di proses..100%!!" + color.end)
                        time.sleep(1)
                        os.system("cls")
                        if (T_harga<=0):
                            print(color.merah + "Terjadi kesalahan pada pembelian ini!!!" + color.end)
                        else:
                            print(color.kuning + "Berikut ini adalah Struk Pembayaran")
                            time.sleep(2)
                            print("||===========================================||")
                            print("||        Toko Bangunan Jaya Abadi           ||")
                            print("||            Struk Pembayaran               ||")
                            print("||Nama stock  :", B_barang)
                            print("||Jumlah stock:", JB_barang)
                            print("||Total harga : Rp.", T_harga)
                            print("||===========================================||" + color.end)
                            time.sleep(7)
                            os.system("cls")
                            print(color.kuning + "||===========================================||")
                            print("||     Silahkan ke kasir untuk pembayaran    ||")
                            print("||        Kembali ke menu Pelanggan          ||")
                            print("||===========================================||" + color.end)
                    else:
                        print(color.merah + "Maaf jumlah penyewaan jasa yang tersedia tidak cukup" + color.end)
            else:
                print(color.merah + "Maaf nama penyewaan jasa yang anda masukkan tidak ada" + color.end)
        elif (sewa_penyewaan == "2" or sewa_penyewaan == "Penyewaan Alat" or sewa_penyewaan == "penyewaan alat"):
            print(color.ungu + "ini adalah beberapa penyewaan alat yang tersedia" + color.end)
            table = PrettyTable(["Nama", "Jumlah", "Harga", "Jenis"])
            for x in data_penyewaanalat:
                table.add_row(x)
            table.align = "l"
            print(table)
            cek_barang3 = len(data_penyewaanalat) - 1
            B_barang = input(color.hijau + "Masukkkan nama penyewaaan yang mau anda pilih : " + color.end)
            while (cek_barang3 >= 0):
                if (B_barang == data_penyewaanalat[cek_barang3][0]):
                    break
                else:
                    cek_barang3 -= 1
            if (B_barang == data_penyewaanalat[cek_barang3][0]):
                try:
                    JB_barang = int(input(color.hijau + "Masukkan jumlah penyewaan alat yang ingin disewa : " + color.end))
                except ValueError:
                    print(color.merah + "Jumlah yang di masukkan salah" + color.end)
                    time.sleep(3)
                    os.system("cls")
                    print(color.merah +">Mohon masukkan kembali jumlah penyewaan yang ingin disewa dengan benar<" + color.end)
                    pilih_penyewaan()
                else:
                    if (JB_barang <= 0):
                        print(color.merah + "Maaf jumlah pesanan anda tidak valid" + color.end)
                    elif (JB_barang <= data_penyewaanalat[cek_barang3][1]):
                        T_harga = JB_barang * data_penyewaanalat[cek_barang3][2]
                        time.sleep(2)
                        os.system("cls")
                        print(color.kuning + "Pesanan anda sedang di proses..0%")
                        time.sleep(3)
                        print("Pesanan anda sedang di proses..50%")
                        time.sleep(2)
                        print("Pesanan anda sedang di proses..75%")
                        time.sleep(2)
                        print("Pesanan anda sedang di proses..100%!!" + color.end)
                        time.sleep(1)
                        os.system("cls")
                        if (T_harga<=0):
                            print(color.merah + "Terjadi kesalahan pada pembelian ini!!!" + color.end)
                        else:
                            print(color.kuning + "Berikut ini adalah Struk Pembayaran")
                            time.sleep(2)
                            print("||===========================================||")
                            print("||        Toko Bangunan Jaya Abadi           ||")
                            print("||            Struk Pembayaran               ||")
                            print("||Nama stock  :", B_barang)
                            print("||Jumlah stock:", JB_barang)
                            print("||Total harga : Rp.", T_harga)
                            print("||===========================================||" + color.end)
                            time.sleep(7)
                            os.system("cls")
                            print(color.kuning + "||===========================================||")
                            print("||     Silahkan ke kasir untuk pembayaran    ||")
                            print("||        Kembali ke menu Pelanggan          ||")
                            print("||===========================================||" + color.end)
                    else:
                        print(color.merah + "Maaf jumlah penyewaan alat yang tersedia tidak cukup" + color.end)
            else:
                print(color.merah + "Maaf nama penyewaan alat yang anda masukkan tidak ada" + color.end)
        else:
            print(color.merah + "Saat ini hanya data diatas yang tersedia" + color.end)
    print(color.biru + "||=====================================================||")
    print("||  Disini tersedia bahan,alat bangunan dan lain-lain  ||")
    print("||=====================================================||")
    print("||    1. Bahan Bangunan                                ||")
    print("||    2. Alat Bangunan                                 ||")
    print("||    3. Penyewaan                                     ||")
    print("||=====================================================||" + color.end)
    yg_dijual = input(color.hijau + "anda mau pilih apa? : " + color.end)
    if (yg_dijual == "1" or yg_dijual == "Bahan Bangunan" or yg_dijual == "bahan bangunan"):
        beli_bahanbangunan()
    elif (yg_dijual == "2" or yg_dijual == "alat bangunan" or yg_dijual == "Alat Bangunan"):
        beli_alatbangunan()
    elif (yg_dijual == "3" or yg_dijual == "Penyewaan" or yg_dijual == "penyewaan"):
        pilih_penyewaan()
    else:
        print(color.merah + "Saat ini hanya itu saja yang kami jual" + color.end)

#Menu Admin
def menu_admin():
    while True:
        print(color.biru + "||===========================================||")
        print("||               MENU ADMIN                  ||")
        print("||===========================================||")       
        print("||    1. Lihat stock                         ||")   
        print("||    2. Tambahkan stock                     ||")
        print("||    3. Update stock                        ||")
        print("||    4. Hapus stock                         ||")
        print("||    5. Logout                              ||")
        print("||===========================================||" + color.end)
        pilihan1 = input(color.hijau + "Masukkan pilihan : " + color.end)
        if (pilihan1 == "1" or pilihan1 == "lihat stock" or pilihan1 == "Lihat Stock"):
            lihat_stock()
        elif (pilihan1 == "2" or pilihan1 == "tambahkan stock" or pilihan1 == "Tambahkan stock"):
            tambah_stock()
        elif (pilihan1 == "3" or pilihan1 == "Update Stock" or pilihan1 == "update stock"):
            update_stock()
        elif (pilihan1 == "4" or pilihan1 == "Hapus stock" or pilihan1 == "hapus stock"):
            hapus_stock()
        elif (pilihan1 == "5" or pilihan1 == "logout" or pilihan1 == "Logout"):
            print(color.kuning + "||===========================================||")
            print("||          Telah berhasil logout!!          ||")
            print("||===========================================||" + color.end)
            break        
        else:
            print(color.merah + "Maaf, menu yang anda pilih tidak tersedia" + color.end)
        time.sleep(3)
        os.system("cls")

#Menu Pelanggan
def menu_pelanggan():
    while True:
        print(color.biru + "||===========================================||")
        print("||               MENU PELANGGAN              ||")
        print("||===========================================||")       
        print("||    1. Beli Stock                          ||")
        print("||    2. Logout                              ||")
        print("||===========================================||" + color.end)
        pilihan2 = input(color.hijau + "Masukkan pilihan beli atau logout : " + color.end)
        if (pilihan2 == "1" or pilihan2 == "beli stock" or pilihan2 == "Beli Stock"):
            beli_stock()
        elif (pilihan2 == "2" or pilihan2 == "logout" or pilihan2 == "Logout"):
            print(color.kuning + "||===========================================||")
            print("||          Telah berhasil logout!!          ||")
            print("||===========================================||" + color.end)
            break
        else:
            print(color.merah + "Maaf menu yang anda pilih tidak tersedia" + color.end)
        time.sleep(3)
        os.system("cls")
        

#Menu awal
while True:
    print(color.ungu + "||===========================================||")
    print("||               Menu Awal                   ||")
    print("||===========================================||")
    print("||  1.Login                                  ||")
    print("||  2.Keluar                                 ||")
    print("||===========================================||" + color.end)
    menu_awal = input(color.hijau + "Pilih menu : " + color.end)
    if (menu_awal == "1" or menu_awal == "Login" or menu_awal == "login"):
        cek = len(username) - 1
        print(color.ungu + "||===========================================||")
        print("||     Silahkan masukan username             ||" + color.end)
        cek_username = input(color.hijau + "Username : " + color.end)
        print(color.ungu + "||     Silahkan masukan password             ||" + color.end)
        cek_password = input(color.hijau + "Password : " + color.end)
        print(color.ungu + "||===========================================||" + color.end)
        while (cek >= 0):
            if (cek_username == username[cek]):
                if (cek_password == password[cek]):
                    break
                else:
                    cek -= 1
            else:
                cek -= 1
                
        if (cek == -1):
            print(color.merah + "Maaf username atau password yang anda masukkan salah")
            print("Silahkan masukan username atau password dengan benar!" + color.end)

        elif (sebagai[cek] == "Admin"):
            print(color.kuning + "||===========================================||")
            print("||     Awali hari kerjamu dengan senyuman    ||")
            print("||            Selamat bekerja!!              ||")
            print("||===========================================||" + color.end)
            time.sleep(3)
            os.system("cls")
            menu_admin()
            time.sleep(3)
            os.system("cls")
            print(color.kuning + "||===========================================||")
            print("||           Kembali ke menu awal            ||")
            print("||===========================================||" + color.end)
        elif (sebagai[cek] == "User"):
            print(color.kuning + "||===========================================||")
            print("||Selamat Datang di Toko Bangunan Jaya Abadi ||")
            print("||          Selamat berbelanja!!             ||")
            print("||===========================================||" + color.end)
            time.sleep(3)
            os.system("cls")
            menu_pelanggan()
            time.sleep(3)
            os.system("cls")
            print(color.kuning + "||===========================================||")
            print("||       Terima kasih telah berbelanja       ||")
            print("||          Selamat datang kembali!          ||")
            print("||           Kembali ke menu awal            ||")
            print("||===========================================||" + color.end)
    elif (menu_awal == "2" or menu_awal == "keluar" or menu_awal == "Keluar"):
        print("Anda telah keluar")
        break
    else:
        print(color.kuning + ">Menu yang anda pilih salah!!!" + color.end)
    time.sleep(3)
    os.system("cls")