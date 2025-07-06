"""Audio rendering for CommitWav."""
import io
import wave
import math
import struct

SAMPLE_RATE = 48000
DURATION = 1  # seconds


def render_audio(data):
    """Return WAV bytes from analysis data."""
    buffer = io.BytesIO()
    with wave.open(buffer, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        frames = bytearray()
        for i in range(int(SAMPLE_RATE * DURATION)):
            sample = int(32767 * math.sin(2 * math.pi * 440 * i / SAMPLE_RATE))
            frames += struct.pack('<h', sample)
        wf.writeframes(frames)
    return buffer.getvalue()
