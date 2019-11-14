'''
import json
import requests
response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
print(todos)
'''

import json
from devicemainboard import BCmb
'''
data = {}
data['steps'] = []

data['steps'].append({
    'Type': 'Begin'
})

data['steps'].append({
    'Type': 'Pause',
    'Time': '10000'
})

data['steps'].append({
    'Type': 'Charge',
    'Time': '1200000',
    'Current': '20.0',
    'Maxtemp':'30.0',
    'Mintemp':'20.0'
})

data['steps'].append({
    'Type': 'Charge',
    'Time': '900000',
    'Current': '22.7',
    'Maxtemp':'31.0',
    'Mintemp':'20.0'
})

data['steps'].append({
    'Type': 'Charge',
    'Time': '1200000',
    'Current': '27.0',
    'Maxtemp':'31.0',
    'Mintemp':'20.5'
})

data['steps'].append({
    'Type': 'Charge',
    'Time': '180000',
    'Current': '24.0',
    'Maxtemp':'31.0',
    'Mintemp':'21.0'
})

data['steps'].append({
    'Type': 'Charge',
    'Time': '180000',
    'Current': '24.0',
    'Maxtemp':'31.0',
    'Mintemp':'21.0'
})

data['steps'].append({
    'Type': 'Pause',
    'Time': '60000'
})

data['steps'].append({
    'Type': 'Charge',
    'Time': '1200000',
    'Current': '26.5',
    'Maxtemp':'29.0',
    'Mintemp':'20.1'
})

data['steps'].append({
    'Type': 'Charge',
    'Time': '600000',
    'Current': '30.0',
    'Maxtemp':'30.3',
    'Mintemp':'20.0'
})

data['steps'].append({
    'Type': 'End'
})
'''
'''
data = {}
data['steps'] = []

data['steps'].append({
    'Type': 'Begin'
})

data['steps'].append({
    'Type': 'Pause',
    'Time': '25000'
})

data['steps'].append({
    'Type': 'Charge',
    'Time': '30000',
    'Current': '30.0'
})

data['steps'].append({
    'Type': 'Charge',
    'Time': '1800000',
    'Current': '27.4',
    'Maxtemp':'31.0',
    'Mintemp':'20.0'
})

data['steps'].append({
    'Type': 'Charge',
    'Time': '1200000',
    'Current': '18.6',
    'Maxtemp':'31.0',
    'Mintemp':'20.5'
})

data['steps'].append({
    'Type': 'Pause',
    'Time': '180000'
})

data['steps'].append({
    'Type': 'Charge',
    'Time': '1200000',
    'Current': '9.0',
})

data['steps'].append({
    'Type': 'Pause',
    'Time': '60000'
})

data['steps'].append({
    'Type': 'Charge',
    'Time': '900000',
    'Current': '12.4',
    'Maxtemp':'29.0',
    'Mintemp':'20.1'
})

data['steps'].append({
    'Type': 'Charge',
    'Time': '1200000',
    'Current': '8.2',
    'Maxtemp':'30.3',
    'Mintemp':'20.0'
})

data['steps'].append({
    'Type': 'Charge',
    'Time': '1500000',
    'Current': '25.6',
    'Maxtemp':'30.3',
    'Mintemp':'20.0'
})

data['steps'].append({
    'Type': 'Pause',
    'Time': '180000'
})

data['steps'].append({
    'Type': 'Charge',
    'Time': '1200000',
    'Current': '17.6',
})

data['steps'].append({
    'Type': 'End'
})

'''

data = {}
data['steps'] = []

data['steps'].append({
    'Type': 'Begin'
})

data['steps'].append({
    'Type': 'Charge',
    'Time': '180000',
    'Current': '30.0'
})

data['steps'].append({
    'Type': 'Charge',
    'Time': '1200000',
    'Current': '25.6',
    'Maxtemp':'31.0',
    'Mintemp':'20.0'
})

data['steps'].append({
    'Type': 'Pause',
    'Time': '300000'
})

data['steps'].append({
    'Type': 'Charge',
    'Time': '1200000',
    'Current': '18.6',
    'Maxtemp':'31.0',
    'Mintemp':'20.5'
})

data['steps'].append({
    'Type': 'Charge',
    'Time': '600000',
    'Current': '10.5',
})

data['steps'].append({
    'Type': 'Charge',
    'Time': '1200000',
    'Current': '19.2',
    'Maxtemp':'29.0',
    'Mintemp':'20.1'
})

data['steps'].append({
    'Type': 'Charge',
    'Time': '600000',
    'Current': '28.4',
    'Maxtemp':'30.3',
    'Mintemp':'20.0'
})

data['steps'].append({
    'Type': 'Charge',
    'Time': '900000',
    'Current': '23.5',
    'Maxtemp':'30.3',
    'Mintemp':'20.0'
})

data['steps'].append({
    'Type': 'Charge',
    'Time': '1200000',
    'Current': '14.7',
})

data['steps'].append({
    'Type': 'Pause',
    'Time': '300000'
})

data['steps'].append({
    'Type': 'Charge',
    'Time': '1200000',
    'Current': '26.7',
})

data['steps'].append({
    'Type': 'Charge',
    'Time': '900000',
    'Current': '27.5',
    'Maxtemp':'30.3',
    'Mintemp':'20.0'
})

data['steps'].append({
    'Type': 'End'
})


print(data['steps'][0])
print(len(data['steps']))

def remove_char(input_string, index):
    first_part = input_string[:index]
    second_part = input_string[index+1:]
    return first_part + second_part

def prepare_toSend(dataOrig):

    #print(dataOrig)
    data2 = str(dataOrig).replace("{\"steps\": ", '')
    #print(data2)
    value_index = len(data2)-1
    data3 = remove_char(data2, value_index)
    #print(data3)
    return data3


with open('program3.json', 'w') as outfile:
    json.dump(data, outfile)

f= open("program3.json","r")
contents = f.read()
f.close()

print(prepare_toSend(contents))

#BCmb.writeProgramClient('ditsa-Lenovo-C20-00.local',1,prepare_toSend(contents))
