# 🗺️ Türkiye Deprem Risk Haritası - Streamlit Uygulaması

Bu uygulama, Türkiye İl Bazlı Deprem Risk Analizi Model V3 verilerini kullanarak interaktif bir harita sunar.

## 📋 Gereksinimler

- Python 3.8 veya üzeri
- Gerekli Python paketleri (requirements.txt dosyasında listelenmiştir)

## 🚀 Kurulum

1. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

2. Uygulamayı çalıştırın:
```bash
streamlit run streamlit_harita.py
```

3. Tarayıcınızda otomatik olarak açılacak (genellikle http://localhost:8501)

## 🎯 Kullanım

### Haritaya Tıklama
- Haritada bir ile tıklayarak o ile ait detaylı risk bilgilerini görebilirsiniz
- Tıklama sonrası il detayları sayfanın altında görüntülenecektir

### Dropdown Menü
- Sayfanın üst kısmındaki dropdown menüden istediğiniz ili seçebilirsiniz
- Seçim yaptığınızda il detayları otomatik olarak görüntülenecektir

### Harita Özellikleri
- **Renk Kodlaması:**
  - 🟢 Yeşil: Düşük Risk (1-3)
  - 🟡 Turuncu: Orta Risk (4-6)
  - 🟠 Kırmızı: Yüksek Risk (7-8)
  - 🔴 Koyu Kırmızı: Çok Yüksek Risk (9-10)

- **Tooltip:** Haritada bir ilin üzerine geldiğinizde il adı ve risk skoru görüntülenir
- **Popup:** Bir ile tıkladığınızda hızlı bilgi popup'ı açılır

## 📊 Gösterilen Bilgiler

Her il için şu bilgiler gösterilir:

- **Risk Skoru (1-10)**: Genel deprem risk skoru
- **Risk Seviyesi**: Düşük, Orta, Yüksek veya Çok Yüksek
- **Toplam Tehlike Puanı**: Fay ve tarihsel tehlikelerin birleşik puanı
- **Fay Tehlike Puanı**: Fay hatlarına yakınlık puanı
- **Tarihsel Tehlike Puanı**: Geçmiş depremlerin büyüklük toplamı puanı
- **Kırılganlık Puanı**: Eski bina oranına dayalı kırılganlık puanı
- **Eski Hane Oranı**: 2000 öncesi bina oranı
- **Toplam Nüfus**: İl nüfusu
- **Fay Tehlike Oranı**: İl alanının faylara yakınlık oranı
- **Tarihsel Puan (Toplam Mag)**: 50km etki alanındaki depremlerin büyüklük toplamı

## 📁 Gerekli Dosyalar

Uygulamanın çalışması için aşağıdaki dosyanın mevcut olması gerekir:
- `TURKIYE_IL_BAZLI_RISK_ANALIZI_V3.geojson`

## 🔧 Sorun Giderme

### GeoJSON dosyası bulunamıyor
- `TURKIYE_IL_BAZLI_RISK_ANALIZI_V3.geojson` dosyasının `streamlit_harita.py` ile aynı dizinde olduğundan emin olun

### Paket yükleme hataları
- Python sürümünüzün 3.8 veya üzeri olduğundan emin olun
- Virtual environment kullanmanız önerilir:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Haritada tıklama çalışmıyor
- Tarayıcınızın JavaScript'i desteklediğinden emin olun
- Alternatif olarak dropdown menüden il seçebilirsiniz

## 📝 Notlar

- Model V3, %70 Fay + %30 Tarihsel (Büyüklük Toplamı) ağırlıklı toplam tehlike kullanır
- 50km etki alanı dikkate alınmıştır
- Risk skoru = %50 Toplam Tehlike + %50 Kırılganlık formülü ile hesaplanır


