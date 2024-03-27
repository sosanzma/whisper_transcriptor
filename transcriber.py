import whisperx
from utils import load_audio_file

def transcribe_audio(audio_file_path, language="es", device="cuda", batch_size=16, compute_type="int8"):
    # Cargar modelo WhisperX
    model = whisperx.load_model("large-v2", device, compute_type=compute_type)
    
    # Cargar audio
    audio = load_audio_file(audio_file_path)
    
    # Transcribir audio
    result = model.transcribe(audio, language=language, batch_size=batch_size)
    
    return result
