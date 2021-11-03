from prettytable import PrettyTable
import json
import os

tabel = {
    "akun": PrettyTable(),
    "jualan": PrettyTable()
}

data = {
    "akun": [
        {"username": "admin", "password": 'admin'},
        {"username": "bayu", "password": 'geh'}
    ],
    "jualan": [
        {"kode": "123", "barang": "actionfigure1", "harga":  100000, "stok": 5},
        {"kode": "456", "barang": "actionfigure2", "harga": 100000, "stok": 10},
        {"kode": "789", "barang": "actionfigure3", "harga": 100000, "stok": 15}
    ]
}


def select(select_data):
    return data.get(select_data)


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def fetch_data():
    if os.path.isfile('data.json'):
        with open('data.json') as json_file:
            data = json.load(json_file)


def confirm(state):
    return input(f'\ndata telah {state}, tekan Enter untuk kembali ke menu...')


def pilih_tabel():
    pilih_tabel = input('tabel yang mana ?[akun,jualan] : ')

    if pilih_tabel == 'akun' or pilih_tabel == "jualan":
        print(tabel.get(pilih_tabel))
        return pilih_tabel
    else:
        print("\ntabel tidak ditemukan")
        return False


def input_data():
    tabel = pilih_tabel()
    if tabel == 'akun':
        us = input("masukan username : ")
        pw = input("masukan password : ")

        for akun in select('akun'):
            if us == akun.get('username') and pw == akun.get('password'):
                print(f"\nakun {us} sudah ada di database")
                return input_data()

        select('akun').append({"username": us, "password": pw})

    elif tabel == 'jualan':
        kode = input("masukan kode barang: ")
        brng = input('masukan nama barang : ')
        hrg = int(input('masukan harga : '))
        jmlh = int(input('masukan jumlah barang : '))

        select('jualan').append(
            {"kode": kode, "barang": brng, "harga": hrg, "stok": jmlh}
        )
    else:
        return input_data()

    confirm('ditambakan')


def tampil_data():
    pilih_tabel()
    input('Tekan enter untuk kembali ke menu...')


def ubah_data():
    print(tabel.get('jualan'))
    target = input('pilih barang (kode barang)?:')

    for jualan in select('jualan'):
        if target == jualan.get('kode'):
            ubah = input('data apa yang ingin diubah?[nama, harga, stok] : ')
            if ubah == 'nama':
                jualan[ubah] = input('masukan perubahan :')
            elif ubah == 'harga' or ubah == 'stok':
                jualan[ubah] = int(input('masukan perubahan :'))
            confirm('diubah')


def hapus_data():

    tabel = pilih_tabel()

    if not tabel:
        return hapus_data()

    target = int(
        input('pilih data mana yang akan dihapus ?[misalnya list ke-1] : '))
    try:
        if target > 0:
            select(tabel).pop(target-1)
            confirm('dihapus')

    except IndexError:
        print(f'\ntidak ada data ke-{target} pada tabel')
        return hapus_data()


def updatetabel():
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)

    tabel_akun = tabel.get('akun')
    tabel_akun.field_names = ["No.", "username", "password"]
    tabel_akun.clear_rows()

    tabel_jualan = tabel.get("jualan")
    tabel_jualan.field_names = ['No.', 'kode', 'barang', 'harga', 'stok']
    tabel_jualan.clear_rows()

    data_jualan = select('jualan')
    for i, jualan in enumerate(data_jualan):
        tabel_jualan.add_row(
            [i + 1, jualan.get('kode'), jualan.get('barang'),
             f"Rp {jualan.get('harga')}", jualan.get("stok")]
        )

    data_akun = select('akun')
    for i, akun in enumerate(data_akun):
        tabel_akun.add_row(
            [i + 1, akun.get('username'),
             akun.get('password')]
        )


def menu():
    print(f"""
  ==============================
  |            MENU            |
  ==============================
    | {"1. input data"}          |
    | {"2. Tampil Data"}         |
    | {"3. Ubah Data(jualan)"}   |
    | {"4. Hapus Data"}          |
    | {"5. Exit"}                |
    ==========================""")
    return int(input("pilih Menu : "))


def main():
    if login():
        while True:
            clearConsole()
            updatetabel()
            pilih = menu()

            if pilih == 1:
                input_data()

            if pilih == 2:
                tampil_data()

            elif pilih == 3:
                ubah_data()

            elif pilih == 4:
                hapus_data()

            elif pilih == 5:
                return print('keluar dari program')


def login():
    username = input("masukan username :")
    password = input("masukan password :")
    for user in select('akun'):
        if username == user.get('username') and password == user.get('password'):
            return True

    print('username/password yang anda masukan salah\n')
    return login()


try:
    fetch_data()
    main()
except KeyboardInterrupt:
    print('\nkeluar dari program')
