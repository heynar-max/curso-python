import csv  

def read_csv(path):   #lee es CSV
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable} #para volverlo un dicionario
            data.append(country_dict)
    return data

if __name__ == '__main__':
    data = read_csv('./app/data.csv')
    print(data[0])