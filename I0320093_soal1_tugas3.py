#Membuat list teman
list_teman = ['zanet','yola','salma','diva','moris','titus','vincen','rana','tito','zafir']

#Menampilkan isi list indeks nomor 4,6,7
print("Nama Teman 4,6,7 : ", list_teman[3], ",", list_teman[5], ",", list_teman[6])

#Mengganti nama teman pada list 3,5,9
list_teman[2] = 'rara'
list_teman[4] = 'rafli'
list_teman[8] = 'stefany'

#Menambah nama teman
list_teman.append('issa')
list_teman.append('gea')

#Menampilkan list nama teman dengan perulangan
print(list_teman*4)

#Menampilkan panjang list
print (len(list_teman))