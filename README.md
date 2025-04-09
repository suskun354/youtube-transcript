# YouTube Transkript Uygulaması

Bu uygulama, YouTube videolarının transkriptlerini kolayca alıp, Word belgesi olarak indirmenizi sağlar.

![YouTube Transkript Uygulaması](https://i.imgur.com/OQSBFsP.png)

## Özellikler

- 🎬 YouTube video URL'sinden transkript alabilme
- 📝 Transkript metnini görüntüleme
- 📄 Transkriptleri Word (.docx) belgesi olarak indirebilme
- 🎥 Video önizleme

## Kurulum

### Gereksinimler

- Python 3.8 veya üzeri

### Adımlar

1. Repoyu klonlayın:
```bash
git clone https://github.com/kullaniciadi/youtube-transcript.git
cd youtube-transcript
```

2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

3. Uygulamayı çalıştırın:
```bash
streamlit run app.py
```

## Kullanım

1. Uygulama başladığında YouTube video URL'sini giriş alanına yapıştırın
2. "Transkripti Al" düğmesine tıklayın
3. Transkript alındıktan sonra metni görüntüleyin
4. İsterseniz "Word Dosyası Olarak İndir" düğmesine tıklayarak transkripti .docx formatında indirin

## Desteklenen Diller

Uygulama, YouTube'un desteklediği tüm dillerde transkript alabilir ancak öncelikli olarak İngilizce ve Türkçe transkriptleri almaya çalışır.

## Teknolojiler

- [Streamlit](https://streamlit.io/) - Web arayüzü
- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api) - YouTube transkriptlerini almak için
- [Python-DOCX](https://python-docx.readthedocs.io/en/latest/) - Word belgesi oluşturmak için

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakın.

## İletişim

Sorularınız veya önerileriniz için lütfen [GitHub Issues](https://github.com/kullaniciadi/youtube-transcript/issues) üzerinden iletişime geçin. 