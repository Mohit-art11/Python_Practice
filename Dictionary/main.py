# Dictionary => unorderd collection of unique key:value pairs

countries = {"India": "New Delhi",
             "Australia": "Canberra",
             'New Zealand': 'Wellington',
             'Brazil': 'Rio de Janerio'
             }

countries.update({"Austria": "Vienna"})
countries.pop('Austria')
# countries.clear()

# print(countries["Germany"])
# print(countries.get('Austria'))
# print(countries.keys())
# print(countries.values())
# print(countries.items())

for key, value in countries.items():
    print(f"{key} - {value}")
