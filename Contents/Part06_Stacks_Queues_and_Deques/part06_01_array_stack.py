from DataStructures.stack import ArrayStack

# 6.1.3.
def reverse_file(filename):
    s = ArrayStack()
    original = open(filename)
    for line in original:
        s.push(line.rstrip('\n'))
    original.close()

    output = open(filename, 'w')
    while not s.is_empty():
        output.write(s.pop + '\n')
    output.close()

def is_matched(expr):
    lefty = '({['
    righty = ')}]'
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if lefty.index(S.pop()) != righty.index(c):
                return False
    return S.is_empty()

def is_matched_html(raw):
    S = ArrayStack()
    j = raw.find('<')
    while j > -1:
        k = raw.find('>', j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        print(tag)
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            elif S.pop() != tag[1:]:
                return False
        j = raw.find('<', k+1)
    return S.is_empty()


if __name__ == '__main__':
    # expr = '(5+3*{12+1})+[1-3]'
    # print(is_matched(expr))

    html = '<body><center><h1> The Little Boat </h1></center><p> The storm tossed the little boat like a cheap sneaker in an old washing machine.</p><ol><li> Will the salesman die? </li><li> What color is the boat? </li><li> And what about Naomi? </li></ol></body>'
    print(is_matched_html(html))