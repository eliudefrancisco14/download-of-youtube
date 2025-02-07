Aqui está um **README.md** bem estruturado para o seu projeto no GitHub. Ele inclui instruções de instalação, uso e requisitos.  

```markdown
# 🎥 YouTube Video & Playlist Downloader

Um script Python para baixar vídeos ou playlists do YouTube. Ele identifica automaticamente se o link fornecido é um **vídeo único** ou uma **playlist**, e no caso de playlists, baixa apenas os **10 primeiros vídeos**.

## 🚀 Funcionalidades

- 📥 **Baixa vídeos do YouTube** em **MP4** com a melhor qualidade disponível.
- 🎞 **Baixa até 10 vídeos de uma playlist** automaticamente.
- 🎯 **Detecta automaticamente** se o link é um vídeo único ou uma playlist.
- 📂 **Organiza os downloads** na pasta `downloads/`.

## 📌 Pré-requisitos

Certifique-se de ter os seguintes pacotes instalados antes de rodar o script:

1. **Python 3** instalado no seu sistema.
2. **yt-dlp** (para baixar os vídeos):
   ```sh
   pip install yt-dlp
   ```
3. **FFmpeg** (para conversão e fusão de vídeo/áudio):
   - Baixe e instale a versão compatível com seu sistema: [FFmpeg Download](https://ffmpeg.org/download.html).
   - Adicione o `ffmpeg` ao seu `PATH`.

## 🛠 Como Usar

1. Clone o repositório:
   ```sh
   git clone https://github.com/eliudefrancisco14/download-of-youtube.git
   cd download-of-youtube
   ```

2. Execute o script:
   ```sh
   python main.py
   ```

3. Insira o link do vídeo ou playlist na caixa de diálogo.

4. Os vídeos serão baixados na pasta `downloads/`.

## 📜 Licença

Este projeto é de código aberto e está licenciado sob a [MIT License](LICENSE).

---

💡 **Sugestões ou problemas?** Sinta-se à vontade para abrir uma [issue](https://github.com/eliudefrancisco14/download-of-youtube/issues) ou contribuir com um PR! 🚀

