from method import Converter
from time import sleep

# sekali kali pake class biar greget 😅
class Converting:

    def __init__(self):
        self.pnjng_inp = 0
        self.pnjng_out = 0 
        self.satuan_inp = ""
        self.satuan_out = ""

    # ambil data user seperlunya
    def user_input(self):
        inputan = input("Masukan panjang beserta satuannya : ") # misal : 22 cm
        ls = inputan.split()

        a = "0"
        while a == "0":
            try :
                self.pnjng_inp = int(ls[0])
                a = "1"
            except :
                a = input("\nError, tidak memasukan angka dengan benar.\nKetik 0 untuk coba lagi : ")
                if a != "0" : a = "1"

        satuan_inp = ls[1].lower()

        satuan_out = input(f"{self.pnjng_inp} {self.satuan_inp} akan diubah ke satuan : ") # misal : km atau kilometer


    # setelah di olah, tampilkan hasil nya
    def user_output(self):
        cnv = Converter(self.pnjng_inp, self.satuan_inp, self.satuan_out)
        print("\n\tprocessing...")
        sleep(1.5)
        print(f"{cnv.angka_inp} {cnv.satuan_inp} = {cnv.angka_out} {cnv.satuan_out}")


converting = Converting()
converting.user_input()
converting.user_output()




