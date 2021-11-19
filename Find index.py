def solution(list_, number):
    if number in list_:
        print(list_.index(number))
    else:
        i = 0
        for c in list_:
            if c < number:
                i += 1
        print(i)


serie = [1, 2, 3, 4, 5, 6, 7, 9]
num = 8
solution(serie, num)