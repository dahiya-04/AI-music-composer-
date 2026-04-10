import streamlit as st
from app.main import MusicLLM
from app.utils import *
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()
st.set_page_config(page_title="AI Music Composer",layout="centered")
st.title("AI MUSIC COMPOSER")
st.markdown("Generate AI Music by describing the style and content")

music_input =st.text_input("Describe the music you want to create (e.g., 'A happy, uplifting melody with a jazzy feel')")
style = st.selectbox("Select a style to adapt to",["Classical","Jazz","Rock","Pop","Electronic"])

if st.button("Generate Music") and music_input:
    genre = MusicLLM()
    with st.spinner("Generating music..."):
        melody = genre.generate_melody(music_input)
        harmony = genre.generate_harmony(melody)
        rhythm = genre.generate_rhythm(melody)
        styled_music = genre.adapt_style(style, melody, harmony, rhythm)
        st.subheader("Generated Music Summary")
        # st.write(styled_music)

        melody_notes = melody.split()
        melody_freqs = note_to_freq(melody_notes)

        harmony_chords = harmony.split(",")
        harmony_notes = []
        for chord in harmony_chords:
            harmony_notes.extend(chord.split("-"))
        harmony_freqs = note_to_freq(harmony_notes)
        
        all_freqs = melody_freqs+harmony_freqs
        wav_data = generate_wav_from_freqs(all_freqs)
        
    st.audio(BytesIO(wav_data), format="audio/wav")
    st.success("Music generated successfully!")

    with st.expander("Show summary of composition"):
        st.text(styled_music)

        