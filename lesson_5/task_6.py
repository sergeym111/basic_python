def hours(str):
    sum = 0
    types_of_lessons = ['лекция', 'практика', 'лабораторная']
    content_list = str.split()
    out_list = []
    for i, val in enumerate(content_list):
        if val in types_of_lessons:
            sum += int(content_list[i + 1])
    out_list.append((content_list[0], sum))
    return out_list


discipline_hours = {}
with open('discipline.txt', 'r', encoding='UTF-8') as f_discipline:
    for line in f_discipline:
        discipline_hours.update(hours(line))
    print(discipline_hours)
