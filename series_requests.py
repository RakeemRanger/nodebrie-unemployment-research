import requests
import json
import prettytable

df = open( 'oh_county.txt', 'r')
# opening the file in read mode
my_file = df

# reading the file
data1 = my_file.read()

# replacing end splitting the text 
# when newline ('\n') is seen.
data_into_list = data1.split("\n")
d = data_into_list

headers = {'Content-type': 'application/json'}
data = json.dumps({"seriesid": d,"startyear":"2012", "endyear":"2022"})
p = requests.post('https://api.bls.gov/publicAPI/v1/timeseries/data/', data=data, headers=headers)
json_data = json.loads(p.text)
for series in json_data['Results']['series']:
    x=prettytable.PrettyTable(["series id","year","period","value","footnotes"])
    seriesId = series['seriesID']
    for item in series['data']:
        year = item['year']
        period = item['period']
        value = item['value']
        footnotes=""
        for footnote in item['footnotes']:
            if footnote:
                footnotes = footnotes + footnote['text'] + ','
    
        if 'M01' <= period <= 'M12':
            x.add_row([seriesId,year,period,value,footnotes[0:-1]])
    output = open(seriesId + '.txt','w')
    output.write (x.get_string())
    output.close()
    
