from transcriber import transcribe_audio
from utils import save_transcription_to_file, download_file

# Define la ruta al archivo de audio MP3
audio_file_path = "path_to_your_audio_file.mp3"

transcription_result = transcribe_audio(audio_file_path)


# Guarda la transcripción en un archivo de texto
save_transcription_to_file(transcription_result["segments"], "transcription.txt")

# Descarga o indica al usuario dónde encontrar el archivo de transcripción
download_file("transcription.txt")
