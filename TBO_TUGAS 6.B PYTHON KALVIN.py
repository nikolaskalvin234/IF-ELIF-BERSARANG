#.TUGAS 6.B - Kuliah TBO
#.DOSEN = Arnes Y.V, M.Kom
#. IF ...ELIF.. . bersarang [BAHAN UAS]
print("NAMA = NIKOLAS KALVIN");
print("NPM = 21421002");
#
nilai = int(input("Masukkan nilai: "))
if nilai >= 90:
  print('Kategori beasiswa penuh')
elif nilai >= 80:
  print ("kategori beasiswa I")
elif nilai >= 70:
  print ("kategori beasiswa II")
else:
  print ("Tidak mendapatkan beasiswa")