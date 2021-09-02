def missing_char(str, n):
    prvdel = str[:n]
    vtordel = str[n + 1 :]
    return prvdel + vtordel

ch = missing_char("Maja", 3)
print(ch)