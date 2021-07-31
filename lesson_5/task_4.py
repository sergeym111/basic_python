russian_num = ['один', 'два', 'три', 'четыре']
with open('new_numbers.txt', 'w', encoding='UTF-8') as target:
    with open('change.txt', 'r', encoding='UTF-8') as source:
        count = 0
        for i in source:
            word_list = i.split()
            word_list[0] = russian_num[count]
            count += 1
            target.write(' '.join(word_list)+'\n')