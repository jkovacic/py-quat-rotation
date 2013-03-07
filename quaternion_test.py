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


from __future__ import print_function
import sys
from quaternion import Quaternion, QuaternionException

"""
A collection of unit tests for quaternion arithmetics,
implemented by quaternion.Quaternion-
"""


try:
    # First assign values to unit quaternions:
    o = Quaternion(o=1.0)
    i = Quaternion(i=1.0)
    j = Quaternion(j=1.0)
    k = Quaternion(k=1.0)
    
    print("Unit quaternions:")
    print("o = {0}".format(o))
    print("i = {0}".format(i))
    print("j = {0}".format(j))
    print("k = {0}".format(k))
    print()
    
    print("Squares of unit quaternions:")
    print("o*o = {0}".format(o*o))
    print("i*i = {0}".format(i*i))
    print("j*j = {0}".format(j*j))
    print("k*k = {0}".format(k*k))
    print()
    
    print("Products of components:")
    print("o*i = {0}\ti*o = {1}".format(o*i, i*o))
    print("o*j = {0}\tj*o = {1}".format(o*j, j*o))
    print("o*k = {0}\tk*o = {1}".format(o*k, k*o))
    print("i*j = {0}\tj*i = {1}".format(i*j, j*i))
    print("i*k = {0}\tk*i = {1}".format(i*k, k*i))
    print("j*k = {0}\tk*j = {1}".format(j*k, k*j))
    print()
    
    p = Quaternion(i)
    p.setScalar(-3).setJ(2).setK(-1)
    print("p=({0}, {1}, {2}, {3})".format(p.getScalar(), p.getI(), p.getJ(), p.getK()))
    # sqrt(15) = 3.87298
    print("||p|| = {0} (correct: 3.87298)".format(p.norm()))
    
    q = p.reciprocal()
    qc = "-0.2-0.0666666666667i-0.133333333333j+0.0666666666667k"
    
    print("p**(-1) = {0}\n(correct: {1})".format(q, qc))
    print("p*p**(-1) = {0}".format(p*q)) 
    print("p**(-1)*p = {0}".format(q*p))
    print()
    
    q = Quaternion(1, -2, 3, -4)
    print("q = {0}".format(q))
    print("p+q = {0}".format(p+q))
    print("p-q = {0}".format(p-q))
    print("p*q = {0}".format(p*q)) # -11+2*i-j+18*k
    print("q*p = {0}".format(q*p)) # -11+12*i-13*j+4*k
    print()
    
    p *= q
    print("p*q = {0}".format(p))
    p += q
    print("p*q+q = {0}".format(p))
    p -= q
    print("p*q+q-q = {0}".format(p))
    
    print("q+2 = {0}".format(q+2))
    print("q-7 = {0}".format(q-7))
    print("q*3 = {0}".format(q*3))
    print()
    
    q *= 2
    print("q*2 = {0}".format(q))
    q += 5
    print("q*2+5 = {0}".format(q))
    q -= 5
    print("q*2+5-5 = {0}".format(q))
    
except QuaternionException as ex:
    print("\nQuaternion exception raised: '{0}'".format(ex), file=sys.stderr)
else :
    print("\nQuaternion test completed successfully.")
