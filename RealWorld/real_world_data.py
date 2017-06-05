import csv, re


def real_world_data(n=10, fn='rawdata_2001.txt'):
    gdp = []
    labels = []
    for i, row in enumerate(csv.reader(open(fn), delimiter='\t')):
        print(row)
        # remove punctuation ($ ,)
        gdp_value = re.sub(r'[\$, ]', '', row[2])
        #  convert string to value
        gdp.append(float(gdp_value)/1e9)
        # add label to list
        labels.append(row[1].strip())
        #  Stop after 10 rows
        if (i == n-1):
            return (gdp, labels)