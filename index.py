# Muhammad Zaki Fahmi
# LOOPING OPEN
def garis():
    print("---------------------------------------")

print("APLIKASI PENGURUT ANGKA")

def asc(num):
    a = len(num)
    for b in range(a):
        for c in range(a-b-1):
            if num[c] > num[c+1]:
                num[c], num[c+1] = num[c+1], num[c]
    return num

def dsc(num):
    a = len(num)
    for b in range(a):
        for c in range(a-b-1):
            if num[c] < num[c+1]:
                num[c], num[c+1] = num[c+1], num[c]
    return num

def rata(angka):
    return sum(angka)/len(angka)
# LOOPING ENDED

garis()
print("Masukkan tiga buah nilai")
angka1 = int(input("Nilai A: "))
angka2 = int(input("Nilai B: "))
angka3 = int(input("Nilai C: "))
satuan = [angka1,angka2,angka3]
garis()

print("Hasil Akhir----")
print(f"Hasil Ascending:", asc(satuan))
print(f"Hasil Descending:", dsc(satuan))
print(f"Angka Terbesar:", max(satuan))
print(f"Angka Terkecil:", min(satuan))
print(f"Rata-Rata:", round(rata(satuan),2))