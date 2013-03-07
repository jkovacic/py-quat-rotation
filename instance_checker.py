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
# limitations under the License.# -*- coding: utf-8 -*-



class InstanceCheck :
    """
    A class with "static" methods that check whether an input variable is
    an instance of certain types/classes
    """
    
    @staticmethod
    def isFloat(n) :
        """
        Checks whether n is a float or an integer
        (mathematically, integers are a subset of real numbers).
        """
        return isinstance(n, float) or isinstance(n, int)
