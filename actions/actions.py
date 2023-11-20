# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from weather_forecast import get_weather_data

# class ActionFallback(Action):

#     def name(self):
#         return "action_fallback"

#     def run(self, dispatcher, tracker, domain):
#         dispatcher.utter_message("I couldn't understand your request. Please try rephrasing it or asking something else.")
#         return []

class ActionExtractCityName(Action):

    def name(self):
        return "action_extract_city_name"

    def run(self, dispatcher, tracker, domain):
        latest_message = tracker.latest_message
        city_name = latest_message.get("text")
        dispatcher.utter_message(f"I understand that your location is {city_name}.")
        return [city_name]

class Action_weather_condition(Action):

    def name(self) -> Text:
        return "Action_weather_condition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            print(tracker)

            slot_value = tracker.get_slot("location")
            # entities = tracker.latest_message.get("entities", [])
            # for entity in entities:
            #     city=entity

            print(slot_value)

            response = get_weather_data(slot_value)

            text = " The temperature in the "+str(response.get("city"))+" is "+str(response.get("temp"))+". And the climate is "+str(response.get("climate"))

            dispatcher.utter_message(text)


            return [SlotSet("location", None)]
