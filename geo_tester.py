import mygeometry as ge
p = ge.GeometryCache()
p.load("f.txt")
p.allPoints()
p.allCircles()
p.allRectangles()
p.allLines()
p.allPolylines()
p.allGeometries()#查看所有几何图形的信息
p.countPoints#几何图形计数
p.countCircles
p.countRectangles
p.countLines
p.countPolylines
p.countAll
p.lstPolyline[0].allpieces#查看所有线段
p.lstPolyline[0].point(1)#查询第一个点的信息
print(p.lstRectangle[0].area)
print(p.lstPolyline[0].length)
print(p.lstCircle[1].r)
p.lstPolyline[0].draw()#绘出线段
