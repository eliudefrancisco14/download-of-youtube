import os
import subprocess
import yt_dlp
from tkinter import Tk, simpledialog

# Configurar pasta de download
output_folder = "downloads"
os.makedirs(output_folder, exist_ok=True)

def get_video_info(url):
    """Obtém informações do vídeo/playlist."""
    ydl_opts = {"quiet": True, "extract_flat": True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
    return info

def download_video(url):
    """Faz o download do vídeo e converte para MP4."""
    print(f"Baixando: {url}")
    cmd = [
        "yt-dlp", "-f", "bestvideo+bestaudio", "--merge-output-format", "mp4",
        "-o", os.path.join(output_folder, "%(title)s.%(ext)s"), url
    ]
    subprocess.run(cmd)
    print("Download concluído!")

def download_playlist(url, max_videos=10):
    """Baixa apenas os primeiros vídeos da playlist."""
    print("Identificando vídeos da playlist...")
    info = get_video_info(url)
    videos = info.get("entries", [])[:max_videos]

    for idx, video in enumerate(videos, 1):
        print(f"Baixando vídeo {idx}/{max_videos}: {video['title']}")
        download_video(video["url"])

def main():
    """Interface simples para inserir link."""
    root = Tk()
    root.withdraw()
    url = simpledialog.askstring("Input", "Digite o link do vídeo/playlist do YouTube:")

    if not url:
        print("Nenhum link foi fornecido.")
        return

    info = get_video_info(url)

    if "entries" in info:  # É uma playlist
        print(f"Playlist detectada: {info['title']}")
        download_playlist(url)
    else:  # É um vídeo único
        print(f"Vídeo detectado: {info['title']}")
        download_video(url)

if __name__ == "__main__":
    main()
