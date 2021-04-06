from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.events import FollowupAction
from rasa_sdk.events import BotUttered
import mysql.connector
import logging
logger = logging.getLogger(__name__)



mydb = mysql.connector.connect(
  host="192.168.1.12",
  user="root",
  password="onslario89",
  port="31851",
  database="chatbot"
)

class ActionProductSearch(Action):
    def name(self) -> Text:
        return "action_product_search"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        # connect to DB
        mycursor = mydb.cursor()

        # get slots and save as tuple
        product = [(tracker.get_slot("comic")), int((tracker.get_slot("num_comic")))]

        # place cursor on correct row based on search criteria
        mycursor.execute("SELECT * FROM inventory WHERE item IN (%s) AND qty=%s", product)
        
        # retrieve sqlite row
        myresult = mycursor.fetchall()
        data_row=[]
        for x in myresult:
            data_row.append(x[0])

        # in any function
        logger.debug(data_row)

        if data_row:
            # provide in stock message
            dispatcher.utter_message(template="utter_in_stock")
            slots_to_reset = ["comic", "num_comic"]
            return [SlotSet(slot, None) for slot in slots_to_reset]
        else:
            # provide out of stock
            dispatcher.utter_message(template="utter_no_stock")
            slots_to_reset = ["comic", "num_comic"]
            return [SlotSet(slot, None) for slot in slots_to_reset]
