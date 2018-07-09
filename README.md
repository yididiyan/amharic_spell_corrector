# Amharic Spelling Corrector

Spelling corrector can be handy where you need to post process outputs of an OCR(Optical Character Recognition), STT(Speech to text).

### Dependencies

* PySymSpell - pure Python port of [SymSpell](https://github.com/wolfgarbe/SymSpell).
* BeautifulSoap

### Installation
```bash
pip install -r requirements.txt
```

### Usage

#### Spelling correctortion

```python
from spell_corrector import lookup
suggestions = lookup('አሽናቆት')
suggestions[0].term
>> 'አድናቆት'
```

#### Edit Distance Calculation
The function calculates the number of edit [ insertion, update, delete ] needed to correct a word to another

```python
from spell_corrector import calculate_disance
calculate_distance('አክብሮትና', 'አክብሮት')
>> 1
```

#### Crawling More Words
The `crawler.py` script crawls around **1 million** frequently used Amharic words on the Web.
```bash
python crawler.py
```
