import whisperx

def diarize_transcription(transcription_result, device="cuda"):
    # Cargar modelo de diarización
    diarize_model = whisperx.DiarizationPipeline(use_auth_token="YOUR_HF_TOKEN", device=device)
    
    # Aplicar diarización
    diarize_segments = diarize_model(transcription_result["audio"])
    
    return whisperx.assign_word_speakers(diarize_segments, transcription_result)
