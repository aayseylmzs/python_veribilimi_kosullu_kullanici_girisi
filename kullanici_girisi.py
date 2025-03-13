# Değişkenler ve Kullanıcı Girişi
#Soru: Kullanıcıdan adını, soyadını ve yaşını alan bir Python programı yazın. Alınan bilgileri şu formatta ekrana yazdırın:
#"Merhaba [Ad Soyad], [Yaş] yaşındasınız. Hoş geldiniz!"

def kullaniciBilgileri():
    kullaniciAdi = input("lütfen adınızı giriniz : ")
    kullaniciSoyAdi = input("lütfen soyadınızı giriniz : ")

    kullaniciYas = input("lütfen yaşınızı giriniz : ") 

    print(f"Merhaba {kullaniciAdi} {kullaniciSoyAdi}, {kullaniciYas} yaşınızdasınız.Hoş geldiniz!")

kullaniciBilgileri()