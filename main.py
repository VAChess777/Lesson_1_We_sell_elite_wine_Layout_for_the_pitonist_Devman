import datetime

from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('vine_template.html')


# opening_winery_year = 1920


def get_years(opening_winery_year):
    year_now = datetime.datetime.now().year
    age_delta = year_now - opening_winery_year
    if age_delta % 10 == 1 and age_delta != 11 and age_delta % 100 != 11:  # +
        return "{0} год".format(age_delta)
    elif 1 < age_delta % 10 <= 4 and age_delta != 12 and age_delta != 13 and age_delta != 14:
        return "{0} года".format(age_delta)
    else:
        return "{0} лет".format(age_delta)


def main():
    rendered_page = template.render(
        cap1_title="Проверено временем",
        cap1_text=f'Уже {get_years(opening_winery_year)} с Вами!',
        # cap2_title="Чёрная кепка",
        # cap2_text="$ 120.00",
        # cap3_title="Ещё одна чёрная кепка",
        # cap3_text="$ 90.00",
    )
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':

    main()