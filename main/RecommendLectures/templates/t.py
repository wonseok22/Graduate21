m = 99999999


def rights(s, cnt, cursor, name):
    global m
    a = ord(name[cursor]) - ord(s[cursor])
    b = 26 - (ord(name[cursor]) - ord(s[cursor]))
    i = a if a <= b else b
    s = s[:cursor] + chr(ord(s[cursor]) + a) + s[cursor + 1:]
    cnt += i
    if s == name:
        m = min(m, cnt)
        return
    rights(s, cnt + 1, (cursor + 1) % len(s), name)

def left(s, cnt, cursor, name):
    global m
    a = ord(name[cursor]) - ord(s[cursor])
    b = 26 - (ord(name[cursor]) - ord(s[cursor]))
    i = a if a <= b else b
    s = s[:cursor] + chr(ord(s[cursor]) + a) + s[cursor + 1:]
    cnt += i
    if s == name:
        m = min(m, cnt)
        return
    left(s, cnt + 1, (cursor - 1) % len(s), name)


def solution(name):
    answer = 0
    rights("A" * len(name), 0, 0, name)
    left("A" * len(name), 0, 0, name)
    print(m)
    return answer
