from gtts import gTTS
import os
import time

def text_to_speech_multi():
    try:
        text = input("Enter the text: ")
        filename = input("Enter the filename (press Enter for auto-generated name): ")
        
        if not filename:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"voice_{timestamp}"
            
        tts = gTTS(text=text, lang="en")
        tts.save(f"{filename}.mp3")
        print(f"Audio saved successfully as '{filename}.mp3'")
    except(EOFError, ValueError):
        pass

if __name__ == "__main__":
    while(1):
        print("Press 1 to convert your text to speech.")
        print("Press 2 to exit.")

        choice = int(input("Enter the Choice: "))

        if choice == 1:
            text_to_speech_multi()
        elif choice == 2:
            break
        else:
            print("Invalid Input... Press 1 or 2.")