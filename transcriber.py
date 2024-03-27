def transcribe_audio(audio_file_path, language="es", device="cuda", batch_size=16, compute_type="int8"):
    # Inicialización del modelo de transcripción
    model = whisperx.load_model("large-v2", device, compute_type=compute_type)

    # Carga del audio utilizando la función específica de WhisperX
    audio = whisperx.load_audio(audio_file_path)

    # Transcripción del audio
    transcription_result = model.transcribe(audio, language=language, batch_size=batch_size)

    # Alineación (si es necesario para tu flujo de trabajo)
    model_a, metadata = whisperx.load_align_model(language_code=language, device=device)
    aligned_result = whisperx.align(transcription_result["segments"], model_a, metadata, audio, device, return_char_alignments=False)

    # Diarización y asignación de etiquetas a los hablantes (opcional)
    # Nota: Reemplaza YOUR_HF_TOKEN con tu token de Hugging Face si usas esta funcionalidad
    diarize_model = whisperx.DiarizationPipeline(use_auth_token="YOUR_HF_TOKEN", device=device)
    diarize_segments = diarize_model(audio)
    final_result = whisperx.assign_word_speakers(diarize_segments, aligned_result)

    return final_result
