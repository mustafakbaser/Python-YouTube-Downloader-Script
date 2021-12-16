from pytube import YouTube 

SAVE_PATH = "D:\Archive\Music"

link = ["https://www.youtube.com/watch?v=iDqrgjyv09A",
        "https://www.youtube.com/watch?v=iDqrgjyv09A"
        ]
print("İndirme işlemi başladı.") 
for i in link: 
    try:
        youtube = YouTube(i)
        youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download(SAVE_PATH)
    except: 
        print("Bağlantı hatası.") 
print("İndirme tamamlandı.", "(Dosya sayısı:", + len(link), ")")
