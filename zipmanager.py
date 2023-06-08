import zipfile
import os

def extract_zip(zip_file_path, extract_path):
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
    except FileNotFoundError:
        print("Hata: Dosya yolu yanlış yazıldı veya dosya mevcut değil.")

def split_file_to_zip(input_file, chunk_size):
    
    # Dosya boyutunu alın
    try:
        file_size = os.path.getsize(input_file)
    except FileNotFoundError:
        print("Hata: Dosya yolu yanlış yazıldı veya dosya mevcut değil.")
        return
    # Chunk boyutunu belirleyin
    chunk_size = chunk_size * 1024 * 1024  # megabyte cinsinden
    # Bölümlerin sayısını hesaplayın
    num_chunks = file_size // chunk_size + (1 if file_size % chunk_size != 0 else 0)
    # Girdi dosyasını açın
    with open(input_file, 'rb') as infile:
        for i in range(num_chunks):
            # Zip dosyası adını oluşturun
            zip_filename = f"{input_file}_part{i+1}.zip"
            # Zip dosyasını oluşturun
            with zipfile.ZipFile(zip_filename, 'w', compression=zipfile.ZIP_DEFLATED) as outfile:
                # Chunk boyutunda okuma yapın
                data = infile.read(chunk_size)
                # Dosya sonuna kadar okunacaksa
                if not data:
                    break
                # Zip dosyasına yazın
                outfile.writestr(os.path.basename(input_file), data)

    print(f"{num_chunks} adet zip dosyası oluşturuldu.")
    
def extract_zip_here(zip_file_path):

    # zip dosyasının adını ve dizin yolunu ayrıştırın
    zip_dir, zip_filename = os.path.split(zip_file_path)
    # zip dosyasının adından uzantıyı silin
    folder_name = os.path.splitext(zip_filename)[0]
    # çıkarma klasörünü oluşturun ve zip dosyasını çıkarın
    extract_path = os.path.join(zip_dir, folder_name)
    os.makedirs(extract_path, exist_ok=True)
    extract_zip(zip_file_path, extract_path)
    print(f"{zip_filename} dosyasının içeriği {extract_path} klasörüne çıkartıldı.")
    
def durum(islem):
    while True:
        if islem=="çıkart":
            secenek=input("Dosyayı çıkartmak istediğiniz yeri giriniz(burası / dizine): ")
            while True:
                if secenek== "burası":
                    zipyol=input("zip dosyasının yolunu girin: ")
                    extract_zip_here(zipyol)
                    break
                elif secenek == "dizine":
                    zipyol=input("zip dosyasının yolunu girin: ")
                    klasor_ac=input("Çıkarılacak dosya yolunu girin: ")
                    extract_zip(zipyol, klasor_ac)
                    break
                else:
                    print("Hatalı işlem seçimi!")
                    secenek=input("Dosyayı çıkartmak istediğiniz yeri giriniz(burası / dizine): ")           
            break
        elif islem=="böl":
            buyuk_dosya=input("Zip dosyasının yolunu giriniz: ")
            while True:
                boyut=input("Kaçar megabytelık ziplere bölmek istiyorsunuz? ")
                if type(boyut) == int:
                    split_file_to_zip(buyuk_dosya, boyut)
                    break
                else:
                    print("Lütfen bir tamsayı değeri girin!")     
                    boyut=input("Kaçar megabytelık ziplere bölmek istiyorsunuz? ")
            break
        else:
            print("Hata: Yanlış işlem seçildi. Lütfen 'aç' veya 'böl' girin.")
            islem=input("yapılacak işlemi giriniz(çıkart / böl): ")

if __name__ == '__main__':

    islem=input("yapılacak işlemi giriniz(çıkart / böl): ")
    durum(islem)
"""
bölünen dosyayı da istenilen dizine çıkartmak için araştırma yapılacak.
"""