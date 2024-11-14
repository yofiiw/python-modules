import math

print('''---MENU KALKULATOR---
1. Menghitung Nilai Faktorial
2. Menghitung Akar Kuadrat
3. Menghitung Bilangan Berpangkat
4. Menghitung Nilai Sin
5. Menghitung Nilai Cos
6. Menghitung Nilai Tan
7. Keluar''')

while True:
  select = int(input("Silahkan pilih menu yang ingin dicari : "))

  if select == 1:
    print("Menghitung Nilai Faktorial")
    num = int(input("Masukkan angka : "))
    if num < 0:
      print("Faktorial hanya bisa dihitung untuk angka non-negatif!")
    else:
      print(f"Nilai {num}! adalah {math.factorial(num)}")

  elif select == 2:
    print("Menghitung Akar Kuadrat")
    num = int(input("Masukkan angka : "))
    if num < 0:
      print("Akar kuadrat hanya bisa dihitung untuk angka non-negatif!")
    else:
      print(f"Akar Kuadrat dari {num} adalah {math.sqrt(num)}")

  elif select == 3:
    print("Menghitung Nilai Sin")
    num = int(input("Masukkan angka : "))
    pow = int(input("Masukkan pangkatnya : "))
    print(f"{num} pangkat {pow} adalah {math.pow(num, pow)}")

  elif select == 4:
    print("Menghitung Nilai Cos")
    num = float(input("Masukkan angka : "))
    radians = math.radians(num)
    print(f"Sin {num} adalah {math.sin(radians)}")

  elif select == 5:
    print("Menghitung Nilai Tan")
    num = float(input("Masukkan angka : "))
    radians = math.radians(num)
    print(f"Cos {num} adalah {math.cos(radians)}")

  elif select == 6:
    print("")
    num = float(input("Masukkan angka : "))
    radians = math.radians(num)
    print(f"Tan {num} adalah {math.tan(radians)}")

  elif select == 7:
    break
  
  else:
    print("Tolong pilih kembali!")
