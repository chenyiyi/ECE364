import math,os,sys,re,operator

class PointND:
    def __init__(self, *args):
        self.t = args
        self.n = len(args)
        for i in args:
            if type(i) is not float:
                raise ValueError("Cannot instantiate an object with non-float values.")

    def __str__(self):
        ss = '('
        for i in range(0, self.n-1):
            ss += str('%.2f' %self.t[i])
            ss += ', '
        ss += str('%.2f' %self.t[self.n-1])
        ss += ")"
        return ss

    def __hash__(self):
        return hash(self.t)

    def distanceFrom(self, other):
        if self.n != other.n:
            raise ValueError("Cannot calculate distance between points of different cardinality.")
        else:
            distance = 0
            for i in range(0,self.n):
                distance += (self.t[i]-other.t[i]) **2
            distance = math.sqrt(distance)

        return distance

    def nearestPoint(self, points):
        if (len(points) == 0):
            raise ValueError("Input cannot be empty")
        else:
            mindis = 99999
            closest = None
            for single in points:
                distance = self.distanceFrom(single)
                if distance < mindis:
                    mindis = distance
                    closest = single
        return closest


    def clone(self):
        point = PointND(*self.t)
        return point


    def __add__(self, other):
        if isinstance(other, PointND):
            if self.n != other.n:
                raise ValueError("Cannot operate on points with different cardinalities.")
            else:
                newpoint = []
                for i in range(0, self.n):
                    newpoint.append(self.t[i] + other.t[i])
                returnpoint = PointND(*tuple(newpoint))
                return returnpoint

        if isinstance(other, float):
            newpoint = []
            for i in range(0, self.n):
                newpoint.append(self.t[i] + other)
            returnpoint = PointND(*tuple(newpoint))
            return returnpoint

    def __radd__(self, other):
        if isinstance(other, float):
            newpoint = []
            for i in range(0, self.n):
                newpoint.append(self.t[i] + other)
            returnpoint = PointND(*tuple(newpoint))
            return returnpoint


    def __sub__(self, other):
        if isinstance(other, PointND):
            if self.n != other.n:
                raise ValueError("Cannot operate on points with different cardinalities.")
            else:
                newpoint = []
                for i in range(0, self.n):
                    newpoint.append(self.t[i] - other.t[i])
                returnpoint = PointND(*tuple(newpoint))
                return returnpoint

        if isinstance(other, float):
            newpoint = []
            for i in range(0, self.n):
                newpoint.append(self.t[i] - other)
            returnpoint = PointND(*tuple(newpoint))
            return returnpoint


    def __mul__(self, other):
        newpoint = []
        for i in range(0, self.n):
            newpoint.append(self.t[i] * other)
        returnpoint = PointND(*tuple(newpoint))
        return returnpoint

    def __rmul__(self, other):
        newpoint = []
        for i in range(0, self.n):
            newpoint.append(self.t[i] * other)
        returnpoint = PointND(*tuple(newpoint))
        return returnpoint

    def __truediv__(self, other):
        if isinstance(other, float):
            newpoint = []
            for i in range(0, self.n):
                newpoint.append(self.t[i] / other)
            returnpoint = PointND(*tuple(newpoint))
        return returnpoint

    def __neg__(self):
        newpoint = []
        for i in range(0, self.n):
            newpoint.append(-self.t[i])
        returnpoint = PointND(*tuple(newpoint))
        return returnpoint

    def __getitem__(self, item):
        return self.t[item]

    def __eq__(self, other):
        if self.n != other.n:
            raise ValueError("Cannot operate on points with different cardinalities.")

        for i in range(0, self.n):
            if self.t[i] != other.t[i]:
                return False
        return True

    def __nq__(self, other):
        if self.n != other.n:
            raise ValueError("Cannot operate on points with different cardinalities.")

        for i in range(0, self.n):
            if self.t[i] == other.t[i]:
                return False
        return True


    def __gt__(self, other):
        if self.n != other.n:
            raise ValueError("Cannot operate on points with different cardinalities.")

        ori=[]
        for i in range(0, self.n):
            ori.append(0.0)
        originalpoint = PointND(*tuple(ori))
        firstdis = self.distanceFrom(originalpoint)
        seconddis = other.distanceFrom(originalpoint)
        if firstdis > seconddis:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.n != other.n:
            raise ValueError("Cannot operate on points with different cardinalities.")

        ori=[]
        for i in range(0, self.n):
            ori.append(0.0)
        originalpoint = PointND(*tuple(ori))
        firstdis = self.distanceFrom(originalpoint)
        seconddis = other.distanceFrom(originalpoint)
        if firstdis >= seconddis:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.n != other.n:
            raise ValueError("Cannot operate on points with different cardinalities.")

        ori=[]
        for i in range(0, self.n):
            ori.append(0.0)
        originalpoint = PointND(*tuple(ori))
        firstdis = self.distanceFrom(originalpoint)
        seconddis = other.distanceFrom(originalpoint)
        if firstdis < seconddis:
            return True
        else:
            return False

    def __le__(self, other):
        if self.n != other.n:
            raise ValueError("Cannot operate on points with different cardinalities.")

        ori=[]
        for i in range(0, self.n):
            ori.append(0.0)
        originalpoint = PointND(*tuple(ori))
        firstdis = self.distanceFrom(originalpoint)
        seconddis = other.distanceFrom(originalpoint)
        if firstdis <= seconddis:
            return True
        else:
            return False

class Point3D(PointND):
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z
        PointND.__init__(self,x,y,z)


class PointSet:
    def __init__(self, **kwargs):
        self.points = set(kwargs['pointList'])
        if (len(kwargs['pointList']) == 0):
            raise ValueError("'pointList' input parameter cannot be empty.")
        self.n = kwargs['pointList'][0].n
        for i in kwargs['pointList']:
            if self.n != i.n:
                raise ValueError("Expecting a point with cardinality {0}.".format(self.n))

    def addPoint(self,p):
        if p.n != self.n:
            raise ValueError("Expecting a point with cardinality {0}.".format(self.n))
        else:
            self.points.add(p)

    def count(self):
        return len(self.points)

    def computeBoundingHyperCube(self):
        minpoint=[]
        maxpoint=[]
        for i in range(0,self.n):
            minpoint.append(100000.00)
            maxpoint.append(0.00)
        for dimen in range(0,self.n):
            for single in list(self.points):
                if single.t[dimen] > maxpoint[dimen]:
                    maxpoint[dimen] = single.t[dimen]
                if single.t[dimen] < minpoint[dimen]:
                    minpoint[dimen] = single.t[dimen]

        returnmin = PointND(*tuple(minpoint))
        returnmax = PointND(*tuple(maxpoint))

        return returnmin, returnmax


    def computeNearestNeighbors(self, otherPointSet):
        returnlist = []
        for single in self.points:
            closepoint = single.nearestPoint(otherPointSet.points)
            returnlist.append(tuple([single,closepoint]))
        return returnlist


    def __add__(self, other):
        if other.n != self.n:
            raise ValueError("Expecting a point with cardinality {0}.".format(self.n))
        else:
            self.points.add(other)

        return self

    def __sub__(self, other):
        if other in self.points:
            self.points.remove(other)

        return self

    def __contains__(self, item):
        if item in self.points:
            return True
        else:
            return False