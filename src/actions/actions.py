from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.1.12",
  user="root",
  password="onslario89",
  port="31851",
  database="chatbot"
)

class ComicsForm(FormAction):
# your form functions go here
    def name(self):
        return "comic_form"
    
    @staticmethod
    def required_slots(tracker): 
        '''
        it configures which slots are required by the form. 
        In addition to specifying the required slots, we’re also introducing a bit of conditional logic.
        '''

        return ["comic", "num_comic", "date"]
    
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked
            
            This function is optional when creating a form. 
            You need to map slots only if you don’t want to automatically fill 
            slots with entities of the same name, and want to enforce some other logic."""

        return {

            "comic": [
                self.from_entity(entity="comic"),
                self.from_intent(intent="deny", value="None"),
            ],
            "num_comic": [
                self.from_entity(entity="num_comic"),
                self.from_text(intent="deny"),
            ],
            "date": [
                self.from_entity(entity="date"),
                self.from_text(intent="deny"),
            ],
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
        ) -> List[Dict]:
        '''
        This tells the assistant what to do when all of the slots in the form have been filled.
        '''

        #check comic availability from here!!

        dispatcher.utter_message("Perfetto, cercherò il tuo albo!")
        return []
    

# class ValidateComicsForm(FormValidationAction):
#     """Example of a form validation action."""

#     def name(self) -> Text:
#         return "validate_comic_form"

#     @staticmethod
#     def comic_db() -> List[Text]:
#         """Database of supported cuisines."""

#         mycursor = mydb.cursor()
#         mycursor.execute("SELECT * FROM inventory")
#         myresult = mycursor.fetchall()
#         list=[]
#         for x in myresult:
#             list.append(x[0])
#         return list

#     @staticmethod
#     def is_int(string: Text) -> bool:
#         """Check if a string is an integer."""

#         try:
#             int(string)
#             return True
#         except ValueError:
#             return False

#     def validate_comic(
#         self,
#         value: Text,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> Dict[Text, Any]:
#         """Validate cuisine value."""

#         if value.lower() in self.comic_db():
#             # validation succeeded, set the value of the "cuisine" slot to value
#             return {"comic": value}
#         else:
#             dispatcher.utter_message(response="utter_wrong_comic")
#             # validation failed, set this slot to None, meaning the
#             # user will be asked for the slot again
#             return {"comic": None}

#     def validate_num_comic(
#         self,
#         value: Text,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> Dict[Text, Any]:
#         """Validate num_people value."""

#         if self.is_int(value) and int(value) > 0:
#             return {"num_comic": value}
#         else:
#             dispatcher.utter_message(response="utter_wrong_num_comic")
#             # validation failed, set slot to None
#             return {"num_comic": None}
