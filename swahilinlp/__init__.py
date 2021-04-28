import sys
import requests

# text = "Waziri anatoka Tanga"

class SwahiliNLP(object):
    def __init__(self):
        self.NER_URL = "https://bellbot.tech/api/v1/ner-swahili"

    @staticmethod
    def get_headers():
        return {"Content-Type": "application/json"}

    # NER
    def ner(self, sentence, json: bool = True):
        try:
            response = self._get_ner_response(sentence=sentence)
            return response
        except:
            return None

    def _get_ner_response(self, sentence):
        try:
            response = requests.get(
                self.NER_URL, json={"text": sentence}, headers=self.get_headers()
            ).json()
            return response
        except (requests.ConnectionError, requests.ConnectTimeout):
            raise ConnectionError("Ooops..! Something wrong happened.")


sys.modules[__name__] = SwahiliNLP()