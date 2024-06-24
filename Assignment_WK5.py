LG_in_Kwara = ['Ilorin west', 'Ekiti', 'Oke-ero', 'Ifelodun', 'Barutee', 'Asa', 'Ilorin south', 'Kaiama', 'Share']
Width = len (LG_in_Kwara)


# Correcting misspelled 'Barutee' as 'Baruten' in the list 'LG_in_Kwara'
for i in range(Width):
    if LG_in_Kwara[i] == 'Barutee':
        LG_in_Kwara[i] = 'Baruten'

# Adding ' LGA' to each element in the array stored in variable 'LG_in_Kwara'
for i in range(Width):
    LG_in_Kwara [i] += ' LGA'

for i in LG_in_Kwara:
    print(i)
