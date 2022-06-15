def hash_code(s):
    mask = (1<<32)-1
    h = 0
    for character in s:
        h = (h<<5&mask)|(h>>27)
        h += ord(character)
    return h


if __name__ == '__main__':
    # for i in range(26):
    #     s = chr(65+i)
    #     h = hash_code(s)
    #     print(s, h)
    # for i in range(26):
    #     s = chr(97+i)
    #     h = hash_code(s)
    #     print(s, h)

    a = [200+5*i for i in range(81)]
    m_100 = []
    m_101 = []
    n = 101
    for i in a:
        mod = i%100
        if mod not in m_100:
            m_100.append(mod)
        mod = i%101
        if mod not in m_101:
            m_101.append(mod)
    print(len(m_100))
    print(len(m_101))