from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger

class FirstRoboticsSkill(MycroftSkill):
    def __init__(self):
        super(FirstRoboticsSkill, self).__init__(name="FirstRoboticsSkill")

    @intent_handler(IntentBuilder("StartRobotIntent").require('StartRobot'))
    def handle_start_robot(self, message):
        self.speak_dialog('start.robot')

    @intent_handler(IntentBuilder("StopRobotIntent").require('StopRobot'))
    def handle_stop_robot(self, message):
        self.speak_dialog('stop.robot')

