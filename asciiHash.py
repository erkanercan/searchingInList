# Mühendislik projesi 1. ödev
# Erkan Ercan 2015213024
# Yazılan dil : Python3

# Her bir açıklama satırı altındaki
# fonksiyon ya da işlemi açıklamak için yazılmıştır.

# Python üzerinde dizi yapısı olmadığı için 203 indisli
# ve indisleri NULL olan bir liste oluşturuluyor.
global lstHashListesi
lstHashListesi = []
for i in range(0, 203):
    lstHashListesi.append(None)


def dosyaAc():
    # Üstteki satırda dosya açma işlemi yapılıyor.
    # lstKelimeler değişkeni diğer fonksiyonlarda kullanılmak için
    # global yapılıyor.
    global lstKelimeler
    # txt dosyası açılıp her satır ayrı ayrı listeye atılıyor.
    lstKelimeler = open("kelimeler.txt").read().splitlines()
    # Tüm kelimeler tek tek kontrol edilerek küçük harfe dönüştürülüyor
    lstKelimeler = [item.lower() for item in lstKelimeler]

# Python üzerinde hali hazırda bir hash() fonksiyonu bulunduğu için hash()
# olarak istenen fonksiyonun ismi hashBul yapıldı.


def hashBul(key, n):
    # ascii toplamları bulunan kelimeler listede yerlerine
    # quadratic probing yöntemi ile yerleştiriliyor
    global quadraticYerlestirmeSayisi
    sayac = 1
    quadraticYerlestirmeSayisi = key % n
    # yerleştirilene kadar dönmesi için bir sonsuz döngü
    while n > 1:

        if lstHashListesi[quadraticYerlestirmeSayisi] is None:
            lstHashListesi[quadraticYerlestirmeSayisi] = key
            break

        else:
            quadraticYerlestirmeSayisi = (
                quadraticYerlestirmeSayisi + pow(sayac, 2)) % n
            sayac = sayac + 1


# alınan kelimeler for döngüsü ile tek tek karakterlerine ayırılıp ascii
# numaraları ile keyler oluşturuluyor.
def karakterListesiOlustur():
    global quadraticCarpimSayisi, key
    for kelime in lstKelimeler:
        key = 0
        # her kelime tek tek harflerine ayrılıyor.
        karakterAyir = list(kelime)
        # kelimenin uzunluğu bulunuyor (quadratic probing yöntemi için.)
        quadraticCarpimSayisi = 1
        for harf in karakterAyir:
            # ascii numaraları bulunup toplanıyor
            key = key + ord(harf) * quadraticCarpimSayisi
            quadraticCarpimSayisi = quadraticCarpimSayisi + 1
        hashBul(key, len(lstHashListesi))


# Dosya açma ve karakter listesi oluşturup
# hash dizisine atama fonksiyonları çalıştırılıyor.
dosyaAc()
karakterListesiOlustur()
print("Hash listesinin son hali : \n" + str(lstHashListesi))

# Arama için kullanıcıdan giriş alınıyor.
print("Lütfen aramak istediğiniz kelimeyi giriniz :")
kullaniciGiris = input()


def girisHarflereAyir(kullaniciGiris):
    # Kullanıcıdan alınan kelime harflerine ayrılarak
    # kullaniciHarf dizisine harf harf atanıyor.
    global kullaniciHashToplam
    kullaniciHashToplam = 0
    kullaniciHarf = []
    quadraticCarpimSayisi = 1
    for harf in kullaniciGiris:
        kullaniciHarf.append(harf)
        # Kullanıcı girişinin hash değeri bulunuyor.
        kullaniciHashToplam = kullaniciHashToplam + \
            (ord(harf) * quadraticCarpimSayisi)
        quadraticCarpimSayisi = quadraticCarpimSayisi + 1
    print("Aradığınız kelimenin harflerine ayrılmış hali : "
          + str(kullaniciHarf) +
          "\nAradığınız kelimenin hash değeri : "
          + str(kullaniciHashToplam))


def listedeAra(kullaniciHashToplam):
    bulunanIndex = None
    try:
        bulunanIndex = lstHashListesi.index(kullaniciHashToplam)
    except ValueError:
        print("List does not contain value")
    print("Kelimeniz listenin " + str(bulunanIndex) + ". elemanında.")


girisHarflereAyir(kullaniciGiris)
listedeAra(kullaniciHashToplam)
