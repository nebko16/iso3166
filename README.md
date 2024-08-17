# [ISO 1366-1 Country Codes](https://en.wikipedia.org/wiki/ISO_3166-1)

<hr>

### Data last refreshed: 2024-08-17 05:57:35.

<br>
This repo is to provide a convenient and quick source for lookup data for `ISO 1366-1` country codes.  Most programmatic sources are behind a paywall, and the rest require you to manually parse them.

This data doesn't change too often, so you should be able to just grab one of the files in the [data](data/) directory (or links below) and be good to go.  If you want it to be fresh, you can clone the repo and run [the scraper](source/scrape.py) to refresh the files.  The data in the current files was updated 2024-08-17 05:57:35.

Scraping is legal, but not always perceived well, so scrape at your own discretion.  This ISO data doesn't change often, so scraping at build time is probably as frequent as you'd really need.

<br>

## JSON

<hr>

- [iso3166_from_alpha2.json](data/json/iso3166_from_alpha2.json)
- [iso3166_from_alpha3.json](data/json/iso3166_from_alpha3.json)
- [iso3166_from_numeric.json](data/json/iso3166_from_numeric.json)
- [iso3166_list.json](data/json/iso3166_list.json)

<br>

## YAML

<hr>

- [iso3166_from_alpha2.yaml](data/yaml/iso3166_from_alpha2.yaml)
- [iso3166_from_alpha3.yaml](data/yaml/iso3166_from_alpha3.yaml)
- [iso3166_from_numeric.yaml](data/yaml/iso3166_from_numeric.yaml)
- [iso3166_from_list.yaml](data/yaml/iso3166_from_list.yaml)

<br>

## SQL

<hr>

**DDL**
```sql

    CREATE TABLE iso3166 (
        `country_name` VARCHAR(255),
        `alpha2` CHAR(2),
        `alpha3` CHAR(3),
        `numeric` CHAR(3)
    );
    
```

**DML**
- [iso3166.sql](data/sql/iso3166.sql)

<br>

## CSV

<hr>

- [iso3166.csv](data/csv/iso3166.csv)

<br>

## Pickle

<hr>

- [iso3166_from_alpha2.pickle](data/pickle/iso3166_from_alpha2.pickle)
- [iso3166_from_alpha3.pickle](data/pickle/iso3166_from_alpha3.pickle)
- [iso3166_from_numeric.pickle](data/pickle/iso3166_from_numeric.pickle)
- [iso3166_list.pickle](data/pickle/iso3166_list.pickle)

<hr>

<br>