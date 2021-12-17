import csv
def createCsv(data, stats, firstRow):

    with open('./exports/'+ stats +'.csv','w', newline='') as out:
        csv_out = csv.writer(out, delimiter=';')
        csv_out.writerow(firstRow)
        for row in data:
            csv_out.writerow(row)