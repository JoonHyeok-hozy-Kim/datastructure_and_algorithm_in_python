from DataStructures.tree import LinkedBinaryTree, EulerTour

class PreorderPrintIndentedTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        print(2*d*' '+str(p.element()))

class PreorderPrintLabledTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        text_list = [2*d*' ']
        for i in path:
            text_list.append(str(i+1))
            text_list.append('.')
        text_list.append(' ')
        text_list.append(str(p.element()))
        print(''.join(text_list))

class ParenthesizeTour(EulerTour):

    def _hook_previsit(self, p, d, path):
        print(str(p.element()), end='')
        if not self.tree().is_leaf(p):
            print(' (', end='')

    def _hook_postvisit(self, p, d, path, results):
        if not self.tree().is_leaf(p):
            print(') ', end='')

        if self.tree().root() != p:
            parent = self.tree().parent(p)
            if self.tree().num_children(parent) == 2 and self.tree().left(parent) == p:
                print(', ', end='')

if __name__ == '__main__':
    a = LinkedBinaryTree()
    a._add_root('a')
    a._add_left(a.root(), 'b')
    a._add_right(a.root(), 'c')
    a._add_left(a.left(a.root()), 'd')
    a._add_right(a.left(a.root()), 'e')
    a._add_left(a.right(a.root()), 'f')
    a._add_right(a.right(a.root()), 'g')

    # for i in a.positions():
    #     print(i.element())

    e1 = PreorderPrintIndentedTour(a)
    e1.execute()

    e2 = PreorderPrintLabledTour(a)
    e2.execute()

    e3 = ParenthesizeTour(a)
    e3.execute()

