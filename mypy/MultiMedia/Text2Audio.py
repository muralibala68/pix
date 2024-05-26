import pyttsx3


class Text2Audio:
    def __init__(self):
        self.engine = pyttsx3.init()

    def __enter__(self):
        print("Context management: entering with block...")
        voices = self.engine.getProperty("voices")
        # 0 female, 1 male voice? defaults to female voice
        self.engine.setProperty("voice", voices[0].id)
        return self

    def __exit__(self, exc_type, exc_val, exc_trace):
        print("Context management: exiting with block...")
        self.engine.stop()
        if exc_type:
            print(f"Exception occurred: {exc_val}, {exc_trace}")
            return False  # cascading it...

    def say(self, what_2_say: str):
        if not what_2_say:
            self.engine.say("What do you want me to say?")
            self.engine.runAndWait()
            return
        self.engine.say(what_2_say)
        self.engine.runAndWait()


def main():
    what_2_say: str = input("What to say?")
    with Text2Audio() as text_2_audio:
        text_2_audio.say(what_2_say)


if __name__ == "__main__":
    main()
