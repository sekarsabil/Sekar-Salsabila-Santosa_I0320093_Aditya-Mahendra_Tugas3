#Dictionary berisi hobi, sosial media, lagu kesukaan, makanan favorit
dict = {'Hobi': ['Bernyanyi','Menonton Film','Mendengarkan Musik'],'Sosial Media': ['Instagram', 'Line', 'Whatsapp'], 'Lagu Kesukaan': ['Like to be you','Mutual','Misfit'], 'Makanan Favorit': ['Udang', 'Mie', 'Dimsum']}

#Mengubah Salah Satu Hobi dan Sosial Media
dict['Hobi'][1]=('Belajar')
dict['Sosial Media'][2]=('Twitter')

#Menghapus 2 Makanan Favorit
del dict['Makanan Favorit'][1:3]

#Menambahkan Satu Hobi
dict.update({"Hobi":"Jalan-jalan"})

print(dict)