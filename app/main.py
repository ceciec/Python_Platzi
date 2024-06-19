import utils
import read_csv
import charts
import pandas as pd


def run():

    data = read_csv.read_csv('C:/Users/personal/Desktop/Tercer_Curso/app/data.csv')
    #cometar el codigo generate_pie_chart para generar el otro grafico.
    data = list(filter(lambda item: item['Continent'] == 'Africa', data))

    countries = list(map(lambda x: x['Country'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    charts.generate_pie_chart(countries, percentages)
    
    country = input('Type Country => ')

    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country'], labels, values)


if __name__ == '__main__':
    run()