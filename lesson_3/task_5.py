# специальный символ '~'
def my_func(a, old_sum):
    for i in a:
        if i != '~':
            old_sum += int(i)
        else:
            break
    return old_sum


b = []
old_sum = 0
while True:
    a = (input('число'))
    b.extend(a.split())
    old_sum = my_func(b, old_sum)
    print(old_sum)
    if '~' in b:
        break
    b = []
