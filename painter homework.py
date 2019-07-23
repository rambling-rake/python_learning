class Shape(object):

    def __init__(self):
       self.style = None

    def draw(self):
        pass

    def show(self):
        pass

    def hide(self):
        pass

    def rotate(self, pt,angle):
        pass

    def scale(self, factor):
        pass

    def move (self, x,y):
        pass

    def duplicate(self):
        pass

    def contains(self, x, y):
        pass


class Point(Shape):
    pass

    def draw(self):
        pass


class Line(Shape):
    pass

    def draw(self):
        pass


class Circle(Shape):
    pass

    def draw(self):
        pass


class Triangle(Shape):
    pass

    def draw(self):
        pass


class Rectangle(Shape):
    pass

    def draw(self):
        pass


class Screen(object):
    def __init__(self):
        self.height = None
        self.width = None
        self.leftUpper = None
        self.bgColor = None
        self.shapeContainer:list[Shape]

    def addshape(self):
        pass

    def removeshape(self):
        pass

    def getshape (self):
        pass

    def update (self):
        pass

    def getShapeFt(self, x,y):
        pass


class Style(object):
    def __init__(self):
        self.color = None
        self.thickness = None
        self.linestyle = None
        self.bgColor = None
        self.textstyle

    def applyStyle (self):
        pass


class Group(object):
    def __init__(self):
        self.name = None
        self.UIDContainer:list[Shape] = None

    def move (self):
        pass

    def apply (Style):
        pass


class Compound(Shape):
    def __init__(self):
        self.children:list[Shape] = None

    def getChildren (self):
        pass

# point = Point()
# point2 = Point()
#
# point.draw()
# point.test()
# print point.style
# point.style = 321
# print point.style
# print point2.style
#
# print dir(Point)
# print dir(object)
