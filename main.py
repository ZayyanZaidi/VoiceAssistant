import datetime
import pyttsx3
import speech_recognition as sr
from customtkinter import CTk, CTkButton


class VoiceAssistantGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Voice Assistant")
        self.master.geometry('600x400')
        self.start_button = CTkButton(self.master, text='START', font=("times new roman", 14), command=self.start_option)
        self.start_button.place(x=150, y=320)
        self.close_button = CTkButton(self.master, text='CLOSE', font=("times new roman", 14), command=self.close_window)
        self.close_button.place(x=350, y=320)
        self.engine = pyttsx3.init()
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
    def start_option(self):
        # Greet the user based on the time
        current_time = datetime.datetime.now().strftime("%H:%M")
        if "00:00" <= current_time < "12:00":
            self.speak("Good morning! How can I assist you?")
        elif "12:00" <= current_time < "18:00":
            self.speak("Good afternoon! How can I assist you?")
        else:
            self.speak("Good evening! How can I assist you?")
        user_input = self.listen()
        response = self.process_input(user_input)
        self.speak(response)

    def listen(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            # Use Google's free Web Speech API for speech recognition
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
            return ""
        except sr.RequestError as e:
            print("Sorry, there was an error with the speech recognition service; {0}".format(e))
            return ""

    def process_input(self, input_text):
        if "time" in input_text:
            current_time = datetime.datetime.now().strftime("%H:%M")
            return "The current time is " + current_time
        elif "date" in input_text:
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            return "Today's date is " + current_date
        elif "hello" in input_text:
            return "Hello! What would you like me to do for you today?"
        elif "make me a sandwich" in input_text:
            return "Abra Cadabra! You're a Sandwich"
        else:
            return "Sorry, I didn't catch that. Can you please repeat?"

    # Close the window
    def close_window(self):
        self.master.destroy()

# Create the main window using custom tkinter
root = CTk()
app = VoiceAssistantGUI(root)
root.mainloop()

