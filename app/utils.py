import music21
import os
from  scipy.io.wavfile import write as write_wav
import numpy as np
import io
from synthesizer import Synthesizer,Waveform 

def note_to_freq(note_list):
    """Convert a list of music21 note objects to their corresponding frequencies."""
    freqs= []
    for note_str in note_list:
        try:
            not_ = music21.note.Note(note_str)
            freqs.append(not_.pitch.frequency)

        except:
            continue
    return freqs

def generate_wav_from_freqs(note_freqs):
    """Generate a WAV file from a list of frequencies."""
    synth = Synthesizer(osc1_waveform=Waveform.sine,osc1_volume=0.5,use_osc2=False)
    sample_rate = 44100
    audio =np.concatenate([synth.generate_constant_wave(freq,0.5) for freq in note_freqs])
    buffer = io.BytesIO()
    write_wav(buffer, sample_rate, audio.astype(np.float32))
    return buffer.getvalue()





