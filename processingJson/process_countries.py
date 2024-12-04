from json import load

f=open("C:\\Users\\HP\\Desktop\\Pythonworks\\datasets\\countries.json",encoding="utf-8")

data=load(f)

# print(len(data))

all_country_names=[country.get("name") for country in data]

# print(all_country_names)

all_regions_name=[country.get("region") for country in data]

# print(set(all_regions_name))

region_count={region: all_regions_name.count(region) for region in all_regions_name}

# print(region_count)

max_region_cout=max(region_count,key=lambda k:region_count.get(k))

# print(max_region_cout,region_count.get(max_region_cout))



country_capital=[country.get ("capital")for country in data if country.get("name")=="India"]

# print(country_capital)


#  


# borders_count = [(country["name"], len(country.get("borders", []))) for country in data]

# # Find the country with the maximum number of borders using max() and a key function
# max_borders_country, max_borders_count = max(borders_count, key=lambda x: x[1])

# print(borders_count)

country_borders={country.get("name"):len(country.get("borders",[]))for country in data}

# print(country_borders)


max_border_country=max(data,key=lambda country:len(country.get("borders",[]))).get("name")

# print(max_border_country)

most_populated_country=max(data,key=lambda country:country.get("population",0)).get("name")

# print(most_populated_country)



india_borders = [country.get("borders") for country in data if country.get("name") == "India"][0]

bordering_countries = [country.get("name") for country in data if country.get("alpha3Code") in india_borders]


print(bordering_countries)
print(india_borders)




