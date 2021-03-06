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
# from the MycroftSkill class.  
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
        r = requests.post('https://directline.botframework.com/v3/directline/conversations', json=payload, 
                           headers={'Authorization':'Bearer odJ5VKzB8oY.cwA.9E0.IkVvS809oGsfqJPFTe4kui6sYWbPXqUbSTUnLncIn_U'})    
                                                                                                                                        
        
        LOG.debug("POST response r.text is " + r.text)
        payload2 = { 'type': 'message', 'from': {'id': 'mycroftclient'}, 'text': utterance }
        requests.post('https://directline.botframework.com/v3/directline/conversations/' + r.json()['conversationId'] + '/activities', headers={'Authorization':'Bearer '+r.json()['token']}, json=payload2)

        r3 = requests.get('https://directline.botframework.com/v3/directline/conversations/' 
                          + r.json()['conversationId'] + '/activities', 
                          headers={'Authorization':'Bearer '+r.json()['token']}) 
        LOG.debug("GET response r3.text is " + r3.text)

        lastActivityIndex = len(r3.json()['activities']) - 1
        
        dialogText = r3.json()['activities'][lastActivityIndex]['text'] 
        if dialogText.startswith('Sorry, I do not understand'):
            return False

        self.speak(dialogText)
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
