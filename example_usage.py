from transcriber import transcribe_audio
from diarizer import diarize_transcription
from utils import download_file

# Ruta del archivo de audio
audio_file_path = "path_to_your_audio_file.mp3"

# Transcribir audio
transcription_result = transcribe_audio(audio_file_path)

# Diarizar transcripción
final_result = diarize_transcription(transcription_result)

# Opcional: guardar y descargar el resultado final
# Esto depende de cómo desees manejar la salida

print(final_result)  # O cualquier otra forma de visualización que prefieras
