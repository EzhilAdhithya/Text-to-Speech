from gtts import gTTS

def text_to_speech():

    try:

        text = input("Enter the text: ")

        tts = gTTS(text=text, lang="en")

        tts.save("voice.mp3")

        print("audio saved successfully")
    
    except(EOFError, ValueError):
        pass

if __name__ == "__main__":
    while(1):
        print("Press 1 to convert your text to speech.")
        print("Press 2 to exit.")

        choice = int(input("Enter the Choice: "))

        if choice == 1:
            text_to_speech()
        elif choice == 2:
            break
        else:
            print("Invalid Input... Press 1 or 2.")