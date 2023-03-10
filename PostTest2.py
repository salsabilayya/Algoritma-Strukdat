arr = ['Arsel','Avivah','Daiva',['Wahyu','Wibi']]
def linearsearch(arr,cari):
    for l in range(len(arr)):
        if type(arr[l]) == list:
            hasil1 = linearsearch(arr[l],cari)
            if hasil1 == -1:
                return -1
            else:
                print(f'{cari} telah ditemukan pada indeks {l} pada kolom {hasil1}')
                exit()
        elif arr[l] == cari:
            return l
    return -1
print(arr)

cari = input('Masukan nama yang ingin dicari : ')
hasil2 = linearsearch(arr,cari)
if hasil2 == -1:
    print(f'{cari} telah ditemukan pada indeks {hasil2}')
else:
    print(f'{cari} telah ditemukan pada indeks {hasil2}')

