import edge_tts
import asyncio
import os

# Updated list of available voices including new English and Malayalam voices
voices = {
    "1": "en-US-AriaNeural",        # English Female
    "2": "en-US-AnaNeural",         # English Female
    "3": "en-US-ChristopherNeural", # English Male
    "4": "en-US-EricNeural",        # English Male
    "5": "en-US-GuyNeural",         # English Male
    "6": "en-US-JennyNeural",       # English Female
    "7": "en-US-MichelleNeural",    # English Female
    "8": "en-US-RogerNeural",       # English Male
    "9": "en-US-SteffanNeural",     # English Male
    "10": "ml-IN-MidhunNeural",     # Malayalam Male
    "11": "ml-IN-SobhanaNeural",    # Malayalam Female
    "12": "en-ZA-LeahNeural",       # English Female (South Africa)
    "13": "en-ZA-LukeNeural",       # English Male (South Africa)
    "14": "en-TZ-ElimuNeural",      # English Male (Tanzania)
    "15": "en-TZ-ImaniNeural",      # English Female (Tanzania)
    "16": "en-GB-LibbyNeural",      # English Female (United Kingdom)
    "17": "en-IN-NeerjaNeural",     # English Female (India)
    "18": "en-IN-PrabhatNeural",    # English Male (India)
}

# Function to save TTS audio
async def save_tts(text, selected_voice_code, output_path):
    try:
        voice = voices[selected_voice_code]
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output_path)
        print(f"Audio saved successfully to {output_path}")
    except KeyError:
        print("Error: Invalid voice selection. Please select a valid number from the list.")
    except edge_tts.exceptions.NoAudioReceived:
        print("Error: No audio was received. Please verify that your parameters are correct.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main execution
def main():
    print("Available Voices:")
    for number, voice in voices.items():
        print(f"{number}: {voice}")

    selected_voice_code = input("Enter the number of the voice you want to use: ")

    print("Enter the text you want to convert to speech. Type 'done' on a new line when you are finished:")
    
    # Collecting multi-line input
    input_lines = []
    while True:
        line = input()
        if line.lower() == "done":
            break
        input_lines.append(line)
    
    # Join all lines into a single text block
    text = "\n".join(input_lines)

    # Define output path in the Downloads folder
    output_path = "/storage/emulated/0/Download/output_audio.wav"

    # Run the TTS function
    asyncio.run(save_tts(text, selected_voice_code, output_path))

if __name__ == "__main__":
    main()
