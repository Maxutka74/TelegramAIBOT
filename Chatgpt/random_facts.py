from random import randint

CATEGORY_FACTS = {
    1: 'Історія',
    2: 'Кіно',
    3: 'Ігри',
    4: 'Природа',
    5: 'Наука',
    6: 'Географія',
    7: 'Культура',
    8: 'Людське тіло',
    9: 'Космос',
    10: 'Технології'
}

def generate_category(start: int = 1, end: int = 5) -> str:
    return CATEGORY_FACTS.get(randint(start, end), 'History')

