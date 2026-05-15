FROM debian:bookworm-slim

# Instalar Python, Tkinter y un servidor de pantalla virtual ligero
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-tk \
    x11vnc \
    xvfb \
    fluxbox \
    novnc \
    && rm -rf /var/lib/apt/lists/*

# Crear un usuario sin privilegios para correr la app
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app

# Copiar los archivos del proyecto
COPY --chown=user . $HOME/app

# Instalar requerimientos si existen
RUN pip3 install --no-cache-dir -r requirements.txt --break-system-packages || true

# Configurar el puerto web obligatorio para Hugging Face
EXPOSE 7860

# Comando mágico: Enciende la pantalla virtual silenciosamente y arranca tu código solo
CMD Xvfb :99 -screen 0 1024x768x16 & \
    sleep 2 && \
    fluxbox & \
    x11vnc -display :99 -nopw -forever -shared & \
    /usr/share/novnc/utils/launch.sh --vnc localhost:5900 --port 7860 & \
    export DISPLAY=:99 && \
    python3 Lab2_Ley_NEWTON.py
