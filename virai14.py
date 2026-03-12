import customtkinter as ctk
from tkinter import messagebox, filedialog, simpledialog
import threading
import os
import random
import asyncio
import edge_tts
import yt_dlp
import re
import subprocess
import requests
import g4f
import time
import traceback
import math
import textwrap
import webbrowser
import sys
import platform
import urllib.parse
import json 
import tempfile 
from PIL import Image
import numpy as np
from moviepy import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip, concatenate_audioclips, CompositeAudioClip, concatenate_videoclips, ImageClip
from deep_translator import GoogleTranslator
from proglog import ProgressBarLogger
import time
import imageio_ffmpeg
FFMPEG_YOLU = imageio_ffmpeg.get_ffmpeg_exe()
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

try:
    import pygame
    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False

if platform.system() == "Windows":
    MAC_FONT_PATH = "C:/Windows/Fonts/arialbd.ttf"
elif platform.system() == "Darwin":
    MAC_FONT_PATH = "/System/Library/Fonts/Helvetica.ttc"
else:
    MAC_FONT_PATH = "Arial"
class ViraiRenderLogger(ProgressBarLogger):
    def __init__(self, log_callback, prog_callback):
        super().__init__()
        self.log_callback = log_callback
        self.prog_callback = prog_callback
        self.start_time = time.time()

    def bars_callback(self, bar, attr, value, old_value=None):
        if bar == 't': 
            total = self.bars[bar]['total']
            if total > 0:
                progress = (value / total) * 100
                self.prog_callback(progress)
                
                elapsed = time.time() - self.start_time
                if progress > 0 and progress < 100:
                    eta = elapsed * (100 - progress) / progress
                    eta_str = time.strftime("%M:%S", time.gmtime(eta))
                    self.log_callback(f"💾 Render: Kalan Süre ~ {eta_str} | İlerleme: %{int(progress)}")
API_URL = "https://lunacomputer.com/api.php"
IYZICO_LINK_PRO = "https://iyzi.link/AKfFvA"
IYZICO_LINK_STUDIO = "https://iyzi.link/AKfFwA"
APP_VERSION = "1.0.0"

APP_BG = "#0B0F19"
GLASS_BG = "#151B2B"
GLASS_BORDER = "#2A3143"
TEXT_COLOR = "#E2E8F0"
ACCENT_COLOR = "#0EA5E9"
HOVER_COLOR = "#0284C7"
GOLD_COLOR = "#FBBF24"
DANGER_COLOR = "#EF4444"

import importlib
try:
    readers = importlib.import_module("moviepy.audio.io.readers")
    if hasattr(readers, 'FFMPEG_AudioReader'):
        _original_del = getattr(readers.FFMPEG_AudioReader, '__del__', None)
        def _safe_del(self):
            try:
                if hasattr(self, 'proc'):
                    if _original_del: _original_del(self)
            except: pass
        readers.FFMPEG_AudioReader.__del__ = _safe_del
except: pass

def safe_set_audio(clip, audio): return clip.with_audio(audio) if hasattr(clip, 'with_audio') else clip.set_audio(audio)
def safe_set_duration(clip, d): return clip.with_duration(d) if hasattr(clip, 'with_duration') else clip.set_duration(d)
def safe_set_start(clip, s): return clip.with_start(s) if hasattr(clip, 'with_start') else clip.set_start(s)
def safe_set_position(clip, p): return clip.with_position(p) if hasattr(clip, 'with_position') else clip.set_position(p)
def safe_subclip(clip, start, end):
    if hasattr(clip, 'subclipped'): return clip.subclipped(start, end)
    elif hasattr(clip, 'subclip'): return clip.subclip(start, end)
    return clip
def safe_opacity(clip, op):
    try:
        if hasattr(clip, 'with_opacity'): return clip.with_opacity(op)
        elif hasattr(clip, 'set_opacity'): return clip.set_opacity(op)
    except: pass
    return clip
def akilli_ses_kisici(clip, oran):
    try:
        if hasattr(clip, "volumex"): return clip.volumex(oran)
        elif hasattr(clip, "with_volume_scaled"): return clip.with_volume_scaled(oran)
        elif hasattr(clip, "multiply_volume"): return clip.multiply_volume(oran)
    except Exception as e: pass
    return clip

PRESETS_FILE = os.path.join(os.path.expanduser("~"), ".virai_presets.json")

TEMP_DIR = tempfile.gettempdir()
TEMP_VIDEO_DOSYASI = os.path.join(TEMP_DIR, "virai_temp_parca.mp4")
TEMP_MUZIK_DOSYASI = os.path.join(TEMP_DIR, "virai_temp_muzik.mp3")
POP_SES_DOSYASI = os.path.join(TEMP_DIR, "virai_pop_sfx.mp3")
TEMP_TEST_SESI = os.path.join(TEMP_DIR, "virai_temp_test_voice.mp3")

ELEVENLABS_API_KEY = "77b06c2dfce030abb46123e2c26c0c162a5b0891476a98d8eb38e5a8329386e8"

ELEVENLABS_VOICES = {
    "⭐ Adam (Derin/Belgeselci)": "pNInz6obpgDQGcFmaJgB",
    "⭐ kel toni (Kalın/Anlatıcı)": "TX3LPaxmHKxFdv7VOQHJ",
    "⭐ Ferdi (dpg)": "onwK4e9ZLuTAKqWW03F9",
    "⭐ Mehmet Ali (Haber Spikeri)": "lxZLq5dcyw12UangGJgN",
    "⭐ Ruhi (Bilgilendirici)": "RXCCWbOxP7Hisa63Xsv5",
    "⭐ Selin (Neşeli Kadın)": "8LQS4H6IYf1unP46qbKD",
    "⭐ Faruk (Radio FM)": "IuRRIAcbQK5AQk1XevPj",
    "⭐ Lila (Psikolog)": "xsGHrtxT5AdDzYXTQT0d",
    "⭐ Gülsüm (Enerjik)": "EJGs6dWlD5VrB3llhBqB",
    "⭐ Hugo (Çizgi Film)": "DUnzBkwtjRWXPr6wRbmL",
    "⭐ Serhat (Gür)": "7VqWGAWwo2HMrylfKrcm",
    "⭐ Ömer (Haber 2)": "21m00Tcm4TlvDq8ikWAM",
    "⭐ Bella (Yumuşak Yabancı Kadın)": "EXAVITQu4vr4xnSDxMaL",
    "⭐ Leon (Güçlü Yabancı Adam)": "DMyrgzQFny3JI1Y1paM5",
}

ctk.set_appearance_mode("Dark")

def dosya_gecerli_mi(yol, min_bayt=1000):
    if not os.path.exists(yol) or os.path.getsize(yol) < min_bayt: return False
    try:
        with open(yol, "rb") as f:
            ilk_baytlar = f.read(50).lower()
            if b"<!doctype" in ilk_baytlar or b"<html" in ilk_baytlar: return False
    except: return False
    return True

def internetten_muzik_indir(kategori, log_callback):
    for f in [TEMP_MUZIK_DOSYASI, TEMP_MUZIK_DOSYASI.replace('.mp3', '') + ".mp3"]:
        if os.path.exists(f):
            try: os.remove(f)
            except: pass
    terimler = {"Korku / Gerilim": "no copyright horror ambient music scary background", "Hüzünlü / Dram": "no copyright sad piano emotional background music", "Hareketli / Viral": "no copyright upbeat viral background music vlog", "Rastgele": "no copyright background music"}
    arama_sorgusu = terimler.get(kategori, "no copyright background music")
    log_callback(f"🎵 Müzik aranıyor: '{kategori}'...")
    out_tmpl = os.path.join(TEMP_DIR, 'virai_temp_muzik')
    ydl_opts = {
        'quiet': True, 'no_warnings': True, 'format': 'bestaudio/best', 
        'outtmpl': out_tmpl, 'noplaylist': True, 
        'ffmpeg_location': FFMPEG_YOLU, # <--- BU SATIRI EKLEDİK
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}]
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch5:{arama_sorgusu}", download=False)
            entries = info.get('entries', [])
            if not entries: return None
            uygunlar = [e for e in entries if e.get('duration', 0) > 60]
            if not uygunlar: uygunlar = entries
            secilen = random.choice(uygunlar)
            ydl.download([secilen['webpage_url']])
            final_path = out_tmpl + ".mp3"
            if dosya_gecerli_mi(final_path, 5000): return final_path
            return None
    except Exception: return None

def sfx_indir():
    if os.path.exists(POP_SES_DOSYASI) and dosya_gecerli_mi(POP_SES_DOSYASI, 1000):
        return
    try:
        url = "https://raw.githubusercontent.com/KilledByAPixel/Shattered-Pixel-Dungeon/master/assets/sounds/surface.mp3"
        r = requests.get(url, timeout=10)
        if r.status_code == 200 and len(r.content) > 1000:
            with open(POP_SES_DOSYASI, "wb") as f: f.write(r.content)
    except: pass
    if not dosya_gecerli_mi(POP_SES_DOSYASI, 1000):
        try:
            out_tmpl = os.path.join(TEMP_DIR, 'virai_pop_sfx')
            ydl_opts = {
                'quiet': True, 'no_warnings': True, 'format': 'bestaudio/best', 
                'outtmpl': out_tmpl, 'noplaylist': True, 
                'ffmpeg_location': FFMPEG_YOLU, # <--- BU SATIRI EKLEDİK
                'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '128'}]
            } 
            with yt_dlp.YoutubeDL(ydl_opts) as ydl: ydl.download(['ytsearch1:pop sound effect short 1 second'])
        except: pass
def hizli_youtube_arama(kelime, limit=6):
    ydl_opts = {'quiet': True, 'extract_flat': True, 'force_generic_extractor': False}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch{limit}:{kelime}", download=False)
            return info.get('entries', [])
    except Exception:
        return []
def get_youtube_video_id(url):
    """
    YouTube video ID'sini URL'den çıkarır.
    """
    if 'youtu.be' in url:
        return url.split('/')[-1].split('?')[0]
    elif 'youtube.com' in url:
        match = re.search(r'v=([^&]+)', url)
        if match:
            return match.group(1)
    return None

def youtubeda_video_ara_liste(anahtar_kelime, log_callback):
    log_callback(f"🔍 Arka plan taranıyor: '{anahtar_kelime[:30]}...'")
    ydl_opts = {'quiet': True, 'no_warnings': True, 'noplaylist': True, 'age_limit': 17}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # ytsearch yerine ytsearch15 kullanarak arama sayısını limitliyoruz
            info = ydl.extract_info(f"ytsearch15:{anahtar_kelime}", download=False)
            entries = info.get('entries', [])
            if not entries:
                return []
            
            results = []
            for video in entries:
                video_id = get_youtube_video_id(video.get('webpage_url', ''))
                if video_id:
                    results.append({
                        "title": video.get('title', 'Başlık Yok'),
                        "url": video.get('webpage_url'),
                        "video_id": video_id,
                        "thumbnail_url": f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg"
                    })
            return results
    except Exception as e:
        log_callback(f"⚠️ YouTube arama hatası: {e}")
        return []

def youtubeda_video_bul(anahtar_kelime, log_callback):
    log_callback(f"🔍 Arka plan taranıyor: '{anahtar_kelime[:30]}...'")
    ydl_opts = {'quiet': True, 'no_warnings': True, 'noplaylist': True, 'age_limit': 17}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch5:{anahtar_kelime}", download=False)
            entries = info.get('entries', [])
            if not entries: return None
            uygun_videolar = [e for e in entries if e.get('duration', 0) > 300]
            if not uygun_videolar: uygun_videolar = entries
            secilen = random.choice(uygun_videolar)
            log_callback(f"✅ Video Seçildi: {secilen.get('title')[:30]}")
            return secilen.get('webpage_url') or secilen.get('url')
    except Exception: return None

def nokta_atisi_indir(url, istenen_sure, log_callback):
    if os.path.exists(TEMP_VIDEO_DOSYASI):
        try: os.remove(TEMP_VIDEO_DOSYASI)
        except: pass
    log_callback("⬇️ Kaynak video indiriliyor...")
    
    # yt-dlp'ye ffmpeg'in yerini özel olarak belirtiyoruz
    ydl_opts = {
        'quiet': True, 
        'no_warnings': True, 
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'ffmpeg_location': FFMPEG_YOLU
    }
    
    video_url, audio_url, toplam_saniye = None, None, 0
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            toplam_saniye = info.get('duration', 0)
            if 'requested_formats' in info:
                for f in info['requested_formats']:
                    if f.get('vcodec') != 'none': video_url = f['url']
                    elif f.get('acodec') != 'none': audio_url = f['url']
            else: video_url = info.get('url')
            
        if toplam_saniye < istenen_sure: baslangic = 0
        else: baslangic = random.uniform(0, max(0, toplam_saniye - istenen_sure - 10))
        
        # subprocess için "ffmpeg" yazmak yerine doğrudan kendi çalıştırıcısını (FFMPEG_YOLU) kullanıyoruz
        komut_base = [FFMPEG_YOLU, "-ss", str(baslangic)]
        
        if audio_url and video_url:
            komut = komut_base + ["-i", video_url, "-ss", str(baslangic), "-i", audio_url, "-t", str(istenen_sure + 5), "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-c:a", "aac", "-preset", "fast", "-y", "-loglevel", "error", TEMP_VIDEO_DOSYASI]
        else:
            komut = komut_base + ["-i", video_url, "-t", str(istenen_sure + 5), "-c:v", "libx264", "-c:a", "aac", "-y", "-loglevel", "error", TEMP_VIDEO_DOSYASI]
            
        subprocess.run(komut, check=True)
        return dosya_gecerli_mi(TEMP_VIDEO_DOSYASI, 5000)
    except Exception as e: 
        print(f"Indirme hatasi: {e}")
        return False

def icerik_getir(konu, mod, dil_modu, sure_secimi, icerik_tipi, log_callback):
    headers = {'User-Agent': 'python:viral.video.factory:v2.0'}
    limitler = {"15 Saniye (Shorts)": 230, "30 Saniye (Reels)": 480, "60 Saniye (TikTok)": 950, "Sınırsız (Max)": 2500}
    max_karakter = limitler.get(sure_secimi, 2500)
    ceviri_yap = "TR Çeviri" in dil_modu
    tam_metin = ""
    
    if "Instagram" in icerik_tipi:
        try:
            dil = "Türkçe" if "TR" in dil_modu else "İngilizce"
            istek = f"Görevin şu Instagram hesabının profilini, hedef kitlesini ve içerik tarzını tahmin etmek/analiz etmek: {konu}. Lütfen bu hesabın tarzına %100 uygun yepyeni bir viral kısa video senaryosu yaz. Sadece direkt konuya gir, ekstra hiçbir yorum yapma, başlık atma. Maksimum {max_karakter} karakter. Dil: {dil}"
            # GÜNCELLEME: Provider kısıtlamaları kaldırıldı, model düzeltildi
            try: response = g4f.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": istek}])
            except: response = g4f.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": istek}])
            tam_metin = "".join(response) if not isinstance(response, str) else response
            if tam_metin: return tam_metin.strip().replace("**", "").replace("*", "").replace("#", "")
            return None
        except Exception: return None
        
    elif "Yapay Zeka" in icerik_tipi:
        try:
            dil = "Türkçe" if "TR" in dil_modu else "İngilizce"
            if mod != "rastgele" and konu.strip():
                istek = f"Sen profesyonel bir TikTok/Shorts metin yazarısın. Konumuz: '{konu}'.\nLütfen son derece akıcı, yazım kurallarına uygun ve doğal bir {dil} ile viral bir video senaryosu yaz.\nKurallar:\n1. İlk cümleye çok çarpıcı, merak uyandıran şok edici bir bilgiyle başla (Buna Hook denir).\n2. 'Merhaba', 'Videoma hoşgeldiniz', 'Bugün sizlere' gibi amatör girişler kesinlikle KULLANMA. Doğrudan konuya gir.\n3. Anlatım dilin çok doğal, sürükleyici ve hikaye anlatır gibi olsun. Robotik ifadelerden, garip çevirilerden ve devrik cümlelerden kaçın.\n4. SADECE okunacak seslendirme metnini yaz. Başlık, hashtag, sahne açıklaması veya emoji KESİNLİKLE EKLEME.\nMaksimum uzunluk: {max_karakter} karakter."
            else:
                istek = f"Sen profesyonel bir TikTok/Shorts metin yazarısın. Rastgele, zihin açıcı, korkutucu veya çok az bilinen ilginç bir bilgi/hikaye anlat.\nLütfen son derece akıcı, yazım kurallarına uygun ve doğal bir {dil} ile yaz.\nKurallar:\n1. İlk cümleye çok çarpıcı ve merak uyandıran bir kancayla (Hook) başla.\n2. 'Merhaba', 'Bugün sizlere' gibi klasik girişler KULLANMA. Doğrudan konuya gir.\n3. Anlatım çok doğal ve sürükleyici olsun. Robotik çeviri kokan ifadelerden kaçın.\n4. SADECE okunacak seslendirme metnini ver. Başlık, hashtag, sahne açıklaması veya emoji KESİNLİKLE EKLEME.\nMaksimum uzunluk: {max_karakter} karakter."
            
            # GÜNCELLEME: Provider kısıtlamaları kaldırıldı, model düzeltildi
            try: response = g4f.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": istek}])
            except: response = g4f.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": istek}])
            tam_metin = "".join(response) if not isinstance(response, str) else response
            if tam_metin: return tam_metin.strip().replace("**", "").replace("*", "").replace("#", "")
            return None
        except Exception: return None
        
    elif "Bilgi" in icerik_tipi or "Wikipedia" in icerik_tipi:
        wiki_lang = "tr" if "TR" in dil_modu else "en"
        base_url = f"https://{wiki_lang}.wikipedia.org/w/api.php"
        try:
            if mod == "rastgele" or not konu.strip():
                params = {"action": "query", "generator": "random", "grnnamespace": 0, "prop": "extracts", "exchars": int(max_karakter + 500), "explaintext": 1, "format": "json"}
                resp = requests.get(base_url, params=params, headers=headers).json()
                pages = resp.get('query', {}).get('pages', {})
                for page_id in pages: tam_metin = pages[page_id].get('extract', '')
            else:
                params_search = {"action": "query", "list": "search", "srsearch": konu, "format": "json"}
                search_resp = requests.get(base_url, params=params_search, headers=headers).json()
                search_results = search_resp.get('query', {}).get('search', [])
                if search_results:
                    title = search_results[0]['title']
                    params_ext = {"action": "query", "prop": "extracts", "exchars": int(max_karakter + 500), "explaintext": 1, "titles": title, "format": "json"}
                    extract_resp = requests.get(base_url, params=params_ext, headers=headers).json()
                    pages = extract_resp.get('query', {}).get('pages', {})
                    for page_id in pages: tam_metin = pages[page_id].get('extract', '')
            if tam_metin:
                tam_metin = re.sub(r'==.*?==', '', tam_metin)
                tam_metin = re.sub(r'\[\d+\]', '', tam_metin)
                log_callback("✅ Bilgi başarıyla çekildi!")
        except Exception: log_callback(f"⚠️ Wikipedia Hatası")
    else:
        if "Tavsiye" in icerik_tipi: subs = "tavsiye+KGBTR" if "Orijinal" in dil_modu else "LifeProTips+YouShouldKnow"
        else: subs = "hikayeler+itiraf" if "Orijinal" in dil_modu else "confessions+tifu+AmItheAsshole"
        secilen_icerik = None
        url = f"https://www.reddit.com/r/{subs}/top.json" if mod == "rastgele" or not konu.strip() else f"https://www.reddit.com/r/{subs}/search.json"
        params = {"t": "month", "limit": 40} if mod == "rastgele" or not konu.strip() else {"q": konu, "restrict_sr": 1, "sort": "relevance", "limit": 25}
        try:
            cevap = requests.get(url, params=params, headers=headers)
            if cevap.status_code == 200:
                posts = cevap.json()['data']['children']
                valid_posts = [p['data'] for p in posts if 'selftext' in p['data'] and len(p['data']['selftext']) > 100]
                if valid_posts: secilen_icerik = random.choice(valid_posts)
        except Exception: pass
        if secilen_icerik:
            baslik = secilen_icerik.get('title', '')
            icerik = secilen_icerik.get('selftext', '')
            tam_metin = f"{baslik}. {icerik}"
            tam_metin = re.sub(r'http\S+', '', tam_metin).replace("Edit:", "").replace("&amp;", "&")
            log_callback("✅ Reddit içeriği başarıyla bulundu!")
            
    if not tam_metin.strip(): return None
    try:
        if len(tam_metin) > max_karakter:
            kismi_text = tam_metin[:max_karakter]
            son_nokta = max(kismi_text.rfind('.'), kismi_text.rfind('!'), kismi_text.rfind('?'))
            if son_nokta > len(kismi_text) * 0.4: tam_metin = kismi_text[:son_nokta+1]
            else: tam_metin = kismi_text[:kismi_text.rfind(' ')] + "..." if kismi_text.rfind(' ') != -1 else kismi_text
        return GoogleTranslator(source='auto', target='tr').translate(tam_metin) if ceviri_yap else tam_metin
    except Exception: return None
def metadata_uret(metin):
    istek = f"Aşağıdaki kısa video metni için YouTube Shorts/TikTok'a uygun, tık tuzaklı (viral) kısa bir BAŞLIK ve SEO uyumlu bol hashtagli bir AÇIKLAMA yaz. Sadece başlık ve açıklamayı ver.\nMetin: '{metin}'"
    try:
        try: loop = asyncio.get_event_loop()
        except RuntimeError: asyncio.set_event_loop(asyncio.new_event_loop())
        try: response = g4f.ChatCompletion.create(model="openai", provider=g4f.Provider.Blackbox, messages=[{"role": "user", "content": istek}])
        except: response = g4f.ChatCompletion.create(model="openai", provider=g4f.Provider.PollinationsAI, messages=[{"role": "user", "content": istek}])
        tam_metin = "".join(response) if not isinstance(response, str) else response
        return tam_metin.strip() if tam_metin else None
    except: return None

async def sesleri_olustur(cumleler, dil_modu, ses_modu, custom_voice_id, progress_callback):
    ses_klipleri, temp_files, toplam_sure = [], [], 0
    if "⭐" in ses_modu or "🔥" in ses_modu:
        if "🔥" in ses_modu:
            voice_id = custom_voice_id
            if not voice_id: raise Exception("Lütfen ElevenLabs Ses ID'sini kutucuğa yapıştırın!")
        else: voice_id = ELEVENLABS_VOICES.get(ses_modu, "ErXwobaYiN019PkySvjV")
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
        headers = {"Accept": "audio/mpeg", "Content-Type": "application/json", "xi-api-key": ELEVENLABS_API_KEY}
        for i, cumle in enumerate(cumleler):
            if not cumle.strip(): continue
            dosya_adi = os.path.join(TEMP_DIR, f"virai_temp_ses_{i}.mp3")
            data = {"text": cumle, "model_id": "eleven_multilingual_v2", "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}}
            response = requests.post(url, json=data, headers=headers)
            if response.status_code == 200:
                with open(dosya_adi, 'wb') as f: f.write(response.content)
            else:
                try: hata_detayi = response.json().get("detail", {}).get("message", response.text)
                except: hata_detayi = response.text
                raise Exception(f"ElevenLabs İsteği Reddedildi:\n\n{hata_detayi}")
            if dosya_gecerli_mi(dosya_adi, 500):
                try:
                    klip = AudioFileClip(dosya_adi)
                    ses_klipleri.append(klip)
                    temp_files.append(dosya_adi)
                    toplam_sure += klip.duration
                except: pass
            progress_callback(10 + (i / len(cumleler) * 20))
    else:
        if "Kadın" in ses_modu:
            ses_modeli = "en-US-JennyNeural" if "EN" in dil_modu else "tr-TR-EmelNeural"
            rate_str, pitch_str = ("+10%", "+5Hz") if "Enerjik" in ses_modu else ("+0%", "+0Hz")
        else:
            ses_modeli = "en-US-ChristopherNeural" if "EN" in dil_modu else "tr-TR-AhmetNeural"
            rate_str, pitch_str = ("-5%", "-10Hz") if "Gerçekçi" in ses_modu else ("+0%", "+0Hz")
        for i, cumle in enumerate(cumleler):
            if not cumle.strip(): continue
            dosya_adi = os.path.join(TEMP_DIR, f"virai_temp_ses_{i}.mp3")
            await edge_tts.Communicate(cumle, voice=ses_modeli, rate=rate_str, pitch=pitch_str).save(dosya_adi)
            if dosya_gecerli_mi(dosya_adi, 500):
                try:
                    klip = AudioFileClip(dosya_adi)
                    ses_klipleri.append(klip)
                    temp_files.append(dosya_adi)
                    toplam_sure += klip.duration
                except: pass
            progress_callback(10 + (i / len(cumleler) * 20))
    return ses_klipleri, temp_files, toplam_sure

async def altyazi_olustur(cumle, ses_suresi, baslangic_zamani, stil, t_color_isim, t_bg_isim):
    klipler = []
    temiz = cumle.strip().upper()
    color_map = {"Sarı": "#FFD700", "Beyaz": "white", "Siyah": "black", "Kırmızı": "red", "Yeşil": "green", "Mavi": "#0EA5E9"}
    bg_map = {"Yok (Şeffaf)": None, "Siyah": "black", "Beyaz": "white", "Kırmızı": "red", "Mavi": "blue", "Yeşil": "green"}
    c_hex = color_map.get(t_color_isim, "#FFD700")
    bg_hex = bg_map.get(t_bg_isim, None)
    s_color = "white" if c_hex == "black" else "black"
    
    if "1 Kelime" in stil: chunk_size = 1
    elif "2 Kelime" in stil: chunk_size = 2
    elif "3 Kelime" in stil: chunk_size = 3
    else: chunk_size = 999 
    
    kelimeler = temiz.split()
    if not kelimeler: return []
    
    if chunk_size == 999: parcalar = [temiz]
    else: parcalar = [" ".join(kelimeler[i:i+chunk_size]) for i in range(0, len(kelimeler), chunk_size)]
        
    toplam_harf = sum(len(p) for p in parcalar)
    cur_t = baslangic_zamani
    for p in parcalar:
        if toplam_harf == 0: continue
        dur = (len(p) / toplam_harf) * ses_suresi
        f_size = 85 if chunk_size != 999 else 55
        wrap_width = 13 if chunk_size != 999 else 28
        formatted_text = "\n".join(textwrap.wrap(p, width=wrap_width))
        txt_kwargs = {"text": formatted_text, "font_size": f_size, "color": c_hex, "font": MAC_FONT_PATH, "stroke_color": s_color, "stroke_width": 4 if chunk_size != 999 else 3, "text_align": "center"}
        if bg_hex: txt_kwargs["bg_color"] = bg_hex
        if chunk_size == 999:
            txt_kwargs["method"] = "caption"
            txt_kwargs["size"] = (1000, None)
        else:
            txt_kwargs["method"] = "label"

        txt = TextClip(**txt_kwargs)
        txt = safe_set_position(txt, ('center', 'center'))
        txt = safe_set_start(txt, cur_t)
        txt = safe_set_duration(txt, txt_kwargs.get("duration", dur))
        klipler.append((txt, cur_t))
        cur_t += dur
    return klipler

def apply_bw(img):
    bw = np.dot(img[...,:3], [0.2989, 0.5870, 0.1140])
    return np.dstack([bw, bw, bw]).astype(np.uint8)

def apply_contrast(img):
    return np.clip(img.astype(float) * 1.3, 0, 255).astype(np.uint8)

def apply_vignette(img):
    h, w = img.shape[:2]
    X, Y = np.meshgrid(np.arange(w), np.arange(h))
    dist = np.sqrt((X - w/2)**2 + (Y - h/2)**2)
    max_dist = np.sqrt((w/2)**2 + (h/2)**2)
    mask = 1 - (dist / max_dist) ** 1.5 
    mask = np.clip(mask + 0.3, 0, 1) 
    return (img * mask[:, :, np.newaxis]).astype(np.uint8)

async def video_islem_baslat(metin, s, cikis_adi, log, prog):
    temp_files = []
    prog(5) 
    try:
        log("🗣️ VAI Sesi İşliyor...")
        cumleler = [c for c in re.split(r'(?<=[.!?])\s+', metin.replace("\n", " ")) if c.strip()]
        if not cumleler: return False, "Okunacak geçerli bir metin bulunamadı."
        
        try:
            ses_klipleri, t_files, tot_sure = await sesleri_olustur(cumleler, s["dil"], s["ses"], s["custom_voice_id"], prog)
            temp_files.extend(t_files)
        except Exception as e: return False, str(e)
            
        if not ses_klipleri: return False, "Ses oluşturulamadı."
        
        video_yolu = None
        if s["tip"] == "local":
            if not s.get("yerel_video_yolu") or not os.path.exists(s["yerel_video_yolu"]):
                return False, "Seçilen yerel video dosyası bulunamadı."
            video_yolu = s["yerel_video_yolu"]
            log("🎬 Yerel arka plan videosu kullanılıyor...")
        elif s["tip"] == "ai_video":
            prompt = s["kaynak"]
            log("🎨 VAI Uygun Yapay Zeka Videosunu Arıyor...")
            en_prompt = GoogleTranslator(source='auto', target='en').translate(prompt[:100])
            search_query = f"{en_prompt} vertical background loop no copyright"
            final_url = youtubeda_video_bul(search_query, log)
            if not final_url: return False, "Uygun yapay zeka arka plan videosu bulunamadı."
            if not nokta_atisi_indir(final_url, tot_sure, log): return False, "Yapay zeka videosu indirilemedi."
            video_yolu = TEMP_VIDEO_DOSYASI
        else:
            # GÜNCELLEME: Listeden seçilen veya manuel girilen kesin linki doğrudan kullanıyoruz. Tekrar arama YOK!
            final_url = s["kaynak"] 
            if not final_url: return False, "Geçerli bir YouTube arka plan videosu linki bulunamadı."
            if not nokta_atisi_indir(final_url, tot_sure, log): return False, "YouTube'dan arka plan videosu indirilemedi."
            video_yolu = TEMP_VIDEO_DOSYASI
            
        prog(50)
        log("🎞️ Kurgu yapılıyor...")
        try: 
            v_ana = VideoFileClip(video_yolu)
            
            if s.get("video_vfx") == "Siyah & Beyaz":
                log("🎨 Siyah & Beyaz filtre uygulanıyor...")
                if hasattr(v_ana, 'image_transform'): v_ana = v_ana.image_transform(apply_bw) 
                else: v_ana = v_ana.fl_image(apply_bw) 
            elif s.get("video_vfx") == "Yüksek Kontrast":
                log("🎨 Yüksek Kontrast filtre uygulanıyor...")
                if hasattr(v_ana, 'image_transform'): v_ana = v_ana.image_transform(apply_contrast)
                else: v_ana = v_ana.fl_image(apply_contrast)
            elif s.get("video_vfx") == "Sinematik Vignette":
                log("🎨 Sinematik Vignette uygulanıyor...")
                if hasattr(v_ana, 'image_transform'): v_ana = v_ana.image_transform(apply_vignette)
                else: v_ana = v_ana.fl_image(apply_vignette)

            if s.get("zoom_fx"):
                log("🔍 Sinematik Kamera Yakınlaştırması uygulanıyor...")
                def zoom_filter(get_frame, t):
                    img = get_frame(t)
                    h, w = img.shape[:2]
                    zoom = 1.0 + 0.15 * (t / tot_sure)
                    new_w, new_h = int(w / zoom), int(h / zoom)
                    x1, y1 = (w - new_w) // 2, (h - new_h) // 2
                    cropped = img[y1:y1+new_h, x1:x1+new_w]
                    pil_img = Image.fromarray(cropped).resize((w, h), Image.Resampling.LANCZOS)
                    return np.array(pil_img)
                if hasattr(v_ana, 'transform'): v_ana = v_ana.transform(zoom_filter)
                else: v_ana = v_ana.fl(zoom_filter)

            if s["kurgu"] == "Düz Akış" and v_ana.duration < tot_sure:
                loop_count = int(tot_sure / v_ana.duration) + 1
                v_ana = concatenate_videoclips([v_ana] * loop_count)

            kesme_zamanlari = []
            
            if s["kurgu"] == "Sıçramalı (Jump-Cut)":
                parca_klipler, cur_t = [], 0
                while cur_t < tot_sure:
                    dur = min(random.uniform(2.5, 4.5), tot_sure - cur_t)
                    start = random.uniform(0, max(0, v_ana.duration - dur))
                    if hasattr(v_ana, 'subclipped'): parca_klipler.append(v_ana.subclipped(start, start + dur))
                    else: parca_klipler.append(v_ana.subclip(start, start + dur))
                    if cur_t > 0: kesme_zamanlari.append(cur_t) 
                    cur_t += dur
                v_kesit = concatenate_videoclips(parca_klipler, method="compose")
            else:
                if hasattr(v_ana, 'subclipped'): v_kesit = v_ana.subclipped(0, min(v_ana.duration, tot_sure + 1))
                else: v_kesit = v_ana.subclip(0, min(v_ana.duration, tot_sure + 1))
        except Exception: return False, "Seçilen arka plan bozuk çıktı veya okunamadı."

        # GÜNCELLEME: KATI DİKEY VİDEO (9:16) ORANLAYICI VE KIRPICI (EVRENSEL ÇÖZÜM)
        video_size = v_kesit.size if hasattr(v_kesit, 'size') and v_kesit.size else (1080, 1920)
        v_w, v_h = video_size
        target_w, target_h = 1080, 1920
        target_ratio = target_w / target_h
        current_ratio = v_w / v_h

        if current_ratio > target_ratio:
            new_w = int(v_h * target_ratio)
            if hasattr(v_kesit, 'cropped'): v_kesit = v_kesit.cropped(width=new_w, height=v_h, x_center=v_w/2, y_center=v_h/2)
            else: v_kesit = v_kesit.crop(width=new_w, height=v_h, x_center=v_w/2, y_center=v_h/2)
        elif current_ratio < target_ratio:
            new_h = int(v_w / target_ratio)
            if hasattr(v_kesit, 'cropped'): v_kesit = v_kesit.cropped(width=v_w, height=new_h, x_center=v_w/2, y_center=v_h/2)
            else: v_kesit = v_kesit.crop(width=v_w, height=new_h, x_center=v_w/2, y_center=v_h/2)

        # HATA ÇÖZÜMÜ: Positional Tuple kullanarak Moviepy 1.x ve 2.x sorununu çözdük
        if hasattr(v_kesit, 'resized'): 
            v_kesit = v_kesit.resized((1080, 1920))
        else: 
            v_kesit = v_kesit.resize((1080, 1920))
        
        w, h = v_kesit.size 
        final_yazilar = []
        
        if s.get("flash_fx") and s["kurgu"] == "Sıçramalı (Jump-Cut)":
            white_bg = np.full((h, w, 3), [255, 255, 255], dtype=np.uint8)
            for kz in kesme_zamanlari:
                flash = ImageClip(white_bg)
                flash = safe_set_duration(flash, 0.15)
                flash = safe_set_start(flash, kz)
                flash = safe_set_position(flash, ("center", "center"))
                flash = safe_opacity(flash, 0.8)
                final_yazilar.append(flash)

        log("🎬 Alt yazılar oluşturuluyor...")
        sfx_zamanlari, cur_t = [], 0
        for i, cumle in enumerate(cumleler):
            s_dur = ses_klipleri[i].duration
            klipler = await altyazi_olustur(cumle, s_dur, cur_t, s["stil"], s["text_color"], s["text_bg"])
            for txt_clip, start_t in klipler:
                final_yazilar.append(txt_clip)
                sfx_zamanlari.append(start_t)
            cur_t += s_dur 
            
        logo_clip, txt_clip, current_x_offset = None, None, 0
        if s.get("logo_yolu") and os.path.exists(s["logo_yolu"]):
            try:
                logo_clip = ImageClip(s["logo_yolu"])
                if hasattr(logo_clip, 'resized'): logo_clip = logo_clip.resized(height=80)
                else: logo_clip = logo_clip.resize(height=80)
                logo_clip = safe_opacity(logo_clip, 0.6) 
                current_x_offset = logo_clip.w + 15 
            except: pass

        if s["filigran"].strip():
            txt_kwargs = {"text": s["filigran"].strip(), "font_size": 40, "color": '#FFFFFF', "font": MAC_FONT_PATH, "stroke_color": "black", "stroke_width": 2, "method": "label"}
            txt_clip = TextClip(**txt_kwargs)
            txt_clip = safe_opacity(txt_clip, 0.6)

        total_w = current_x_offset + (txt_clip.w if txt_clip else 0)
        total_h = max((logo_clip.h if logo_clip else 0), (txt_clip.h if txt_clip else 0))

        if total_w > 0:
            v_size2 = v_kesit.size if hasattr(v_kesit, 'size') and v_kesit.size else (1080, 1920)
            v_w, v_h = v_size2
            max_x = max(0, v_w - total_w)
            max_y = max(0, v_h - total_h)
            ph_x, ph_y, sp_x, sp_y = random.uniform(0, 6.28), random.uniform(0, 6.28), random.uniform(0.3, 0.6), random.uniform(0.3, 0.6)
            def move_x(t): return (math.sin(t * sp_x + ph_x) + 1) / 2 * max_x
            def move_y(t): return (math.cos(t * sp_y + ph_y) + 1) / 2 * max_y
            if logo_clip:
                def logo_pos(t): return (int(move_x(t)), int(move_y(t)))
                logo_clip = safe_set_position(logo_clip, logo_pos)
                logo_clip = safe_set_duration(logo_clip, tot_sure)
                final_yazilar.append(logo_clip)
            if txt_clip:
                def txt_pos(t): return (int(move_x(t) + current_x_offset), int(move_y(t) + (total_h - txt_clip.h)/2))
                txt_clip = safe_set_position(txt_clip, txt_pos)
                txt_clip = safe_set_duration(txt_clip, tot_sure)
                final_yazilar.append(txt_clip)

        if s.get("progress_bar"):
            log("⏳ İlerleme Çubuğu ekleniyor...")
            bar_h = 15
            red_bg = np.full((bar_h, w, 3), [220, 38, 38], dtype=np.uint8)
            p_bar = ImageClip(red_bg)
            p_bar = safe_set_duration(p_bar, tot_sure)
            def bar_pos(t): return (int((t/tot_sure)*w) - w, h - bar_h - 20)
            p_bar = safe_set_position(p_bar, bar_pos)
            final_yazilar.append(p_bar)

        log("🔊 Ses tasarımı yapılıyor...")
        voice_audio = concatenate_audioclips(ses_klipleri)
        if s["vol_settings"]["voice"] != 1.0: voice_audio = akilli_ses_kisici(voice_audio, s["vol_settings"]["voice"])
        final_audio_list = [voice_audio]
        
        if s["sfx"]:
            sfx_indir()
            if dosya_gecerli_mi(POP_SES_DOSYASI, 1000):
                try:
                    for t in sfx_zamanlari: 
                        pop_c = AudioFileClip(POP_SES_DOSYASI)
                        pop_dur = pop_c.duration if hasattr(pop_c, 'duration') and pop_c.duration else 1.0
                        if pop_dur > 1.0: 
                            if hasattr(pop_c, 'subclipped'): pop_c = pop_c.subclipped(0, 1.0)
                            else: pop_c = pop_c.subclip(0, 1.0)
                        pop_c = akilli_ses_kisici(pop_c, s["vol_settings"]["sfx"])
                        if hasattr(pop_c, 'with_start'): pop_c = pop_c.with_start(t)
                        else: pop_c = pop_c.set_start(t)
                        final_audio_list.append(pop_c)
                except Exception as e: print(f"[SFX HATA]: {e}")

        if s["muzik"] != "Yok":
            m_yolu = None
            if s["muzik"] == "Yerel Dosya Seç...":
                if os.path.exists(s.get("yerel_muzik_yolu", "")): m_yolu = s["yerel_muzik_yolu"]
            else: m_yolu = internetten_muzik_indir(s["muzik"], log)

            if m_yolu and dosya_gecerli_mi(m_yolu, 1000):
                try:
                    m_c = AudioFileClip(m_yolu)
                    m_c_dur = m_c.duration if hasattr(m_c, 'duration') and m_c.duration else 1000
                    baslangic = 3 if m_c_dur > 15 else 0
                    if m_c_dur < (tot_sure + baslangic):
                        tekrar = int((tot_sure + baslangic) / m_c_dur) + 1
                        m_klipler = [AudioFileClip(m_yolu) for _ in range(tekrar)] 
                        m_c = concatenate_audioclips(m_klipler)
                    if hasattr(m_c, 'subclipped'): m_c = m_c.subclipped(baslangic, tot_sure + baslangic)
                    else: m_c = m_c.subclip(baslangic, tot_sure + baslangic)
                    m_c = akilli_ses_kisici(m_c, s["vol_settings"]["music"])
                    final_audio_list.append(m_c)
                except Exception as e: print(f"[MÜZİK HATA]: {e}")

        log("Sistem Miksajı Başlatıyor...")
        final_composite_audio = CompositeAudioClip(final_audio_list)
        final_composite_audio.fps = 44100 
            
        final_video = CompositeVideoClip([v_kesit] + final_yazilar)
        if hasattr(final_video, 'with_audio'): final_video = final_video.with_audio(final_composite_audio).with_duration(tot_sure)
        else: final_video = final_video.set_audio(final_composite_audio).set_duration(tot_sure)
        
        log("Sistem Miksajı Başlatıyor...")
        my_logger = ViraiRenderLogger(log, prog)
        gecici_ses_yolu = os.path.join(TEMP_DIR, f"virai_temp_audio_{random.randint(1000,9999)}.m4a")
        final_video.write_videofile(cikis_adi, fps=30, codec="libx264", audio_codec="aac", audio_fps=44100, bitrate="5000k", preset="medium", temp_audiofile=gecici_ses_yolu, logger=my_logger)
        return True, ""
        
    except Exception as e:
        hata_detayi = traceback.format_exc()
        print(f"--- DETAYLI HATA RAPORU ---\n{hata_detayi}")
        return False, str(e)
        
    finally:
        for f in temp_files:
            try: os.remove(f)
            except: pass
        for r_file in [TEMP_VIDEO_DOSYASI, TEMP_MUZIK_DOSYASI, POP_SES_DOSYASI, TEMP_TEST_SESI]:
            try: os.remove(r_file)
            except: pass


# ==========================================
# ASIL PROGRAM (WIZARD ARAYÜZÜ)
# ==========================================
class UltimateApp:
    
    def __init__(self, root, username, plan_type, credits, sub_end):
        self.root = root
        self.username = username
        self.plan_type = int(plan_type) 
        self.credits = int(credits) 
        self.is_generating_text = False
        self.current_step = 1 
        
        self.local_music_path = "" 
        self.local_logo_path = "" 
        self.local_video_path = ""
        self.presets = self.load_presets_from_file()
        self.cikti_klasoru = os.path.join(os.path.expanduser("~"), "Desktop", "VIRAI_Videolar")
        if self.plan_type == 0: durum_metni = "ÜCRETSİZ"
        elif self.plan_type == 1: durum_metni = "👑 PRO"
        else: durum_metni = "💎 STUDIO"

        bitis_metni = f" - Bitiş: {sub_end}" if sub_end else ""
        
        self.root.title(f"VIRAI STUDIO (BETA) - Kullanıcı: {username} [{durum_metni}{bitis_metni}]")
        self.root.geometry("1300x850") 
        self.root.resizable(False, False) 
        self.root.configure(fg_color=APP_BG) 

        edge_voices = ["Gerçekçi/Kalın Erkek (Edge)", "Standart Erkek (Edge)", "Standart Kadın (Edge)", "Enerjik Kadın (Edge)"]
        eleven_voices = list(ELEVENLABS_VOICES.keys()) + ["🔥 Kendi Ses ID'ni Kullan (ElevenLabs)"]
        self.voice_opts = edge_voices + eleven_voices
        self.batch_opts = ["1 Video", "3 Video", "5 Video", "10 Video", "15 Video"]
        self.duration_opts = ["15 Saniye (Shorts)", "30 Saniye (Reels)", "60 Saniye (TikTok)", "Sınırsız (Max)"]
        self.music_opts = ["Korku / Gerilim", "Hüzünlü / Dram", "Hareketli / Viral", "Rastgele", "Yerel Dosya Seç...", "Yok"]

        # --- ÜST BAŞLIK ---
        top_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        top_frame.pack(fill="x", pady=(15, 0))
        
        title_frame = ctk.CTkFrame(top_frame, fg_color="transparent")
        title_frame.pack(side="left", padx=20)
        title_lbl = ctk.CTkLabel(title_frame, text=f"VIRAI STUDIO (BETA)", font=ctk.CTkFont(size=26, weight="bold"), text_color=ACCENT_COLOR)
        title_lbl.pack(side="left")
        
        help_btn = ctk.CTkButton(title_frame, text="❓ Nasıl Kullanılır?", width=120, height=30, fg_color="#334155", hover_color="#475569", command=self.open_tutorial_window)
        help_btn.pack(side="left", padx=(20,0))

        self.credit_lbl = ctk.CTkLabel(top_frame, text=f"🪙 Günlük Kredi: {self.credits}", font=ctk.CTkFont(size=18, weight="bold"), text_color=GOLD_COLOR)
        self.credit_lbl.pack(side="right", padx=20)

        if self.plan_type < 2:
            buy_btn = ctk.CTkButton(top_frame, text="💎 Abonelikler", fg_color=DANGER_COLOR, hover_color="#B91C1C", text_color="white", corner_radius=10, command=self.open_subscriptions)
            buy_btn.pack(side="right", padx=10)

        self.main_container = ctk.CTkFrame(self.root, fg_color="transparent")
        self.main_container.pack(fill="both", expand=True, padx=20, pady=10)
        
        self.left_col = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.left_col.pack(side="left", fill="both", expand=True, padx=(0, 10))
        
        self.right_col = ctk.CTkFrame(self.main_container, fg_color="transparent", width=420)
        self.right_col.pack(side="right", fill="y", expand=False)
        self.right_col.pack_propagate(False)

        # ========================================================
        # SOL BÖLÜM: WIZARD (AŞAMA AŞAMA EKRANLAR)
        # ========================================================
        self.wizard_header = ctk.CTkLabel(self.left_col, text="Aşama 1: İçerik ve Senaryo Üretimi (Beta)", font=ctk.CTkFont(size=20, weight="bold"), text_color="white")
        self.wizard_header.pack(anchor="w", pady=(0, 10))

        # --- AŞAMA 1: İÇERİK OLUŞTURMA ---
        self.step1_frame = ctk.CTkFrame(self.left_col, fg_color="transparent")
        self.app_mode_var = ctk.StringVar(value="Yapay Zeka (Klasik)")

        self.input_card = ctk.CTkFrame(self.step1_frame, corner_radius=16, fg_color=GLASS_BG, border_width=1, border_color=GLASS_BORDER)
        self.input_card.pack(fill="x", pady=5)
        
        self.classic_frame = ctk.CTkFrame(self.input_card, fg_color="transparent")
        self.classic_frame.pack(fill="x", padx=15, pady=10)
        self.content_type_combo = ctk.CTkComboBox(self.classic_frame, values=["Yapay Zeka (Özel Prompt)", "Hikaye (Reddit)", "Bilgi (Wikipedia)", "Tavsiye (Pratikler)"], width=200, fg_color="#0F172A", border_color=GLASS_BORDER, text_color=TEXT_COLOR)
        self.content_type_combo.set("Yapay Zeka (Özel Prompt)")
        self.content_type_combo.pack(side="left", padx=(0,10))
        
        # Konu/Prompt Entry
        self.topic_entry = ctk.CTkEntry(self.classic_frame, placeholder_text="Örn: Uzaylılar hakkında ilginç bilgi...", height=32, fg_color="#0F172A", border_color=GLASS_BORDER, text_color=TEXT_COLOR)
        self.topic_entry.pack(side="left", fill="x", expand=True)

        opts_f = ctk.CTkFrame(self.input_card, fg_color="transparent")
        opts_f.pack(fill="x", padx=15, pady=10)
        self.lang_combo = ctk.CTkComboBox(opts_f, values=["TR Orijinal (Yerli)", "TR Çeviri (Yabancı)", "EN Orijinal (Yabancı)"], width=170, fg_color="#0F172A", border_color=GLASS_BORDER, text_color=TEXT_COLOR)
        self.lang_combo.set("TR Orijinal (Yerli)")
        self.lang_combo.pack(side="left", padx=(0,5))
        self.duration_combo = ctk.CTkComboBox(opts_f, values=self.duration_opts, width=150, command=self.on_duration_change, fg_color="#0F172A", border_color=GLASS_BORDER, text_color=TEXT_COLOR)
        self.duration_combo.set("15 Saniye (Shorts)")
        self.duration_combo.pack(side="left", padx=5)
        self.voice_combo = ctk.CTkComboBox(opts_f, values=self.voice_opts, width=200, command=self.on_voice_change, fg_color="#0F172A", border_color=GLASS_BORDER, text_color=TEXT_COLOR)
        self.voice_combo.set(self.voice_opts[0])
        self.voice_combo.pack(side="left", padx=5)
        
        self.custom_voice_entry = ctk.CTkEntry(self.input_card, placeholder_text="ElevenLabs Ses ID'sini buraya yapıştırın...", fg_color="#0F172A", border_color=GLASS_BORDER, text_color=TEXT_COLOR)
        
        self.find_btn = ctk.CTkButton(self.input_card, text="✨ SENARYOYU ÜRET (BETA)", command=self.start_story_search, fg_color=GOLD_COLOR, hover_color="#D97706", text_color="black", height=40, font=ctk.CTkFont(weight="bold"))
        self.find_btn.pack(fill="x", padx=15, pady=(5,15))

        self.text_area = ctk.CTkTextbox(self.step1_frame, wrap="word", border_width=1, border_color=GLASS_BORDER, fg_color="#0F172A", text_color=TEXT_COLOR)
        self.text_area.pack(fill="both", expand=True, pady=10)
        self.text_area.insert("1.0", "Senaryonuz burada görünecektir. Üretildikten sonra dilediğiniz gibi düzenleyebilirsiniz...")

      # --- AŞAMA 2: MEDYA SEÇİMİ (ARKA PLAN) ---
        self.step2_frame = ctk.CTkFrame(self.left_col, fg_color="transparent")
        
        bg_card = ctk.CTkFrame(self.step2_frame, corner_radius=16, fg_color=GLASS_BG, border_width=1, border_color=GLASS_BORDER)
        bg_card.pack(fill="x", pady=10)
        ctk.CTkLabel(bg_card, text="🎬 Arka Plan Videosu", font=ctk.CTkFont(size=14, weight="bold"), text_color=TEXT_COLOR).pack(anchor="w", padx=15, pady=(15, 5))
        
        self.video_source_var = ctk.StringVar(value="search")
        radio_f = ctk.CTkFrame(bg_card, fg_color="transparent")
        radio_f.pack(fill="x", padx=15, pady=5)
        
        ctk.CTkRadioButton(radio_f, text="Oto. Arama", variable=self.video_source_var, value="search", command=self.toggle_video_inputs, text_color=TEXT_COLOR).pack(side="left", padx=(0, 10))
        # ctk.CTkRadioButton(radio_f, text="Yapay Zeka (Otopilot)", variable=self.video_source_var, value="ai_video", command=self.toggle_video_inputs, text_color=GOLD_COLOR).pack(side="left", padx=(0, 10))
        ctk.CTkRadioButton(radio_f, text="YouTube Link", variable=self.video_source_var, value="link", command=self.toggle_video_inputs, text_color=TEXT_COLOR).pack(side="left", padx=(0, 10))
        ctk.CTkRadioButton(radio_f, text="Kendi Videom", variable=self.video_source_var, value="local", command=self.toggle_video_inputs, text_color=TEXT_COLOR).pack(side="left")

        # Yeni Arama Arayüzü Elemanları
        search_wrap = ctk.CTkFrame(bg_card, fg_color="transparent")
        search_wrap.pack(fill="x", padx=15, pady=(10, 5))
        
        self.search_entry = ctk.CTkEntry(search_wrap, placeholder_text="Arama kelimesi (Boşsa konuyu arar)", height=40, fg_color="#0F172A", border_color=GLASS_BORDER, text_color=TEXT_COLOR)
        self.search_entry.pack(side="left", fill="x", expand=True)
        
        self.search_yt_btn = ctk.CTkButton(search_wrap, text="🔍 Bul", width=60, height=40, fg_color=ACCENT_COLOR, hover_color=HOVER_COLOR, command=self.perform_visual_search)
        self.search_yt_btn.pack(side="left", padx=(10, 0))

        self.yt_results_frame = ctk.CTkScrollableFrame(bg_card, height=120, fg_color="#0F172A", border_color=GLASS_BORDER, border_width=1)
        self.selected_yt_url_var = ctk.StringVar(value="")

        self.link_entry = ctk.CTkEntry(bg_card, placeholder_text="https://www.youtube.com/watch...", height=40, fg_color="#0F172A", border_color=GLASS_BORDER, text_color=TEXT_COLOR)
        self.local_vid_btn = ctk.CTkButton(bg_card, text="📁 Bilgisayardan Video Seç", fg_color=ACCENT_COLOR, hover_color=HOVER_COLOR, height=40, text_color="white", corner_radius=10, command=self.select_local_video)
        self.local_vid_lbl = ctk.CTkLabel(bg_card, text="Video seçilmedi.", text_color="#64748B", font=ctk.CTkFont(size=11, slant="italic")) 
        self.search_entry.pack(fill="x", padx=15, pady=(10, 20)) 

        music_card = ctk.CTkFrame(self.step2_frame, corner_radius=16, fg_color=GLASS_BG, border_width=1, border_color=GLASS_BORDER)
        music_card.pack(fill="x", pady=10)
        ctk.CTkLabel(music_card, text="🎵 Arka Plan Müziği", font=ctk.CTkFont(size=14, weight="bold"), text_color=TEXT_COLOR).pack(anchor="w", padx=15, pady=(15, 5))
        m_inner = ctk.CTkFrame(music_card, fg_color="transparent")
        m_inner.pack(fill="x", padx=15, pady=(5,20))
        self.music_combo = ctk.CTkComboBox(m_inner, values=self.music_opts, width=200, command=self.on_music_combo_change, fg_color="#0F172A", border_color=GLASS_BORDER, text_color=TEXT_COLOR)
        self.music_combo.set("Korku / Gerilim")
        self.music_combo.pack(side="left", padx=(0,15))
        self.local_music_lbl = ctk.CTkLabel(m_inner, text="", text_color="#A9A9A9", font=ctk.CTkFont(size=11, slant="italic"))
        self.local_music_lbl.pack(side="left", fill="x", expand=True)

        # --- AŞAMA 3: ÖZET VE ÜRETİM ---
        self.step3_frame = ctk.CTkFrame(self.left_col, fg_color="transparent")
        
        sum_card = ctk.CTkFrame(self.step3_frame, corner_radius=16, fg_color=GLASS_BG, border_width=1, border_color=GLASS_BORDER)
        sum_card.pack(fill="x", pady=10)
        ctk.CTkLabel(sum_card, text="📊 Üretim Özeti", font=ctk.CTkFont(size=16, weight="bold"), text_color=TEXT_COLOR).pack(anchor="w", padx=15, pady=(15, 5))
        self.summary_lbl = ctk.CTkLabel(sum_card, text="Ayarlar yükleniyor...", text_color="#94A3B8", justify="left")
        self.summary_lbl.pack(anchor="w", padx=15, pady=(0,15))

        meta_card = ctk.CTkFrame(self.step3_frame, corner_radius=16, fg_color=GLASS_BG, border_width=1, border_color=GLASS_BORDER)
        meta_card.pack(fill="both", expand=True, pady=10)
        ctk.CTkLabel(meta_card, text="🔥 YouTube/TikTok SEO Etiketleri", font=ctk.CTkFont(size=14, weight="bold"), text_color=GOLD_COLOR).pack(anchor="w", padx=15, pady=(10, 5))
        self.meta_area = ctk.CTkTextbox(meta_card, wrap="word", border_width=1, border_color=GLASS_BORDER, fg_color="#0F172A", text_color=TEXT_COLOR)
        self.meta_area.pack(fill="both", expand=True, padx=15, pady=(0, 15))
        
        render_box = ctk.CTkFrame(self.step3_frame, fg_color="transparent")
        render_box.pack(fill="x", pady=10)
        
        bf = ctk.CTkFrame(render_box, fg_color="transparent")
        bf.pack(fill="x", pady=5)
        ctk.CTkLabel(bf, text="🏭 Kaç Adet Üretilecek? (Toplu Üretim):", text_color=TEXT_COLOR).pack(side="left")
        self.batch_combo = ctk.CTkComboBox(bf, values=self.batch_opts, width=100, command=self.on_batch_change, fg_color="#0F172A", border_color=GLASS_BORDER, text_color=TEXT_COLOR)
        self.batch_combo.set("1 Video")
        self.batch_combo.pack(side="left", padx=15)

        self.status_label = ctk.CTkLabel(render_box, text="Hazır - Sistem Bekliyor...", text_color="#94A3B8", font=ctk.CTkFont(family="Courier", size=13))
        self.status_label.pack(pady=(5, 5))
        self.progress = ctk.CTkProgressBar(render_box, mode="determinate", height=12, progress_color=ACCENT_COLOR)
        self.progress.pack(fill="x", pady=(0, 15))
        self.progress.set(0.0)
        
        btn_frame = ctk.CTkFrame(render_box, fg_color="transparent")
        btn_frame.pack(fill="x")
        self.generate_btn = ctk.CTkButton(btn_frame, text="🎬 VİDEOYU OLUŞTUR (BETA)", command=self.start_batch_generation, fg_color="#059669", hover_color="#047857", text_color="white", font=ctk.CTkFont(size=18, weight="bold"), height=50, corner_radius=12)
        self.generate_btn.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.reset_btn = ctk.CTkButton(btn_frame, text="🔄 Her Şeyi Sıfırla", command=self.reset_to_start_direct, fg_color="#334155", hover_color="#475569", text_color="white", font=ctk.CTkFont(size=14, weight="bold"), height=50, width=140, corner_radius=12)
        self.reset_btn.pack(side="right")

        # --- SİHİRBAZ YÖNLENDİRME BUTONLARI ---
        self.nav_frame = ctk.CTkFrame(self.left_col, fg_color="transparent")
        self.nav_frame.pack(side="bottom", fill="x", pady=5)
        self.btn_prev = ctk.CTkButton(self.nav_frame, text="◀ Geri Dön", fg_color="#334155", hover_color="#475569", width=120, height=40, command=self.go_prev)
        self.btn_prev.pack(side="left")
        self.btn_next = ctk.CTkButton(self.nav_frame, text="İleri Devam Et ▶", fg_color=ACCENT_COLOR, hover_color=HOVER_COLOR, width=150, height=40, font=ctk.CTkFont(weight="bold"), command=self.go_next)
        self.btn_next.pack(side="right")


        # ========================================================
        # SAĞ BÖLÜM: YÖNETMEN MASASI (SÜREKLİ AKTİF)
        # ========================================================
        dir_frame = ctk.CTkFrame(self.right_col, corner_radius=16, fg_color=GLASS_BG, border_width=1, border_color=GLASS_BORDER)
        dir_frame.pack(fill="both", expand=True)
        
        preset_f = ctk.CTkFrame(dir_frame, fg_color="transparent")
        preset_f.pack(fill="x", padx=10, pady=(15,5))
        ctk.CTkLabel(preset_f, text="💾 Hazır Ayarlar (Presets)", font=ctk.CTkFont(size=14, weight="bold"), text_color=GOLD_COLOR).pack(anchor="w", pady=(0,5))
        
        row_p1 = ctk.CTkFrame(preset_f, fg_color="transparent")
        row_p1.pack(fill="x", pady=2)
        self.preset_combo = ctk.CTkComboBox(row_p1, values=list(self.presets.keys()) if self.presets else ["Varsayılan"], command=self.apply_preset, fg_color="#0F172A", border_color=GLASS_BORDER, text_color=TEXT_COLOR)
        if not self.presets: self.preset_combo.set("Varsayılan")
        else: self.preset_combo.set(list(self.presets.keys())[0])
        self.preset_combo.pack(side="left", fill="x", expand=True, padx=(0,5))
        ctk.CTkButton(row_p1, text="Sil", width=50, fg_color=DANGER_COLOR, hover_color="#B91C1C", command=self.delete_preset).pack(side="right")

        row_p2 = ctk.CTkFrame(preset_f, fg_color="transparent")
        row_p2.pack(fill="x", pady=5)
        ctk.CTkButton(row_p2, text="Yeni Ayar Kaydet", fg_color="#059669", hover_color="#047857", command=self.save_preset).pack(fill="x")

        ctk.CTkLabel(dir_frame, text="🎛️ Yönetmen Masası", font=ctk.CTkFont(size=18, weight="bold"), text_color=TEXT_COLOR).pack(pady=(15, 5))
        ctk.CTkLabel(dir_frame, text="(Her Aşamada Düzenlenebilir)", font=ctk.CTkFont(size=11), text_color="#94A3B8").pack(pady=(0, 15))

        # 1. Ses Mikseri
        mix_f = ctk.CTkFrame(dir_frame, fg_color="transparent")
        mix_f.pack(fill="x", padx=10, pady=5)
        ctk.CTkLabel(mix_f, text="🔊 Ses Düzeyleri", font=ctk.CTkFont(weight="bold"), text_color=ACCENT_COLOR).pack(anchor="w", pady=(0,5))
        self.vol_voice_var = ctk.DoubleVar(value=1.0)
        self.vol_music_var = ctk.DoubleVar(value=0.35)
        self.vol_sfx_var = ctk.DoubleVar(value=0.50)
        self._create_compact_slider(mix_f, "🗣️ Anlatıcı", self.vol_voice_var, 0.0, 2.0, "voice")
        self._create_compact_slider(mix_f, "🎵 Müzik", self.vol_music_var, 0.0, 1.0, "music")
        self._create_compact_slider(mix_f, "💥 Efekt", self.vol_sfx_var, 0.0, 1.0, "sfx")

        # 2. Metin Stili
        txt_f = ctk.CTkFrame(dir_frame, fg_color="transparent")
        txt_f.pack(fill="x", padx=10, pady=10)
        ctk.CTkLabel(txt_f, text="🎨 Altyazı Stili", font=ctk.CTkFont(weight="bold"), text_color=ACCENT_COLOR).pack(anchor="w", pady=(0,5))
        self.subtitle_combo = ctk.CTkComboBox(txt_f, values=["Dinamik (1 Kelime - Hızlı)", "Dinamik (2 Kelime - TikTok)", "Dinamik (3 Kelime - Akıcı)", "Klasik (Tam Cümle)"], fg_color="#0F172A", border_color=GLASS_BORDER, text_color=TEXT_COLOR)
        self.subtitle_combo.set("Klasik (Tam Cümle)")
        self.subtitle_combo.pack(fill="x", pady=2)
        
        row1 = ctk.CTkFrame(txt_f, fg_color="transparent")
        row1.pack(fill="x", pady=5)
        ctk.CTkLabel(row1, text="Renk:", text_color=TEXT_COLOR).pack(side="left")
        self.text_color_combo = ctk.CTkComboBox(row1, values=["Sarı", "Beyaz", "Siyah", "Kırmızı", "Yeşil", "Mavi"], width=80, fg_color="#0F172A", border_color=GLASS_BORDER, text_color=TEXT_COLOR)
        self.text_color_combo.set("Sarı")
        self.text_color_combo.pack(side="left", padx=5)
        ctk.CTkLabel(row1, text="Arkaplan:", text_color=TEXT_COLOR).pack(side="left", padx=(10,0))
        self.text_bg_combo = ctk.CTkComboBox(row1, values=["Yok (Şeffaf)", "Siyah", "Beyaz", "Kırmızı", "Mavi", "Yeşil"], width=100, fg_color="#0F172A", border_color=GLASS_BORDER, text_color=TEXT_COLOR)
        self.text_bg_combo.set("Yok (Şeffaf)")
        self.text_bg_combo.pack(side="left", padx=5)

        # 3. Görsel Efektler
        vfx_f = ctk.CTkFrame(dir_frame, fg_color="transparent")
        vfx_f.pack(fill="x", padx=10, pady=10)
        ctk.CTkLabel(vfx_f, text="🎬 Görsel Efektler", font=ctk.CTkFont(weight="bold"), text_color=ACCENT_COLOR).pack(anchor="w", pady=(0,5))
        self.b_roll_combo = ctk.CTkComboBox(vfx_f, values=["Sıçramalı (Jump-Cut)", "Düz Akış"], fg_color="#0F172A", border_color=GLASS_BORDER, text_color=TEXT_COLOR)
        self.b_roll_combo.set("Düz Akış")
        self.b_roll_combo.pack(fill="x", pady=2)
        
        row2 = ctk.CTkFrame(vfx_f, fg_color="transparent")
        row2.pack(fill="x", pady=5)
        ctk.CTkLabel(row2, text="Video Filtre:", text_color=TEXT_COLOR).pack(side="left")
        self.vfx_combo = ctk.CTkComboBox(row2, values=["Yok", "Siyah & Beyaz", "Yüksek Kontrast", "Sinematik Vignette"], command=self.on_vfx_change, fg_color="#0F172A", border_color=GLASS_BORDER, text_color=TEXT_COLOR)
        self.vfx_combo.set("Yok")
        self.vfx_combo.pack(side="right", fill="x", expand=True, padx=(10,0))

        # 4. Pro Özellikler (Toggles)
        pro_f = ctk.CTkFrame(dir_frame, fg_color="transparent")
        pro_f.pack(fill="x", padx=10, pady=10)
        self.sfx_check = ctk.CTkCheckBox(pro_f, text="Pop (Balon) Sesi", onvalue=True, offvalue=False, text_color=TEXT_COLOR)
        self.sfx_check.select()
        self.sfx_check.pack(anchor="w", pady=2)
        self.prog_bar_check = ctk.CTkCheckBox(pro_f, text="⏳ İlerleme Çubuğu", onvalue=True, offvalue=False, text_color=TEXT_COLOR, command=self.on_pro_feature_click)
        self.prog_bar_check.pack(anchor="w", pady=2)
        self.flash_check = ctk.CTkCheckBox(pro_f, text="⚡ Flaş Geçiş", onvalue=True, offvalue=False, text_color=TEXT_COLOR, command=self.on_pro_feature_click)
        self.flash_check.pack(anchor="w", pady=2)
        self.zoom_check = ctk.CTkCheckBox(pro_f, text="🔍 Sinematik Zoom", onvalue=True, offvalue=False, text_color=TEXT_COLOR, command=self.on_pro_feature_click)
        self.zoom_check.pack(anchor="w", pady=2)

        # 5. Filigran
        wm_frame = ctk.CTkFrame(dir_frame, fg_color="transparent")
        wm_frame.pack(fill="x", padx=10, pady=(10, 0))
        self.wm_entry = ctk.CTkEntry(wm_frame, placeholder_text="@KanalAdi (Opsiyonel)", fg_color="#0F172A", border_color=GLASS_BORDER, text_color=TEXT_COLOR)
        self.wm_entry.pack(side="left", fill="x", expand=True, padx=(0,5))
        self.logo_btn = ctk.CTkButton(wm_frame, text="🖼️ Logo", width=60, fg_color="#334155", hover_color="#475569", corner_radius=10, command=self.select_logo)
        self.logo_btn.pack(side="right")
        
        if self.plan_type == 0:
            self.wm_entry.insert(0, "@VIRAI")
            self.wm_entry.bind("<Button-1>", self.on_wm_focus)
            self.wm_entry.bind("<FocusIn>", self.on_wm_focus)

        self.update_wizard_ui()
        self.toggle_video_inputs()

    def load_presets_from_file(self):
        if os.path.exists(PRESETS_FILE):
            try:
                with open(PRESETS_FILE, 'r') as f: return json.load(f)
            except: return {}
        return {}
    def perform_visual_search(self):
        kelime = self.search_entry.get().strip() or self.topic_entry.get().strip()
        if not kelime:
            messagebox.showwarning("Uyarı", "Lütfen bir arama kelimesi girin veya 1. Aşamada konu belirleyin.")
            return

        self.search_yt_btn.configure(state="disabled", text="⏳")
        for widget in self.yt_results_frame.winfo_children(): 
            widget.destroy()
        
        # UI Refresh Hatasını Önlemek İçin Çerçeveyi Zorla Güncelle
        self.yt_results_frame.update_idletasks()
        
        def _search():
            sonuclar = hizli_youtube_arama(kelime, limit=5) # 5 sonuç UI için idealdir
            
            # Thumbnail'leri thread içinde arayüzü dondurmadan indiriyoruz
            import requests
            from io import BytesIO
            from PIL import Image
            
            for video in sonuclar:
                vid_id = video.get('id') or video.get('url')
                thumb_url = f"https://i.ytimg.com/vi/{vid_id}/mqdefault.jpg" if vid_id else None
                video['ctk_image'] = None
                
                if thumb_url:
                    try:
                        resp = requests.get(thumb_url, timeout=3)
                        if resp.status_code == 200:
                            img = Image.open(BytesIO(resp.content))
                            # 16:9 oranında çok şık bir kapak fotoğrafı boyutu
                            video['ctk_image'] = ctk.CTkImage(light_image=img, dark_image=img, size=(120, 67))
                    except:
                        pass
                        
            # Sonuçları ekrana basmak için ana thread'e dön
            self.root.after(0, lambda: self._update_visual_results(sonuclar))
            
        threading.Thread(target=_search, daemon=True).start()

    def _update_visual_results(self, sonuclar):
        self.search_yt_btn.configure(state="normal", text="🔍 Bul")
        
        if not sonuclar:
            ctk.CTkLabel(self.yt_results_frame, text="Sonuç bulunamadı.", text_color=DANGER_COLOR).pack(pady=10)
            return
            
        # Olası eski seçim buglarını engellemek için string variable'ı sıfırla
        self.selected_yt_url_var.set("") 
            
        for idx, video in enumerate(sonuclar):
            sure = video.get('duration')
            sure_metni = time.strftime('%M:%S', time.gmtime(sure)) if sure else "Bilinmiyor"
            baslik = video.get('title', 'İsimsiz Video')
            
            # yt-dlp flat extract url'yi bazen sadece ID olarak verir, bunu kesin bir URL'ye çevirelim
            vid_id = video.get('id') or video.get('url', '')
            tam_url = f"https://www.youtube.com/watch?v={vid_id}" if not str(vid_id).startswith("http") else vid_id
            
            # Başlık ve Süre metni (Taşmaları önlemek için alt satıra geçirdik)
            gosterim_metni = f"{baslik[:45]}...\n⏱️ Süre: {sure_metni}" if len(baslik) > 45 else f"{baslik}\n⏱️ Süre: {sure_metni}"
            
            # Thumbnail ve Butonu yan yana tutacak kapsayıcı bir çerçeve (Çok daha şık durur)
            item_frame = ctk.CTkFrame(self.yt_results_frame, fg_color="#1E293B", corner_radius=8)
            item_frame.pack(fill="x", pady=5, padx=5)
            
            # Kapak fotoğrafı varsa sol tarafa ekle
            if video.get('ctk_image'):
                img_lbl = ctk.CTkLabel(item_frame, text="", image=video['ctk_image'])
                img_lbl.pack(side="left", padx=(5, 10), pady=5)
                
            rb = ctk.CTkRadioButton(
                item_frame, 
                text=gosterim_metni, 
                variable=self.selected_yt_url_var, 
                value=tam_url, 
                text_color=TEXT_COLOR,
                font=ctk.CTkFont(size=12, weight="bold")
            )
            rb.pack(side="left", fill="x", expand=True, pady=5)
            
            # İlk sonucu hem arayüzde seçilmiş göster hem de arka plandaki değişkene KAYDET
            if idx == 0: 
                rb.select()
                self.selected_yt_url_var.set(tam_url)
                
        # ScrollableFrame'in Scroll'unu başa alarak "İleri-Geri" yapma bug'ını yok et
        try:
            self.yt_results_frame._parent_canvas.yview_moveto(0)
        except:
            pass
    def save_preset(self):
        name = simpledialog.askstring("Preset Kaydet", "Bu ayarlar için bir isim girin:")
        if not name: return
        current_settings = {
            "voice": self.voice_combo.get(), "custom_voice_id": self.custom_voice_entry.get(),
            "vol_voice": self.vol_voice_var.get(), "vol_music": self.vol_music_var.get(), "vol_sfx": self.vol_sfx_var.get(),
            "subtitle_style": self.subtitle_combo.get(), "text_color": self.text_color_combo.get(), "text_bg": self.text_bg_combo.get(),
            "b_roll": self.b_roll_combo.get(), "vfx": self.vfx_combo.get(),
            "sfx": self.sfx_check.get(), "prog_bar": self.prog_bar_check.get(), "flash": self.flash_check.get(), "zoom": self.zoom_check.get(),
            "wm": self.wm_entry.get()
        }
        self.presets[name] = current_settings
        with open(PRESETS_FILE, 'w') as f: json.dump(self.presets, f)
        self.preset_combo.configure(values=list(self.presets.keys()))
        self.preset_combo.set(name)
        messagebox.showinfo("Başarılı", f"'{name}' ayarı kaydedildi!")

    def apply_preset(self, choice):
        if choice not in self.presets: return
        s = self.presets[choice]
        try:
            self.voice_combo.set(s["voice"])
            self.custom_voice_entry.delete(0, "end")
            self.custom_voice_entry.insert(0, s["custom_voice_id"])
            self.on_voice_change(s["voice"])
            self.vol_voice_var.set(s["vol_voice"])
            self.vol_music_var.set(s["vol_music"])
            self.vol_sfx_var.set(s["vol_sfx"])
            self.subtitle_combo.set(s["subtitle_style"])
            self.text_color_combo.set(s["text_color"])
            self.text_bg_combo.set(s["text_bg"])
            self.b_roll_combo.set(s["b_roll"])
            self.vfx_combo.set(s["vfx"])
            if s["sfx"]: self.sfx_check.select()
            else: self.sfx_check.deselect()
            if s["prog_bar"]: self.prog_bar_check.select()
            else: self.prog_bar_check.deselect()
            if s["flash"]: self.flash_check.select()
            else: self.flash_check.deselect()
            if s["zoom"]: self.zoom_check.select()
            else: self.zoom_check.deselect()
            if self.plan_type > 0:
                self.wm_entry.delete(0, "end")
                self.wm_entry.insert(0, s["wm"])
        except Exception as e: print(f"Preset uygulama hatası: {e}")

    def delete_preset(self):
        choice = self.preset_combo.get()
        if choice in self.presets and messagebox.askyesno("Onay", f"'{choice}' ayarını silmek istediğine emin misin?"):
            del self.presets[choice]
            with open(PRESETS_FILE, 'w') as f: json.dump(self.presets, f)
            self.preset_combo.configure(values=list(self.presets.keys()) if self.presets else ["Varsayılan"])
            if self.presets: self.preset_combo.set(list(self.presets.keys())[0])
            else: self.preset_combo.set("Varsayılan")

    def open_tutorial_window(self):
        tut_win = ctk.CTkToplevel(self.root)
        tut_win.title("VIRAI Hızlı Başlangıç Rehberi")
        tut_win.geometry("600x700")
        tut_win.configure(fg_color=APP_BG)
        ctk.CTkLabel(tut_win, text="🚀 VIRAI STUDIO Nasıl Kullanılır?", font=ctk.CTkFont(size=22, weight="bold"), text_color=ACCENT_COLOR).pack(pady=20)
        scroll_f = ctk.CTkScrollableFrame(tut_win, fg_color="transparent")
        scroll_f.pack(fill="both", expand=True, padx=20, pady=10)
        steps = [
            ("Aşama 1: Senaryo Üretimi", "Burada yapay zekaya bir konu verirsiniz (örn: 'Uzaylılar'). O da size viral olacak, dikkat çekici (Hook'lu) bir video metni yazar. Üretilen metni istediğiniz gibi düzenleyebilirsiniz."),
            ("Aşama 2: Medya Seçimi", "Videonuzun arka planında ne oynayacağını seçersiniz. 'Oto. Arama' derseniz yapay zeka senaryoya uygun videoyu YouTube'dan bulur. Boş bırakırsanız ilk baştaki konunuzu arar."),
            ("Aşama 3: Üretim", "Son kontrolleri yapıp 'Videoyu Oluştur' butonuna basarsınız. Program sizin için sesi, görüntüyü ve altyazıları birleştirip MP4 dosyasını hazırlar."),
            ("🎛️ Yönetmen Masası (Sağ Panel)", "Burası sizin kontrol merkezinizdir. İstediğiniz aşamadayken sağ taraftan ses düzeylerini, altyazı renklerini, video filtrelerini ve efektleri anlık olarak değiştirebilirsiniz. Yaptığınız ayarları 'Hazır Ayarlar' kısmından kaydedebilirsiniz.")
        ]
        for title, desc in steps:
            f = ctk.CTkFrame(scroll_f, fg_color=GLASS_BG, border_color=GLASS_BORDER, border_width=1)
            f.pack(fill="x", pady=10)
            ctk.CTkLabel(f, text=title, font=ctk.CTkFont(size=16, weight="bold"), text_color=GOLD_COLOR).pack(anchor="w", padx=15, pady=(10,5))
            ctk.CTkLabel(f, text=desc, wraplength=500, text_color=TEXT_COLOR, justify="left").pack(anchor="w", padx=15, pady=(0,15))
        ctk.CTkButton(tut_win, text="Anladım, Başlayalım! 👍", fg_color=ACCENT_COLOR, height=40, command=tut_win.destroy).pack(pady=20)

    def reset_to_start_direct(self):
        self.current_step = 1
        self.text_area.delete("1.0", "end")
        self.text_area.insert("1.0", "Senaryonuz burada görünecektir. Üretildikten sonra dilediğiniz gibi düzenleyebilirsiniz...")
        self.topic_entry.delete(0, "end")
        self.meta_area.delete("1.0", "end")
        self.search_entry.delete(0, "end")
        self.progress.set(0.0)
        self.status_label.configure(text="Hazır - Sistem Bekliyor...", text_color="#94A3B8")
        self.update_wizard_ui()
        self.toggle_video_inputs()
        
    def reset_to_start(self, pub_win):
        pub_win.destroy()
        self.reset_to_start_direct()

    def go_next(self):
        if self.current_step < 3:
            self.current_step += 1
            self.update_wizard_ui()
            self.toggle_video_inputs()

    def go_prev(self):
        if self.current_step > 1:
            self.current_step -= 1
            self.update_wizard_ui()
            self.toggle_video_inputs()

    def update_wizard_ui(self):
        self.step1_frame.pack_forget()
        self.step2_frame.pack_forget()
        self.step3_frame.pack_forget()

        if self.current_step == 1:
            self.wizard_header.configure(text="Aşama 1: İçerik ve Senaryo Üretimi (Beta)")
            self.step1_frame.pack(fill="both", expand=True)
            self.btn_prev.configure(state="disabled", fg_color="transparent", text_color=APP_BG)
            self.btn_next.configure(text="İleri (Medya Seçimi) ▶", state="normal", fg_color=ACCENT_COLOR, text_color="white")
        elif self.current_step == 2:
            self.wizard_header.configure(text="Aşama 2: Görsel ve Müzik Seçimi")
            self.step2_frame.pack(fill="both", expand=True)
            self.btn_prev.configure(state="normal", fg_color="#334155", text_color="white")
            self.btn_next.configure(text="İleri (Üretim Aşaması) ▶", state="normal", fg_color=ACCENT_COLOR, text_color="white")
        elif self.current_step == 3:
            self.wizard_header.configure(text="Aşama 3: Son Kontrol ve Video Üretimi (Beta)")
            self.update_step3_summary()
            self.generate_metadata_thread() 
            self.step3_frame.pack(fill="both", expand=True)
            self.btn_prev.configure(state="normal", fg_color="#334155", text_color="white")
            self.btn_next.configure(state="disabled", fg_color="transparent", text_color=APP_BG)

    def generate_metadata_thread(self):
        metin = self.text_area.get("1.0", "end-1c").strip()
        if not metin or "Senaryonuz burada" in metin or "VIRAI Nöral" in metin or "❌" in metin:
            self.meta_area.delete("1.0", "end")
            self.meta_area.insert("1.0", "SEO Etiketlerinin üretilebilmesi için lütfen önce 1. Aşamada geçerli bir senaryo üretin.")
            return
        if "🔥" in self.meta_area.get("1.0", "end") or "#" in self.meta_area.get("1.0", "end"):
            return
        self.meta_area.delete("1.0", "end")
        self.meta_area.insert("1.0", "⏳ Yapay Zeka SEO Başlık ve Etiketlerini Üretiyor... Lütfen Bekleyin.")
        def fetch():
            meta = metadata_uret(metin)
            self.root.after(0, lambda: self.update_meta_area(meta))
        threading.Thread(target=fetch, daemon=True).start()

    def update_meta_area(self, meta):
        self.meta_area.delete("1.0", "end")
        if meta: self.meta_area.insert("1.0", meta)
        else: self.meta_area.insert("1.0", "❌ SEO Etiketleri üretilemedi. Lütfen tekrar deneyin veya kendiniz yazın.")

    def update_step3_summary(self):
        mod = self.app_mode_var.get()
        dil = self.lang_combo.get()
        sure = self.duration_combo.get()
        bg_tip = self.video_source_var.get()
        bg_text = "Oto. Arama" if bg_tip == "search" else "Yapay Zeka (Otopilot)" if bg_tip == "ai_video" else "YouTube Linki" if bg_tip == "link" else "Yerel Dosya"
        sum_text = f"⚙️ İşlem Modu: {mod}\n"
        sum_text += f"🗣️ Dil ve Süre: {dil} | {sure}\n"
        sum_text += f"🎬 Arka Plan: {bg_text}\n"
        sum_text += f"🎵 Müzik: {self.music_combo.get()}"
        self.summary_lbl.configure(text=sum_text)

    def _create_compact_slider(self, parent, label_text, var, from_val, to_val, audio_type):
        row = ctk.CTkFrame(parent, fg_color="transparent")
        row.pack(fill="x", pady=2)
        ctk.CTkLabel(row, text=label_text, width=80, anchor="w", text_color=TEXT_COLOR).pack(side="left")
        val_lbl = ctk.CTkLabel(row, text=f"%{int(var.get()*100)}", width=35, text_color=TEXT_COLOR)
        val_lbl.pack(side="left")
        def update_lbl(val): val_lbl.configure(text=f"%{int(float(val)*100)}")
        slider = ctk.CTkSlider(row, from_=from_val, to=to_val, variable=var, width=120, command=update_lbl, progress_color=ACCENT_COLOR, button_color="#E2E8F0", button_hover_color="white")
        slider.pack(side="left", padx=5)
        btn = ctk.CTkButton(row, text="▶", width=30, height=20, fg_color="#334155", hover_color="#475569", corner_radius=6, command=lambda: self.test_audio(audio_type))
        btn.pack(side="right")

    def open_payment(self, plan_id=1):
        if plan_id == 1: webbrowser.open(IYZICO_LINK_PRO)
        elif plan_id == 2: webbrowser.open(IYZICO_LINK_STUDIO)
        else: webbrowser.open(IYZICO_LINK_PRO)

    def open_subscriptions(self):
        sub_win = ctk.CTkToplevel(self.root)
        sub_win.title("VIRAI Abonelik Planları")
        sub_win.geometry("950x500")
        sub_win.configure(fg_color=APP_BG)
        sub_win.transient(self.root)
        sub_win.grab_set()
        ctk.CTkLabel(sub_win, text="Size Uygun Planı Seçin", font=ctk.CTkFont(size=24, weight="bold"), text_color=TEXT_COLOR).pack(pady=20)
        cards_frame = ctk.CTkFrame(sub_win, fg_color="transparent")
        cards_frame.pack(fill="both", expand=True, padx=20, pady=10)
        free_card = ctk.CTkFrame(cards_frame, fg_color=GLASS_BG, border_width=1, border_color=GLASS_BORDER, width=280, height=400)
        free_card.pack(side="left", padx=10, expand=True)
        free_card.pack_propagate(False)
        ctk.CTkLabel(free_card, text="ÜCRETSİZ", font=ctk.CTkFont(size=20, weight="bold"), text_color="#94A3B8").pack(pady=(20,5))
        ctk.CTkLabel(free_card, text="0₺ / Ay", font=ctk.CTkFont(size=18), text_color=TEXT_COLOR).pack(pady=(0,20))
        features_free = ["✓ Günde 7 Video Kredisi", "✓ Standart Robot Sesleri", "✓ 30 Saniye Sınırı", "❌ Sadece Temel Kurgu", "❌ Zorunlu Filigran", "❌ ElevenLabs Yok"]
        for f in features_free: ctk.CTkLabel(free_card, text=f, text_color=TEXT_COLOR, anchor="w").pack(fill="x", padx=20, pady=2)
        pro_card = ctk.CTkFrame(cards_frame, fg_color=GLASS_BG, border_width=2, border_color=ACCENT_COLOR, width=280, height=400)
        pro_card.pack(side="left", padx=10, expand=True)
        pro_card.pack_propagate(False)
        ctk.CTkLabel(pro_card, text="👑 PRO", font=ctk.CTkFont(size=20, weight="bold"), text_color=ACCENT_COLOR).pack(pady=(20,5))
        ctk.CTkLabel(pro_card, text="59₺ / Ay", font=ctk.CTkFont(size=18), text_color=TEXT_COLOR).pack(pady=(0,20))
        features_pro = ["✓ Günde 10 Video Kredisi", "✓ Video Filtreleri & FX", "✓ Animasyonlu Progress Bar", "✓ 60 Saniye Sınırı", "✓ 10'lu Toplu Üretim", "✓ Filigranı Kaldır"]
        for f in features_pro: ctk.CTkLabel(pro_card, text=f, text_color=TEXT_COLOR, anchor="w").pack(fill="x", padx=20, pady=2)
        ctk.CTkButton(pro_card, text="Satın Al", fg_color=ACCENT_COLOR, hover_color=HOVER_COLOR, command=lambda: self.open_payment(1)).pack(side="bottom", pady=20)
        stu_card = ctk.CTkFrame(cards_frame, fg_color=GLASS_BG, border_width=2, border_color=GOLD_COLOR, width=280, height=400)
        stu_card.pack(side="left", padx=10, expand=True)
        stu_card.pack_propagate(False)
        ctk.CTkLabel(stu_card, text="💎 STUDIO", font=ctk.CTkFont(size=20, weight="bold"), text_color=GOLD_COLOR).pack(pady=(20,5))
        ctk.CTkLabel(stu_card, text="219₺ / Ay", font=ctk.CTkFont(size=18), text_color=TEXT_COLOR).pack(pady=(0,20))
        features_stu = ["✓ PRO'daki Her Şey", "✓ ElevenLabs İnsan Sesleri", "✓ Sınırsız Süre (Max)", "✓ 15'li Toplu Üretim", "✓ Kendi Ses ID'ni Kullan", "✓ Öncelikli Destek"]
        for f in features_stu: ctk.CTkLabel(stu_card, text=f, text_color=TEXT_COLOR, anchor="w").pack(fill="x", padx=20, pady=2)
        ctk.CTkButton(stu_card, text="Satın Al", fg_color=GOLD_COLOR, hover_color="#D97706", text_color="black", command=lambda: self.open_payment(2)).pack(side="bottom", pady=20)

    def on_vfx_change(self, choice):
        if self.plan_type == 0 and choice != "Yok":
            answer = messagebox.askyesno("Premium Özellik", "Sinematik video filtreleri (VFX) PRO veya STUDIO abonelik gerektirir.\nPlanları incelemek ister misiniz?")
            self.vfx_combo.set("Yok")
            if answer: self.open_subscriptions()

    def on_pro_feature_click(self):
        if self.plan_type == 0:
            answer = messagebox.askyesno("Premium Özellik", "İlerleme Çubuğu ve Flaş Geçişler gibi profesyonel kurgu araçları PRO veya STUDIO abonelik gerektirir.\nPlanları incelemek ister misiniz?")
            self.prog_bar_check.deselect()
            self.flash_check.deselect()
            self.zoom_check.deselect()
            if answer: self.open_subscriptions()

    def on_duration_change(self, choice):
        if self.plan_type == 0 and choice in ["60 Saniye (TikTok)", "Sınırsız (Max)"]:
            answer = messagebox.askyesno("Premium Özellik", "60 Saniye ve Sınırsız video üretimi PRO veya STUDIO abonelik gerektirir.\nPlanları incelemek ister misiniz?")
            self.duration_combo.set("30 Saniye (Reels)")
            if answer: self.open_subscriptions()
        elif self.plan_type == 1 and choice == "Sınırsız (Max)":
            answer = messagebox.askyesno("Premium Özellik", "Sınırsız video üretimi STUDIO abonelik gerektirir.\nPlanları incelemek ister misiniz?")
            self.duration_combo.set("60 Saniye (TikTok)")
            if answer: self.open_subscriptions()

    def on_batch_change(self, choice):
        if self.plan_type == 0 and choice != "1 Video":
            answer = messagebox.askyesno("Premium Özellik", "Toplu video üretimi PRO veya STUDIO abonelik gerektirir.\nPlanları incelemek ister misiniz?")
            self.batch_combo.set("1 Video")
            if answer: self.open_subscriptions()
        elif self.plan_type == 1 and choice in ["15 Video", "20 Video"]:
            answer = messagebox.askyesno("Premium Özellik", "15'li video üretimi STUDIO abonelik gerektirir.\nPlanları incelemek ister misiniz?")
            self.batch_combo.set("10 Video")
            if answer: self.open_subscriptions()

    def on_wm_focus(self, event):
        if self.plan_type == 0:
            self.root.focus_set() 
            answer = messagebox.askyesno("Premium Özellik", "Özel filigran belirlemek ve zorunlu filigranı kaldırmak PRO abonelik gerektirir.\nPlanları incelemek ister misiniz?")
            if answer: self.open_subscriptions()

    def select_local_video(self):
        path = filedialog.askopenfilename(title="Video Seç", filetypes=[("Video Dosyaları", "*.mp4 *.mov *.avi *.mkv")])
        if path:
            self.local_video_path = path
            self.local_vid_lbl.configure(text=f"📁 {os.path.basename(path)[:30]}", text_color=ACCENT_COLOR)
        else:
            self.local_video_path = ""
            self.local_vid_lbl.configure(text="Video seçilmedi.", text_color="#64748B")

    def select_logo(self):
        if self.plan_type == 0:
            answer = messagebox.askyesno("Premium Özellik", "Kendi logonuzu yüklemek PRO abonelik gerektirir.\nPlanları incelemek ister misiniz?")
            if answer: self.open_subscriptions()
            return
        file_path = filedialog.askopenfilename(title="Logo Seç", filetypes=[("Resim Dosyaları", "*.png *.jpg *.jpeg")])
        if file_path:
            self.local_logo_path = file_path
            self.logo_btn.configure(text="✅ Seçildi", fg_color="#059669")
        else:
            self.local_logo_path = ""
            self.logo_btn.configure(text="🖼️ Logo", fg_color="#334155")

    def on_voice_change(self, choice):
        if "🔥" in choice: self.custom_voice_entry.pack(fill="x", padx=15, pady=5)
        else: self.custom_voice_entry.pack_forget()
        if self.plan_type < 2 and ("⭐" in choice or "🔥" in choice):
            answer = messagebox.askyesno("Premium Özellik", "ElevenLabs (Ultra-Gerçekçi) insan sesleri STUDIO abonelik gerektirir.\nPlanları incelemek ister misiniz?")
            self.voice_combo.set("Gerçekçi/Kalın Erkek (Edge)")
            self.custom_voice_entry.pack_forget()
            if answer: self.open_subscriptions()

    def on_music_combo_change(self, choice):
        if choice == "Yerel Dosya Seç...":
            if self.plan_type == 0:
                answer = messagebox.askyesno("Premium Özellik", "Kendi müziğinizi yüklemek PRO abonelik gerektirir.\nPlanları incelemek ister misiniz?")
                self.music_combo.set("Korku / Gerilim")
                if answer: self.open_subscriptions()
                return
            file_path = filedialog.askopenfilename(title="Müzik Seç", filetypes=[("Ses Dosyaları", "*.mp3 *.wav *.ogg *.m4a")])
            if file_path:
                self.local_music_path = file_path
                filename = os.path.basename(file_path)
                display_name = (filename[:25] + '..') if len(filename) > 25 else filename
                self.local_music_lbl.configure(text=f"📁 {display_name}", text_color=ACCENT_COLOR)
            else:
                self.music_combo.set("Yok")
                self.local_music_path = ""
                self.local_music_lbl.configure(text="")
        else:
            self.local_music_path = ""
            self.local_music_lbl.configure(text="")

    def log(self, msg):
        color = "#10B981" if "✅" in msg else DANGER_COLOR if "❌" in msg or "⚠️" in msg else "#94A3B8"
        self.root.after(0, lambda: self.status_label.configure(text=msg, text_color=color))

    def update_progress(self, val):
        self.root.after(0, lambda: self.progress.set(val / 100.0))

    def toggle_video_inputs(self):
        v = self.video_source_var.get()
        if v == "ai_video" and self.plan_type == 0:
            answer = messagebox.askyesno("Premium Özellik", "Yapay zeka ile hareketli video üretimi PRO abonelik gerektirir.\nPlanları incelemek ister misiniz?")
            self.video_source_var.set("search")
            v = "search"
            if answer: self.open_subscriptions()
            
        self.search_entry.master.pack_forget() # search_wrap'i gizle
        self.yt_results_frame.pack_forget()
        self.link_entry.pack_forget()
        self.local_vid_btn.pack_forget()
        self.local_vid_lbl.pack_forget()
        
        if v == "search": 
            self.search_entry.configure(placeholder_text="Arama kelimesi (Boşsa konuyu arar)")
            self.search_entry.master.pack(fill="x", padx=15, pady=(10, 5))
            self.yt_results_frame.pack(fill="x", padx=15, pady=(0, 20))
        elif v == "ai_video":
            self.search_entry.configure(placeholder_text="Görsel Promptu (Boş bırakırsanız konuyu çizer)")
            self.search_entry.master.pack(fill="x", padx=15, pady=(10, 20))
            self.search_yt_btn.pack_forget() # Otopilotta butonu gizle
        elif v == "link": 
            self.link_entry.pack(fill="x", padx=15, pady=(10, 20))
        elif v == "local":
            self.local_vid_btn.pack(fill="x", padx=15, pady=(10, 5))
            self.local_vid_lbl.pack(fill="x", padx=15, pady=(0, 20))

    def test_audio(self, a_type):
        if not PYGAME_AVAILABLE: return
        def play_thread():
            try:
                pygame.mixer.init()
                pygame.mixer.music.stop()
                if a_type == "voice":
                    self.log("⏳ Test sesi oluşturuluyor...")
                    v_mod = self.voice_combo.get()
                    d_mod = self.lang_combo.get().split()[0]
                    test_metni = "Ses seviyesi testi, bir, iki, üç."
                    if "⭐" in v_mod or "🔥" in v_mod:
                        if "🔥" in v_mod:
                            voice_id = self.custom_voice_entry.get().strip()
                            if not voice_id: return
                        else: voice_id = ELEVENLABS_VOICES.get(v_mod, "ErXwobaYiN019PkySvjV")
                        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
                        headers = {"Accept": "audio/mpeg", "Content-Type": "application/json", "xi-api-key": ELEVENLABS_API_KEY}
                        data = {"text": test_metni, "model_id": "eleven_multilingual_v2"}
                        response = requests.post(url, json=data, headers=headers)
                        if response.status_code == 200:
                            with open(TEMP_TEST_SESI, 'wb') as f: f.write(response.content)
                        else: return
                    else:
                        ses_modeli = "en-US-JennyNeural" if "Kadın" in v_mod and "EN" in d_mod else "tr-TR-EmelNeural" if "Kadın" in v_mod else "en-US-ChristopherNeural" if "EN" in d_mod else "tr-TR-AhmetNeural"
                        rate_str, pitch_str = ("+10%", "+5Hz") if "Enerjik" in v_mod else ("-5%", "-10Hz") if "Gerçekçi" in v_mod else ("+0%", "+0Hz")
                        try: loop = asyncio.get_event_loop()
                        except: asyncio.set_event_loop(asyncio.new_event_loop())
                        asyncio.run(edge_tts.Communicate(test_metni, voice=ses_modeli, rate=rate_str, pitch=pitch_str).save(TEMP_TEST_SESI))
                    if dosya_gecerli_mi(TEMP_TEST_SESI, 500):
                        pygame.mixer.music.load(TEMP_TEST_SESI)
                        pygame.mixer.music.set_volume(self.vol_voice_var.get())
                        pygame.mixer.music.play()
                        self.log("▶️ Anlatıcı sesi test ediliyor.")
                elif a_type == "sfx":
                    sfx_indir()
                    if dosya_gecerli_mi(POP_SES_DOSYASI, 1000):
                        pygame.mixer.music.load(POP_SES_DOSYASI)
                        pygame.mixer.music.set_volume(self.vol_sfx_var.get())
                        pygame.mixer.music.play()
                        self.log("▶️ Efekt sesi test ediliyor.")
                elif a_type == "music":
                    mk = self.music_combo.get()
                    if mk == "Yok": return
                    if mk == "Yerel Dosya Seç...":
                        if not self.local_music_path or not os.path.exists(self.local_music_path): return
                        m_yolu = self.local_music_path
                    else:
                        if not os.path.exists(TEMP_MUZIK_DOSYASI) or not dosya_gecerli_mi(TEMP_MUZIK_DOSYASI, 5000):
                            internetten_muzik_indir(mk, lambda x: print(x))
                        m_yolu = TEMP_MUZIK_DOSYASI
                    if dosya_gecerli_mi(m_yolu, 1000):
                        pygame.mixer.music.load(m_yolu)
                        pygame.mixer.music.set_volume(self.vol_music_var.get())
                        pygame.mixer.music.play()
                        self.log("▶️ Müzik test ediliyor.")
            except: pass
        threading.Thread(target=play_thread, daemon=True).start()

    def animate_thinking(self, frame_idx=0):
        if not self.is_generating_text: return
        frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        phrases = ["VIRAI Nöral Ağına Bağlanılıyor...", "İçerik Çözümleniyor...", "Viral Kancalar (Hooks) Üretiliyor...", "Senaryo Yazılıyor...", "Büyük Dil Modeli İşliyor..."]
        phrase = phrases[(frame_idx // 15) % len(phrases)]
        frame = frames[frame_idx % len(frames)]
        self.text_area.delete("1.0", "end")
        self.text_area.insert("1.0", f"{frame} {phrase}\n\nLütfen bekleyin, VIRAI sizin için harika bir içerik hazırlıyor...")
        self.root.after(100, self.animate_thinking, frame_idx + 1)

    def type_text(self, text, index=0):
        if index == 0:
            self.text_area.delete("1.0", "end")
            self.text_area.configure(border_color=GLASS_BORDER) 
        if index < len(text):
            chunk_size = random.randint(3, 6)
            self.text_area.insert("end", text[index:index+chunk_size])
            self.text_area.see("end") 
            self.root.after(15, self.type_text, text, index + chunk_size)
        else:
            self.find_btn.configure(state="normal", text="✨ SENARYOYU ÜRET (BETA)")

    def log_to_server(self, s, text):
        def _send():
            try:
                data = {
                    "action": "log_generation", "username": self.username, "topic": s.get("konu", ""),
                    "generated_text": text, "bg_type": s.get("tip", ""), "voice": s.get("ses", ""),
                    "music": s.get("muzik", ""), "duration": s.get("sure", ""), "text_color": s.get("text_color", ""), "text_bg": s.get("text_bg", "")
                }
                requests.post(API_URL, data=data, timeout=5)
            except: pass
        threading.Thread(target=_send, daemon=True).start()

    def start_story_search(self):
        konu = self.topic_entry.get().strip()
        icerik_tipi = self.content_type_combo.get()
            
        if not konu: return messagebox.showwarning("Hata", "Lütfen bir konu girin!")
        
        self.find_btn.configure(state="disabled", text="⏳ İşleniyor...")
        self.text_area.configure(border_color=ACCENT_COLOR)
        
        self.is_generating_text = True
        self.animate_thinking()
        
        dil = self.lang_combo.get().split(" ")[0] + " " + self.lang_combo.get().split(" ")[1] 
        sure = self.duration_combo.get()
        
        threading.Thread(target=self.run_story, args=(konu, dil, sure, icerik_tipi), daemon=True).start()

    def run_story(self, konu, dil, sure, icerik_tipi):
        story = icerik_getir(konu, "subject", dil, sure, icerik_tipi, self.log)
        self.root.after(0, lambda: self.set_story(story))

    def set_story(self, story):
        self.is_generating_text = False 
        if story: self.type_text(story) 
        else:
            self.text_area.configure(border_color=GLASS_BORDER)
            self.find_btn.configure(state="normal", text="✨ SENARYOYU ÜRET (BETA)")
            self.text_area.delete("1.0", "end")
            self.text_area.insert("1.0", "❌ İçerik üretilemedi. Lütfen tekrar deneyin.")

    def start_batch_generation(self):
        metin = self.text_area.get("1.0", "end-1c").strip()
        batch_count = int(self.batch_combo.get().split()[0])
        
        if not metin or "Senaryonuz burada" in metin or "VIRAI Nöral" in metin or "❌" in metin: 
            return messagebox.showwarning("Hata", "Lütfen önce 1. Aşamada geçerli bir senaryo üretin!")
        
        if self.credits < batch_count:
            answer = messagebox.askyesno("Yetersiz Kredi", f"Bu işlemi yapmak için {batch_count} krediye ihtiyacınız var. Mevcut krediniz: {self.credits}\n\nKrediniz her gece yenilenir veya planınızı yükseltebilirsiniz.\nPlanları incelemek ister misiniz?")
            if answer: self.open_subscriptions()
            return

        kullanici_filigran = self.wm_entry.get()
        if self.plan_type == 0: kullanici_filigran = "@VIRAI"
            
        # GÜNCELLEME: AKILLI KAYNAK BULUCU (Kutuyu boş bırakırsa 1. aşamadaki konuyu kullanır)
# ESKİ KODUN YERİNE:
        kaynak_input = ""
        v_source = self.video_source_var.get()
        if v_source == "link":
            kaynak_input = self.link_entry.get().strip()
        elif v_source == "search":
            kaynak_input = self.selected_yt_url_var.get().strip() # Radyo butonundan gelen URL
            if not kaynak_input: return messagebox.showwarning("Hata", "Lütfen listeden bir arka plan videosu seçin!")
        elif v_source == "ai_video":
            kaynak_input = self.search_entry.get().strip() or self.topic_entry.get().strip()

        sett = {
            "tip": self.video_source_var.get(), "kaynak": kaynak_input,
            "yerel_video_yolu": getattr(self, "local_video_path", ""), "muzik": self.music_combo.get(), "yerel_muzik_yolu": self.local_music_path, 
            "dil": self.lang_combo.get().split(" ")[0] + " " + self.lang_combo.get().split(" ")[1], "ses": self.voice_combo.get(), "custom_voice_id": self.custom_voice_entry.get().strip(),
            "stil": self.subtitle_combo.get(), "kurgu": self.b_roll_combo.get(), "sfx": self.sfx_check.get(), "filigran": kullanici_filigran, "logo_yolu": getattr(self, "local_logo_path", ""), 
            "sure": self.duration_combo.get(), "icerik_tipi": "Manual", "konu": self.topic_entry.get().strip(),
            "text_color": self.text_color_combo.get(), "text_bg": self.text_bg_combo.get(),
            "video_vfx": self.vfx_combo.get(), "progress_bar": self.prog_bar_check.get(), "flash_fx": self.flash_check.get(), "zoom_fx": self.zoom_check.get(),
            "vol_settings": {"voice": self.vol_voice_var.get(), "music": self.vol_music_var.get(), "sfx": self.vol_sfx_var.get()}
        }
        
        if sett["tip"] == "local" and not sett["yerel_video_yolu"]: 
            return messagebox.showwarning("Hata", "Lütfen 2. Aşamada cihazınızdan bir arka plan videosu seçin!")
        elif sett["tip"] != "local" and not sett["kaynak"]: 
            return messagebox.showwarning("Hata", "Lütfen 1. Aşamada bir konu yazın veya 2. Aşamada bir arama kelimesi girin!")
            
        self.generate_btn.configure(state="disabled", fg_color="#555", text="⏳ VİDEO ÜRETİLİYOR...")
        self.progress.set(0.0)
        self.islem_baslangic = time.time()
        
        if PYGAME_AVAILABLE:
            try: pygame.mixer.music.stop()
            except: pass
        threading.Thread(target=self.run_batch, args=(metin, batch_count, sett), daemon=True).start()

    def run_batch(self, ilk_metin, b_count, s):
        os.makedirs(self.cikti_klasoru, exist_ok=True)
        for i in range(b_count):
            cikis_adi = f"virai_video_{i+1}.mp4" if b_count > 1 else "hazir_video.mp4"
            # Sadece isim değil, MASAÜSTÜ TAM YOLUNU veriyoruz
            cikis_adi_tam_yol = os.path.join(self.cikti_klasoru, cikis_adi) 
            
            self.log(f"⚙️ VIRAI İşliyor: Video {i+1}/{b_count} hazırlanıyor...")
            aktif_metin = ilk_metin
            
            if i > 0:
                self.log(f"🔍 Yeni içerik aranıyor ({i+1}/{b_count})...")
                yeni = icerik_getir(s["konu"], "subject", s["dil"], s["sure"], s["icerik_tipi"], self.log)
                if yeni: aktif_metin = yeni
                
                metadata = metadata_uret(aktif_metin)
                if metadata:
                    self.root.after(0, lambda m=metadata, v_idx=i+1: self.meta_area.insert("end", f"\n\n--- VİDEO {v_idx} ---\n" + m))
            
            self.log_to_server(s, aktif_metin)
                
            basari, hata_mesaji = asyncio.run(video_islem_baslat(aktif_metin, s, cikis_adi_tam_yol, self.log, self.update_progress))
            if not basari: 
                self.log(f"❌ Video {i+1} arızalandı!")
                self.root.after(0, lambda h=hata_mesaji: messagebox.showerror("Render Hatası", f"Hata:\n{h}"))
                self.root.after(0, lambda: self.reset_ui(False, None))
                return 

        try:
            resp = requests.post(API_URL, data={"action": "use_credit", "username": self.username, "count": b_count}, timeout=5)
            res = resp.json()
            if res.get("status") == "success":
                self.credits = res.get("remaining_credits", self.credits)
                self.root.after(0, lambda: self.credit_lbl.configure(text=f"🪙 Günlük Kredi: {self.credits}"))
        except: pass

        self.root.after(0, lambda: self.reset_ui(True, cikis_adi))

    def reset_ui(self, success, son_video_adi):
        self.generate_btn.configure(state="normal", fg_color="#059669", text="🎬 VİDEOYU OLUŞTUR (BETA)")
        gecen_sure = time.time() - self.islem_baslangic
        dakika, saniye = int(gecen_sure // 60), int(gecen_sure % 60)
        s_metni = f"{dakika} dk {saniye} sn" if dakika > 0 else f"{saniye} sn"
        
        if success:
            self.log(f"✅ TÜM İŞLEMLER TAMAM! ({s_metni})")
            pub_win = ctk.CTkToplevel(self.root)
            pub_win.title("Video Hazır!")
            pub_win.geometry("450x330")
            pub_win.configure(fg_color=APP_BG)
            pub_win.transient(self.root)
            pub_win.grab_set()
            
            ctk.CTkLabel(pub_win, text="🎉 Video Başarıyla Üretildi!", font=ctk.CTkFont(size=22, weight="bold"), text_color=ACCENT_COLOR).pack(pady=(25, 10))
            ctk.CTkLabel(pub_win, text=f"İşlem Süresi: {s_metni}", font=ctk.CTkFont(size=14), text_color=TEXT_COLOR).pack(pady=(0, 20))
            
            ctk.CTkButton(pub_win, text="🚀 Kanalıma Yükle (YouTube Shorts)", height=40, fg_color="#DC2626", hover_color="#991B1B", text_color="white", font=ctk.CTkFont(weight="bold"), command=lambda: self.publish_to_youtube(son_video_adi)).pack(fill="x", padx=40, pady=5)
            ctk.CTkButton(pub_win, text="Klasörü Aç", height=35, fg_color="#334155", hover_color="#1E293B", text_color="white", command=lambda: os.startfile(self.cikti_klasoru) if os.name == 'nt' else subprocess.call(["open", self.cikti_klasoru]) if sys.platform == "darwin" else subprocess.call(["xdg-open", self.cikti_klasoru])).pack(fill="x", padx=40, pady=(5, 15))
            ctk.CTkButton(pub_win, text="🔄 Başa Dön ve Yeni Video Üret", height=40, fg_color="#0EA5E9", hover_color="#0284C7", text_color="white", font=ctk.CTkFont(weight="bold"), command=lambda: self.reset_to_start(pub_win)).pack(fill="x", padx=40)
        else: 
            self.log(f"❌ İŞLEM İPTAL EDİLDİ")

    def publish_to_youtube(self, video_path):
        messagebox.showinfo("Auto-Publish (Otomatik Yükleme)", "Kanalınıza API üzerinden %100 otomatik yükleme yapabilmemiz için Google Cloud entegrasyonu gerekmektedir.\n\nSizi YouTube'un doğrudan yükleme sayfasına yönlendiriyoruz. Lütfen videonuzu yükleyip, sağdaki kutuda yazan başlık ve açıklamayı kopyalayın.")
        webbrowser.open("https://studio.youtube.com/channel/UC/videos/upload?d=ud")

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Giriş Yap - VIRAI (BETA)")
        self.root.geometry("400x520") 
        self.root.resizable(False, False)
        self.root.configure(fg_color=APP_BG)
        self.check_for_updates()
        
        try:
            logo_yolu = resource_path("viraiBrand/juslogoVirai.png")
            my_logo = ctk.CTkImage(light_image=Image.open(logo_yolu), dark_image=Image.open(logo_yolu), size=(100, 50))
            ctk.CTkLabel(self.root, text="", image=my_logo).pack(pady=(25, 10))
        except Exception as e:
            ctk.CTkLabel(self.root, text="🚀", font=ctk.CTkFont(size=50)).pack(pady=(25, 10))
            
        ctk.CTkLabel(self.root, text="VIRAI (BETA)", font=ctk.CTkFont(size=24, weight="bold"), text_color=ACCENT_COLOR).pack()
        ctk.CTkLabel(self.root, text="Yapay Zeka Destekli İçerik Üreticisi", font=ctk.CTkFont(size=12), text_color="#94A3B8").pack(pady=(0, 15))
        
        self.frame = ctk.CTkFrame(self.root, width=320, height=350, corner_radius=20, fg_color=GLASS_BG, border_width=1, border_color=GLASS_BORDER)
        self.frame.pack(pady=10)
        self.frame.pack_propagate(False)

        ctk.CTkLabel(self.frame, text="Kullanıcı Adı:", text_color=TEXT_COLOR).pack(anchor="w", padx=20, pady=(15, 2))
        self.user_entry = ctk.CTkEntry(self.frame, width=280, placeholder_text="Kullanıcı adınız...", fg_color="#0F172A", border_color=GLASS_BORDER, text_color=TEXT_COLOR)
        self.user_entry.pack(padx=20)

        ctk.CTkLabel(self.frame, text="Şifre:", text_color=TEXT_COLOR).pack(anchor="w", padx=20, pady=(10, 2))
        self.pass_entry = ctk.CTkEntry(self.frame, width=280, placeholder_text="Şifreniz...", show="*", fg_color="#0F172A", border_color=GLASS_BORDER, text_color=TEXT_COLOR)
        self.pass_entry.pack(padx=20)

        ctk.CTkLabel(self.frame, text="E-Posta (Sadece Kayıt İçin):", text_color=TEXT_COLOR).pack(anchor="w", padx=20, pady=(10, 2))
        self.email_entry = ctk.CTkEntry(self.frame, width=280, placeholder_text="ornek@mail.com", fg_color="#0F172A", border_color=GLASS_BORDER, text_color=TEXT_COLOR)
        self.email_entry.pack(padx=20)

        self.login_btn = ctk.CTkButton(self.frame, text="GİRİŞ YAP", width=280, corner_radius=10, command=self.login, fg_color="#059669", hover_color="#047857", text_color="white")
        self.login_btn.pack(pady=(20, 10))

        self.reg_btn = ctk.CTkButton(self.frame, text="Yeni Kayıt Ol", width=280, corner_radius=10, command=self.register, fg_color="#334155", hover_color="#475569", text_color="white")
        self.reg_btn.pack(pady=(0, 10))
        
        
    def check_for_updates(self):
        def _check():
            try:
                response = requests.post(API_URL, data={"action": "check_update"}, timeout=5)
                result = response.json()
                if result.get("status") == "success":
                    latest = result.get("latest_version")
                    url = result.get("download_url")
                    is_mandatory = result.get("is_mandatory")

                    if latest != APP_VERSION:
                        if is_mandatory:
                            self.root.after(0, lambda: messagebox.showwarning("Zorunlu Güncelleme", f"Uygulamanın yeni bir sürümü ({latest}) çıktı!\nKullanmaya devam etmek için lütfen yeni sürümü indirin."))
                            webbrowser.open(url)
                            self.root.after(0, lambda: sys.exit())
                        else:
                            answer = messagebox.askyesno("Yeni Güncelleme", f"Uygulamanın yeni bir sürümü ({latest}) çıktı.\nŞimdi indirmek ister misiniz?")
                            if answer: webbrowser.open(url)
            except Exception as e: pass
        threading.Thread(target=_check, daemon=True).start()

    def login(self):
        user = self.user_entry.get().strip()
        pwd = self.pass_entry.get().strip()
        if not user or not pwd: return messagebox.showwarning("Hata", "Lütfen Kullanıcı Adı ve Şifre alanlarını doldurun.")
        self.login_btn.configure(text="Giriş Yapılıyor...", state="disabled")
        threading.Thread(target=self._send_request, args=("login", user, pwd, ""), daemon=True).start()

    def register(self):
        user = self.user_entry.get().strip()
        pwd = self.pass_entry.get().strip()
        email = self.email_entry.get().strip()
        if not user or not pwd or not email: return messagebox.showwarning("Hata", "Kayıt olmak için Kullanıcı Adı, Şifre ve E-Posta alanlarının hepsini doldurun.")
        if "@" not in email or "." not in email: return messagebox.showwarning("Hata", "Lütfen geçerli bir e-posta adresi girin.")
        self.reg_btn.configure(text="Kayıt Yapılıyor...", state="disabled")
        threading.Thread(target=self._send_request, args=("register", user, pwd, email), daemon=True).start()

    def _send_request(self, action, user, pwd, email):
        try:
            response = requests.post(API_URL, data={"action": action, "username": user, "password": pwd, "email": email}, timeout=10)
            result = response.json()
            if result.get("status") == "success":
                if action == "login":
                    plan_type = result.get("plan_type", 0)
                    credits = result.get("credits", 0)
                    sub_end = result.get("sub_end", "")
                    self.root.after(0, lambda: self.open_main_app(user, plan_type, credits, sub_end))
                else: self.root.after(0, lambda: messagebox.showinfo("Başarılı", result.get("message")))
            else: self.root.after(0, lambda: messagebox.showerror("Hata", result.get("message")))
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Bağlantı Hatası", f"Sunucuya bağlanılamadı. İnternet bağlantınızı kontrol edin."))
        finally:
            self.root.after(0, lambda: self.login_btn.configure(text="GİRİŞ YAP", state="normal"))
            self.root.after(0, lambda: self.reg_btn.configure(text="Yeni Kayıt Ol", state="normal"))

    def open_main_app(self, username, plan_type, credits, sub_end):
        self.root.destroy() 
        main_root = ctk.CTk()
        app = UltimateApp(main_root, username, plan_type, credits, sub_end)
        main_root.mainloop()

if __name__ == "__main__":
    root = ctk.CTk()
    login_app = LoginApp(root)
    root.mainloop()