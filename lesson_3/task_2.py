def print_user_data(name, surname, birth_year, city, e_mail, phone):
    print('Пользователь', name, surname, birth_year, city, e_mail, phone)


user_data = {'user_1':
                 {'name': 'Boris',
                  'surname': 'Popov',
                  'birth_year': 1984,
                  'city': 'Moscow',
                  'e_mail': 'popov_boris@mail.ru',
                  'phone': '+7(927)354-45-12'},
             'user_2':
                 {'name': 'Alex',
                  'surname': 'Serov',
                  'birth_year': 1953,
                  'city': 'Tambov',
                  'e_mail': 'alex@mail.ru',
                  'phone': '+7(927)184-15-65'}
             }
for item in user_data.items():
    print_user_data(name=item[1]['name'],
                    surname=item[1]['surname'],
                    birth_year=item[1]['birth_year'],
                    city=item[1]['city'],
                    e_mail=item[1]['e_mail'],
                    phone=item[1]['phone'])
