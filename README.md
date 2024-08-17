# [ISO 1366-1 Country Codes](https://en.wikipedia.org/wiki/ISO_3166-1)

<hr>

### Data last refreshed: 2024-08-17 05:09:06.

<br>
This repo is to provide a convenient and quick source for lookup data for `ISO 1366-1` country codes.  Most programmatic sources are behind a paywall, and the rest require you to manually parse them.

This data doesn't change too often, so you should be able to just grab one of the files in the [data](data/) directory (or links below) and be good to go.  If you want it to be fresh, you can clone the repo and run [the scraper](source/scrape.py) to refresh the files.  The data in the current files was updated 2024-08-17 05:09:06.

Scraping is legal, but not always perceived well, so scrape at your own discretion.  This ISO data doesn't change often, so scraping at build time is probably as frequent as you'd really need.

<br>

## JSON

<hr>

[iso3166_from_alpha2.json](data/json/iso3166_from_alpha2.json)
```json
{
    "AD": {
        "alpha3": "AND",
        "country_name": "Andorra",
        "numeric": "020"
    },
    "AE": {
        "alpha3": "ARE",
        "country_name": "United Arab Emirates (the)",
        "numeric": "784"
    },
    "AF": {
        "alpha3": "AFG",
        "country_name": "Afghanistan",
        "numeric": "004"
    },
    "AG": {
        "alpha3": "ATG",
        "country_name": "Antigua and Barbuda",
        "numeric": "028"
    },
    "AI": {
        "alpha3": "AIA",
        "country_name": "Anguilla",
        "numeric": "660"
    },
    "AL": {
        "alpha3": "ALB",
        "country_name": "Albania",
        "numeric": "008"
    },
    "AM": {
        "alpha3": "ARM",
        "country_name": "Armenia",
        "numeric": "051"
    },
    "AO": {
        "alpha3": "AGO",
        "country_name": "Angola",
        "numeric": "024"
    },
    "AQ": {
        "alpha3": "ATA",
        "country_name": "Antarctica",
        "numeric": "010"
    },
    "AR": {
        "alpha3": "ARG",
        "country_name": "Argentina",
        "numeric": "032"
    },
    "AS": {
        "alpha3": "ASM",
        "country_name": "American Samoa",
        "numeric": "016"
    },
    "AT": {
        "alpha3": "AUT",
        "country_name": "Austria",
        "numeric": "040"
    },
    "AU": {
        "alpha3": "AUS",
        "country_name": "Australia",
        "numeric": "036"
    },
    "AW": {
        "alpha3": "ABW",
        "country_name": "Aruba",
        "numeric": "533"
    },
    "AX": {
        "alpha3": "ALA",
        "country_name": "\u00c5land Islands",
        "numeric": "248"
    },
    "AZ": {
        "alpha3": "AZE",
        "country_name": "Azerbaijan",
        "numeric": "031"
    },
    "BA": {
        "alpha3": "BIH",
        "country_name": "Bosnia and Herzegovina",
        "numeric": "070"
    },
    "BB": {
        "alpha3": "BRB",
        "country_name": "Barbados",
        "numeric": "052"
    },
    "BD": {
        "alpha3": "BGD",
        "country_name": "Bangladesh",
        "numeric": "050"
    },
    "BE": {
        "alpha3": "BEL",
        "country_name": "Belgium",
        "numeric": "056"
    },
    "BF": {
        "alpha3": "BFA",
        "country_name": "Burkina Faso",
        "numeric": "854"
    },
    "BG": {
        "alpha3": "BGR",
        "country_name": "Bulgaria",
        "numeric": "100"
    },
    "BH": {
        "alpha3": "BHR",
        "country_name": "Bahrain",
        "numeric": "048"
    },
    "BI": {
        "alpha3": "BDI",
        "country_name": "Burundi",
        "numeric": "108"
    },
    "BJ": {
        "alpha3": "BEN",
        "country_name": "Benin",
        "numeric": "204"
    },
    "BL": {
        "alpha3": "BLM",
        "country_name": "Saint Barth\u00e9lemy",
        "numeric": "652"
    },
    "BM": {
        "alpha3": "BMU",
        "country_name": "Bermuda",
        "numeric": "060"
    },
    "BN": {
        "alpha3": "BRN",
        "country_name": "Brunei Darussalam",
        "numeric": "096"
    },
    "BO": {
        "alpha3": "BOL",
        "country_name": "Bolivia (Plurinational State of)",
        "numeric": "068"
    },
    "BQ": {
        "alpha3": "BES",
        "country_name": "Bonaire, Sint Eustatius and Saba",
        "numeric": "535"
    },
    "BR": {
        "alpha3": "BRA",
        "country_name": "Brazil",
        "numeric": "076"
    },
    "BS": {
        "alpha3": "BHS",
        "country_name": "Bahamas (the)",
        "numeric": "044"
    },
    "BT": {
        "alpha3": "BTN",
        "country_name": "Bhutan",
        "numeric": "064"
    },
    "BV": {
        "alpha3": "BVT",
        "country_name": "Bouvet Island",
        "numeric": "074"
    },
    "BW": {
        "alpha3": "BWA",
        "country_name": "Botswana",
        "numeric": "072"
    },
    "BY": {
        "alpha3": "BLR",
        "country_name": "Belarus",
        "numeric": "112"
    },
    "BZ": {
        "alpha3": "BLZ",
        "country_name": "Belize",
        "numeric": "084"
    },
    "CA": {
        "alpha3": "CAN",
        "country_name": "Canada",
        "numeric": "124"
    },
    "CC": {
        "alpha3": "CCK",
        "country_name": "Cocos (Keeling) Islands (the)",
        "numeric": "166"
    },
    "CD": {
        "alpha3": "COD",
        "country_name": "Congo (the Democratic Republic of the)",
        "numeric": "180"
    },
    "CF": {
        "alpha3": "CAF",
        "country_name": "Central African Republic (the)",
        "numeric": "140"
    },
    "CG": {
        "alpha3": "COG",
        "country_name": "Congo (the)",
        "numeric": "178"
    },
    "CH": {
        "alpha3": "CHE",
        "country_name": "Switzerland",
        "numeric": "756"
    },
    "CI": {
        "alpha3": "CIV",
        "country_name": "C\u00f4te d'Ivoire",
        "numeric": "384"
    },
    "CK": {
        "alpha3": "COK",
        "country_name": "Cook Islands (the)",
        "numeric": "184"
    },
    "CL": {
        "alpha3": "CHL",
        "country_name": "Chile",
        "numeric": "152"
    },
    "CM": {
        "alpha3": "CMR",
        "country_name": "Cameroon",
        "numeric": "120"
    },
    "CN": {
        "alpha3": "CHN",
        "country_name": "China",
        "numeric": "156"
    },
    "CO": {
        "alpha3": "COL",
        "country_name": "Colombia",
        "numeric": "170"
    },
    "CR": {
        "alpha3": "CRI",
        "country_name": "Costa Rica",
        "numeric": "188"
    },
    "CU": {
        "alpha3": "CUB",
        "country_name": "Cuba",
        "numeric": "192"
    },
    "CV": {
        "alpha3": "CPV",
        "country_name": "Cabo Verde",
        "numeric": "132"
    },
    "CW": {
        "alpha3": "CUW",
        "country_name": "Cura\u00e7ao",
        "numeric": "531"
    },
    "CX": {
        "alpha3": "CXR",
        "country_name": "Christmas Island",
        "numeric": "162"
    },
    "CY": {
        "alpha3": "CYP",
        "country_name": "Cyprus",
        "numeric": "196"
    },
    "CZ": {
        "alpha3": "CZE",
        "country_name": "Czechia",
        "numeric": "203"
    },
    "DE": {
        "alpha3": "DEU",
        "country_name": "Germany",
        "numeric": "276"
    },
    "DJ": {
        "alpha3": "DJI",
        "country_name": "Djibouti",
        "numeric": "262"
    },
    "DK": {
        "alpha3": "DNK",
        "country_name": "Denmark",
        "numeric": "208"
    },
    "DM": {
        "alpha3": "DMA",
        "country_name": "Dominica",
        "numeric": "212"
    },
    "DO": {
        "alpha3": "DOM",
        "country_name": "Dominican Republic (the)",
        "numeric": "214"
    },
    "DZ": {
        "alpha3": "DZA",
        "country_name": "Algeria",
        "numeric": "012"
    },
    "EC": {
        "alpha3": "ECU",
        "country_name": "Ecuador",
        "numeric": "218"
    },
    "EE": {
        "alpha3": "EST",
        "country_name": "Estonia",
        "numeric": "233"
    },
    "EG": {
        "alpha3": "EGY",
        "country_name": "Egypt",
        "numeric": "818"
    },
    "EH": {
        "alpha3": "ESH",
        "country_name": "Western Sahara",
        "numeric": "732"
    },
    "ER": {
        "alpha3": "ERI",
        "country_name": "Eritrea",
        "numeric": "232"
    },
    "ES": {
        "alpha3": "ESP",
        "country_name": "Spain",
        "numeric": "724"
    },
    "ET": {
        "alpha3": "ETH",
        "country_name": "Ethiopia",
        "numeric": "231"
    },
    "FI": {
        "alpha3": "FIN",
        "country_name": "Finland",
        "numeric": "246"
    },
    "FJ": {
        "alpha3": "FJI",
        "country_name": "Fiji",
        "numeric": "242"
    },
    "FK": {
        "alpha3": "FLK",
        "country_name": "Falkland Islands (the) [Malvinas]",
        "numeric": "238"
    },
    "FM": {
        "alpha3": "FSM",
        "country_name": "Micronesia (Federated States of)",
        "numeric": "583"
    },
    "FO": {
        "alpha3": "FRO",
        "country_name": "Faroe Islands (the)",
        "numeric": "234"
    },
    "FR": {
        "alpha3": "FRA",
        "country_name": "France",
        "numeric": "250"
    },
    "GA": {
        "alpha3": "GAB",
        "country_name": "Gabon",
        "numeric": "266"
    },
    "GB": {
        "alpha3": "GBR",
        "country_name": "United Kingdom of Great Britain and Northern Ireland (the)",
        "numeric": "826"
    },
    "GD": {
        "alpha3": "GRD",
        "country_name": "Grenada",
        "numeric": "308"
    },
    "GE": {
        "alpha3": "GEO",
        "country_name": "Georgia",
        "numeric": "268"
    },
    "GF": {
        "alpha3": "GUF",
        "country_name": "French Guiana",
        "numeric": "254"
    },
    "GG": {
        "alpha3": "GGY",
        "country_name": "Guernsey",
        "numeric": "831"
    },
    "GH": {
        "alpha3": "GHA",
        "country_name": "Ghana",
        "numeric": "288"
    },
    "GI": {
        "alpha3": "GIB",
        "country_name": "Gibraltar",
        "numeric": "292"
    },
    "GL": {
        "alpha3": "GRL",
        "country_name": "Greenland",
        "numeric": "304"
    },
    "GM": {
        "alpha3": "GMB",
        "country_name": "Gambia (the)",
        "numeric": "270"
    },
    "GN": {
        "alpha3": "GIN",
        "country_name": "Guinea",
        "numeric": "324"
    },
    "GP": {
        "alpha3": "GLP",
        "country_name": "Guadeloupe",
        "numeric": "312"
    },
    "GQ": {
        "alpha3": "GNQ",
        "country_name": "Equatorial Guinea",
        "numeric": "226"
    },
    "GR": {
        "alpha3": "GRC",
        "country_name": "Greece",
        "numeric": "300"
    },
    "GS": {
        "alpha3": "SGS",
        "country_name": "South Georgia and the South Sandwich Islands",
        "numeric": "239"
    },
    "GT": {
        "alpha3": "GTM",
        "country_name": "Guatemala",
        "numeric": "320"
    },
    "GU": {
        "alpha3": "GUM",
        "country_name": "Guam",
        "numeric": "316"
    },
    "GW": {
        "alpha3": "GNB",
        "country_name": "Guinea-Bissau",
        "numeric": "624"
    },
    "GY": {
        "alpha3": "GUY",
        "country_name": "Guyana",
        "numeric": "328"
    },
    "HK": {
        "alpha3": "HKG",
        "country_name": "Hong Kong",
        "numeric": "344"
    },
    "HM": {
        "alpha3": "HMD",
        "country_name": "Heard Island and McDonald Islands",
        "numeric": "334"
    },
    "HN": {
        "alpha3": "HND",
        "country_name": "Honduras",
        "numeric": "340"
    },
    "HR": {
        "alpha3": "HRV",
        "country_name": "Croatia",
        "numeric": "191"
    },
    "HT": {
        "alpha3": "HTI",
        "country_name": "Haiti",
        "numeric": "332"
    },
    "HU": {
        "alpha3": "HUN",
        "country_name": "Hungary",
        "numeric": "348"
    },
    "ID": {
        "alpha3": "IDN",
        "country_name": "Indonesia",
        "numeric": "360"
    },
    "IE": {
        "alpha3": "IRL",
        "country_name": "Ireland",
        "numeric": "372"
    },
    "IL": {
        "alpha3": "ISR",
        "country_name": "Israel",
        "numeric": "376"
    },
    "IM": {
        "alpha3": "IMN",
        "country_name": "Isle of Man",
        "numeric": "833"
    },
    "IN": {
        "alpha3": "IND",
        "country_name": "India",
        "numeric": "356"
    },
    "IO": {
        "alpha3": "IOT",
        "country_name": "British Indian Ocean Territory (the)",
        "numeric": "086"
    },
    "IQ": {
        "alpha3": "IRQ",
        "country_name": "Iraq",
        "numeric": "368"
    },
    "IR": {
        "alpha3": "IRN",
        "country_name": "Iran (Islamic Republic of)",
        "numeric": "364"
    },
    "IS": {
        "alpha3": "ISL",
        "country_name": "Iceland",
        "numeric": "352"
    },
    "IT": {
        "alpha3": "ITA",
        "country_name": "Italy",
        "numeric": "380"
    },
    "JE": {
        "alpha3": "JEY",
        "country_name": "Jersey",
        "numeric": "832"
    },
    "JM": {
        "alpha3": "JAM",
        "country_name": "Jamaica",
        "numeric": "388"
    },
    "JO": {
        "alpha3": "JOR",
        "country_name": "Jordan",
        "numeric": "400"
    },
    "JP": {
        "alpha3": "JPN",
        "country_name": "Japan",
        "numeric": "392"
    },
    "KE": {
        "alpha3": "KEN",
        "country_name": "Kenya",
        "numeric": "404"
    },
    "KG": {
        "alpha3": "KGZ",
        "country_name": "Kyrgyzstan",
        "numeric": "417"
    },
    "KH": {
        "alpha3": "KHM",
        "country_name": "Cambodia",
        "numeric": "116"
    },
    "KI": {
        "alpha3": "KIR",
        "country_name": "Kiribati",
        "numeric": "296"
    },
    "KM": {
        "alpha3": "COM",
        "country_name": "Comoros (the)",
        "numeric": "174"
    },
    "KN": {
        "alpha3": "KNA",
        "country_name": "Saint Kitts and Nevis",
        "numeric": "659"
    },
    "KP": {
        "alpha3": "PRK",
        "country_name": "Korea (the Democratic People's Republic of)",
        "numeric": "408"
    },
    "KR": {
        "alpha3": "KOR",
        "country_name": "Korea (the Republic of)",
        "numeric": "410"
    },
    "KW": {
        "alpha3": "KWT",
        "country_name": "Kuwait",
        "numeric": "414"
    },
    "KY": {
        "alpha3": "CYM",
        "country_name": "Cayman Islands (the)",
        "numeric": "136"
    },
    "KZ": {
        "alpha3": "KAZ",
        "country_name": "Kazakhstan",
        "numeric": "398"
    },
    "LA": {
        "alpha3": "LAO",
        "country_name": "Lao People's Democratic Republic (the)",
        "numeric": "418"
    },
    "LB": {
        "alpha3": "LBN",
        "country_name": "Lebanon",
        "numeric": "422"
    },
    "LC": {
        "alpha3": "LCA",
        "country_name": "Saint Lucia",
        "numeric": "662"
    },
    "LI": {
        "alpha3": "LIE",
        "country_name": "Liechtenstein",
        "numeric": "438"
    },
    "LK": {
        "alpha3": "LKA",
        "country_name": "Sri Lanka",
        "numeric": "144"
    },
    "LR": {
        "alpha3": "LBR",
        "country_name": "Liberia",
        "numeric": "430"
    },
    "LS": {
        "alpha3": "LSO",
        "country_name": "Lesotho",
        "numeric": "426"
    },
    "LT": {
        "alpha3": "LTU",
        "country_name": "Lithuania",
        "numeric": "440"
    },
    "LU": {
        "alpha3": "LUX",
        "country_name": "Luxembourg",
        "numeric": "442"
    },
    "LV": {
        "alpha3": "LVA",
        "country_name": "Latvia",
        "numeric": "428"
    },
    "LY": {
        "alpha3": "LBY",
        "country_name": "Libya",
        "numeric": "434"
    },
    "MA": {
        "alpha3": "MAR",
        "country_name": "Morocco",
        "numeric": "504"
    },
    "MC": {
        "alpha3": "MCO",
        "country_name": "Monaco",
        "numeric": "492"
    },
    "MD": {
        "alpha3": "MDA",
        "country_name": "Moldova (the Republic of)",
        "numeric": "498"
    },
    "ME": {
        "alpha3": "MNE",
        "country_name": "Montenegro",
        "numeric": "499"
    },
    "MF": {
        "alpha3": "MAF",
        "country_name": "Saint Martin (French part)",
        "numeric": "663"
    },
    "MG": {
        "alpha3": "MDG",
        "country_name": "Madagascar",
        "numeric": "450"
    },
    "MH": {
        "alpha3": "MHL",
        "country_name": "Marshall Islands (the)",
        "numeric": "584"
    },
    "MK": {
        "alpha3": "MKD",
        "country_name": "Republic of North Macedonia",
        "numeric": "807"
    },
    "ML": {
        "alpha3": "MLI",
        "country_name": "Mali",
        "numeric": "466"
    },
    "MM": {
        "alpha3": "MMR",
        "country_name": "Myanmar",
        "numeric": "104"
    },
    "MN": {
        "alpha3": "MNG",
        "country_name": "Mongolia",
        "numeric": "496"
    },
    "MO": {
        "alpha3": "MAC",
        "country_name": "Macao",
        "numeric": "446"
    },
    "MP": {
        "alpha3": "MNP",
        "country_name": "Northern Mariana Islands (the)",
        "numeric": "580"
    },
    "MQ": {
        "alpha3": "MTQ",
        "country_name": "Martinique",
        "numeric": "474"
    },
    "MR": {
        "alpha3": "MRT",
        "country_name": "Mauritania",
        "numeric": "478"
    },
    "MS": {
        "alpha3": "MSR",
        "country_name": "Montserrat",
        "numeric": "500"
    },
    "MT": {
        "alpha3": "MLT",
        "country_name": "Malta",
        "numeric": "470"
    },
    "MU": {
        "alpha3": "MUS",
        "country_name": "Mauritius",
        "numeric": "480"
    },
    "MV": {
        "alpha3": "MDV",
        "country_name": "Maldives",
        "numeric": "462"
    },
    "MW": {
        "alpha3": "MWI",
        "country_name": "Malawi",
        "numeric": "454"
    },
    "MX": {
        "alpha3": "MEX",
        "country_name": "Mexico",
        "numeric": "484"
    },
    "MY": {
        "alpha3": "MYS",
        "country_name": "Malaysia",
        "numeric": "458"
    },
    "MZ": {
        "alpha3": "MOZ",
        "country_name": "Mozambique",
        "numeric": "508"
    },
    "NA": {
        "alpha3": "NAM",
        "country_name": "Namibia",
        "numeric": "516"
    },
    "NC": {
        "alpha3": "NCL",
        "country_name": "New Caledonia",
        "numeric": "540"
    },
    "NE": {
        "alpha3": "NER",
        "country_name": "Niger (the)",
        "numeric": "562"
    },
    "NF": {
        "alpha3": "NFK",
        "country_name": "Norfolk Island",
        "numeric": "574"
    },
    "NG": {
        "alpha3": "NGA",
        "country_name": "Nigeria",
        "numeric": "566"
    },
    "NI": {
        "alpha3": "NIC",
        "country_name": "Nicaragua",
        "numeric": "558"
    },
    "NL": {
        "alpha3": "NLD",
        "country_name": "Netherlands (the)",
        "numeric": "528"
    },
    "NO": {
        "alpha3": "NOR",
        "country_name": "Norway",
        "numeric": "578"
    },
    "NP": {
        "alpha3": "NPL",
        "country_name": "Nepal",
        "numeric": "524"
    },
    "NR": {
        "alpha3": "NRU",
        "country_name": "Nauru",
        "numeric": "520"
    },
    "NU": {
        "alpha3": "NIU",
        "country_name": "Niue",
        "numeric": "570"
    },
    "NZ": {
        "alpha3": "NZL",
        "country_name": "New Zealand",
        "numeric": "554"
    },
    "OM": {
        "alpha3": "OMN",
        "country_name": "Oman",
        "numeric": "512"
    },
    "PA": {
        "alpha3": "PAN",
        "country_name": "Panama",
        "numeric": "591"
    },
    "PE": {
        "alpha3": "PER",
        "country_name": "Peru",
        "numeric": "604"
    },
    "PF": {
        "alpha3": "PYF",
        "country_name": "French Polynesia",
        "numeric": "258"
    },
    "PG": {
        "alpha3": "PNG",
        "country_name": "Papua New Guinea",
        "numeric": "598"
    },
    "PH": {
        "alpha3": "PHL",
        "country_name": "Philippines (the)",
        "numeric": "608"
    },
    "PK": {
        "alpha3": "PAK",
        "country_name": "Pakistan",
        "numeric": "586"
    },
    "PL": {
        "alpha3": "POL",
        "country_name": "Poland",
        "numeric": "616"
    },
    "PM": {
        "alpha3": "SPM",
        "country_name": "Saint Pierre and Miquelon",
        "numeric": "666"
    },
    "PN": {
        "alpha3": "PCN",
        "country_name": "Pitcairn",
        "numeric": "612"
    },
    "PR": {
        "alpha3": "PRI",
        "country_name": "Puerto Rico",
        "numeric": "630"
    },
    "PS": {
        "alpha3": "PSE",
        "country_name": "Palestine, State of",
        "numeric": "275"
    },
    "PT": {
        "alpha3": "PRT",
        "country_name": "Portugal",
        "numeric": "620"
    },
    "PW": {
        "alpha3": "PLW",
        "country_name": "Palau",
        "numeric": "585"
    },
    "PY": {
        "alpha3": "PRY",
        "country_name": "Paraguay",
        "numeric": "600"
    },
    "QA": {
        "alpha3": "QAT",
        "country_name": "Qatar",
        "numeric": "634"
    },
    "RE": {
        "alpha3": "REU",
        "country_name": "R\u00e9union",
        "numeric": "638"
    },
    "RO": {
        "alpha3": "ROU",
        "country_name": "Romania",
        "numeric": "642"
    },
    "RS": {
        "alpha3": "SRB",
        "country_name": "Serbia",
        "numeric": "688"
    },
    "RU": {
        "alpha3": "RUS",
        "country_name": "Russian Federation (the)",
        "numeric": "643"
    },
    "RW": {
        "alpha3": "RWA",
        "country_name": "Rwanda",
        "numeric": "646"
    },
    "SA": {
        "alpha3": "SAU",
        "country_name": "Saudi Arabia",
        "numeric": "682"
    },
    "SB": {
        "alpha3": "SLB",
        "country_name": "Solomon Islands",
        "numeric": "090"
    },
    "SC": {
        "alpha3": "SYC",
        "country_name": "Seychelles",
        "numeric": "690"
    },
    "SD": {
        "alpha3": "SDN",
        "country_name": "Sudan (the)",
        "numeric": "729"
    },
    "SE": {
        "alpha3": "SWE",
        "country_name": "Sweden",
        "numeric": "752"
    },
    "SG": {
        "alpha3": "SGP",
        "country_name": "Singapore",
        "numeric": "702"
    },
    "SH": {
        "alpha3": "SHN",
        "country_name": "Saint Helena, Ascension and Tristan da Cunha",
        "numeric": "654"
    },
    "SI": {
        "alpha3": "SVN",
        "country_name": "Slovenia",
        "numeric": "705"
    },
    "SJ": {
        "alpha3": "SJM",
        "country_name": "Svalbard and Jan Mayen",
        "numeric": "744"
    },
    "SK": {
        "alpha3": "SVK",
        "country_name": "Slovakia",
        "numeric": "703"
    },
    "SL": {
        "alpha3": "SLE",
        "country_name": "Sierra Leone",
        "numeric": "694"
    },
    "SM": {
        "alpha3": "SMR",
        "country_name": "San Marino",
        "numeric": "674"
    },
    "SN": {
        "alpha3": "SEN",
        "country_name": "Senegal",
        "numeric": "686"
    },
    "SO": {
        "alpha3": "SOM",
        "country_name": "Somalia",
        "numeric": "706"
    },
    "SR": {
        "alpha3": "SUR",
        "country_name": "Suriname",
        "numeric": "740"
    },
    "SS": {
        "alpha3": "SSD",
        "country_name": "South Sudan",
        "numeric": "728"
    },
    "ST": {
        "alpha3": "STP",
        "country_name": "Sao Tome and Principe",
        "numeric": "678"
    },
    "SV": {
        "alpha3": "SLV",
        "country_name": "El Salvador",
        "numeric": "222"
    },
    "SX": {
        "alpha3": "SXM",
        "country_name": "Sint Maarten (Dutch part)",
        "numeric": "534"
    },
    "SY": {
        "alpha3": "SYR",
        "country_name": "Syrian Arab Republic",
        "numeric": "760"
    },
    "SZ": {
        "alpha3": "SWZ",
        "country_name": "Eswatini",
        "numeric": "748"
    },
    "TC": {
        "alpha3": "TCA",
        "country_name": "Turks and Caicos Islands (the)",
        "numeric": "796"
    },
    "TD": {
        "alpha3": "TCD",
        "country_name": "Chad",
        "numeric": "148"
    },
    "TF": {
        "alpha3": "ATF",
        "country_name": "French Southern Territories (the)",
        "numeric": "260"
    },
    "TG": {
        "alpha3": "TGO",
        "country_name": "Togo",
        "numeric": "768"
    },
    "TH": {
        "alpha3": "THA",
        "country_name": "Thailand",
        "numeric": "764"
    },
    "TJ": {
        "alpha3": "TJK",
        "country_name": "Tajikistan",
        "numeric": "762"
    },
    "TK": {
        "alpha3": "TKL",
        "country_name": "Tokelau",
        "numeric": "772"
    },
    "TL": {
        "alpha3": "TLS",
        "country_name": "Timor-Leste",
        "numeric": "626"
    },
    "TM": {
        "alpha3": "TKM",
        "country_name": "Turkmenistan",
        "numeric": "795"
    },
    "TN": {
        "alpha3": "TUN",
        "country_name": "Tunisia",
        "numeric": "788"
    },
    "TO": {
        "alpha3": "TON",
        "country_name": "Tonga",
        "numeric": "776"
    },
    "TR": {
        "alpha3": "TUR",
        "country_name": "Turkey",
        "numeric": "792"
    },
    "TT": {
        "alpha3": "TTO",
        "country_name": "Trinidad and Tobago",
        "numeric": "780"
    },
    "TV": {
        "alpha3": "TUV",
        "country_name": "Tuvalu",
        "numeric": "798"
    },
    "TW": {
        "alpha3": "TWN",
        "country_name": "Taiwan (Province of China)",
        "numeric": "158"
    },
    "TZ": {
        "alpha3": "TZA",
        "country_name": "Tanzania, United Republic of",
        "numeric": "834"
    },
    "UA": {
        "alpha3": "UKR",
        "country_name": "Ukraine",
        "numeric": "804"
    },
    "UG": {
        "alpha3": "UGA",
        "country_name": "Uganda",
        "numeric": "800"
    },
    "UM": {
        "alpha3": "UMI",
        "country_name": "United States Minor Outlying Islands (the)",
        "numeric": "581"
    },
    "US": {
        "alpha3": "USA",
        "country_name": "United States of America (the)",
        "numeric": "840"
    },
    "UY": {
        "alpha3": "URY",
        "country_name": "Uruguay",
        "numeric": "858"
    },
    "UZ": {
        "alpha3": "UZB",
        "country_name": "Uzbekistan",
        "numeric": "860"
    },
    "VA": {
        "alpha3": "VAT",
        "country_name": "Holy See (the)",
        "numeric": "336"
    },
    "VC": {
        "alpha3": "VCT",
        "country_name": "Saint Vincent and the Grenadines",
        "numeric": "670"
    },
    "VE": {
        "alpha3": "VEN",
        "country_name": "Venezuela (Bolivarian Republic of)",
        "numeric": "862"
    },
    "VG": {
        "alpha3": "VGB",
        "country_name": "Virgin Islands (British)",
        "numeric": "092"
    },
    "VI": {
        "alpha3": "VIR",
        "country_name": "Virgin Islands (U.S.)",
        "numeric": "850"
    },
    "VN": {
        "alpha3": "VNM",
        "country_name": "Viet Nam",
        "numeric": "704"
    },
    "VU": {
        "alpha3": "VUT",
        "country_name": "Vanuatu",
        "numeric": "548"
    },
    "WF": {
        "alpha3": "WLF",
        "country_name": "Wallis and Futuna",
        "numeric": "876"
    },
    "WS": {
        "alpha3": "WSM",
        "country_name": "Samoa",
        "numeric": "882"
    },
    "YE": {
        "alpha3": "YEM",
        "country_name": "Yemen",
        "numeric": "887"
    },
    "YT": {
        "alpha3": "MYT",
        "country_name": "Mayotte",
        "numeric": "175"
    },
    "ZA": {
        "alpha3": "ZAF",
        "country_name": "South Africa",
        "numeric": "710"
    },
    "ZM": {
        "alpha3": "ZMB",
        "country_name": "Zambia",
        "numeric": "894"
    },
    "ZW": {
        "alpha3": "ZWE",
        "country_name": "Zimbabwe",
        "numeric": "716"
    }
}
```
- [iso3166_from_alpha3.json](data/json/iso3166_from_alpha3.json)
- [iso3166_from_numeric.json](data/json/iso3166_from_numeric.json)
- [iso3166_list.json](data/json/iso3166_list.json)

<br>

## YAML

<hr>

[iso3166_from_alpha2.yaml](data/yaml/iso3166_from_alpha2.yaml)
```yaml
AD:
  alpha3: AND
  country_name: Andorra
  numeric: '020'
AE:
  alpha3: ARE
  country_name: United Arab Emirates (the)
  numeric: '784'
AF:
  alpha3: AFG
  country_name: Afghanistan
  numeric: '004'
AG:
  alpha3: ATG
  country_name: Antigua and Barbuda
  numeric: 028
AI:
  alpha3: AIA
  country_name: Anguilla
  numeric: '660'
AL:
  alpha3: ALB
  country_name: Albania
  numeric: 008
AM:
  alpha3: ARM
  country_name: Armenia
  numeric: '051'
AO:
  alpha3: AGO
  country_name: Angola
  numeric: '024'
AQ:
  alpha3: ATA
  country_name: Antarctica
  numeric: '010'
AR:
  alpha3: ARG
  country_name: Argentina
  numeric: '032'
AS:
  alpha3: ASM
  country_name: American Samoa
  numeric: '016'
AT:
  alpha3: AUT
  country_name: Austria
  numeric: '040'
AU:
  alpha3: AUS
  country_name: Australia
  numeric: '036'
AW:
  alpha3: ABW
  country_name: Aruba
  numeric: '533'
AX:
  alpha3: ALA
  country_name: "\xC5land Islands"
  numeric: '248'
AZ:
  alpha3: AZE
  country_name: Azerbaijan
  numeric: '031'
BA:
  alpha3: BIH
  country_name: Bosnia and Herzegovina
  numeric: '070'
BB:
  alpha3: BRB
  country_name: Barbados
  numeric: '052'
BD:
  alpha3: BGD
  country_name: Bangladesh
  numeric: '050'
BE:
  alpha3: BEL
  country_name: Belgium
  numeric: '056'
BF:
  alpha3: BFA
  country_name: Burkina Faso
  numeric: '854'
BG:
  alpha3: BGR
  country_name: Bulgaria
  numeric: '100'
BH:
  alpha3: BHR
  country_name: Bahrain
  numeric: 048
BI:
  alpha3: BDI
  country_name: Burundi
  numeric: '108'
BJ:
  alpha3: BEN
  country_name: Benin
  numeric: '204'
BL:
  alpha3: BLM
  country_name: "Saint Barth\xE9lemy"
  numeric: '652'
BM:
  alpha3: BMU
  country_name: Bermuda
  numeric: '060'
BN:
  alpha3: BRN
  country_name: Brunei Darussalam
  numeric: 096
BO:
  alpha3: BOL
  country_name: Bolivia (Plurinational State of)
  numeric: 068
BQ:
  alpha3: BES
  country_name: Bonaire, Sint Eustatius and Saba
  numeric: '535'
BR:
  alpha3: BRA
  country_name: Brazil
  numeric: '076'
BS:
  alpha3: BHS
  country_name: Bahamas (the)
  numeric: '044'
BT:
  alpha3: BTN
  country_name: Bhutan
  numeric: '064'
BV:
  alpha3: BVT
  country_name: Bouvet Island
  numeric: '074'
BW:
  alpha3: BWA
  country_name: Botswana
  numeric: '072'
BY:
  alpha3: BLR
  country_name: Belarus
  numeric: '112'
BZ:
  alpha3: BLZ
  country_name: Belize
  numeric: 084
CA:
  alpha3: CAN
  country_name: Canada
  numeric: '124'
CC:
  alpha3: CCK
  country_name: Cocos (Keeling) Islands (the)
  numeric: '166'
CD:
  alpha3: COD
  country_name: Congo (the Democratic Republic of the)
  numeric: '180'
CF:
  alpha3: CAF
  country_name: Central African Republic (the)
  numeric: '140'
CG:
  alpha3: COG
  country_name: Congo (the)
  numeric: '178'
CH:
  alpha3: CHE
  country_name: Switzerland
  numeric: '756'
CI:
  alpha3: CIV
  country_name: "C\xF4te d'Ivoire"
  numeric: '384'
CK:
  alpha3: COK
  country_name: Cook Islands (the)
  numeric: '184'
CL:
  alpha3: CHL
  country_name: Chile
  numeric: '152'
CM:
  alpha3: CMR
  country_name: Cameroon
  numeric: '120'
CN:
  alpha3: CHN
  country_name: China
  numeric: '156'
CO:
  alpha3: COL
  country_name: Colombia
  numeric: '170'
CR:
  alpha3: CRI
  country_name: Costa Rica
  numeric: '188'
CU:
  alpha3: CUB
  country_name: Cuba
  numeric: '192'
CV:
  alpha3: CPV
  country_name: Cabo Verde
  numeric: '132'
CW:
  alpha3: CUW
  country_name: "Cura\xE7ao"
  numeric: '531'
CX:
  alpha3: CXR
  country_name: Christmas Island
  numeric: '162'
CY:
  alpha3: CYP
  country_name: Cyprus
  numeric: '196'
CZ:
  alpha3: CZE
  country_name: Czechia
  numeric: '203'
DE:
  alpha3: DEU
  country_name: Germany
  numeric: '276'
DJ:
  alpha3: DJI
  country_name: Djibouti
  numeric: '262'
DK:
  alpha3: DNK
  country_name: Denmark
  numeric: '208'
DM:
  alpha3: DMA
  country_name: Dominica
  numeric: '212'
DO:
  alpha3: DOM
  country_name: Dominican Republic (the)
  numeric: '214'
DZ:
  alpha3: DZA
  country_name: Algeria
  numeric: '012'
EC:
  alpha3: ECU
  country_name: Ecuador
  numeric: '218'
EE:
  alpha3: EST
  country_name: Estonia
  numeric: '233'
EG:
  alpha3: EGY
  country_name: Egypt
  numeric: '818'
EH:
  alpha3: ESH
  country_name: Western Sahara
  numeric: '732'
ER:
  alpha3: ERI
  country_name: Eritrea
  numeric: '232'
ES:
  alpha3: ESP
  country_name: Spain
  numeric: '724'
ET:
  alpha3: ETH
  country_name: Ethiopia
  numeric: '231'
FI:
  alpha3: FIN
  country_name: Finland
  numeric: '246'
FJ:
  alpha3: FJI
  country_name: Fiji
  numeric: '242'
FK:
  alpha3: FLK
  country_name: Falkland Islands (the) [Malvinas]
  numeric: '238'
FM:
  alpha3: FSM
  country_name: Micronesia (Federated States of)
  numeric: '583'
FO:
  alpha3: FRO
  country_name: Faroe Islands (the)
  numeric: '234'
FR:
  alpha3: FRA
  country_name: France
  numeric: '250'
GA:
  alpha3: GAB
  country_name: Gabon
  numeric: '266'
GB:
  alpha3: GBR
  country_name: United Kingdom of Great Britain and Northern Ireland (the)
  numeric: '826'
GD:
  alpha3: GRD
  country_name: Grenada
  numeric: '308'
GE:
  alpha3: GEO
  country_name: Georgia
  numeric: '268'
GF:
  alpha3: GUF
  country_name: French Guiana
  numeric: '254'
GG:
  alpha3: GGY
  country_name: Guernsey
  numeric: '831'
GH:
  alpha3: GHA
  country_name: Ghana
  numeric: '288'
GI:
  alpha3: GIB
  country_name: Gibraltar
  numeric: '292'
GL:
  alpha3: GRL
  country_name: Greenland
  numeric: '304'
GM:
  alpha3: GMB
  country_name: Gambia (the)
  numeric: '270'
GN:
  alpha3: GIN
  country_name: Guinea
  numeric: '324'
GP:
  alpha3: GLP
  country_name: Guadeloupe
  numeric: '312'
GQ:
  alpha3: GNQ
  country_name: Equatorial Guinea
  numeric: '226'
GR:
  alpha3: GRC
  country_name: Greece
  numeric: '300'
GS:
  alpha3: SGS
  country_name: South Georgia and the South Sandwich Islands
  numeric: '239'
GT:
  alpha3: GTM
  country_name: Guatemala
  numeric: '320'
GU:
  alpha3: GUM
  country_name: Guam
  numeric: '316'
GW:
  alpha3: GNB
  country_name: Guinea-Bissau
  numeric: '624'
GY:
  alpha3: GUY
  country_name: Guyana
  numeric: '328'
HK:
  alpha3: HKG
  country_name: Hong Kong
  numeric: '344'
HM:
  alpha3: HMD
  country_name: Heard Island and McDonald Islands
  numeric: '334'
HN:
  alpha3: HND
  country_name: Honduras
  numeric: '340'
HR:
  alpha3: HRV
  country_name: Croatia
  numeric: '191'
HT:
  alpha3: HTI
  country_name: Haiti
  numeric: '332'
HU:
  alpha3: HUN
  country_name: Hungary
  numeric: '348'
ID:
  alpha3: IDN
  country_name: Indonesia
  numeric: '360'
IE:
  alpha3: IRL
  country_name: Ireland
  numeric: '372'
IL:
  alpha3: ISR
  country_name: Israel
  numeric: '376'
IM:
  alpha3: IMN
  country_name: Isle of Man
  numeric: '833'
IN:
  alpha3: IND
  country_name: India
  numeric: '356'
IO:
  alpha3: IOT
  country_name: British Indian Ocean Territory (the)
  numeric: 086
IQ:
  alpha3: IRQ
  country_name: Iraq
  numeric: '368'
IR:
  alpha3: IRN
  country_name: Iran (Islamic Republic of)
  numeric: '364'
IS:
  alpha3: ISL
  country_name: Iceland
  numeric: '352'
IT:
  alpha3: ITA
  country_name: Italy
  numeric: '380'
JE:
  alpha3: JEY
  country_name: Jersey
  numeric: '832'
JM:
  alpha3: JAM
  country_name: Jamaica
  numeric: '388'
JO:
  alpha3: JOR
  country_name: Jordan
  numeric: '400'
JP:
  alpha3: JPN
  country_name: Japan
  numeric: '392'
KE:
  alpha3: KEN
  country_name: Kenya
  numeric: '404'
KG:
  alpha3: KGZ
  country_name: Kyrgyzstan
  numeric: '417'
KH:
  alpha3: KHM
  country_name: Cambodia
  numeric: '116'
KI:
  alpha3: KIR
  country_name: Kiribati
  numeric: '296'
KM:
  alpha3: COM
  country_name: Comoros (the)
  numeric: '174'
KN:
  alpha3: KNA
  country_name: Saint Kitts and Nevis
  numeric: '659'
KP:
  alpha3: PRK
  country_name: Korea (the Democratic People's Republic of)
  numeric: '408'
KR:
  alpha3: KOR
  country_name: Korea (the Republic of)
  numeric: '410'
KW:
  alpha3: KWT
  country_name: Kuwait
  numeric: '414'
KY:
  alpha3: CYM
  country_name: Cayman Islands (the)
  numeric: '136'
KZ:
  alpha3: KAZ
  country_name: Kazakhstan
  numeric: '398'
LA:
  alpha3: LAO
  country_name: Lao People's Democratic Republic (the)
  numeric: '418'
LB:
  alpha3: LBN
  country_name: Lebanon
  numeric: '422'
LC:
  alpha3: LCA
  country_name: Saint Lucia
  numeric: '662'
LI:
  alpha3: LIE
  country_name: Liechtenstein
  numeric: '438'
LK:
  alpha3: LKA
  country_name: Sri Lanka
  numeric: '144'
LR:
  alpha3: LBR
  country_name: Liberia
  numeric: '430'
LS:
  alpha3: LSO
  country_name: Lesotho
  numeric: '426'
LT:
  alpha3: LTU
  country_name: Lithuania
  numeric: '440'
LU:
  alpha3: LUX
  country_name: Luxembourg
  numeric: '442'
LV:
  alpha3: LVA
  country_name: Latvia
  numeric: '428'
LY:
  alpha3: LBY
  country_name: Libya
  numeric: '434'
MA:
  alpha3: MAR
  country_name: Morocco
  numeric: '504'
MC:
  alpha3: MCO
  country_name: Monaco
  numeric: '492'
MD:
  alpha3: MDA
  country_name: Moldova (the Republic of)
  numeric: '498'
ME:
  alpha3: MNE
  country_name: Montenegro
  numeric: '499'
MF:
  alpha3: MAF
  country_name: Saint Martin (French part)
  numeric: '663'
MG:
  alpha3: MDG
  country_name: Madagascar
  numeric: '450'
MH:
  alpha3: MHL
  country_name: Marshall Islands (the)
  numeric: '584'
MK:
  alpha3: MKD
  country_name: Republic of North Macedonia
  numeric: '807'
ML:
  alpha3: MLI
  country_name: Mali
  numeric: '466'
MM:
  alpha3: MMR
  country_name: Myanmar
  numeric: '104'
MN:
  alpha3: MNG
  country_name: Mongolia
  numeric: '496'
MO:
  alpha3: MAC
  country_name: Macao
  numeric: '446'
MP:
  alpha3: MNP
  country_name: Northern Mariana Islands (the)
  numeric: '580'
MQ:
  alpha3: MTQ
  country_name: Martinique
  numeric: '474'
MR:
  alpha3: MRT
  country_name: Mauritania
  numeric: '478'
MS:
  alpha3: MSR
  country_name: Montserrat
  numeric: '500'
MT:
  alpha3: MLT
  country_name: Malta
  numeric: '470'
MU:
  alpha3: MUS
  country_name: Mauritius
  numeric: '480'
MV:
  alpha3: MDV
  country_name: Maldives
  numeric: '462'
MW:
  alpha3: MWI
  country_name: Malawi
  numeric: '454'
MX:
  alpha3: MEX
  country_name: Mexico
  numeric: '484'
MY:
  alpha3: MYS
  country_name: Malaysia
  numeric: '458'
MZ:
  alpha3: MOZ
  country_name: Mozambique
  numeric: '508'
NA:
  alpha3: NAM
  country_name: Namibia
  numeric: '516'
NC:
  alpha3: NCL
  country_name: New Caledonia
  numeric: '540'
NE:
  alpha3: NER
  country_name: Niger (the)
  numeric: '562'
NF:
  alpha3: NFK
  country_name: Norfolk Island
  numeric: '574'
NG:
  alpha3: NGA
  country_name: Nigeria
  numeric: '566'
NI:
  alpha3: NIC
  country_name: Nicaragua
  numeric: '558'
NL:
  alpha3: NLD
  country_name: Netherlands (the)
  numeric: '528'
'NO':
  alpha3: NOR
  country_name: Norway
  numeric: '578'
NP:
  alpha3: NPL
  country_name: Nepal
  numeric: '524'
NR:
  alpha3: NRU
  country_name: Nauru
  numeric: '520'
NU:
  alpha3: NIU
  country_name: Niue
  numeric: '570'
NZ:
  alpha3: NZL
  country_name: New Zealand
  numeric: '554'
OM:
  alpha3: OMN
  country_name: Oman
  numeric: '512'
PA:
  alpha3: PAN
  country_name: Panama
  numeric: '591'
PE:
  alpha3: PER
  country_name: Peru
  numeric: '604'
PF:
  alpha3: PYF
  country_name: French Polynesia
  numeric: '258'
PG:
  alpha3: PNG
  country_name: Papua New Guinea
  numeric: '598'
PH:
  alpha3: PHL
  country_name: Philippines (the)
  numeric: '608'
PK:
  alpha3: PAK
  country_name: Pakistan
  numeric: '586'
PL:
  alpha3: POL
  country_name: Poland
  numeric: '616'
PM:
  alpha3: SPM
  country_name: Saint Pierre and Miquelon
  numeric: '666'
PN:
  alpha3: PCN
  country_name: Pitcairn
  numeric: '612'
PR:
  alpha3: PRI
  country_name: Puerto Rico
  numeric: '630'
PS:
  alpha3: PSE
  country_name: Palestine, State of
  numeric: '275'
PT:
  alpha3: PRT
  country_name: Portugal
  numeric: '620'
PW:
  alpha3: PLW
  country_name: Palau
  numeric: '585'
PY:
  alpha3: PRY
  country_name: Paraguay
  numeric: '600'
QA:
  alpha3: QAT
  country_name: Qatar
  numeric: '634'
RE:
  alpha3: REU
  country_name: "R\xE9union"
  numeric: '638'
RO:
  alpha3: ROU
  country_name: Romania
  numeric: '642'
RS:
  alpha3: SRB
  country_name: Serbia
  numeric: '688'
RU:
  alpha3: RUS
  country_name: Russian Federation (the)
  numeric: '643'
RW:
  alpha3: RWA
  country_name: Rwanda
  numeric: '646'
SA:
  alpha3: SAU
  country_name: Saudi Arabia
  numeric: '682'
SB:
  alpha3: SLB
  country_name: Solomon Islands
  numeric: 090
SC:
  alpha3: SYC
  country_name: Seychelles
  numeric: '690'
SD:
  alpha3: SDN
  country_name: Sudan (the)
  numeric: '729'
SE:
  alpha3: SWE
  country_name: Sweden
  numeric: '752'
SG:
  alpha3: SGP
  country_name: Singapore
  numeric: '702'
SH:
  alpha3: SHN
  country_name: Saint Helena, Ascension and Tristan da Cunha
  numeric: '654'
SI:
  alpha3: SVN
  country_name: Slovenia
  numeric: '705'
SJ:
  alpha3: SJM
  country_name: Svalbard and Jan Mayen
  numeric: '744'
SK:
  alpha3: SVK
  country_name: Slovakia
  numeric: '703'
SL:
  alpha3: SLE
  country_name: Sierra Leone
  numeric: '694'
SM:
  alpha3: SMR
  country_name: San Marino
  numeric: '674'
SN:
  alpha3: SEN
  country_name: Senegal
  numeric: '686'
SO:
  alpha3: SOM
  country_name: Somalia
  numeric: '706'
SR:
  alpha3: SUR
  country_name: Suriname
  numeric: '740'
SS:
  alpha3: SSD
  country_name: South Sudan
  numeric: '728'
ST:
  alpha3: STP
  country_name: Sao Tome and Principe
  numeric: '678'
SV:
  alpha3: SLV
  country_name: El Salvador
  numeric: '222'
SX:
  alpha3: SXM
  country_name: Sint Maarten (Dutch part)
  numeric: '534'
SY:
  alpha3: SYR
  country_name: Syrian Arab Republic
  numeric: '760'
SZ:
  alpha3: SWZ
  country_name: Eswatini
  numeric: '748'
TC:
  alpha3: TCA
  country_name: Turks and Caicos Islands (the)
  numeric: '796'
TD:
  alpha3: TCD
  country_name: Chad
  numeric: '148'
TF:
  alpha3: ATF
  country_name: French Southern Territories (the)
  numeric: '260'
TG:
  alpha3: TGO
  country_name: Togo
  numeric: '768'
TH:
  alpha3: THA
  country_name: Thailand
  numeric: '764'
TJ:
  alpha3: TJK
  country_name: Tajikistan
  numeric: '762'
TK:
  alpha3: TKL
  country_name: Tokelau
  numeric: '772'
TL:
  alpha3: TLS
  country_name: Timor-Leste
  numeric: '626'
TM:
  alpha3: TKM
  country_name: Turkmenistan
  numeric: '795'
TN:
  alpha3: TUN
  country_name: Tunisia
  numeric: '788'
TO:
  alpha3: TON
  country_name: Tonga
  numeric: '776'
TR:
  alpha3: TUR
  country_name: Turkey
  numeric: '792'
TT:
  alpha3: TTO
  country_name: Trinidad and Tobago
  numeric: '780'
TV:
  alpha3: TUV
  country_name: Tuvalu
  numeric: '798'
TW:
  alpha3: TWN
  country_name: Taiwan (Province of China)
  numeric: '158'
TZ:
  alpha3: TZA
  country_name: Tanzania, United Republic of
  numeric: '834'
UA:
  alpha3: UKR
  country_name: Ukraine
  numeric: '804'
UG:
  alpha3: UGA
  country_name: Uganda
  numeric: '800'
UM:
  alpha3: UMI
  country_name: United States Minor Outlying Islands (the)
  numeric: '581'
US:
  alpha3: USA
  country_name: United States of America (the)
  numeric: '840'
UY:
  alpha3: URY
  country_name: Uruguay
  numeric: '858'
UZ:
  alpha3: UZB
  country_name: Uzbekistan
  numeric: '860'
VA:
  alpha3: VAT
  country_name: Holy See (the)
  numeric: '336'
VC:
  alpha3: VCT
  country_name: Saint Vincent and the Grenadines
  numeric: '670'
VE:
  alpha3: VEN
  country_name: Venezuela (Bolivarian Republic of)
  numeric: '862'
VG:
  alpha3: VGB
  country_name: Virgin Islands (British)
  numeric: 092
VI:
  alpha3: VIR
  country_name: Virgin Islands (U.S.)
  numeric: '850'
VN:
  alpha3: VNM
  country_name: Viet Nam
  numeric: '704'
VU:
  alpha3: VUT
  country_name: Vanuatu
  numeric: '548'
WF:
  alpha3: WLF
  country_name: Wallis and Futuna
  numeric: '876'
WS:
  alpha3: WSM
  country_name: Samoa
  numeric: '882'
YE:
  alpha3: YEM
  country_name: Yemen
  numeric: '887'
YT:
  alpha3: MYT
  country_name: Mayotte
  numeric: '175'
ZA:
  alpha3: ZAF
  country_name: South Africa
  numeric: '710'
ZM:
  alpha3: ZMB
  country_name: Zambia
  numeric: '894'
ZW:
  alpha3: ZWE
  country_name: Zimbabwe
  numeric: '716'

```
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