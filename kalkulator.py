# fungsi operasi aritmatika
def tambah():
  print("Masukkan bilangan pertama: ")
  firstnum = int(input())
  print("Masukkan bilangan kedua: ")
  secondnum = int(input())
  hasil = firstnum + secondnum
  return hasil

def kurang():
  print("Masukkan bilangan pertama: ")
  firstnum = int(input())
  print("Masukkan bilangan kedua: ")
  secondnum = int(input())
  hasil = firstnum - secondnum
  return hasil

def kali():
  print("Masukkan bilangan pertama: ")
  firstnum = int(input())
  print("Masukkan bilangan kedua: ")
  secondnum = int(input())
  hasil = firstnum * secondnum
  return hasil

def bagi():
  print("Masukkan bilangan pertama: ")
  firstnum = int(input())
  print("Masukkan bilangan kedua: ")
  secondnum = int(input())
  if (secondnum == 0):
    return "Cannot divide by zero"
  else:
    hasil = firstnum / secondnum
    return hasil

def mod():
  print("Masukkan bilangan pertama: ")
  firstnum = int(input())
  print("Masukkan bilangan kedua: ")
  secondnum = int(input())
  if (secondnum == 0):
    return None
  else:
    hasil = firstnum % secondnum
    return hasil

while True:
  print("Kalkulator sederhana")
  print("Created by Radiance Alam Pratama")
  print("Pilih operasi hitung :(1/2/3/4)")
  print("1. Penjumlahan")
  print("2. Pengurangan")
  print("3. Perkalian")
  print("4. Pembagian")
  print("5. Sisa bagi")
  print("Jawaban Anda: ")
  jawab = int(input())
  if (jawab == 1):
    print("Hasil penjumlahannya : " ,str(tambah()))
    print("Ulangi lagi: (Y/N)")
    ulang = input()
  elif (jawab == 2):
    print("Hasil pengurangannya : " ,str(kurang()))
    print("Ulangi lagi: (Y/N)")
    ulang = input()
  elif (jawab == 3):
    print("Hasil perkaliannya : " ,str(kali()))
    print("Ulangi lagi: (Y/N)")
    ulang = input()
  elif (jawab == 4):
    print("Hasil pembagiannya : " ,str(bagi()))
    print("Ulangi lagi: (Y/N)")
    ulang = input()
  elif (jawab == 5):
    print("Sisa baginya : " ,str(mod()))
    print("Ulangi lagi: (Y/N)")
    ulang = input()
  if ulang == "N":
    print("Sampai jumpa lagi")
    break