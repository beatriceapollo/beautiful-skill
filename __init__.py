from mycroft import MycroftSkill, intent_handler
from adapt.intent import IntentBuilder


class Beautiful(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder('BeautifulIntent').require('beautiful'))
    def handle_beautiful(self, message):
        self.speak("thank you")


def create_skill():
    return Beautiful()

