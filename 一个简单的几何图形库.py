import math
import numpy as np
from matplotlib.patches import Circle
import matplotlib.pyplot as plt
class ExcessivePointsException(Exception):
    def __init__(self):
        self.data = "ExcessivePointsException" #定义异常
class UnknownGeometryException(Exception):
    def __init__(self):
        self.data = "UnknownGeometryException" #定义异常
class Geometry(object):
    def __init__(self):
        pass
    @property
    def gtype(self):
        return "unknown"
class Point(Geometry):
    def __init__(self,x,y):
        self._x = x
        self._y = y
    @property     
    def gtype(self):
        return "point"
    @property
    def x(self):
        return self._x 
    @x.setter
    def x(self,v):
        self._x = v
    @property
    def y(self):
        return self._y 
    @y.setter
    def y(self,v):
        self._y = v
    @property
    def length(self):
        return math.sqrt(self._x**2+self._y**2)
    def __str__(self):
        return "Point(%f,%f)"%(self._x,self._y)
class Rect(Point):
    def __init__(self,x,y,w,h):
        Point.__init__(self,x,y)
        self._w = w
        self._h = h
    @property
    def gtype(self):
        return "Rectangle"
    @property
    def w(self):
        return self._w
    @property
    def h(self):
        return self._h
    @property
    def area(self):
        return self._w*self._h
    def draw(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        rect = plt.Rectangle((self._x,self._y),self.w,self.h)
        ax.add_patch(rect)
        plt.axis('equal') 
    def __str__(self):
        return "Rectangle(%f,%f,%f,%f)"%(self._x,self._y,self._w,self._h)
class myCircle(Point):
    def __init__(self,x,y,r):
        Point.__init__(self,x,y)#继承了Point的方法
        self._r = r    
        self._x = x
        self._y = y
    def draw(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        cir1 = Circle(xy = (self._x, self._y), radius=self._r)
        ax.add_patch(cir1)
        plt.axis('equal') 
        plt.show()
    @property
    def gtype(self):
        return "circle"
    @property
    def area(self):
        return math.pi*(self._r)**2
    @property
    def r(self):
        return self._r
    def __str__(self):
        return "Circle(%f,%f,%f)"%(self._x,self._y,self._r)
    
class Ellipse(Point):
    def __init__(self,x,y,a,b):
        Point.__init__(self,x,y)
        self._a = a
        self._b = b
        self._c = math.sqrt(self._a**2-self._b**2)
    @property
    def a(self):
        return self._a
    @property
    def b(self):
        return self._b
    @property
    def e(self):
        return self._c/self._a 
    @property
    def c(self):
        return self._c
    @property
    def area(self):
        return math.pi*self._a*self._b
    def __str__(self):
        return "Ellipse(%f,%f,%f,%f)"%(self._x,self._y,self._a,self._b)

class Line(Geometry):#继承自几何，为了让Line2d能使用point的方法
    def __init__(self,points):
        self.points = points
        x0 = points[0][0]
        y0 = points[0][1]
        x1 = points[1][0]
        y1 = points[1][1]
        self._start = Point(x0,y0)
        self._end = Point(x1,y1)
    def draw(self):
        x = []
        y = []
        x.append(self.points[0][0])
        x.append(self.points[1][0])
        y.append(self.points[0][1])
        y.append(self.points[1][1])
        plt.plot(x,y)
        plt.show()
    @property
    def gtype(self):
        return "Line"
    @property
    def start(self):
        print(Point(self._start.x,self._start.y))
    @property
    def end(self):
        print(Point(self._end.x,self._end.y))
    @property
    def length(self):
        return math.sqrt((self._end.x-self._start.x)**2+(self._end.y-self._start.y)**2)     
    def __str__(self):
        return ("start.x = %.3f, start.y = %.3f, end.x = %.3f, end.y = %.3f"
        %(self._start.x,self._start.y,self._end.x,self._end.y))

class Polyline(Line):
    def __init__(self, PolyPoints):
        self.PolyPoints =  PolyPoints
        self.point_len = len(PolyPoints)
        self._start = Point(PolyPoints[0][0],PolyPoints[0][1])
        self._end = Point(PolyPoints[-1][0],PolyPoints[-1][1])
        self.pointsofline = []
        self.linepieces = []
        self._length = 0
        for point in range(0, self.point_len):
            self.temp_point = Point(PolyPoints[point][0],PolyPoints[point][1])
            self.pointsofline.append(self.temp_point)
        for point in range(0, self.point_len-1):
            list = [[PolyPoints[point][0], PolyPoints[point][1]],
            [PolyPoints[point+1][0], PolyPoints[point+1][1]]]
            linenew = Line(list)
            self.linepieces.append(linenew)
            self._length += linenew.length
    def draw(self):
        x = []
        y = []
        for point in self.PolyPoints:
            x.append(point[0])
            y.append(point[1])
        plt.plot(x,y)
        plt.show()
    @property
    def allpoints(self):
        print("The polyline has %d points as following:"%self.point_len)
        for i in range(0,self.point_len):
            print(self.pointsofline[i])
    def point(self, i):
        print("POINT %d is: "%i,end='')
        print(self.pointsofline[i])
    @property
    def allpieces(self):
        print("The polyline has %d pieces as following:"%(self.point_len-1))
        for i in range(0,self.point_len-1):
            print("PIECE %d: "%(i+1),end='')
            print(self.linepieces[i])
    def piece(self, i):
        print("PIECE %d is: "%i,end='')
        print(self.linepieces[i])   
    @property
    def length(self):
        return self._length
    @property
    def start(self):
        return ((self.PolyPoints[0][0], self.PolyPoints[0][1])) 
    @property
    def end(self):
        return ((self.PolyPoints[-1][0], self.PolyPoints[-1][1])) 
    def __str__(self):
        return ("start.x = %.3f, start.y = %.3f, end.x = %.3f, end. = %.3f, length = %.4f, has %d points"%
        (self.PolyPoints[0][0],self.PolyPoints[0][1],
        self.PolyPoints[-1][0],self.PolyPoints[-1][1], self._length, self.length))
class GeometryCache():
    def __init__(self):
        self.geometry_stas = {'Point':0,'Rectangle':0,'Line':0,'Circle':0,'Polyline':0}#储存图形个数
    @property
    def gtype(self):
        return "unknown"
    def load(self, filename):
        file = open(filename, 'r')
        self.geos = []
        self.lstLine = []#创建储存
        self.lstPoint = []
        self.lstPolyline = []
        self.lstRectangle = []
        self.lstCircle = []
        for line in file:
           temp = line.split(" ")#按空格得到一个列表
           self.geos.append(temp)#将当前行append到geos
        for item in self.geos:#item即为单个图形的所有信息，item[0]是名称，1及以后是信息
            try:
                if(item[0].lower() == 'point'):
                    try:#如果输入的点多于一个
                        if(len(item)>2):
                            print(1)
                            raise ExcessivePointsException
                    except ExcessivePointsException as ex:
                        raise ex
                    else:
                        point = item[1].split(",")#点是“数字，数字”，使用split得到坐标列表
                        to_float(point)#文本到数字
                        self.Point = Point(point[0],point[1])
                        self.lstPoint.append(self.Point)
                        self.geometry_stas['Point'] += 1 #记录加一
                elif(item[0].lower() == 'rectangle'):
                    item[2] = float(item[2])
                    item[3] = float(item[3])
                    point = item[1].split(",")
                    to_float(point)
                    self.Rect = Rect(point[0],point[1],item[2], item[3])
                    self.lstRectangle.append(self.Rect)
                    self.geometry_stas['Rectangle'] += 1    
                
                elif(item[0].lower() == 'circle'):
                    item[2] = float(item[2])
                    point = item[1].split(",")
                    to_float(point)
                    self.Circle = myCircle(point[0],point[1],item[2])
                    self.lstCircle.append(self.Circle)
                    self.geometry_stas['Circle'] += 1
                elif(item[0].lower() == 'line'):
                    try:#如果输入的点多于两个
                        if(len(item)>3):
                            print(1)
                            raise ExcessivePointsException
                    except ExcessivePointsException as ex:
                        raise ex
                    else:
                        points = []
                        points_input(points, item)#多个点由str转为float
                        self.Line = Line(points)#以列表传入
                        self.geometry_stas['Line'] += 1
                        self.lstLine.append(self.Line)
                    
                elif(item[0].lower() == 'polyline'):
                    points = []
                    points_input(points, item)
                    self.Polyline = Polyline(points)
                    self.geometry_stas['Polyline'] += 1
                    self.lstPolyline.append(self.Polyline)
                else:#如果不是已经定义的图形
                    raise UnknownGeometryException
            except UnknownGeometryException:
                raise UnknownGeometryException
        file.close()        
    #下面用了两种不同的方法输出全部属性，一种是重新定义输出内容，一种是利用__str__重载
    def allPoints(self):
        i = 1
        for item in self.lstPoint:
            print("Point%d"%i,end = ":")
            print("(%.3f,%.3f)"%(item.x,item.y))
            i = i + 1
    def allCircles(self):
        i = 1
        for item in self.lstCircle:
            print("Circle%d"%i,end = ":")
            print("center:(%.3f,%.3f),radius=%.3f"%(item.x,item.y,item.r))
            i = i + 1
    def allRectangles(self):
        i = 1
        for item in self.lstRectangle:
            print("Rectangle%d"%i,end = ":")
            print("vertex:(%.3f,%.3f), high:%.3f, width:%.3f"%(item.x, item.y, item.h, item.w))
            i = i + 1
    def allLines(self):
        i = 1
        for item in self.lstLine:
            print("Line%d"%i,end = ":")
            print(item)
            i = i + 1
    def allPolylines(self):
        i = 1
        for item in self.lstPolyline:
            print("Polyline%d"%i,end = ":")
            print(item)
            i = i + 1
    def allGeometries(self):
        self.allPoints()
        self.allCircles()
        self.allRectangles()
        self.allLines()
        self.allPolylines()
    @property#输出图形的总个数
    def countPoints(self):
        print("number of points:",end=" ")
        print(self.geometry_stas['Point'])
    @property
    def countCircles(self):                
        print("number of circles:",end=" ")
        print(self.geometry_stas['Circle'])
    @property
    def countRectangles(self):
        print("number of rectangles:",end=" ")
        print(self.geometry_stas['Rectangle'])
    @property
    def countLines(self):
        print("number of lines:",end=" ")
        print(self.geometry_stas['Line'])
    @property
    def countPolylines(self):
        print("number of polylines:",end=" ")
        print(self.geometry_stas['Polyline'])
    @property
    def countAll(self):
        print("number of geometries:",end=" ")  
        print(self.geometry_stas['Polyline']+self.geometry_stas['Line']+self.geometry_stas['Rectangle']+
              self.geometry_stas['Circle']+self.geometry_stas['Point'])
def points_input(points,names):
    for point in names[1:len(names)]:
        pointlist = point.split(",")
        to_float(pointlist)                   
        points.append(pointlist) 
        
def to_float(lst):
    for it in range(0,len(lst)):
        lst[it] = float(lst[it])    

