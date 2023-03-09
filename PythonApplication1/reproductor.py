import tkinter as tk
import vlc

class VideoPlayer:
    def __init__(self, master):
        self.master = master
        master.title("Reproductor de video")

        # Crear caja de texto para insertar URL
        self.url_label = tk.Label(master, text="Inserte la URL del video:")
        self.url_label.pack()
        self.url_entry = tk.Entry(master)
        self.url_entry.pack()

        # Crear botón para reproducir el video
        self.play_button = tk.Button(master, text="Reproducir", command=self.play_video)
        self.play_button.pack()

        # Crear botón para salir
        self.quit_button = tk.Button(master, text="Salir", command=master.quit)
        self.quit_button.pack()

        # Crear botones para controlar el video
        self.pause_button = tk.Button(master, text="Pausa", command=self.pause_video, state="disabled")
        self.pause_button.pack()
        self.stop_button = tk.Button(master, text="Detener", command=self.stop_video, state="disabled")
        self.stop_button.pack()

        # Crear slider para ajustar la posición del video
        self.position_slider = tk.Scale(master, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_position, state="disabled")
        self.position_slider.pack()

        # Crear botón para abrir un archivo de video
        self.open_file_button = tk.Button(master, text="Abrir archivo", command=self.open_file)
        self.open_file_button.pack()

        # Crear botón para activar/desactivar el modo de pantalla completa
        self.fullscreen_button = tk.Button(master, text="Pantalla completa", command=self.toggle_fullscreen)

        # Crear reproductor de video y variables de estado
        self.instance = vlc.Instance()
        self.media = None
        self.player = None
        self.is_playing = False
        self.is_paused = False
        self.is_fullscreen = False

    def play_video(self):
        url = self.url_entry.get()
        self.media = self.instance.media_new(url)
        self.player = self.instance.media_player_new()
        self.player.set_media(self.media)
        self.player.play()
        self.is_playing = True
        self.is_paused = False
        self.play_button.config(state="disabled")
        self.pause_button.config(state="normal")
        self.stop_button.config(state="normal")
        self.position_slider.config(state="normal")

    def pause_video(self):
        if self.player is not None:
            if not self.is_paused:
                self.player.pause()
                self.is_paused = True
                self.pause_button.config(text="Reanudar")
            else:
                self.player.play()
                self.is_paused = False
                self.pause_button.config(text="Pausa")

    def stop_video(self):
        if self.player is not None:
            self.player.stop()
            self.is_playing = False
            self.is_paused = False
            self.play_button.config(state="normal")
            self.pause_button.config(state="disabled", text="Pausa")
            self.stop_button.config(state="disabled")
            self.position_slider.config(state="disabled")

    def set_position(self, value):
        if self.player is not None:
            self.player.set_position(float(value) / 100)

    def open_file(self):
        filetypes = (("Video files", "*.mp4 *.avi *.mkv"), ("All files", "*.*"))
        filename = tk.filedialog.askopenfilename(filetypes=filetypes)
        if filename != None:
            self.media = self.instance.media_new(filename)
            self.player = self.instance.media_player_new()
            self.player.set_media(self.media)
            self.play_button.config(state="disabled")
            self.pause_button.config(state="normal")
            self.stop_button.config(state="normal")
            self.position_slider.config(state="normal")
            self.player.play()
            self.is_playing = True
    def toggle_fullscreen(self):
        if self.player is not None:
            if not self.is_fullscreen:
                self.player.set_fullscreen(True)
                self.is_fullscreen = True
                self.fullscreen_button.config(text="Salir de pantalla completa")
            else:
                self.player.set_fullscreen(False)
                self.is_fullscreen = False
                self.fullscreen_button.config(text="Pantalla completa")
root = tk.Tk()
video_player = VideoPlayer(root)
root.mainloop()