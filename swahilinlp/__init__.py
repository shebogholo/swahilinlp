import sys
import requests

# text = "Waziri anatoka Tanga"

class SwahiliNLP(object):
    def __init__(self):
        self.NER_URL = "https://bellbot.tech/api/v1/ner-swahili"
        self.SENTIMENT_URL = "https://bellbot.tech:81/analyse"
        self.LANGID_URL = "https://bellbot.tech:124/v1/langid"

    @staticmethod
    def get_headers():
        return {"Content-Type": "application/json"}

    # NER
    def ner(self, sentence, json: bool = True):
        try:
            response = self._get_response(url=self.NER_URL, sentence=sentence)
            return response
        except:
            return None

    def sentiment(self, sentence, json: bool = True):
        try:
            response = self._get_response(url=self.SENTIMENT_URL, sentence=sentence)
            return response
        except:
            return None
    
    # African Languages Identification
    def langid(self, sentence, json: bool = True):
        try:
            response = self._get_response(url=self.LANGID_URL, sentence=sentence)
            return response
        except:
            return None

    def _get_response(self, url, sentence):
        try:
            response = requests.get(
                url, json={"text": sentence}, headers=self.get_headers()
            ).json()
            return response
        except (requests.ConnectionError, requests.ConnectTimeout):
            raise ConnectionError("Ooops..! Something wrong happened.")


sys.modules[__name__] = SwahiliNLP()