# Hayvanat Bahçesi Simülasyonu(TASK)

Bu proje, 500x500 birimlik bir alanda yaşayan farklı türlerdeki hayvanlar ve bir avcının yer aldığı, zaman içinde hareket, üreme ve avlanma gibi davranışların simüle edildiği bir ekosistem simülasyonudur.

##  Proje Özellikleri

- **79 birey** ile başlayan sistem
- **1000 adım** boyunca ilerleyen simülasyon
- **Pygame** ile gerçek zamanlı görsel sunum
- **Türe özgü** davranış modelleri

##  Algoritma Yaklaşımı

### İlk Üretme
Hayvanlar tanımlı tür, cinsiyet ve sayıda başlangıçta alana rastgele yerleştirilir.

### Hareket
Her hayvan türüne özgü bir mesafede rastgele x ve y eksenlerinde hareket eder. Alan dışına çıkılmaz.

### Avlanma
Avlanabilen türler kendilerine tanımlı menzildeki uygun hayvan türlerini avlar.

### Üreme
Aynı türden, farklı cinsiyette iki canlı 3 birimden yakınsa, rastgele cinsiyetli yeni bir birey rastgele konumda oluşur.

### Görsel Sunum
Pygame ekranında harita (500x500) + bilgi paneli (200px) yer alır. Her hayvan bir daire, bilgi panelinde sayılar ve renge karşılık tür etiketi yer alır.

### Step Takibi
Sağ altta her adım için adım sayacı gösterilir.

##  Proje Yapısı

```
zoo_simulation/
├── models/          # Hayvan sınıfları ve veri modelleri
├── utils/           # Yardımcı fonksiyonlar
├── visual/          # Pygame görsel bileşenleri
├── simulation/      # Simülasyon mantığı
├── main.py          # Ana çalıştırma dosyası
└── requirements.txt # Gerekli kütüphaneler
```

### Sınıflar
- **Hayvan sınıfı** ve türe özgü alt sınıflar tanımlanmıştır
- **Sabitler:** Tüm ayarlar constants.py dosyasında merkezi olarak yönetilir
- **Fonksiyonellik:** Hareket, avlanma, üreme ve sayım işlemleri ayrı fonksiyonlardadır

##  Problemler

### Aşırı Üreme Problemi
Aynı bireyin bir adımda birden fazla çiftleşmesini engellemek için `ureyenler` seti kullanılmıştır.

### Doğum Sınırı
Her tür için adım başına maksimum 3 yavru sınırı eklenerek kontrol sağlanmıştır.

### Ekran Taşma Sorunu
Harita ile Pygame ekranı birebir olacak şekilde tasarlandı, bilgi paneli ayrı bir bölümdedir.

##  Kurulum

1. **Projeyi klonlayın:**
   ```bash
   git clone https://github.com/canturane/zoo_simulation.git
   cd zoo_simulation
   ```

2. **Sanal ortam oluşturun:**
   ```bash
   python -m venv venv
   ```

3. **Sanal ortamı aktifleştirin:**
   ```bash
   # Linux/Mac
   source venv/bin/activate
   
   # Windows
   venv\Scripts\activate
   ```

4. **Gerekli kütüphaneleri yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Simülasyonu çalıştırın:**
   ```bash
   python main.py
   ```

##  Kullanım

Simülasyon başlatıldıktan sonra:
- Hayvanlar otomatik olarak hareket eder
- Avlanma ve üreme davranışları gerçek zamanlı olarak simüle edilir
- Sağ alt köşede adım sayacı görüntülenir
- Bilgi panelinde tür bazlı popülasyon istatistikleri takip edilir

##  Gereksinimler

- Python 3.7+
- Pygame
- NumPy (isteğe bağlı)

##  Ekran Görüntüleri

### 1

<img width="526" height="396" alt="Ekran görüntüsü 2025-07-14 173030" src="https://github.com/user-attachments/assets/a9567e4e-89e7-488e-9196-20c06bcc15ed" />

### 2

<img width="424" height="315" alt="Ekran görüntüsü 2025-07-14 173150" src="https://github.com/user-attachments/assets/dd1a30a6-ac46-4f78-b692-32e65aeeefa2" />
