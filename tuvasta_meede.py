# ver.02
# detailandmed: bamKysimusKood
# ühisprojekti andmed: detailandmed, tegevused, partnerid

# Skript töötab järgmiste meedete JSON struktuuride puhul:
# vaikesed 4 voor
# liitmeede 4 voor
# leader 19.2
# leader 19.3

import json

json_string = open('C:\\Users\\martinpr\\Documents\\GitHub\\sisend_failid\\vaikesed_4voor', 'r',
                   encoding="utf8").read()
parsed_json = json.loads(json_string)

toimik = parsed_json.get('toimik')
taotlusvoor_tahis = toimik.get('taotlusvoorTahis')

print(toimik['taotlusvoorTahis'] + ' ' + toimik['meedeNimi'] + '\n')



def yhisprojekt_andmevaljad(yhisprojektAndmed):

    # erinevaid muutujad kasutusel selleks, et alamobjeki ridade loend algaks alati 0ga
    i = 0
    j = 0
    k = 0

    # TODO: andmeplokidest leitud väärtused kokkuliita ja see järel print - kui palju on kuval andmevälju kokku
    print('\n' + 'Ühisprojekti sammus detailandmed küsimusi kokku ' + str(len(yhisprojekt_detailandmed)) + ':' + '\n')

    # detailandmed ploki andemte leidmine
    for rida in yhisprojekt_detailandmed:

        print("JSON objekt " + str(i) + ": " + rida['bamKysimusKood'])
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


    print('\n' + 'Ühisprojekti sammus tegevus küsimusi kokku ' + str(len(yhisprojekt_tegevused)) + ':' + '\n')


    # tegevused ploki andmete leidmine
    for rida in yhisprojekt_tegevused:
        print("JSON objekt " + str(j) + ". " + '\n' + 'Tegevuse kirjeldus: ' + rida['kirjeldus'] + '\n')
        j = j + 1


    print('\n' + 'Ühisprojekti sammus kokku ' + str(len(yhisprojekt_partnerid)) + ' partnerit: ' + '\n')

    print('Toetuse taotleja ülesande kirjeldus: ' + yhisprojekt_andmed['taotlejaYlesanneteKirjeldus'] + '\n')


    # partnerid ploki andmed leidmine
    for rida in yhisprojekt_partnerid:

        print("JSON objekt " + str(k) + ". ")
        k = k + 1

        if 'nimiArireg' in rida:

            print('Osaleja: ' + rida['nimiArireg'] + '(' + rida['kood'] + ')')
            print('Ülesande kirjeldus: ' + rida['kirjeldus'] + '\n')



        elif 'nimi' in rida:

            print('Osaleja: ' + rida['nimi'] + '(' + rida['kood'] + ') ')
            print('Ülesande kirjeldus: ' + rida['kirjeldus'] + '\n')


        else:
            print('JSON struktuuris on partner objekt olemas aga skript ei suuda leida objekti alt '
                  'atribuuti "nimiArireg" ega "nimi". Palun kontrolli JSON struktuuri!')


def det_andmed_bamKysimuKood(obj_detailandmed):
    i = 0

    print('\n' + 'Detailandmed sammus küsimusi kokku ' + str(len(obj_detailandmed)) + ':' + '\n')

    for rida in obj_detailandmed:

        print("JSON objekt " + str(i) + ": " + rida['bamKysimusKood'])
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

    yhisprojekt_andmed = parsed_json.get('sisu').get('leader192Toetustaotlus').get('yhisprojektAndmed')

    yhisprojekt_detailandmed = parsed_json.get('sisu').get('leader192Toetustaotlus').get('yhisprojektAndmed')\
        .get('detailandmed')

    yhisprojekt_tegevused = parsed_json.get('sisu').get('leader192Toetustaotlus').get('yhisprojektAndmed')\
        .get('tegevused')

    yhisprojekt_partnerid = parsed_json.get('sisu').get('leader192Toetustaotlus').get('yhisprojektAndmed')\
        .get('partnerid')

    yhisprojekt_andmevaljad(yhisprojekt_detailandmed)



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
