list_of_countries = [{"Country": "Canada", 2018: 2.8, 2019: 1.9, 2020: -5.2, 2021: 5, 2022: 3.4},
                     {"Country": "France", 2018: 1.8, 2019: 1.9, 2020: -7.9, 2021: 6.8, 2022: 2.6},
                     {"Country": "Germany", 2018: 1, 2019: 1.1, 2020: -3.7, 2021: 2.6, 2022: 1.8},
                     {"Country": "Italy", 2018: 0.9, 2019: 0.5, 2020: -9, 2021: 7, 2022: 3.7},
                     {"Country": "Japan", 2018: 0.6, 2019: -0.4, 2020: -4.6, 2021: 2.1, 2022: 1.1},
                     {"Country": "UK", 2018: 1.7, 2019: 1.7, 2020: -9.3, 2021: 7.6, 2022: 4},
                     {"Country": "US", 2018: 2.9, 2019: 2.3, 2020: -3.4, 2021: 5.9, 2022: 2.1}]

def between(data):
    return 2 <= data[2019] <= 4

def decline(data):
    return data[2022] < data[2021] < data[2020] < data[2019] < data[2018]

def new():
    country = {"Country": "China", 2018: 6.7, 2019: 5.9, 2020: 2.2, 2021: 8.4, 2022: 2.9}
    list_of_countries.append(country)

def positive(data):
    return data[2019] > 0 and data[2020] > 0 and data[2021] > 0 and data[2022] > 0

between = list(filter(between, list_of_countries))
print(between)

decline = list(filter(decline, list_of_countries))
print(decline)

high = list(filter(lambda country: country[2021] == max(country[2021] for country in list_of_countries), list_of_countries))
print(high)

new()

positive = list(filter(positive, list_of_countries))
print(positive)