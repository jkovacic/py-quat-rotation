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
import math
import sys
from rotation import Rotation, RotationException, Point3D, PointException


"""
A collection of basic unit tests for 3D rotation,
implemented by rotation.Rotation.
"""

try :
    p = Point3D(1,1,1)
    rot = Rotation(rz=1, angle=math.pi/2)
    print("Angle of rotation (must be pi/2 = 90 deg):  {0} deg".format(Rotation.rad2deg(rot.getAngle())))
    print("Rotation around the z-axis:")
    print("Axis of rotation: {0}".format(rot.getAxis()))
    print("{0} --> {1}".format(p, rot.rotate(p)))
    print("Expected: (-1, 1, 1)")
    print()
    
    print("Rotation around the y-axis:")
    rot.setAxis(0, 2, 0)
    print("Axis of rotation: {0}".format(rot.getAxis()))
    print("{0} --> {1}".format(p, rot.rotate(p)))
    print("Expected: (1, 1, -1)")
    print()    
    
    print("Rotation around the x-axis:")
    rot.setAxis(Point3D(3, 0, 0))
    print("Axis of rotation: {0}".format(rot.getAxis()))
    print("{0} --> {1}".format(p, rot.rotate(p)))
    print("Expected: (1, -1, 1)")
    print()
    
    print("Defining the rotation around (2, -3, 1), th=pi/6=30 deg.")
    rot = Rotation(2, -3, 1, Rotation.deg2rad(30))
    print("Normalized axis of rotation: {0}".format(rot.getAxis()))
    # Calculated using Octave:
    print("Expected: (0.53452, -0.80178, 0.26726)")
    print("Angle of rotation: {0} rad,  expected {1}".format(rot.getAngle(),math.pi/6))
    print("Rot. quaternion: {0}".format(rot.getRotationQuaternion()))
    p = Point3D(7, 2, -5)
    tp = rot.rotate(p)
    print("{0} --> {1}".format(p, tp))
    # Calculated using Maxima and the following package:
    # https://github.com/jkovacic/maxima-ht
    print("Expected: (7.856793583014213, 3.917644837685909, -0.9606526529707)")

except RotationException as ex:
    print("\nRotation exception raised: '{0}'".format(ex), file=sys.stderr)
except PointException as ex:
    print("\nPoint exception raised: '{0}'".format(ex), file=sys.stderr)
else :
    print("\nRotation test completed successfully.")
