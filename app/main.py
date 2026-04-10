import os
# Use this for modern LangChain versions (>= 0.1.0)
from langchain_core.prompts import ChatPromptTemplate

from langchain_groq import ChatGroq

class MusicLLM:
    def __init__(self,temperature=0.7):
        self.llm = ChatGroq(temperature=temperature,
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.1-8b-instant")
        
    def generate_melody(self, prompt):
        """Generate a melody based on the given prompt."""
        chat_prompt = ChatPromptTemplate.from_template(
            "You are a music composer. Given the following prompt, generate a melody in the form of a list of music21 note objects: {prompt} .Represent the melody as a space-separated list of note names (e.g., C4, E4, G4)."
        )
        chain = chat_prompt | self.llm
        return chain.invoke({"prompt": prompt}).content.strip()

    def generate_harmony(self,melody):
        """Generate a harmony for the given melody."""
        chat_prompt = ChatPromptTemplate.from_template(
            "You are a music composer. Given the following melody, generate a harmony in the form of a list of music21 note objects: {melody} .Represent the harmony as a space-separated list of note names (e.g., C4-E4-G4, F4-A4-C5)."
        )
        chain = chat_prompt | self.llm
        return chain.invoke({"melody": melody}).content.strip()

    def generate_rhythm(self,melody):
        """Generate a rhythm pattern for the given melody."""
        chat_prompt = ChatPromptTemplate.from_template(
            "You are a music composer. Given the following melody, generate a rhythm pattern in the form of a list of beat corresponding to each note in the melody: {melody} .Represent the rhythm as Format: 1.0 0.5 0.5 2.0."
        )
        chain = chat_prompt | self.llm
        return chain.invoke({"melody": melody}).content.strip()

    def adapt_style(self,style,melody,harmony,rhythm):
        prompt = ChatPromptTemplate.from_template(
            "Adapt to {style} style: \n Melody: {melody}\nHarmony: {harmony}\n Rhythm: {rhythm}\nOutput single string summary"
        )

        chain = prompt | self.llm

        return chain.invoke({
            "style" : style,
            "melody" : melody,
            "harmony" : harmony,
            "rhythm" :rhythm
        }).content.strip()
