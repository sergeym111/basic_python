my_rating = [7, 3, 1]
while True:
    user_value = int(input('Введите число'))
    for i, val in enumerate(my_rating):
        if val < user_value:
            my_rating.insert(i,user_value)
            break
    print(my_rating)