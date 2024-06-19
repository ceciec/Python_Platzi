import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        #obtener nombre de las columnas
        header = next(reader)
        #agregamos un data vacio
        data = []
        for row in reader:
            #unir header con row, creando en tuplas
            iterable = zip(header, row)
            #usando dictionary comprehension
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data

if __name__== '__main__':
    data = read_csv('C:/Users/personal/Desktop/Tercer_Curso/app/data.csv')
    print(data[0])