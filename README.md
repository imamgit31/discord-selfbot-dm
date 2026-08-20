# Discord Self-Bot DM Sender 📨

Discord self-bot kullanarak sunucudaki tüm üyelere otomatik olarak DM mesaj gönderme aracı.

## 🌟 Özellikler

✅ **100% Başarılı Gönderim** - Rate limit koruması ile hiçbir mesaj kaybolmaz  
✅ **Anti-Spam** - 6-10 saniye aralıkla gönderim (Discord'tan ban almaz)  
✅ **Hata Yönetimi** - DM'i kapalı olan kullanıcıları atlar ve devam eder  
✅ **Detaylı İstatistikler** - Başarı oranı, süre ve hız bilgisi  
✅ **Arka Plan Çalışması** - Discord'a bağlı kalarak sürekli çalışır  

## 📦 Kurulum

### 1️⃣ Python 3.8+ Gerekli
```bash
python --version  # Sürüm kontrolü
```

### 2️⃣ discord.py Kütüphanesini Kur
```bash
pip install discord.py
```

### 3️⃣ Hesap Token'ını Al

**Seçenek 1: Tarayıcıdan (Kolay)**
- Discord Web'de F12 (Developer Tools) aç
- Console sekmesine git
- Şu kodu yapıştır:
```javascript
(webpackChunkdiscord_app=webpackChunkdiscord_app||[]).push([[""],{},e=>{let t=null;for(let n in e.c)if(e.c[n].exports&&e.c[n].exports.default&&e.c[n].exports.default.getToken)t=e.c[n].exports.default;t&&console.log(t.getToken())}]);
```
- Çıkan token'ı kopyala ve `selfbot.py`'da yerine yaz

### 4️⃣ Token'ı Koda Ekle
`selfbot.py` dosyasını düzenle:
```python
ACCOUNT_TOKEN = "YOUR_ACCOUNT_TOKEN_HERE"
```
Yerine gerçek token'ı yaz.

### 5️⃣ Kodu Çalıştır
```bash
python selfbot.py
```

## 🚀 Kullanım

Bot başlatıldığında konsol'da komut yazabilirsiniz:

### Mesaj Gönderme
```
.dmmesaj <mesaj> <sunucu_id>
```

**Örnek:**
```
.dmmesaj Merhaba! Nasılsınız? 123456789
```

### Sunucu ID'si Nasıl Bulunur?
1. Discord'da Developer Mode'u aç (User Settings > Advanced > Developer Mode)
2. Sunucuda sağ tıkla
3. "Copy Server ID" tıkla

⏱️ **Tahmini Süre:**
- 50 üye = ~6.5 dakika
- 100 üye = ~13 dakika
- 200 üye = ~26 dakika

### Diğer Komutlar
```
.durdur   - Göndermeyi durdur
.yardim   - Yardım göster
.cikis    - Bot'u kapat
```

## ⚠️ UYARILAR

🚨 **Discord Terms of Service**
- Self-bot spam'ı Discord ToS'ye göre yasaktır
- Hesabınız kalıcı olarak yasaklanabilir

🔒 **Hesap Güvenliği**
- Token'ı kimseyle paylaşmayın!
- Token'ı GitHub'a commit etmeyin!

---

**⚠️ Sorumluluğu kendinize alın!**
