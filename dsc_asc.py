def garis():
    print("========================================================")

#fungsi bubble ascending (kecil ke besar)
def asc(array):
    n = len(array)
    for a in range(n):
        for b in range(n-a-1):
            if array[b] > array[b+1]:
                array[b], array[b+1] = array[b+1], array[b]
    return array

#fungsi bubble descending (besar ke kecil)
def dsc(array):
    n = len(array)
    for a in range(n):
        for b in range(n-a-1):
            if array[b] < array[b+1]:
                array[b], array[b+1] = array[b+1], array[b]
    return array

#fungsi rata-rata
def rata_rata(angka):
    return sum(angka) / len(angka)

garis()
print("*Masukkan nilai dengan spasi, contoh 3 1 4 2")
angka = list(map(int, input("Masukkan Angka: ").split()))

#menentukan nilai
garis()
print("1. Ascending")
print("2. Descending")
pilih = int(input("Pilihan 1/2: "))
garis()
if pilih == 1:
    print(f"Urutan Angka Ascending", (asc(angka)))
elif pilih == 2:
    print(f"Urutan Angka Descending", (dsc(angka)))
else:
    print(f"Input ERROR")

#cari angka terbesar
print("Angka Terbesar:",max(angka))

#cari angka terkecil
print("Angka Terkecil:",min(angka))

#jumlahkan angkanya
print("Jumlah Angka:",sum(angka))

#rata-rata
print("Rata-ratanya: ",round(rata_rata(angka),2))
garis()