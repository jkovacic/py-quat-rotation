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
A module with implemented quaternion arithemtics.

Author: Jernej Kovacic
"""

import math
import exception
from instance_checker import InstanceCheck


class QuaternionException(exception.IException) :
    """Exception raised at illegal quaternion operations"""
    pass

        
class Quaternion() :
    """
    This class implements quaternion arithmetics, e.g. basic operations, norm, etc.
    """
    
    # Internal instance members:
    # o - quaternion's scalar component
    # i - quaternion's 'i' component
    # j - quaternion's 'j' component
    # k - quaternion's 'k' component
    
    """Tolerance for determination whether a number is "close enough" to zero"""
    eps = 1e-12

    def __init__(self, o=0.0, i=0.0, j=0.0, k=0.0) :
        """
        A "constructor" that creates an instance of a quaternion and assigns values to its components.
        
        Input:
        o - scalar component of the quaternion (default: 0)
        i - component 'i' of the quaternion (default: 0)
        j - component 'j' of the quaternion (default: 0)
        k - component 'k' of the quaternion (default: 0)
        
        Alternatively 'o' may be a quaternion. In this case, its components
        are copied into self's ones and all other input arguments are ignored.
        
        A QuaternionExceptionxception is raised if any argument is not an instance
        of supported types (int, float, Quaternion).
        """

        # all functionality is already implemented by setQ
        self.setQ(o, i, j, k)
    
    
    def setQ(self, o=0.0, i=0.0, j=0.0, k=0.0) :
        """
        Assigns values of all quaternion's components.

        Input:
        o - scalar component of the quaternion (default: 0)
        i - component 'i' of the quaternion (default: 0)
        j - component 'j' of the quaternion (default: 0)
        k - component 'k' of the quaternion (default: 0)

        Alternatively 'o' may be a quaternion. In this case, its components
        are copied into self's ones and all other input arguments are ignored.
        
        A QuaternionExceptionxception is raised if any argument is not an instance
        of supported types (int, float, Quaternion).
        """

        if Quaternion.isQuaternion(o) :
            # If o is a quaternion, simply copy its components...
            self.o = o.o
            self.i = o.i
            self.j = o.j
            self.k = o.k
        else:
            # otherwise check if all inputs are floats or integers...
            if not (
                InstanceCheck.isFloat(o) and 
                InstanceCheck.isFloat(i) and 
                InstanceCheck.isFloat(j) and
                InstanceCheck.isFloat(k) ) :
                    raise QuaternionException("Invalid input arguments")
            
            # if they are, just assign their values to quaternion's components
            self.o = o;
            self.i = i;
            self.j = j;
            self.k = k;

            return self
            
            
    def getScalar(self) :
	"""Returns the scalar component of the quaternion"""
        return self.o
    
    def getI(self) :
        """Returns the component 'i' of the quaternion"""
        return self.i
    
    def getJ(self) :
        """Returns the component 'j' of the quaternion"""
        return self.j
    
    def getK(self) :
        """Returns the component 'k' of the quaternion"""
        return self.k
    
    def setScalar(self, o=0.0) :
        """
        Assigns the scalar component of the quaternion.
        
        Input:
        o - value of the scalar component (default: 0)
        
        Raises a QuaternionException if 'o' is not an instance
        of a supported type (float or int).
        """

        if not InstanceCheck.isFloat(o) :
            raise QuaternionException("Invalid input argument")
        self.o = o
        return self

        
    def setI(self, i=0.0) :
        """
        Assigns the component 'i' of the quaternion.
        
        Input:
        i - value of the component 'i' (default: 0)
        
        Raises a QuaternionException if 'i' is not an instance 
        of a supported type (float or int).
        """

        if not InstanceCheck.isFloat(i) :
            raise QuaternionException("Invalid input argument")
        self.i = i;
        return self
    

    def setJ(self, j=0.0) :
        """
        Assigns the component 'j' of the quaternion.
        
        Input:
        j - value of the component 'j' (default: 0)
        
        Raises a QuaternionException if 'j' is not an instance
        of a supported type (float or int).
        """

        if not InstanceCheck.isFloat(j) :
            raise QuaternionException("Invalid input argument")
        self.j = j
        return self

    
    def setK(self, k=0.0) :
        """
        Assigns the component 'k' of the quaternion.

        Input:
        k - value of the component 'k' (default: 0)

        Raises a QuaternionException if 'k' is not an instance 
        of a supported type (float or int).
        """

        if not InstanceCheck.isFloat(k) :
            raise QuaternionException("Invalid input argument")
        self.k = k
        return self

        
    def __add__(self, q) :
        """
        Implementation of the addition operator '+' of two quaternions.
        
        Input:
        q - quaternion or a float value to be added to this one
        
        Return:
        a new instance of Quaternion
        
        A QuaternionException is raised if 'q' is not an instance of
        Quaternion, float or int.
        """

        # Addition of quaternions is trivial:
        #
        #   (a1 + b1*i + c1*j + d1*k) + (a2 + b2*i + c2*j + d2*k) =
        # = ( (a1+a2) + (b1+b2)*i + (c1+c2)*j + (d1+d2)*k )

        if Quaternion.isQuaternion(q) :
            return Quaternion(
                self.o + q.o,
                self.i + q.i,
                self.j + q.j,
                self.k + q.k )
        elif InstanceCheck.isFloat(q) :
            return Quaternion(
                self.o + q,
                self.i,
                self.j,
                self.k )
        else:
            raise QuaternionException("Input must be a quaternion or a float")


    def __sub__(self, q) :
        """
        Implementation of the subtraction operator '-' of two quaternions.
        
        Input:
        q - quaternion or a float value to be subtracted from this one
        
        Return:
        a new instance of Quaternion
        
        A QuaternionException is raised if 'q' is not an instance of 
        Quaternion, float or int.
        """
        
        # Subtraction of quaternions is trivial:
        #
        #   (a1 + b1*i + c1*j + d1*k) - (a2 + b2*i + c2*j + d2*k) =
        # = ( (a1-a2) + (b1-b2)*i + (c1-c2)*j + (d1-d2)*k )

        if Quaternion.isQuaternion(q) :
            return Quaternion(
                self.o - q.o,
                self.i - q.i,
                self.j - q.j,
                self.k - q.k ) 
        elif InstanceCheck.isFloat(q) :
            return Quaternion(
                self.o - q,
                self.i,
                self.j,
                self.k ) 
        else:
            raise QuaternionException("Input must be a quaternion or a float")


    def __mul__(self, q) :
        """
        Implementation of the multiplication operator '*' of two quaternions.
        Note that multiplication of quaternions is not commutative: (p*q != q*p)
        
        Input:
        q - quaternion or a float value to be multiplied by this one
        
        Return:
        a new instance of Quaternion
        
        A QuaternionException is raised if 'q' is not an instance of 
        Quaternion, float or int.
        """
        
        # From the following definitions:
        # i*i = j*j = k*k = -1,
        # i*j = k, j*i = -k, j*k = i, k*j = -i, k*i = j and i*k = -j,
        # the following formula can be quickly derived:
        #
        # (a1 + b1*i + c1*j + d1*k) * (a2 + b2*i + c2*j + d2*k) =
        # = (a1*a2 - b1*b2 - c1*c2 - d1*d2) +
        # + (a1*b2 + b1*a2 + c1*d2 - d1*c2) * i +
        # + (a1*c2 - b1*d2 + c1*a2 + d1*b2) * j +
        # + (a1*d2 + b1*c2 - c1*b2 + d1*a2) * k
        #
        # Note: The following script for GNU Octave or Matlab can be used
        # for a quick unit test of the function:
        # http://mind.cog.jhu.edu/courses/680/octave/Installers/Octave/Octave.OSX10.6/Applications/MATLAB_R2009b.app/toolbox/aero/aero/quatmultiply.m

        if Quaternion.isQuaternion(q) :
            return Quaternion(
                self.o * q.o - self.i * q.i - self.j * q.j - self.k * q.k,
                self.o * q.i + self.i * q.o + self.j * q.k - self.k * q.j,
                self.o * q.j - self.i * q.k + self.j * q.o + self.k * q.i,
                self.o * q.k + self.i * q.j - self.j * q.i + self.k * q.o )
        elif InstanceCheck.isFloat(q) :
            return Quaternion(
                self.o * q,
                self.i * q,
                self.j * q,
                self.k * q )
        else:
            raise QuaternionException("Input must be a quaternion or a float")
   

    def __iadd__(self, q) :
        """
        Addition operator (+=) that adds a quaternion to this one and assigns the sum to itself.
        
        Input:
        q - quaternion or a float value to be added to this one
        
        Return:
        a reference to itself
        
        A QuaternionException is raised if 'q' is not an instance of 
        Quaternion, float or int.
        """
        
        # For a definition of quaternion addition, see __add__

        if Quaternion.isQuaternion(q) :
            self.o += q.o
            self.i += q.i
            self.j += q.j
            self.k += q.k
        elif InstanceCheck.isFloat(q) :
            self.o += q
        else:
            raise QuaternionException("Input must be a quaternion or a float")
        return self


    def __isub__(self, q) :
        """
        Subtraction operator (-=) that subtracts a quaternion from this one and assigns the difference to itself.
        
        Input:
        q - quaternion or a float value to be subtracted from this one
        
        Return:
        a reference to itself
        
        A QuaternionException is raised if 'q' is not an instance of 
        Quaternion, float or int.
        """
        
        # For a definition of quaternion subtraction, see __sub__

        if Quaternion.isQuaternion(q) :
            self.o -= q.o
            self.i -= q.i
            self.j -= q.j
            self.k -= q.k
        elif InstanceCheck.isFloat(q) :
            self.o -= q
        else:
            raise QuaternionException("Input must be a quaternion or a float")
        return self


    def __imul__(self, q) :
        """
        Multiplication operator (*=) that multiplies this by a quaternion and assigns the product to itself.
        
        Input:
        q - quaternion or a float value to be multiplied to this one
        
        Return:
        a reference to itself
        
        A QuaternionException is raised if 'q' is not an instance of 
        Quaternion, float or int.
        """
        
        # For a definition of quaternion multiplication, see __mul__

        if Quaternion.isQuaternion(q) :
            # From maintanance poit of view, this would
            # a more elegant solution:
            #qaux = self * q;
            #self.o = qaux.o;
            #self.i = qaux.i
            #self.j = qaux.j
            #self.k = qaux.k
            # However, this one slightly reduces overhead with
            # instantiation and destruction of another instance of Quaternion:
            self.o, self.i, self.j, self. k = \
                self.o * q.o - self.i * q.i - self.j * q.j - self.k * q.k, \
                self.o * q.i + self.i * q.o + self.j * q.k - self.k * q.j, \
                self.o * q.j - self.i * q.k + self.j * q.o + self.k * q.i, \
                self.o * q.k + self.i * q.j - self.j * q.i + self.k * q.o 
        elif  InstanceCheck.isFloat(q) :
            self.o *= q
            self.i *= q
            self.j *= q
            self.k *= q
        else:
            raise QuaternionException("Input must be a quaternion or a float")
        return self


    def __neg__(self) :
        """
        Unary negation operator (-).
        
        Return:
        negated -self (all components are negated)
        """

        return Quaternion(
            -self.o,
            -self.i,
            -self.j,
            -self.k )


    def conj(self) :
        """
        Conjugation of a quaternion, i.e. components 'i', 'j' an 'k' are negated.
        
        Return: conjugation of self
        """

        return Quaternion(
            self.o,
            -self.i,
            -self.j,
            -self.k )

 
    def __sqsum(self) :
        # An auxiliary method that calculates the sum of all components' squares
        return self.o*self.o + self.i*self.i + self.j*self.j + self.k*self.k

        
    def norm(self) :
        """
        Norm of a quaternion, i.e. a square root of the sum of all components' squares
        """
        return math.sqrt(self.__sqsum())


    def reciprocal(self) :
        """
        Reciprocal of a quaternion (q^(-1)), satisfying condition: q*q^(-1) + q^(-1)*q = 1.
        
        A QuaternionException is raised if quaternion's norm equals 0.
        """
        
        # Reciprocal of q is defined as:
        #
        # q^(-1) = q* / ||q||^2
        #
        # The following formula can be derived from it:
        #
        #                           a - b*i - c*j - d*k
        # (a+b*i+c*j+d*k)^(-1) = -------------------------
        #                          a^2 + b^2 + c^2 + d^2

        nsq = self.__sqsum()
        if nsq < Quaternion.eps :
            raise QuaternionException("Reciprocal of a zero-quaternion does not exist")
        return Quaternion(
            self.o / nsq,
            -self.i / nsq,
            -self.j / nsq,
            -self.k / nsq )

 
    def unit(self) :
        """
        A unit quaternion of 'self', i.e. it norm is equal to 1.
        
        A QuaternionException is raised if quaternion's norm equals 0.
        """

        n = self.norm()
        if n < Quaternion.eps :
            raise QuaternionException("Cannot normalize a zero-quaternion")
        return Quaternion(
            self.o / n,
            self.i / n,
            self.j / n,
            self.k / n )


    def __str__(self) :
        """
        "Nicely" formatted output of the quaternion (e.g. 4-5i+7j-3k).
        
        The method is called by print().
        """
        
        # Primarily the method was introduced for brief unit testing purposes
        # and not much effort was invested into a visually "nice" output
  	
        outstr = str(self.o)
        
        if self.i >= 0 :
            outstr += '+'
        outstr += str(self.i) + 'i'
        
        if self.j >= 0 :
            outstr += '+'
        outstr += str(self.j) + 'j'
        
        if self.k >= 0 :
            outstr += '+'
        outstr += str(self.k) + 'k'
        
        return outstr

    @staticmethod
    def isQuaternion(q) :
        """Is 'q' an instance of Quaternion"""
        return isinstance(q, Quaternion)
