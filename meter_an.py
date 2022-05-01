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

    # fungsi untuk menampilkan hasil
    def user_output(self):
        if b == False : pass
        else :
            cnv = Converter(self.pnjng_inp, self.satuan_inp, self.satuan_out)  # memasukan data user_input ke class Converter kemudian didefinisikan ulang dengan nama cnv
            print("\n\tprocessing...")
            cnv.olah_data() # data inputan user di olah disini
            sleep(1.2)
            # menampilkan hasil olahan tadi sesuai kondisi
            if cnv.angka_out == 'invalid':
                print(f"\ninvalid, {cnv.angka_inp} {cnv.satuan_inp} tidak bisa diubah ke {cnv.satuan_out}\n")
            else :
                print(f"\n{cnv.angka_inp} {cnv.satuan_inp} = {cnv.angka_out} {cnv.satuan_out}\n")

# run kode dalam looping
while True :
    converting = Converting()
    converting.user_input()
    converting.user_output()
    lagi = input("\nKetik 0 untuk mencoba lagi : ")
    if lagi != '0' : break
