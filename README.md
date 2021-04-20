# *Python face_recognition Kütüphanesi ile yoklama uygulaması*

## Projenin Amacı
### *Sınıfın fotoğrafından öğrencileri tespit ederek yoklama alma işleminin daha hızlı yapılmasını sağlamak.*

## Uygulamanın Kullanımı
![uygulama_dosyalari](https://user-images.githubusercontent.com/82876602/115394745-c639df00-a1eb-11eb-9465-dfc087fab736.PNG)
### Uygulama 5 dosyadan oluşmaktadır.

### **dersler Klasörü:** Kayıtlı olan dersleri ve Derslerin yoklamalarının bulunduğu excel dosyalarını barındırmaktadır. 
### **images Klasörü:** Kayıtlı olan öğrencilerin fotoğraflarnı barındırır.
### **dersadlari Dosyası:** Oluşturulmuş derslerin isimlerini tutar.
### **kayitlar dosyası:** Kayıtlı olan öğrencilerin Ad soyad, Öğrenci numarası ve Fotoğraflarının bulunduğu konumu barındırır.
### **Code dosyası:** Projeye ait kodları barındırır.

![uygulama](https://user-images.githubusercontent.com/82876602/115395432-8b847680-a1ec-11eb-8e3f-14068b8e5abc.PNG)
### Uygulama açıldığında karşımıza bu ekran gelmektedir. Bu ekrandan öğrenci ekleme, ders silme, ders oluşturma, yoklama alma işlemlerine ulaşılabilmektedir.

![ogr_ekle](https://user-images.githubusercontent.com/82876602/115396430-a2779880-a1ed-11eb-9bbc-aa3038b04ee4.PNG)
### Öğrenci Ekleme: Eklenecek olan öğrencinin Adı-Soyadı, Öğrenci No girilip ilgili öğrencinin fotoğrafı seçilerek kayıt işlemi yapılır. Eksik bilgi girilmesi halinde uyarı mesajı verilmektedir.

 ![ders_olustur](https://user-images.githubusercontent.com/82876602/115396419-9ee41180-a1ed-11eb-901b-1efb5f9c6c23.PNG)
### Ders Oluştur: Oluşturulacak olan dersin adi ve dersi alan öğrenciler seçilerek oluştur butonuna basılır. İlk olarak oluşturulan dersin adını dersadlari.txt dosyasına ekler. Ardından dersler klasörü altına dersi alan öğrencilerin bulunduğu txt dosyası ve yoklamanın tutulacağı xlsx dosyasınu oluşturur.

![ders_sil](https://user-images.githubusercontent.com/82876602/115396564-cb982900-a1ed-11eb-930d-2aae57dc67fc.PNG)
### Ders Silme: Silinecek Ders/Dersler seçilerek sil butonuna basılır. Seçilen derslerle ilgili bütün kayıtlar silinir.

![yoklama_al](https://user-images.githubusercontent.com/82876602/115396976-3e090900-a1ee-11eb-84cb-a471671c3217.PNG)
### Yoklama Alma: Yoklamanın alınacağı güne ait sınıfın fotoğrafı, dersin adı seçilir. Ardından yoklama tarihi girilerek yoklama al butonuna basılır. Program sınıfın fotografındaki yüzleri kayıtlı olan öğrencilerin yüzleri ile karşılaştırarak 0.55 duyarlılıkla fotoğraftaki kişileri bulur ve derse ait yoklama xlsx dosyasında ilgili kişinin yanına 1 yazar. 
