# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler, FallbackSkill
from mycroft.util.log import LOG
import requests

# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.

# TODO: Change "Template" to a unique name for your skill
class SoftSourceDecideSkill(FallbackSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(SoftSourceDecideSkill, self).__init__(name="SoftSourceDecideSkill")
        
        # Initialize working variables used within the skill.
        self.register_fallback(self.handle_fallback, 10)
        requests
    
    
    def handle_fallback(self, message):
        utterance = message.data.get("utterance")
        LOG.debug("Utterance is: " + utterance)
        payload = utterance
       // r = requests.post('https://directline.botframework.com/v3/directline/conversations', json=payload)
        r = requests.post('https://softsourcechatbot.azurewebsites.net/api/values', json=payload, headers={'Authentication':'Bearer odJ5VKzB8oY.cwA.9E0.IkVvS809oGsfqJPFTe4kui6sYWbPXqUbSTUnLncIn_U'})        
        LOG.debug("POST response text is " + r.text)
        self.speak(r.text.strip('\"'))
        return True

    def shutdown(self):
        """
            Remove this skill from list of fallback skills.
        """
        self.remove_fallback(self.handle_fallback)
        super(SoftSourceDecideSkill, self).shutdown()

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return SoftSourceDecideSkill()
