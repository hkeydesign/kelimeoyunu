import random
import sqlite3 as sql
import os

os.system('cls')

def harfal(kelime,soylenen_harfler,harfler):
    
    while True:
        os.system('cls')
        harf_al = random.randint(0,len(kelime)-1)
        if harf_al not in soylenen_harfler:
            print(harf_al+1,'. harfimiz :',kelime[harf_al])
            harfler[harf_al] = kelime[harf_al]
            soylenen_harfler.append(harf_al)
            break
        elif len(soylenen_harfler) ==len(kelime):
            print('harf kalmadı hayvan')
            break
        else:
            continue

while True:
    toplampuan = 0
    sorgu = input('Ne yapacaksın ?\nKelime Oyunu oyna -1\nSkor Tablosu Sorgula -2\nÇıkış(q):')
    os.system('cls')
    if sorgu == '1':
        name = input('Skor kaydetmem için önce isim alayım lütfen : ')
        for i in range(6):
            while True:
                dosya = open("C:\\Users\\acmlk\\OneDrive\\Masaüstü\\ses\\anlamlar.txt","r",encoding="utf-8")
                for _ in range(random.randint(1,8174)):
                    line = dosya.readline()
                    kelime,anlam= map(
                    lambda n: n.strip(), line.split('**')
                )
                elpuan = len(kelime)*100
                if anlam.strip()=='yok':
                    print('Anlam bulunamadı başa dönülüyor.')
                    continue
                elif anlam.strip() != 'yok':
                    break
            
            soylenen_harfler, harfler = [] ,[]
            for _ in kelime:
                harfler.append('*')
            os.system('cls')
            print(len(kelime),'harften oluşuyor.\nAnlamı :',anlam)
            while True:
                print(anlam,'\n'+str(harfler))
                if kelime[len(kelime)-3:len(kelime)] == "mak" or kelime[len(kelime)-3:len(kelime)] == "mek" :
                    print("Mastar eki var")

                girdi = input('Giriniz:')
                if girdi == kelime :
                    print(elpuan,'kazandın !')
                    toplampuan+=elpuan            
                    print('top : ', toplampuan)
                    __import__('time').sleep(2)
                    os.system('cls')
                    break        
                elif girdi.upper()=='HARF':
                    harfal(kelime,soylenen_harfler,harfler)
                    elpuan-=100
                    continue
            
        print(f'Önceki El Toplam:{toplampuan}kazandın ')
        db = sql.connect('C:\\Users\\acmlk\\OneDrive\\Masaüstü\\ses\\skor.sqlite')
        imlec = db.cursor()
        imlec.execute("CREATE TABLE IF NOT EXISTS skor (İsim,Puan)")
        imlec.execute(f"INSERT INTO skor VALUES('{name}','{toplampuan}')")
        db.commit()
        db.close()
    if sorgu=='2':
        db = sql.connect('C:\\Users\\acmlk\\OneDrive\\Masaüstü\\ses\\skor.sqlite')
        imlec = db.cursor()
        imlec.execute("SELECT İsim,Puan FROM skor WHERE Puan != '0'")
        skorlar = imlec.fetchall()
        print('İSİM - SKOR ŞEKLİNDE')
        for _ in range(len(skorlar)):
            print(skorlar[_])
        input('\n\nÇıkmak için herhangi bir tuşa basın:')
        os.system('cls')
    if sorgu == 'q':
        break
