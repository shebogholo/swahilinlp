# Swahili Natural Language Processing (NLP) Library.

### Installation
```
    pip install swahilinlp --upgrade
```

### Usage
1. Language Identification
```python
    from swahilinlp import langid
    langid('hii ni lugha nzuri afrika')
```


```
    {
        'lang': 'Swahili'
    }
```

2. Named Entity Recognition (NER)
```python
    from swahilinlp import ner
    ner('Mimi ni Waziri Shebogholo, natokea Tanga.')
```


```
    [
        {
            'end': 25,
            'entity': 'Person',
            'score': 1.0,
            'start': 8,
            'value': 'Waziri Shebogholo'
        },
        {
            'end': 40,
            'entity': 'Location',
            'score': 1.0,
            'start': 35,
            'value': 'Tanga'
        }
    ]
```

3. Sentiment Analysis
```python
    from swahilinlp import sentiment    
    sentiment('Leo simba wamecheza mpira mzuri sana, pira biriani')
```


```
    {
        'label': 'Positive', 
        'prob': '0.95'
    }
```