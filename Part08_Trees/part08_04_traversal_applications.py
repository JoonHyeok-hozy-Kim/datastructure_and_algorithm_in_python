from DataStructures.tree import LinkedBinaryTree

def preorder_print(T):
    for i in T.preorder():
        print(i.element())

def preorder_indent(T, p=None, d=None):
    if p is None and d is None:
        p = T.root()
        d = 0
    text_list = []
    for i in range(d):
        text_list.append('  ')
    text_list.append(p.element())
    print(''.join(text_list))
    for c in T.children(p):
        preorder_indent(T, c, d+1)

def preorder_label(T, p=None, label_list=None):
    if p is None and label_list is None:
        p = T.root()
        label_list = []
    label_list.append(' ')
    label_list.append(p.element())
    print(''.join(label_list))
    label_list.pop()
    label_list.pop()
    cnt = 1
    for c in T.children(p):
        label_list.append(str(cnt))
        label_list.append('.')
        preorder_label(T, c, label_list)
        label_list.pop()
        label_list.pop()
        cnt += 1

def parenthesize(T):
    text_list = _parenthesize_text(T)
    return ''.join(text_list)

def _parenthesize_text(T, p=None, text_list=None):
    if p is None:
        p = T.root()
        text_list = []
    text_list.append(p.element())
    if T.num_children(p ) > 0:
        text_list.append(' ( ')
        for c in T.children(p):
            text_list = _parenthesize_text(T, c, text_list)
            text_list.append(', ')
        text_list.pop()
        text_list.append(' ) ')
    return text_list

if __name__ == '__main__':
    t = LinkedBinaryTree()
    t._add_root('Electronics R’Us')
    t._add_left(t.root(), 'R&D')
    t._add_right(t.root(), 'Sales')
    t._add_left(t.right(t.root()), 'Domestic')
    t._add_right(t.right(t.root()), 'International')
    t._add_left(t.left(t.right(t.root())), 'California')
    t._add_right(t.left(t.right(t.root())), 'NewYork')
    t._add_left(t.right(t.right(t.root())), 'Korea')
    t._add_right(t.right(t.right(t.root())), 'Spain')

    # preorder_print(t)
    # preorder_indent(t)
    # preorder_label(t)
    print(parenthesize(t))