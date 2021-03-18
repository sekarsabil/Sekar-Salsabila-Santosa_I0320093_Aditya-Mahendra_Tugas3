#Dictionary berisi hobi, sosial media, lagu kesukaan, makanan favorit
dict = {'Nama': ['Sekar Salsabila Santosa'],
        'Hobi': ['Bernyanyi','Menonton Film','Mendengarkan Musik'],
        'Sosial Media': ['Instagram : @sekarsabill', 'Line : sekarsabil', 'snapchat : sekarsabill'],
        'Lagu Kesukaan': ['Like to be you','Mutual','Misfit'],
        'Makanan Favorit': ['Udang', 'Mie', 'Dimsum']}
print(dict)

#Mengubah Salah Satu Hobi dan Sosial Media
dict['Hobi'][1]=('Belajar')
dict['Sosial Media'][2]=('Twitter : eyow')

#Menghapus 2 Makanan Favorit
del dict['Makanan Favorit'][1:3]

#Menambahkan Satu Hobi
dict['Hobi'].append('Jalan-jalan')

print(dict)