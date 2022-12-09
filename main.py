import datetime
import os
import pathlib
from collections import defaultdict
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

import pandas
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader, select_autoescape


def get_years(opening_winery_year):
    year_now = datetime.datetime.now().year
    age_delta = year_now - int(opening_winery_year)
    if age_delta % 10 == 1 and age_delta != 11 and age_delta % 100 != 11:
        return f'{age_delta} год'
    elif 1 < age_delta % 10 <= 4 and age_delta != 12 and age_delta != 13\
            and age_delta != 14:
        return f'{age_delta} года'
    else:
        return f'{age_delta} лет'


def get_goods(excel_filepath):
    goods_category = pandas.read_excel(
        excel_filepath,
        keep_default_na=False
    ).to_dict(orient="records")
    goods_cards = defaultdict(list)
    for goods in goods_category:
        goods_cards[goods["Категория"]].append(goods)
    return goods_cards


def render_page(excel_filepath, opening_winery_year):
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    winery_age = f'Уже {get_years(opening_winery_year)} с вами:'
    rendered_page = template.render(
        winery_age=winery_age,
        goods_cards=get_goods(excel_filepath)
    )
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


def main():
    load_dotenv()
    excel_filename = os.getenv('EXCEL_FILE')
    excel_filepath = Path(pathlib.Path.cwd(), excel_filename)
    opening_winery_year = os.getenv('OPENING_WINERY_YEAR')
    render_page(excel_filepath, opening_winery_year)
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':

    main()