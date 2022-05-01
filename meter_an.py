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
        a = "0"
        global b
        b = True
        while a == "0":
            try :
                inputan = input("\nMasukan panjang beserta satuannya : ") # misal : 22 cm
                ls = inputan.split()

                self.pnjng_inp = int(ls[0])
                self.satuan_inp = ls[1].lower()
                if b :
                    self.satuan_out = input(f"{self.pnjng_inp} {self.satuan_inp} akan diubah ke satuan : ") # misal : km atau kilometer
                    a = "1"
            except ValueError:
                a = input("\nError, angka dan satuannya tidak benar.\n\tContoh : 1 m (angka dulu & isi spasi)\nKetik 0 memasukan ulang  : ")
                if a != "0" :
                    a = "1"
                    b = False
                else : b = True
            except IndexError:
                a = input("\nError, angka dan satuannya tidak benar.\n\tContoh : 1 m (isi satuannya)\nKetik 0 untuk memasukan ulang   : ")
                if a != "0" :
                    a = "1"
                    b = False
                else : b = True

    # setelah di olah, tampilkan hasil nya
    def user_output(self):
        if b == False : pass
        else :
            cnv = Converter(self.pnjng_inp, self.satuan_inp, self.satuan_out)
            print("\n\tprocessing...")
            cnv.olah_data()
            sleep(1.2)
            if cnv.angka_out == 'invalid':
                print(f"\ninvalid, {cnv.angka_inp} {cnv.satuan_inp} tidak bisa diubah ke {cnv.satuan_out}\n")
            else :
                print(f"\n{cnv.angka_inp} {cnv.satuan_inp} = {cnv.angka_out} {cnv.satuan_out}\n")

while True :
    converting = Converting()
    converting.user_input()
    converting.user_output()
    lagi = input("\nKetik 0 untuk mencoba lagi : ")
    if lagi != '0' : break