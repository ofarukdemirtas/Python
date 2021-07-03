import pafy
url= input("Enter youtube url:")
video = pafy.new(url)
audios= video.getbestaudio()
audios.download()
 