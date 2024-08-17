sources = {
    'iban': {
        'url': 'https://www.iban.com/country-codes',
        'cols': {
            'country_name': 0,
            'alpha2': 1,
            'alpha3': 2,
            'numeric': 3,
        },
        'columns': 4
    },
    'wiki': {
        'url': 'https://en.wikipedia.org/wiki/ISO_3166-1',
        'cols': {
            'country_name': 0,
            'alpha2': 1,
            'alpha3': 2,
            'numeric': 3,
        },
        'columns': 6
    },
    'nationsonline': {
        'url': 'https://www.nationsonline.org/oneworld/country_code_list.htm',
        'cols': {
            'country_name': 1,
            'alpha2': 2,
            'alpha3': 3,
            'numeric': 4,
        },
        'columns': 5
    },
}
