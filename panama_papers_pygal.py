import matplotlib.pyplot as plt
import pandas as pd
from pygal.maps.world import World
from pygal.maps.world import COUNTRIES
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
from country_codes_dict import get_country_code

# Importing the dataset
dataset = pd.read_csv('Entities.csv', keep_default_na=False)
#dataset.replace(to_replace='Russia', value = 'Russian Federation')

dataset.loc[:,'country_codes'].unique()
dataset.loc[:,'country_codes'].describe()

count_status = pd.value_counts(dataset['status'][dataset['status']!=''], sort = True).sort_values(ascending=False)
count_countries = pd.value_counts(dataset['countries'][dataset['countries']!='']).sort_values(ascending=False)
count_codes = pd.value_counts(dataset['country_codes'][dataset['country_codes']!='']).sort_values(ascending=False)
count_jurisdiction = pd.value_counts(dataset['jurisdiction'][dataset['jurisdiction']!='']).sort_values(ascending=False)
count_jurisdiction_des = pd.value_counts(dataset['jurisdiction_description'][dataset['jurisdiction_description']!='']).sort_values(ascending=False)
count_service_provider = pd.value_counts(dataset['service_provider'][dataset['service_provider']!='']).sort_values(ascending=False)
count_company_type = pd.value_counts(dataset['company_type'][dataset['company_type']!='']).sort_values(ascending=False)

providers = dataset['service_provider'][dataset['countries']!='']
countries = dataset['countries'][dataset['countries']!='']


count_status.plot(kind = 'bar')
plt.title("Current Status")
plt.xlabel("Status")
plt.ylabel("# of Occurances")


count_countries[:15].plot(kind = 'bar')
plt.title("Countries")
plt.xlabel("Country")
plt.ylabel("# of Occurances")

           
count_jurisdiction[:15].plot(kind = 'bar')
plt.title("Jurisdictions")
plt.xlabel("jurisdiction")
plt.ylabel("# of Occurances")
           
count_service_provider.plot(kind = 'bar')
plt.title("Service Provider")
plt.xlabel("Provider")
plt.ylabel("# of Occurances")

           
# Total Entities By Country
count_countries1 = count_countries.copy()
combo_dict = {}
combo = []
for k,v in count_countries1.items():
    if len(k.split(";")) > 1:
        for item in k.split(";"):
            combo.append(item)
            try:
                if combo_dict[item]:
                    combo_dict[item] += v
            except KeyError:
                combo_dict[item] = v
    else:
        combo_dict[k] = count_countries1[k] + v



# Dictionary of Country Codes and Number of Occurances
cc_total, cc_excluded = {}, {}
for k, v in combo_dict.items():
    exists = False
    for code, name in COUNTRIES.items():
        if k == name.title() and not exists:
            exists = True
            cc_total[code] = v
    if not exists:
        cc_excluded[k] = v
        try:
            if cc_total[get_country_code(k)]:
                cc_total[get_country_code(k)] = cc_total[get_country_code(k)] + v
        except KeyError:
            if get_country_code(k):
                cc_total[get_country_code(k)] = v

        

# Split into groups based on number of Entities
cc_total1, cc_total2, cc_total3, cc_total4, cc_total5, cc_total6 = {}, {}, {}, {}, {}, {}
for k,v in cc_total.items():
    if v < 50:
        cc_total1[k] = v
    elif v < 200:
        cc_total2[k] = v
    elif v < 1000:
        cc_total3[k] = v
    elif v < 10000:
        cc_total4[k] = v
    elif v < 50000:
        cc_total5[k] = v    
    else:
        cc_total6[k] = v 
    
        
wm_style = RS('#336699', base_style=LCS)
wm = World(style=wm_style)
wm.title = 'Areas with Tax Shelters'
wm.add('0-50 Shelters', cc_total1)
wm.add('51-200 Shelters', cc_total2)
wm.add('201-1000 Shelters', cc_total3)
wm.add('1001-10000 Shelters', cc_total4)
wm.add('10001-50000 Shelters', cc_total5)
wm.add('over 50001 Shelters', cc_total6)
wm.render_to_file('tax_shelters_total.svg')


# Seperating by Service Provider
provider_country = []
country_provider = []
for country, provider in zip(countries, providers):
    if len(country.split(";")) > 1:
        for item in country.split(";"):
            provider_country.append(item)
            country_provider.append(provider)
    else:
        provider_country.append(country)
        country_provider.append(provider)


cc_countries = []
for country in provider_country:
    cc_countries.append(get_country_code(country))
    
provider_by_country = pd.DataFrame({'countries' : cc_countries, 'providers' : country_provider})
#pd.value_counts(provider_by_country['providers'][provider_by_country['countries']=='hk'])
Mossack_Fonseca_co = pd.value_counts(provider_by_country['countries'][provider_by_country['providers']=='Mossack Fonseca'])
Commonwealth_Trust_Limited_co = pd.value_counts(provider_by_country['countries'][provider_by_country['providers']=='Commonwealth Trust Limited'])
Portcullis_Trustnet_co = pd.value_counts(provider_by_country['countries'][provider_by_country['providers']=='Portcullis Trustnet'])


Mossack_Fonseca_dict = Mossack_Fonseca_co.to_dict()
Commonwealth_Trust_Limited_dict = Commonwealth_Trust_Limited_co.to_dict()
Portcullis_Trustnet_dict = Portcullis_Trustnet_co.to_dict()


cc_Mossack1, cc_Mossack2, cc_Mossack3, cc_Mossack4,  = {}, {}, {}, {}
for k,v in Mossack_Fonseca_dict.items():
    if v < 50:
        cc_Mossack1[k] = v
    elif v < 500:
        cc_Mossack2[k] = v
    elif v < 1000:
        cc_Mossack3[k] = v
    else:
        cc_Mossack4[k] = v
        
        
cc_Commonwealth1, cc_Commonwealth2, cc_Commonwealth3, cc_Commonwealth4,  = {}, {}, {}, {}
for k,v in Commonwealth_Trust_Limited_dict.items():
    if v < 50:
        cc_Commonwealth1[k] = v
    elif v < 500:
        cc_Commonwealth2[k] = v
    elif v < 1000:
        cc_Commonwealth3[k] = v
    else:
        cc_Commonwealth4[k] = v     


cc_Portcullis1, cc_Portcullis2, cc_Portcullis3, cc_Portcullis4,  = {}, {}, {}, {}
for k,v in Portcullis_Trustnet_dict.items():
    if v < 50:
        cc_Portcullis1[k] = v
    elif v < 500:
        cc_Portcullis2[k] = v
    elif v < 1000:
        cc_Portcullis3[k] = v
    else:
        cc_Portcullis4[k] = v
        

wm_style = RS('#336699', base_style=LCS)
wm = World(style=wm_style)
wm.title = 'Areas with Tax Shelters'
wm.add('0-50 Shelters', cc_Mossack1)
wm.add('51-500 Shelters', cc_Mossack2)
wm.add('501-1000 Shelters', cc_Mossack3)
wm.add('Over 1000 Shelters', cc_Mossack4)
wm.render_to_file('Mossack_Fonseca.svg')


wm_style = RS('#336699', base_style=LCS)
wm = World(style=wm_style)
wm.title = 'Areas with Tax Shelters'
wm.add('0-50 Shelters', cc_Commonwealth1)
wm.add('51-500 Shelters', cc_Commonwealth2)
wm.add('501-1000 Shelters', cc_Commonwealth3)
wm.add('Over 1000 Shelters', cc_Commonwealth4)
wm.render_to_file('Commonwealth_Trust_Limited.svg')


wm_style = RS('#336699', base_style=LCS)
wm = World(style=wm_style)
wm.title = 'Areas with Tax Shelters'
wm.add('0-50 Shelters', cc_Portcullis1)
wm.add('51-500 Shelters', cc_Portcullis2)
wm.add('501-1000 Shelters', cc_Portcullis3)
wm.add('Over 1000 Shelters', cc_Portcullis4)
wm.render_to_file('Portcullis_Trustnet.svg')
