import pyttsx3

engine = pyttsx3.init()

say = input("What to say?")
voices = engine.getProperty("voices")
# 0 female, 1 male voice?
# defaults to female voice
engine.setProperty("voice", voices[1].id)
engine.say(say)
engine.runAndWait()
engine.stop()
