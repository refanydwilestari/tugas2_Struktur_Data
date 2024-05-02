#Struktur Data
#Kelompok 3
#Nama : Ronald Budi Abdul Wahid   #NIM :23091397142
#Nama : Muhammad Ibnu Nadhif      #NIM :23091397161
#Nama : Refany Dwi Lestari        #NIM :23091397170

class Map():
    def __init__(self):
        self.daftarKota = {}
        self.jumlahKota = 0
    
    def tampilkanPeta(self):
        for kota in self.daftarKota:
            print(f"{kota} -> {self.daftarKota[kota]}")
        print(f"Jumlah Kota: {self.jumlahKota}")
    
    def tambahkanKota(self, kota):
        if kota not in self.daftarKota:
            self.daftarKota[kota] = {}
            self.jumlahKota += 1
    
    def tambahkanJalan(self, kota1, kota2, jarak):
        if kota1 and kota2 in self.daftarKota:
            self.daftarKota[kota1][kota2] = jarak
            self.daftarKota[kota2][kota1] = jarak
    
    def hapusKota(self, kotaDihapus):
        if kotaDihapus in self.daftarKota:
            for kota in self.daftarKota:
                if kotaDihapus in self.daftarKota[kota]:
                    del self.daftarKota[kota][kotaDihapus]
            del self.daftarKota[kotaDihapus]
            self.jumlahKota -= 1
    
    def hapusJalan(self, kota1, kota2):
        if kota1 and kota2 in self.daftarKota:
            del self.daftarKota[kota1][kota2]
            del self.daftarKota[kota2][kota1]
          
petaJawatengah.tambahkanJalan("Semarang","Salatiga", 69)
petaJawatengah.tambahkanJalan("Semarang","Pekalongan", 134)
petaJawatengah.tambahkanJalan("Semarang","Magelang", 113)
petaJawatengah.tambahkanJalan("Semarang","Tegal", 229)
petaJawatengah.tambahkanJalan("Semarang","Surakarta", 155)
petaJawatengah.tambahkanJalan("Semarang","Kudus", 106)
petaJawatengah.tambahkanJalan("Semarang","Klaten", 161)
petaJawatengah.tambahkanJalan("Semarang","Jepara", 136)
petaJawatengah.tambahkanJalan("Semarang","Purwodadi", 109)
petaJawatengah.tambahkanJalan("Semarang","Demak", 62)
petaJawatengah.tambahkanJalan("Semarang","Purwokerto", 279)
petaJawatengah.tambahkanJalan("Semarang","Boyolali", 119)
petaJawatengah.tambahkanJalan("Semarang","Pati", 142)
petaJawatengah.tambahkanJalan("Semarang","Pemalang", 208)
petaJawatengah.tambahkanJalan("Semarang","Rembang", 215)
petaJawatengah.tambahkanJalan("Semarang","Purworejo", 175)
petaJawatengah.tambahkanJalan("Semarang","Wonogiri", 205)
petaJawatengah.tampilkanPeta()
print('------------------------------')
petaJawatengah.hapusKota("Salatiga")
petaJawatengah.hapusJalan("Semarang","Salatiga")
petaJawatengah.tampilkanPeta()
