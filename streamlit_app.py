import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound, VideoUnavailable
import docx
import io
import base64

def get_transcript(video_url):
    try:
        video_id = video_url.split("v=")[1].split("&")[0]
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'tr'])
        raw_text = " ".join([entry['text'] for entry in transcript])
        return raw_text, video_id
    except (TranscriptsDisabled, NoTranscriptFound, VideoUnavailable) as e:
        return f"Hata: {str(e)}", None
    except Exception as e:
        return f"Beklenmeyen bir hata oluştu: {str(e)}", None

def create_word_document(transcript, video_id):
    """Transkripti Word dosyasına dönüştürür."""
    doc = docx.Document()
    doc.add_heading(f'YouTube Video Transkripti - {video_id}', 0)
    
    p = doc.add_paragraph(transcript)
    
    # Belgeyi byte olarak kaydet
    buffer = io.BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    return buffer

def get_download_link(buffer, filename):
    """Word dosyasını indirmek için bir link oluşturur."""
    b64 = base64.b64encode(buffer.getvalue()).decode()
    return f'<a href="data:application/vnd.openxmlformats-officedocument.wordprocessingml.document;base64,{b64}" download="{filename}.docx">Word Dosyası Olarak İndir</a>'

# Sayfa yapılandırması ve başlık
st.set_page_config(
    page_title="YouTube Video Transkripti",
    page_icon="🎬",
    layout="wide"
)

# Başlık ve açıklama
st.title("YouTube Video Transkripti")
st.markdown("YouTube video URL'sini girin ve transkripti alın.")

# Ana içerik
col1, col2 = st.columns([1, 2])

with col1:
    video_url = st.text_input("Video URL", placeholder="YouTube Video URL'sini buraya yapıştırın...")
    get_btn = st.button("Transkripti Al", type="primary")

with col2:
    # Video gösterimi için bir yer ayırıyoruz
    if video_url:
        try:
            video_id = video_url.split("v=")[1].split("&")[0]
            st.video(f"https://youtu.be/{video_id}")
        except:
            st.error("Geçerli bir YouTube URL'si giriniz.")

# Transkript sonucu için büyük bir alan
transcript_container = st.container()

# Butona tıklandığında transkript al
if get_btn:
    with st.spinner("Transkript alınıyor..."):
        transcript, video_id = get_transcript(video_url)
    
    with transcript_container:
        st.text_area("Video Transkripti", value=transcript, height=400)
        
        # Transkript alındıysa ve hata yoksa Word olarak indirme seçeneği göster
        if video_id and not transcript.startswith("Hata:") and not transcript.startswith("Beklenmeyen"):
            word_buffer = create_word_document(transcript, video_id)
            
            # İndirme düğmesi
            st.download_button(
                label="Word Dosyası Olarak İndir",
                data=word_buffer,
                file_name=f"transkript_{video_id}.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

# Alt bilgi
st.markdown("---")
st.markdown("YouTube Transkript Uygulaması")
