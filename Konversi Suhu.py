Suhu = input('Masukkan suhu awal: ')
Tujuan = input('Masukkan satuan tujuan: ')
Awal = Suhu[len(Suhu)-1]
x = float(Suhu[:len(Suhu)-1])

if (Awal=='C'):
    if (Tujuan=='C'):
        y = x
    elif (Tujuan=='F'):
         y = 9/5 * x + 32
    elif (Tujuan=='R'):
         y = 4/5 * x
elif (Awal=='F'):
    if (Tujuan=='C'):
        y = (x-32)*5/9
    elif (Tujuan=='F'):
         y = x
    elif (Tujuan=='R'):
         y = 4/9 * (x-32)

#print (Awal)
print(x,'', Awal,'=', y, '', Tujuan)