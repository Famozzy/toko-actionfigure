from prettytable import PrettyTable
import os

tabel = {
    "akun": PrettyTable(),
    "jualan": PrettyTable()
}

akun = [
    {"ID": 1, "username": "admin", "password": 'admin'},
    {"ID": 2, "username": "bayu", "password": 'geh'}
]

jualan = [
    {"ID": 1, "barang": "action figure1", "harga":  100000, "stock": 5},
    {"ID": 2, "barang": "actionfigure2", "harga": 100000, "stock": 5},
    {"ID": 3, "barang": "actionfigure3", "harga": 100000, "stock": 5}
]


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def inputdata_akun(id, us, pw):
    akun.append({
        "ID": id,
        "username": us,
        "password": pw
    })


def inputdata_jualan(id, brng, hrg, jmlh):
    jualan.append({
        "ID": id,
        "barang": brng,
        "harga": hrg,
        "stock": jmlh
    })


def ubahdata(target):  # ubah data
    for i in range(len(jualan)):
        if target == jualan[i].get('barang'):
            ubah = input('data apa yang ingin diubah?[nama, harga, stock] : ')
            if ubah == 'nama':
                jualan[i][ubah] = input('masukan perubahan :')
            elif ubah == 'harga' or ubah == 'stock':
                jualan[i][ubah] = int(input('masukan perubahan :'))


def hapusdata(tabel, cekdata):
    if tabel == 'akun':
        for i in range(len(akun)):
            if cekdata == akun[i].get('ID'):
                akun.pop(i)

    elif tabel == 'jualan':
        for i in range(len(jualan)):
            if cekdata == jualan[i].get('ID'):
                jualan.pop(i)


def updatetabel():
    tabel_akun = tabel.get('akun')
    tabel_akun.field_names = ["ID", "username", "password"]
    tabel_akun.clear_rows()

    tabel_jualan = tabel.get("jualan")
    tabel_jualan.field_names = ['ID', 'barang', 'harga', 'stock']
    tabel_jualan.clear_rows()

    for i in range(len(jualan)):
        tabel_jualan.add_row(
            [jualan[i].get('ID'), jualan[i].get('barang'),
             jualan[i].get("harga"), jualan[i].get("stock")]
        )

    for i in range(len(akun)):
        tabel_akun.add_row(
            [akun[i].get('ID'), akun[i].get('username'),
             akun[i].get('password')]
        )


def menu():
    print(f"""
  ==============================
  |            MENU            |
  ==============================
    | {"1. input data"}          |
    | {"2. Tampil Data"}         |
    | {"3. Ubah Data(jualan)"}   |
    | {"4. Delete Data"}         |
    | {"5. Exit"}                |
    ==========================""")


def main():
    clearConsole()
    menu()
    updatetabel()
    while True:
        pilih = input("pilih Menu : ")

        if pilih == '1':
            pilih_tabel = input('tabel yang mana ?[akun,jualan] : ')

            if pilih_tabel == 'akun':
                id = int(input("masukan id : "))
                us = input("masukan username : ")
                pw = input("masukan password : ")
                inputdata_akun(id, us, pw)

            elif pilih_tabel == 'jualan':
                id = int(input("masukan id : "))
                brng = input('masukan nama barang : ')
                hrg = int(input('masukan harga : '))
                jmlh = int(input('masukan jumlah barang : '))
                inputdata_jualan(id, brng, hrg, jmlh)
            main()

        if pilih == '2':
            pilih_tabel = input('tabel yang mana ?[akun,jualan] : ')
            print(tabel.get(pilih_tabel))

        elif pilih == '3':
            print(tabel.get('jualan'))
            target = input(
                'pilih barang (nama barang)?:')
            ubahdata(target)
            main()

        elif pilih == '4':
            pilih_tabel = input('tabel yang mana ?[akun,jualan] : ')
            print(tabel.get(pilih_tabel))

            target_id = int(
                input('pilih data mana yang akan dihapus ?[ID] : '))

            hapusdata(pilih_tabel, target_id)
            main()

        elif pilih == '5':
            print('keluar dari program')
            return


def login():
    username = input("masukan username :")
    password = input("masukan password :")

    in_akun = int()
    for index in range(len(akun)):
        if username == akun[index].get('username'):
            in_akun = index

    try:
        if username == akun[in_akun].get('username') and password == akun[in_akun].get('password'):
            main()
        else:
            print("login gagal password anda salah")
    except ValueError:
        print("maaf username tidak tersedia")


login()
