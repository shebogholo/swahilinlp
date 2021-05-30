# Swahili Natural Language Processing (NLP) Library.

A Python library for doing natural language processing on swahili corpus.

## Getting started

```python
>>> from swahilinlp import SwahiliNLP
>>> sentensi = SwahiliNLP('kwenye soka mesi anajua sana')
>>> sentensi.sentiment
{'label': 'Positive', 'prob': '0.75'}
>>> sentensi.language
{'lang': 'Swahili'}
>>> sentensi.entities
[]
```