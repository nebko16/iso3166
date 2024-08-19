from jinja2 import Environment, FileSystemLoader
from bs4 import BeautifulSoup
from datetime import datetime
from sources import sources
from typing import Any
import requests
import pickle
import yaml
import json
import csv


env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('README.md.jinja2')
readme_interpolate = {'last_refreshed': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}


def scrape(source_doc):
    url = source_doc.get('url')
    user_agent = (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
        'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15')
    headers = {
        'User-Agent': user_agent,
        'Content-Type': 'text/html',
        'charset': 'utf-8'
    }
    response = requests.get(url, headers=headers)
    return response.text


def get_tables(source, source_doc):
    html = source_doc.get('html')
    if not html:
        return False

    soup = BeautifulSoup(html, 'html.parser')

    if source == 'wiki':
        caption = soup.find('caption', string="ISO 3166-1 table\n")
        return [caption.find_parent('table')]

    elif source == 'iban':
        return [soup.find('table', id='myTable')]

    elif source == 'nationsonline':
        ids = [
            'Country-Codes-A-C',
            'Country-Codes-D-H',
            'CountryCodes-I-L',
            'Country-Codes-M-P',
            'Country-Codes-Q-T',
            'Country-Codes-U-Z'
        ]
        return [soup.find('table', id=i) for i in ids]


def bad_col_count(cols, expected_count):
    if len(cols) != expected_count:
        return True
    for col in cols:
        if int(col.get('colspan', 1)) > 1:
            return True


def parse(tables, source_doc):
    countries = []
    if not isinstance(tables, list):
        tables = [tables]
    col_names = source_doc.get('cols', {})
    for table in tables:
        rows = table.find_all('tr')[1:]
        for row in rows:
            cols = row.find_all('td')

            if bad_col_count(cols, source_doc.get('columns')):
                continue

            if int(cols[0].get('colspan', 1)) > 1:
                continue

            try:
                countries.append({
                    'country_name': cols[col_names.get('country_name')].text.strip(),
                    'alpha2': cols[col_names.get('alpha2')].text.strip(),
                    'alpha3': cols[col_names.get('alpha3')].text.strip(),
                    'numeric': cols[col_names.get('numeric')].text.strip(),
                })
            except Exception as e_err:
                print(row)
                print(e_err)
                exit()
    return countries


def to_csv(countries, output_dir):
    csv_file = '../data/csv/iso3166.csv'
    csv_columns = ['country_name', 'alpha2', 'alpha3', 'numeric']
    try:
        with open(csv_file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in countries:
                writer.writerow(data)
    except IOError:
        print("I/O error")


def to_yaml_json(countries, output_dir):
    json_data = {'iso3166': countries}

    with open('../data/json/iso3166_collection.json', 'w') as fh:
        fh.write(json.dumps(json_data, indent=4, sort_keys=True))

    with open(f"{output_dir}/yaml/iso3166_collection.yaml", 'w') as fh:
        yaml.dump({'iso3166': countries}, fh, default_flow_style=False)

    with open(f"{output_dir}/yaml/iso3166_from_alpha2.yaml", 'w') as fh:
        alpha2_to_country = {}
        for _country in countries:
            country = _country.copy()
            alpha2 = country.pop('alpha2')
            alpha2_to_country[alpha2] = country
        yaml.dump(alpha2_to_country, fh, default_flow_style=False)

    with open(f"{output_dir}/yaml/iso3166_from_alpha2.yaml", 'r', encoding='utf-8') as fh:
        readme_interpolate.update({
            'yaml_alpha2': fh.read()
        })

    with open('../data/json/iso3166_from_alpha2.json', 'w') as fh:
        fh.write(json.dumps(alpha2_to_country, indent=4, sort_keys=True))

    readme_interpolate.update({
        'json_alpha2': json.dumps(alpha2_to_country, indent=4, sort_keys=True)
    })

    with open(f"{output_dir}/yaml/iso3166_from_alpha3.yaml", 'w') as fh:
        alpha3_to_country = {}
        for _country in countries:
            country = _country.copy()
            alpha3 = country.pop('alpha3')
            alpha3_to_country[alpha3] = country
        yaml.dump(alpha3_to_country, fh, default_flow_style=False)

    with open('../data/json/iso3166_from_alpha3.json', 'w') as fh:
        fh.write(json.dumps(alpha3_to_country, indent=4, sort_keys=True))

    with open(f"{output_dir}/yaml/iso3166_from_numeric.yaml", 'w') as fh:
        numeric_to_country = {}
        for _country in countries:
            country = _country.copy()
            numeric = country.pop('numeric')
            numeric_to_country[numeric] = country
        yaml.dump(numeric_to_country, fh, default_flow_style=False)

    with open('../data/json/iso3166_from_numeric.json', 'w') as fh:
        fh.write(json.dumps(numeric_to_country, indent=4, sort_keys=True))


def to_sql(countries, output_dir):
    ddl_statement = """
CREATE TABLE iso3166 (
    `country_name` VARCHAR(255),
    `alpha2` CHAR(2),
    `alpha3` CHAR(3),
    `numeric` CHAR(3)
);
    """
    with open(f"{output_dir}/sql/iso3166_ddl.sql", 'w') as f:
        f.write(ddl_statement)

    readme_interpolate.update({'sql_ddl': ddl_statement})

    insert_statements = []
    for country in countries:
        insert_statement = f"""INSERT INTO iso3166 (country_name, alpha2, alpha3, numeric) VALUES ('{country.get('country_name').replace("'", "''")}', '{country.get('alpha2').replace("'", "''")}', '{country.get('alpha3').replace("'", "''")}', '{country.get('numeric').replace("'", "''")}');"""
        insert_statements.append(insert_statement.strip())
    sql_script = f"/*\n{ddl_statement}\n*/\n\n{"\n".join(insert_statements)}\nCOMMIT;\n"
    with open(f"{output_dir}/sql/iso3166_dml.sql", 'w') as f:
        f.write(sql_script)


def to_pickle(countries, output_dir):
    _pickle(countries, f"{output_dir}/pickle/iso3166_collection.pickle")

    alpha2_to_country = {}
    for _country in countries:
        country = _country.copy()
        alpha2 = country.pop('alpha2')
        alpha2_to_country[alpha2] = country
    _pickle(alpha2_to_country, f"{output_dir}/pickle/iso3166_from_alpha2.pickle")

    alpha3_to_country = {}
    for _country in countries:
        country = _country.copy()
        alpha3 = country.pop('alpha3')
        alpha3_to_country[alpha3] = country
    _pickle(alpha3_to_country, f"{output_dir}/pickle/iso3166_from_alpha3.pickle")

    numeric_to_country = {}
    for _country in countries:
        country = _country.copy()
        numeric = country.pop('numeric')
        numeric_to_country[numeric] = country
    _pickle(numeric_to_country, f"{output_dir}/pickle/iso3166_from_numeric.pickle")


def _pickle(obj: Any, filepath: str):
    with open(filepath, 'wb') as fh:
        pickle.dump(obj, fh)


def _unpickle(filepath) -> Any:
    with open(filepath, 'rb') as fh:
        return pickle.load(fh)


def process():
    output_dir = f"../data"
    for source, source_doc in sources.items():
        print(source)
        source_doc['html'] = scrape(source_doc)
        tables = get_tables(source, source_doc)
        if tables:
            countries = parse(tables, source_doc)
            to_csv(countries, output_dir)
            to_yaml_json(countries, output_dir)
            to_sql(countries, output_dir)
            to_pickle(countries, output_dir)
            return


if __name__ == '__main__':

    process()

    rendered_content = template.render(readme_interpolate)

    with open('../README.md', 'w') as fh:
        fh.write(rendered_content)
