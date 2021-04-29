import sys
import requests
from typing import List, Dict

# text = "Waziri anatoka Tanga"


class SwahiliNLP(object):

    NER_URL = "https://bellbot.tech/api/v1/ner-swahili"
    SENTIMENT_URL = "https://bellbot.tech:81/analyse"
    LANGID_URL = "https://bellbot.tech:124/v1/langid"

    def __init__(self, sentence: str):
        if not isinstance(sentence, str):
            raise TypeError(
                f"Sentensi must of type <str> not {type(sentence)}")

        self.sentence = sentence

    @staticmethod
    def get_headers():
        return {"Content-Type": "application/json"}

    @property
    def entities(self) -> List:
        """Named Entity Recognition

        Here an example

        >>> from swahilinlp import SwahiliNLP
        >>> sentensi = SwahiliNLP('kwenye soka mesi anajua sana')
        >>> sentensi.entities
        [.....]

        Returns:
            List: [recognized entities]
        """
        try:
            return self._get_response(url=self.NER_URL, sentence=self.sentence)
        except:
            return None

    @property
    def sentiment(self) -> Dict:
        """sentiment [Return sentiment score of sentensi]

        Here an example;

        >>> from swahilinlp import SwahiliNLP
        >>> sentensi = SwahiliNLP('kwenye soka mesi anajua sana')
        >>> sentensi.sentiment
        {'label': 'Positive', 'prob': '0.75'}

        Returns:
            Dict: [description]
        """
        try:
            return self._get_response(
                url=self.SENTIMENT_URL, sentence=self.sentence)
        except:
            return None

    # African Languages Identification

    @property
    def language(self):
        """language [Detect language of the sentence]

        >>> from swahilinlp import SwahiliNLP
        >>> sentensi = SwahiliNLP('kwenye soka mesi anajua sana')
        >>> sentensi.langid()
        {'lang': 'Swahili'}

        Returns:
            [type]: [detected language]
        """
        try:
            return self._get_response(
                url=self.LANGID_URL, sentence=self.sentence)
        except:
            return None

    def _get_response(self, url: str, sentence: str) -> Dict:
        try:
            return requests.get(
                url, json={"text": sentence}, headers=self.get_headers()
            ).json()
        except (requests.ConnectionError, requests.ConnectTimeout):
            raise ConnectionError("Ooops..! Something wrong happened.")


# sys.modules[__name__] = SwahiliNLP()
