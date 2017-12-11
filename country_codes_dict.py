from pygal.maps.world import COUNTRIES

country_code_dict = {'Russia': 'ru', 'Taiwan': 'tw', 'Venezuela': 've', 'Syria': 'sy', 'Macedonia': 'mk',
'Libya': 'ly',
'Dominica': 'do',
'Brunei': 'bn',
'South Korea': 'kp',
'Iran': 'ir',
'Moldova': 'md',
'Qatar': 'bh',
'Cayman Islands': 'jm',
"Cote d'Ivoire": 'ci',
"Côte d'Ivoire": 'ci',
'Gibraltar': 'ma',
'Bolivia': 'bo',
'Isle of Man': 'ie',
'Tanzania': 'tz',
'Guernsey': 'fr',
'Jersey': 'fr',
'Nauru': 'pg',
'American Samoa': 'pg',
'Marshall Islands': 'pg',
'Vanuatu': 'pg',
'Niue': 'pg',
'Cook Islands': 'pg',
'Samoa': 'pg',
'Fiji': 'pg',
'British Virgin Islands': 'do',
'Bahamas': 'do',
'Saint Kitts and Nevis': 'do',
'Barbados': 'do',
'Curaçao': 'do',
'Aruba': 'do',
'Anguilla': 'do',
'Antigua and Barbuda': 'do', 
'Turks and Caicos Islands': 'do',
'Saint Lucia': 'do',
'Saint Vincent and the Grenadines': 'do',
'Trinidad and Tobago': 'do',
'U.S. Virgin Islands': 'do',
'Sint Maarten (Dutch part)': 'do',
'Grenada': 'do',
'Bermuda': 'do'}


def get_country_code(country_name):    
    """Return the Pygal 2-digit country code for the given country."""

    try:
        for code, name in COUNTRIES.items():         
            if name.title() == country_name:
                return code
    except KeyError:
        print('Country Name: ' + country_name + ' not found')
    else:
        try:
            return country_code_dict[country_name]
        except KeyError:
            pass

