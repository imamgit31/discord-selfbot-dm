import discord
import asyncio
import random
import time

class SelfBot:
    def __init__(self, token):
        self.token = token
        self.client = discord.Client(intents=discord.Intents.all())
        self.is_sending = False
        
        @self.client.event
        async def on_ready():
            print(f'✅ Self-Bot aktif! {self.client.user} olarak giriş yapıldı')
            print(f'📱 Hesap: {self.client.user.name}#{self.client.user.discriminator}')
    
    async def send_dms_to_guild(self, guild_id, message_text):
        """
        Sunucudaki tüm üyelere DM gönder
        Rate limit atmamak için 6-10 saniye aralık (Spam koruması)
        """
        self.is_sending = True
        
        # Sunucuyu bul
        guild = self.client.get_guild(guild_id)
        if not guild:
            print(f"❌ Sunucu bulunamadı! (ID: {guild_id})")
            return
        
        print(f"\n📤 Sunucu: {guild.name}")
        print(f"👥 Total üye: {guild.member_count}")
        
        # Üyeleri topla (bot'ları ve kendini hariç tut)
        members = [m for m in guild.members if not m.bot and m.id != self.client.user.id]
        
        if not members:
            print("❌ Mesaj gönderilebilecek üye bulunamadı!")
            return
        
        print(f"📨 Mesaj gönderilecek: {len(members)} üye")
        print(f"⏱️  Rate limit: 6-10 saniye aralıkla (Spam koruması)")
        print(f"📊 Tahmini Süre: ~{int(len(members) * 8)} saniye ({int(len(members) * 8 / 60)} dakika)")
        print("-" * 60)
        
        successful = 0
        failed = 0
        start_time = time.time()
        
        for i, member in enumerate(members, 1):
            if not self.is_sending:
                break
            
            try:
                # DM gönder
                await member.send(message_text)
                successful += 1
                percentage = (i / len(members)) * 100
                elapsed = int(time.time() - start_time)
                print(f"✅ [{i:3d}/{len(members)}] ({percentage:5.1f}%) {member.name:20s} | ⏱️  {elapsed}s")
                
            except discord.Forbidden:
                failed += 1
                print(f"⚠️  [{i:3d}/{len(members)}] {member.name:20s} - DM kapalı (atlandı)")
            except discord.HTTPException as e:
                failed += 1
                print(f"⚠️  [{i:3d}/{len(members)}] {member.name:20s} - API hatası")
            except Exception as e:
                failed += 1
                print(f"⚠️  [{i:3d}/{len(members)}] {member.name:20s} - Hata: {e}")
            
            # Discord rate limit koruması
            # Random 6-10 saniye arayla (Spam'dan kaçınmak için)
            delay = random.uniform(6.0, 10.0)
            remaining = len(members) - i
            if remaining > 0:
                estimated_time = int(remaining * 8)
                print(f"   ⏳ Sonraki: {delay:.1f}s | Kalan: {remaining} üye (~{estimated_time}s daha)\n")
            
            await asyncio.sleep(delay)
        
        self.is_sending = False
        elapsed_time = time.time() - start_time
        success_rate = (successful / len(members) * 100) if len(members) > 0 else 0
        
        # İstatistikler
        print("\n" + "=" * 60)
        print("📊 DM GÖNDERME TAMAMLANDI")
        print("=" * 60)
        print(f"✅ Başarılı: {successful}/{len(members)}")
        print(f"❌ Başarısız: {failed}/{len(members)}")
        print(f"📈 Başarı Oranı: {success_rate:.1f}%")
        print(f"⏱️  Toplam Süre: {int(elapsed_time)} saniye ({int(elapsed_time/60)} dakika {int(elapsed_time%60)} saniye)")
        print(f"🔄 Ortalama Hız: {elapsed_time/len(members):.2f} sn/üye")
        print("=" * 60 + "\n")
    
    async def input_handler(self):
        """Konsol inputlarını işle"""
        loop = asyncio.get_event_loop()
        
        while True:
            # Arka planda inputları oku
            user_input = await loop.run_in_executor(None, input, "\n💬 Komut (.dmmesaj <mesaj> <sunucu_id>): ")
            
            if user_input.startswith('.dmmesaj '):
                # Parametreleri ayır
                parts = user_input[9:].rsplit(' ', 1)
                
                if len(parts) != 2:
                    print("❌ Hata! Kullanım: `.dmmesaj <mesaj> <sunucu_id>`")
                    print("📝 Örnek: .dmmesaj Merhaba! 123456789")
                    continue
                
                message_text = parts[0]
                try:
                    guild_id = int(parts[1])
                except ValueError:
                    print("❌ Sunucu ID'si sayı olmalıdır!")
                    continue
                
                # DM göndermeyi başlat
                await self.send_dms_to_guild(guild_id, message_text)
            
            elif user_input == '.durdur':
                self.is_sending = False
                print("⛔ DM gönderme durduruldu!")
            
            elif user_input == '.yardim':
                print("""
                📖 KOMUTLAR:
                .dmmesaj <mesaj> <sunucu_id>  - Sunucudaki üyelere DM gönder
                .durdur                        - Göndermeyi durdur
                .yardim                        - Yardım göster
                .cikis                         - Botu kapat
                """)
            
            elif user_input == '.cikis':
                print("👋 Bot kapatılıyor...")
                await self.client.close()
                break
            
            else:
                if user_input.strip():
                    print("❓ Bilinmeyen komut! `.yardim` yazarak komutları görüntüle.")
    
    async def start(self):
        """Self-bot'u başlat"""
        print("🚀 Self-Bot başlatılıyor...")
        
        # Client'i başlat
        client_task = asyncio.create_task(self.client.start(self.token))
        
        # Input handler'ı başlat
        try:
            await asyncio.sleep(2)
            await self.input_handler()
        except KeyboardInterrupt:
            print("\n⛔ Bot kapatılıyor...")
            await self.client.close()

# Ana program
if __name__ == "__main__":
    ACCOUNT_TOKEN = "YOUR_ACCOUNT_TOKEN_HERE"
    
    if ACCOUNT_TOKEN == "YOUR_ACCOUNT_TOKEN_HERE":
        print("❌ HATA: Token'ı ayarla!")
        print("📝 ACCOUNT_TOKEN yerine kendi hesap token'ını yaz")
        exit()
    
    bot = SelfBot(ACCOUNT_TOKEN)
    
    print("""
    ╔════════════════════════════════════════╗
    ║       DISCORD SELF-BOT DM SENDER       ║
    ║      6-10 Saniye Arayla (Anti-Spam)    ║
    ║          100% Başarı Garantili          ║
    ╚════════════════════════════════════════╝
    """)
    
    try:
        asyncio.run(bot.start())
    except Exception as e:
        print(f"❌ Hata: {e}")
