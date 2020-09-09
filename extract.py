
from bs4 import BeautifulSoup

def extract(page_source):
    laptops = []
    soup = BeautifulSoup(page_source, 'html.parser')
    for laptop_box in soup.select('div._3O0U0u'):
        name_box = laptop_box.select_one('div._3wU53n')
        rating_box = laptop_box.select_one('div.hGSR34')
        price_box = laptop_box.select_one('div._1vC4OE._2rQ-NK')
        name = name_box.string
        rating = get_rating(rating_box)
        price = price_box.string
        laptops.append({
            'name': name,
            'rating': rating,
            'price': price
        })
    return laptops

def get_rating(rating_box):
    if rating_box is None:
        return ''

    for string in rating_box.stripped_strings:
        return string

    return ''