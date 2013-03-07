# Copyright 2013, Jernej Kovacic
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
A module with implementation of 3D rotations,
based on quaternion arithmetics.

Author: Jernej Kovacic
"""

import math
import exception
from quaternion import Quaternion, QuaternionException
from instance_checker import InstanceCheck

        

# Point3D and PointException may be moved into another module when/if
# more mathematical funxtionality is implemented
class PointException(exception.IException) :
    """Exception raised at illegal operations with points"""
    pass


class Point3D() :
    """
    A class representing a 3d point or a 3D vector. It has 3 internal
    instance members:
    x - x component
    y - y component
    z - z component
    """

    def __init__(self, x=0.0, y=0.0, z=0.0) :
        """
        A "constructor" that initializes a point
        
        Input:
        x - x component of a point/vector
        y - y component of a point/vector
        z - z component of a point/vector
        
        'x' may also be an instance of Point3D. In this case, the other
        arguments are ignored and the method acts as a copy constructor.
        
        A PointException is raised if input arguments are of invalid types.
        """          
        if InstanceCheck.isFloat(x) and InstanceCheck.isFloat(y) and InstanceCheck.isFloat(z) :
            self.x = x
            self.y = y
            self.z = z
        elif Point3D.isPoint3D(x) :
            self.setPoint(x)
        else :
            raise PointException("Invalid input arguments")

    def getX(self) :
        """Returns point's x-component"""
        return self.x
    
    def getY(self) :
        """Returns point's y-component"""
        return self.y
        
    def getZ(self) :
        """Returns point's z-component"""
        return self.z
        
    def setX(self, x=0.0) :
        """
        Sets point's x-component. Other components are not changed.
        A PointException is raised if x is not a float or integer value.
        """
        if InstanceCheck.isFloat(x) :
            self.x = x
        else:
            raise PointException("Invalid input argument")
            
    def setY(self, y=0.0) :
        """
        Sets point's y-component. Other components are not changed.
        A PointException is raised if x is not a float or integer value.
        """
        if InstanceCheck.isFloat(y) :
            self.y = y
        else :
            raise PointException("Invalid input argument")
            
    def setZ(self, z=0.0) :
        """
        Sets point's z-component. Other components are not changed.
        A PointException is raised if x is not a float or integer value.
        """
        if InstanceCheck.isFloat(z) :
            self.z = z
        else :
            raise PointException("Invalid input argument")

    def setPoint(self, p) :
        """
        Copies the point 'p' into this one.
        A PointException is raised if 'p' is not an instance of Point3D.        
        """
        if Point3D.isPoint3D(p) :
            self.x = p.x
            self.y = p.y
            self.z = p.z
        else :
            raise PointException("Invalid input argument")

    def sqSum(self) :
        """A convenience method that calculates a sum of all components' squares"""
        return self.x*self.x + self.y*self.y + self.z*self.z
        
    def __str__(self) :
        """
        "Nicely" formatted output of the point, e.g. "( 1.3, -4.7, 2.89 )".
        
        The method is called by print().
        """
        outstr = '( ' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ' )'
        return outstr
        
    @staticmethod
    def isPoint3D(p) :
        """Is 'p' an instance of Point3D?"""
        return isinstance(p, Point3D)





class RotationException(exception.IException) :
    """Exception raised at illegal operations"""
    pass


class Rotation() :
    """
    3D rotation around an axis, based on quaternion arithmetics.
    
    For the mathematical background about quaternion based rotation, see
    http://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation
    """
    
    # Private internal instance members:
    # __r - a vector representing the axis of ratoation (Point3D)
    # __theta - angle of rotation (in radians)
    # __q - roatation quaternion
    
    def __init__(self, rx=0.0, ry=0.0, rz=0.0, angle=0.0) :
        """
        A "constructor" that initializes an object.__class__
        
        Input:
        - rx - x - component of the vector (default: 0)
        - ry - y - component of the vector (default: 0)
        - rz - z - component of the vector (default: 0)
        - angle - angle of rotation in radians (default: 0)
        
        'rx' may also be an instance of a Point3D. In this case, ry and rz
        are ignored and rx's components are copied into this object.
        
        Note that the vector will automatically be converted into a unit vector.
        
        A RotationException is raised if input arguments are of invalid types.
        """
        if not InstanceCheck.isFloat(angle) :
            raise RotationException("Angle must be a float value")

        self.__theta = angle
        self.setAxis(rx, ry, rz)


    def setAxis(self, rx=0.0, ry=0.0, rz=0.0) :
        """
        Enters a new vector of the rotation. Rotation angle remains unmodified.
        
        Input:
        - rx - x - component of the vector (default: 0)
        - ry - y - component of the vector (default: 0)
        - rz - z - component of the vector (default: 0)
        
        'rx' may also be an instance of a Point3D. In this case, ry and rz
        are ignored and rx's components are copied into this object.
        
        Note that the vector will automatically be converted into a unit vector.
        
        A RotationException is raised if input arguments are of invalid types.
        """
        try :
            self.__r = Point3D(rx, ry, rz)
        except PointException :
            raise RotationException("Invalid input argument")
            
        self.__update()


    def setAngle(self, angle=0.0) :
        """
        Sets a new angle of rotation. 
        Rotation vector's components remain unmodified.
        
        Input:
        - angle - angle of rotation in radians (default: 0)
        
        A RotationException is raised if 'angle' is not a float or integer value.
        """
        if not InstanceCheck.isFloat(angle) :
            raise RotationException("Angle must be float value")
            
        self.__theta = angle
        self.__update()


    def __update(self) :
        # A private method, called after any rotation component (vector or angle)
        # is modified. It normalizes the vector (its length must be 1),
        # updates self.__r and recalculates the rotation quaternion (self.__q).
        #
        # A RotationException is raised if any quaternion operation fails.
        try :
            # copy vector's components into the quaternion and normalize it:
            self.__q = Quaternion(0.0, self.__r.x, self.__r.y, self.__r.z).unit()     
            
            # update __r to a unit vector
            self.__r.x = self.__q.getI()
            self.__r.y = self.__q.getJ() 
            self.__r.z = self.__q.getK()
            
            # Calculate the rotation quaternion, depending on rot. vector and angle:
            # For more info, see::
            # http://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation
            self.__q *= math.sin(0.5*self.__theta)
            self.__q += math.cos(0.5*self.__theta)

        except QuaternionException as qex :
            raise RotationException("Could not generate a rotation quaternion: '{0}'".format(qex))
            
            
    def getAxis(self, factor=1.0) :
        """
        Returns the axis of rotation, represented by a vector (an instance of Point3D).
        
        Note that a unit vector, multiplied by the factor (default: 1) will be returned.
        """
        return Point3D(
                    self.__r.x * factor,
                    self.__r.y * factor,
                    self.__r.z * factor )
    
    def getAngle(self) :
        """Returns the angle of rotation in radians."""
        return self.__theta
    
    def getRotationQuaternion(self) :
        """Returns a rotation quaternion."""
        return self.__q
        
    def rotate(self, p) :
        """
        Performs a rotation of point 'p' around the previously specified
        axis of rotation by the previoulsy specifed angle.
        
        Input:
        - p - a point ot be rotated (an instance of Point3D)
        
        Returns coordinates of the rotated point (an instance of Point3D).
        
        A RotationException is raised if 'p' is not an instance of Point3D.
        """
        if not Point3D.isPoint3D(p) :
            raise RotationException("Input must be an instance of Point3D")
        
        # For more info about rotation using quaternions, see:
        # http://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation
        pq = Quaternion(0, p.x, p.y, p.z)
        pqr = self.__q * pq * self.__q.conj()

        return Point3D( pqr.getI(),
                        pqr.getJ(),
                        pqr.getK() )        
        
        
    @staticmethod    
    def deg2rad(deg) :
        """Conversion from angle degrees to radians"""
        return deg*math.pi/180.0
        
    @staticmethod
    def rad2deg(rad) :
        """Conversion from radians to angle degrees"""
        return rad*180.0/math.pi
