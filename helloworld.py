class FirstClass(object):
    def first(args):
        h = 'h'
        values.append(h)
        FirstClass.second(values)
    def second(args):
        e = 'e'
        values.append(e)
        FirstClass.third(values)
    def third(args):
        l = 'l'
        values.append(l)
        FirstClass.forth(values)
    def forth(args):
        l = 'l'
        values.append(l)
        FirstClass.fifth(values)
    def fifth(args):
        o = 'o'
        values.append(o)
        SecondClass.first(values)


class SecondClass:
    def first(args):
        space = ' '
        values.append(space)
        SecondClass.second(values)
    def second(args):
        w = 'w'
        values.append(w)
        SecondClass.third(values)
    def third(args):
        o = 'o'
        values.append(o)
        SecondClass.forth(values)
    def forth(args):
        r = 'r'
        values.append(r)
        SecondClass.fifth(values)
    def fifth(args):
        l = 'l'
        values.append(l)
        SecondClass.sixth(values)
    def sixth(args):
        d = 'd'
        values.append(d)
        SecondClass.seventh(values)
    def seventh(args):
        if args is not None:
            print("".join(args))
    
    
if __name__ == '__main__':
    values = []
    object = FirstClass()
    object.first()