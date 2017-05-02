import json


# vaikesed_4voor
# liitmeede_liikmetega
# leader_19_2
# leader_19_3
json_string = open('C:\\Users\\martinpr\\Documents\\GitHub\\sisend_failid\\vaikesed_4voor', 'r', encoding="utf8").read()
parsed_json = json.loads(json_string)

toimik = parsed_json.get('toimik')
taotlusvoor_tahis = toimik.get('taotlusvoorTahis')

print(toimik['taotlusvoorTahis'] + ' ' + toimik['meedeNimi'] + '\n')



def det_andmed_bamKysimuKood(obj_detailandmed):
    i = 0

    print('\n' + 'Detailandmed sammus küsimusi kokku ' + str(len(obj_detailandmed)) + ':' + '\n')

    for rida in obj_detailandmed:

        print("Andmeväli " + str(i) + ": " + rida['bamKysimusKood'])
        i = i + 1

        if 'vaartus' in rida:
            print("Väärtus: " + rida['vaartus'])

        elif 'vaartusNimekiri' in rida:
            # tagastab list vaartusNimekiri kõik elemendid komaga eraldatult
            print(', '.join(rida['vaartusNimekiri']))

        elif 'lisadokumendid' in rida:
            # tagastab listi 'lisadokumendid' element indeksiga 0 ja võtme 'nimetus' väärtuse
            print("Faili nimi: " + rida['lisadokumendid'][0]['nimetus'])

        print()




# Leader 19.3
if taotlusvoor_tahis == '19.3.2016':

    obj_detailandmed = parsed_json.get('sisu').get('leader193Toetustaotlus').get('detailandmed')

    det_andmed_bamKysimuKood(obj_detailandmed)



# Leader 19.2
if taotlusvoor_tahis == '19.2.2016':

    obj_detailandmed = parsed_json.get('sisu').get('leader192Toetustaotlus').get('detailandmed')

    det_andmed_bamKysimuKood(obj_detailandmed)


# Liit 4 voor
elif taotlusvoor_tahis == '4.1.2017_4':

    obj_detailandmed = parsed_json.get('sisu').get('liitmeedeToetustaotlus').get('detailandmed')

    det_andmed_bamKysimuKood(obj_detailandmed)


# Väikesed 4 voor
elif taotlusvoor_tahis == '6.3.2017_4':

    obj_detailandmed = parsed_json.get('sisu').get('vaikesteToetustaotlus').get('detailandmed')

    det_andmed_bamKysimuKood(obj_detailandmed)


else:
    print('Tähelepanu! Viga! \nTaotlusvoor tähisega ' + taotlusvoor_tahis + ' tarvis pole skripti arendatud!')
