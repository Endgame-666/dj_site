def func(lst):
    lst = sorted(lst)
    rez = list()
    dif = lst[0]
    cur = list()
    for i in range(len(lst)):
        if abs(lst[i] - i) == dif:
            cur.append(lst[i])
        else:
            if len(cur) != 1:
                rez.append(f"{cur[0]}-{cur[-1]}")
            else:
                rez.append(f"{cur[0]}")
            cur.clear()
            cur.append(lst[i])
            dif = abs(lst[i] - i)
    if len(cur) != 1:
        rez.append(f"{cur[0]}-{cur[-1]}")
    else:
        rez.append(f"{cur[0]}")
    print(", ".join(rez))

func([1, 2, 3, 5, 8, 9, 10])
func([1, 3, 5, 10])
func([1])
