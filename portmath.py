import matematika
radius = float(input("Masukkan Jari-jari Lingkaran : "))
side = float(input("Masukkan Sisi Persegi : "))


print(f"Konstanta π \t\t\t\t\t= {matematika.pi}")
print(f"Luas Lingkaran jika Jari-jarinya {radius} adalah \t= {matematika.areacircle(radius)}")
print(f"Luas Persegi jika Sisinya {side} adalah \t\t= {matematika.areasquare(side)}")
