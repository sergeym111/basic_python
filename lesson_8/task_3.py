class BoolStrInputCheck:
    def __init__(self):
        self.incoming_list = []

    def input_control(self):
        while True:
            try:
                new_elem = input("Введите очередной элемент списка: ")
                if new_elem == 'stop':
                    print(f"Заданный список {self.incoming_list}")
                    return f"Ввод завершен"
                    break
                new_elem = int(new_elem)
                self.incoming_list.append(new_elem)
            except:
                continue
            try:
                new_elem = input("Введите очередной элемент списка: ")
                if new_elem == 'stop':
                    print(f"Заданный список {self.incoming_list}")
                    return f"Ввод завершен"
                    break
                new_elem = float(new_elem)
                self.incoming_list.append(new_elem)
            except:
                continue


my_list = BoolStrInputCheck()
print(my_list.input_control())
