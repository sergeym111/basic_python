import json


list_to_json = []
firm_profit = {}
avg_profit = {}
with open('firm_data.txt', 'r', encoding='UTF-8') as firm_data:
    avg = 0
    sum = 0
    count = 0
    for i in firm_data:
        data = i.split()
        profit = int(data[2]) - int(data[3])
        sum += profit
        count += 1
        print(data)
        firm_profit[data[0]] = profit
    print(firm_profit)
    avg = sum / count
    avg_profit['avg'] = avg
    list_to_json = [firm_profit, avg_profit]
    print(list_to_json)
with open('firm.json', 'w', encoding='utf-8') as file:
    json.dump(list_to_json, file)

