class Converter:
	def __init__(self, angka_inp, satuan_inp, satuan_out):
		self.satuan_inp = satuan_inp
		self.satuan_out = satuan_out
		self.angka_inp = angka_inp
		self.angka_out = 0

	def olah_data(self):
		if self.satuan_inp == "km" or self.satuan_inp == "kilometer" : # km
			if self.satuan_out == "hm" or self.satuan_out == "hektometer" :
				self.angka_out = self.angka_inp * 10
			elif self.satuan_out == "dam" or self.satuan_out == "dekameter" :
				self.angka_out = self.angka_inp * 100
			elif self.satuan_out == "m" or self.satuan_out == "meter" :
				self.angka_out = self.angka_inp * 1000
			elif self.satuan_out == "dm" or self.satuan_out == "centimeter" :
				self.angka_out = self.angka_inp * 10000
			elif self.satuan_out == "cm" or self.satuan_out == "desimeter" :
				self.angka_out = self.angka_inp * 100000
			elif self.satuan_out == "mm" or self.satuan_out == "milimeter" :
				self.angka_out = self.angka_inp * 1000000
			else : self.angka_out = "invalid"

		elif self.satuan_inp == 'hm' or self.satuan_inp == 'hektometer' : # hm
			if self.satuan_out == 'km' or self.satuan_out == 'kilometer' :
				self.angka_out = self.angka_inp / 10
			elif self.satuan_out == 'dam' or self.satuan_out == 'dekameter' :
				self.angka_out = self.angka_inp * 10
			elif self.satuan_out == 'm' or self.satuan_out == 'meter' :
				self.angka_out = self.angka_inp * 100
			elif self.satuan_out == 'dm' or self.satuan_out == 'desimeter' :
				self.angka_out = self.angka_inp * 1000
			elif self.satuan_out == 'cm' or self.satuan_out == 'centimeter' :
				self.angka_out = self.angka_inp * 10000
			elif self.satuan_out == 'mm' or self.satuan_out == 'milimeter' :
				self.angka_out = self.angka_inp * 100000
			else : self.angka_out = "invalid" 

		elif self.satuan_inp == 'dam' or self.satuan_inp == 'dekameter' : # dam
			if self.satuan_out == 'km' or self.satuan_out == 'kilometer' :
				self.angka_out = self.angka_inp / 100
			elif self.satuan_out == 'hm' or self.satuan_out == 'hektometer' :
				self.angka_out = self.angka_inp / 10
			elif self.satuan_out == 'm' or self.satuan_out == 'meter' :
				self.angka_out = self.angka_inp * 10
			elif self.satuan_out == 'dm' or self.satuan_out == 'desimeter' :
				self.angka_out = self.angka_inp * 100
			elif self.satuan_out == 'cm' or self.satuan_out == 'centimeter' :
				self.angka_out = self.angka_inp * 1000
			elif self.satuan_out == 'mm' or self.satuan_out == 'milimeter' :
				self.angka_out = self.angka_inp * 10000
			else : self.angka_out = "invalid" 
			
		elif self.satuan_inp == 'm' or self.satuan_inp == 'meter' : # m
			if self.satuan_out == 'km' or self.satuan_out == 'kilometer' :
				self.angka_out = self.angka_inp / 1000
			elif self.satuan_out == 'hm' or self.satuan_out == 'hektometer' :
				self.angka_out = self.angka_inp / 100
			elif self.satuan_out == 'dam' or self.satuan_out == 'dekameter' :
				self.angka_out = self.angka_inp / 10
			elif self.satuan_out == 'dm' or self.satuan_out == 'desimeter' :
				self.angka_out = self.angka_inp * 10
			elif self.satuan_out == 'cm' or self.satuan_out == 'centimeter' :
				self.angka_out = self.angka_inp * 100
			elif self.satuan_out == 'mm' or self.satuan_out == 'milimeter' :
				self.angka_out = self.angka_inp * 1000
			else : self.angka_out = "invalid" 
			
		elif self.satuan_inp == 'dm' or self.satuan_inp == 'desimeter' : # dm
			if self.satuan_out == 'km' or self.satuan_out == 'kilometer' :
				self.angka_out = self.angka_inp / 10000
			elif self.satuan_out == 'hm' or self.satuan_out == 'hektometer' :
				self.angka_out = self.angka_inp / 1000
			elif self.satuan_out == 'dam' or self.satuan_out == 'dekameter' :
				self.angka_out = self.angka_inp / 100
			elif self.satuan_out == 'm' or self.satuan_out == 'meter' :
				self.angka_out = self.angka_inp / 100
			elif self.satuan_out == 'cm' or self.satuan_out == 'centimeter' :
				self.angka_out = self.angka_inp * 10
			elif self.satuan_out == 'mm' or self.satuan_out == 'milimeter' :
				self.angka_out = self.angka_inp * 100
			else : self.angka_out = "invalid" 
			
		elif self.satuan_inp == 'cm' or self.satuan_inp == 'centimeter' : # cm
			if self.satuan_out == 'km' or self.satuan_out == 'kilometer' :
				self.angka_out = self.angka_inp / 100000
			elif self.satuan_out == 'hm' or self.satuan_out == 'hektometer' :
				self.angka_out = self.angka_inp / 10000
			elif self.satuan_out == 'dam' or self.satuan_out == 'dekameter' :
				self.angka_out = self.angka_inp / 1000
			elif self.satuan_out == 'm' or self.satuan_out == 'meter' :
				self.angka_out = self.angka_inp / 100
			elif self.satuan_out == 'dm' or self.satuan_out == 'desimeter' :
				self.angka_out = self.angka_inp / 10
			elif self.satuan_out == 'mm' or self.satuan_out == 'milimeter' :
				self.angka_out = self.angka_inp * 10
			else : self.angka_out = "invalid" 
			
		elif self.satuan_inp == 'mm' or self.satuan_inp == 'milimeter' : # mm
			if self.satuan_out == 'km' or self.satuan_out == 'kilometer' :
				self.angka_out = self.angka_inp / 1000000
			elif self.satuan_out == 'hm' or self.satuan_out == 'hektometer' :
				self.angka_out = self.angka_inp / 100000
			elif self.satuan_out == 'dam' or self.satuan_out == 'dekameter' :
				self.angka_out = self.angka_inp / 10000
			elif self.satuan_out == 'm' or self.satuan_out == 'meter' :
				self.angka_out = self.angka_inp / 1000
			elif self.satuan_out == 'dm' or self.satuan_out == 'desimeter' :
				self.angka_out = self.angka_inp / 100
			elif self.satuan_out == 'cm' or self.satuan_out == 'centimeter' :
				self.angka_out = self.angka_inp / 10
			else : self.angka_out = "invalid" 







		
			

		
		

			