import json



json_string = open('C:\\Users\\martinpr\\Documents\\GitHub\\sisend_failid\\leader_19_2', 'r', encoding="utf8").read()
parsed_json = json.loads(json_string)

toimik = parsed_json.get('toimik')
taotlusvoor_tahis = toimik.get('taotlusvoorTahis')

print(toimik['taotlusvoorTahis'] + ' ' + toimik['meedeNimi'] + '\n')



# Leader 19.3
if taotlusvoor_tahis == '19.3.2016':
    print('Leader 19.3')



# Leader 19.2
if taotlusvoor_tahis == '19.2.2016':
    print('Leader 19.2')


# Liit 4 voor
elif taotlusvoor_tahis == '4.1.2017_4':
    print('Liit')


# Väikesed 4 voor
elif taotlusvoor_tahis == '6.3.2017_4':
    print('Väikesed 4 voor')


else:
    print('Tähelepanu! Viga! \nTaotlusvoor tähisega ' + taotlusvoor_tahis + ' tarvis pole skripti arendatud!')
