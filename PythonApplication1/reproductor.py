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

    def play_video(self):
        url = self.url_entry.get()
        instance = vlc.Instance()
        media = instance.media_new(url)
        player = instance.media_player_new()
        player.set_media(media)
        player.play()

root = tk.Tk()
video_player = VideoPlayer(root)
root.mainloop()
