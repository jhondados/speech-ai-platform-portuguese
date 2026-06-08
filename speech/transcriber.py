"""Real-time speech transcription with Whisper."""
import whisper
import pyaudio
import numpy as np
import queue
from pyannote.audio import Pipeline
from typing import Generator

class RealTimeTranscriber:
    def __init__(self, model_path: str = "large-v3", language: str = "pt"):
        self.model = whisper.load_model(model_path)
        self.language = language
        self.audio_queue = queue.Queue()
        self.CHUNK = 1024 * 4
        self.RATE = 16000

    def transcribe_file(self, audio_path: str) -> dict:
        result = self.model.transcribe(audio_path, language=self.language,
            task="transcribe", word_timestamps=True, verbose=False)
        return {"text": result["text"], "segments": result["segments"],
                "language": result["language"]}

    def stream_transcribe(self) -> Generator[str, None, None]:
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paFloat32, channels=1, rate=self.RATE,
                        input=True, frames_per_buffer=self.CHUNK)
        print("Listening... (Ctrl+C to stop)")
        audio_buffer = []
        try:
            while True:
                data = stream.read(self.CHUNK)
                audio_np = np.frombuffer(data, dtype=np.float32)
                audio_buffer.extend(audio_np)
                if len(audio_buffer) >= self.RATE * 3:  # 3-second chunks
                    chunk = np.array(audio_buffer[-self.RATE*3:])
                    result = self.model.transcribe(chunk, language=self.language)
                    if result["text"].strip():
                        yield result["text"].strip()
        except KeyboardInterrupt:
            stream.stop_stream(); stream.close(); p.terminate()
