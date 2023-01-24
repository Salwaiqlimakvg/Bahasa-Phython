#Jawaban no. 1
Aksi= 1
while (Aksi < 13):
    print ("deret: ", Aksi)
    Aksi = Aksi + 2

print ("Terima kasih")

#Jawaban no. 2

Nilai_awal = int (input ("Tuliskan nilai awal: "))
Interval = int (input ("Masukkan interval: "))
n = 16
while Nilai_awal <= n:
    print (Nilai_awal)
    Nilai_awal = Nilai_awal + Interval
print ("Selesai..")

#Jawaban no. 3 

isi= input("Tuliskan kalimat yang diinginkan: ")
n = int (input("Tuliskan jumlah pengulangan kata? "))
i= 10

while n <= i:
    n = n+ 1
    print (isi, n)
print ("Thanks")
    

#Jawaban no.4
#operasi pertama
n= 3 
i = 1

kalimat1= input ("Masukkan kalimat pertama: ")
n = int (input("Berapa kali akan diulangi: "))

kalimat2= input ("Masukkan kalimat kedua: ")
s = int (input("Berapa kali akan diulangi: "))

while i <= n:
    print (kalimat1, i)
    
    #operasikedua
    s= 3 #satu
    b = 1 #satu
    while b <= s:
        print (kalimat2, b)
        b= b + 1
        
    i= i + 1

print ("makasih")


#Jawaban no. 5
n = int (input("Berapa banyak data yang dihitung?"))
cacah = 1
total = 0

while cacah <= n:
    angka = int (input("Masukkan angka?"))
    total = total + angka
    rata_rata = total/ n
    cacah = cacah + 1

print ("Total akhir adalah: ", total)
print ("Rerata yang didapatkan adalah: ", rata_rata)
print("berakhir, alhamdulillah")


#Jawaban no.6
password = input ("Masukkan password: ")
peluang = 1

while password != "cawa" and peluang <5:
    print ("Maaf password kamu salah")

    password = input ("Coba masukkan password lagi: ")
    peluang = peluang + 1
#Pengecekkan
if (password =="cawa" and peluang <5):
    print ("Silakan eksekusi, terima kasih")
else:
    print ("Kamu tidak memiliki akses")
    
    
