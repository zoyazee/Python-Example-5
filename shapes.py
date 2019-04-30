
class Circle:
	def __init__(self,r,Area,Circumference):
		self.r=r
		self.Area=Area
		self.Circumference=Circumference


	def Area(self):
		Area=3.142*r*r
		return Area

	def Circumference(self):
		Circumference=2*3.142*r
		return Circumference

class Square:
	def __init__(self,a,Area,Perimeter):
		self.a=a
		self.Area=Area
		self.Circumfrence=Circumference

	def Area(self):
		Area=a*a
		return Area

	def Perimeter(self):
		Perimeter=4*a
		return Perimeter

class Rectangle:
	def __init__(self,w,l,Area,Perimeter):
		self.w=w
		self.l=l
		self.Area=Area
		self.Perimeter=Perimeter

	def Area(self):
		Area=w*l
		return Area

	def Perimeter(self):
		Perimeter=2*l+2*w
		return Perimeter

class Sphere:
	def __init__(self,radius,Surface_area,Volume):
		self.radius=radius
		self.Surface_area=surface_area
		self.Volume=Volume

	def Surface_area(self):
		Surface_area=4*3.14*r*r
		return Surface_area

	def Volume(self):
		Volume=4/3(3.142*r*r)
		return Volume





