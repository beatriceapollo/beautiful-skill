from mycroft import MycroftSkill, intent_file_handler


class Beautiful(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('beautiful.intent')
    def handle_beautiful(self, message):
        self.speak_dialog('beautiful')


def create_skill():
    return Beautiful()

