def timeconverter(s):
    jam = s//3600   #Konversi Jam
    a = s%3600
    menit = a//60   #Konversi Menit
    b = a%60
    detik = b%60    #Konversi Detik

    if len(str(jam)) < 2:                                             #Cek jika jam masih 1 digit
        conv = "0"+str(jam)+":"+str(menit)+":"+str(detik)             #Jam akan ditambahkan "0" pada awal karena jam masih 1 digit
        if len(str(menit))<2:                                              #Cek jika menit masih 1 digit
            conv = "0"+str(jam)+":"+"0"+str(menit)+":"+str(detik)          #menit akan ditambahkan "0" pada awal karena menit masih 1 digit
            if len(str(detik))<2:                                              #Cek jika detik masih 1 digit
                conv = "0"+str(jam)+":"+"0"+str(menit)+":"+"0"+str(detik)
        else:
            if len(str(detik))<2:                                          #Cek jika detik masih 1 digit
                conv = "0"+str(jam)+":"+str(menit)+":"+"0"+str(detik)      #detik akan ditambahkan "0" pada awal karena detik masih 1 digit

    elif len(str(menit))<2:                                         #Jam sudah 2 digit namun menit masih 1 digit
        conv = str(jam)+":"+"0"+str(menit)+":"+str(detik)
        if len(str(detik))<2:
            conv = str(jam)+":"+"0"+str(menit)+":"+"0"+str(detik)

    elif len(str(detik))<2:                                         #Jam dan menit sudah 2 digit namun detik masih 1 digit
            conv = str(jam)+":"+str(menit)+":"+"0"+str(detik)
    return conv

s = int(input("Masukan detik : "))
if s < 0 or s > 359999:                                              #Syarat jika detik negatif atau lebih dari 359999
    print("Invalid Input!")
else:
    print("Konversi : ",timeconverter(s))