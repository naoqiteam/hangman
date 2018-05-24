
class Hangman():
    def __init__(self, app):
        app.start()
        session = app.session
        self.tts = session.service("ALTextToSpeech")

    def play(self):
        self.tts.say("Hallo.")
