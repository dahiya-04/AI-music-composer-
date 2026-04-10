#!/usr/bin/env python3
"""
Quick test script to verify main.py is working correctly
"""
import os
from dotenv import load_dotenv
from app.main import MusicLLM

# Load environment variables
load_dotenv()

def test_main():
    print("=" * 60)
    print("Testing AI Music Composer - main.py")
    print("=" * 60)
    
    # Check API key
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("❌ GROQ_API_KEY not found in .env file")
        return False
    print("✓ GROQ_API_KEY found")
    
    # Initialize MusicLLM
    print("\n1. Initializing MusicLLM...")
    try:
        music_composer = MusicLLM(temperature=0.7)
        print("✓ MusicLLM initialized successfully")
    except Exception as e:
        print(f"❌ Failed to initialize MusicLLM: {e}")
        return False
    
    # Test generate_melody
    print("\n2. Testing generate_melody()...")
    try:
        melody = music_composer.generate_melody("Create a happy uplifting melody")
        print(f"✓ Melody generated: {melody[:100]}...")
    except Exception as e:
        print(f"❌ Failed to generate melody: {e}")
        return False
    
    # Test generate_harmony
    print("\n3. Testing generate_harmony()...")
    try:
        harmony = music_composer.generate_harmony(melody)
        print(f"✓ Harmony generated: {harmony[:200]}...")
    except Exception as e:
        print(f"❌ Failed to generate harmony: {e}")
        return False
    
    # Test generate_rhythm
    print("\n4. Testing generate_rhythm()...")
    try:
        rhythm = music_composer.generate_rhythm(melody)
        print(f"✓ Rhythm generated: {rhythm[:200]}...")
    except Exception as e:
        print(f"❌ Failed to generate rhythm: {e}")
        return False
    
    # Test adapt_style
    print("\n5. Testing adapt_style()...")
    try:
        styled = music_composer.adapt_style("Jazz", melody, harmony, rhythm)
        print(f"✓ Style adapted: {styled[:200]}...")
    except Exception as e:
        print(f"❌ Failed to adapt style: {e}")
        return False
    
    print("\n" + "=" * 60)
    print("✓ All tests passed! main.py is working correctly!")
    print("=" * 60)
    return True

if __name__ == "__main__":
    success = test_main()
    exit(0 if success else 1)
