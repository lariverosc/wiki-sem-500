#
# Copyright 2016 Basis Technology Corp.
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
#

# Utility functions

# Load whichever scandir implementation is available
# (taken from github:benhoyt/scandir README)
try:
    from os import scandir, walk
except ImportError:
    from scandir import scandir, walk

import numpy as np
import six

# Re-export loaded implementation
__all__ = ['scandir', 'walk', 'decode']


def decode(s, encoding="utf-8"):
    if six.PY3 and type(s) == str:
        return s.encode("utf-8").decode(encoding)
    else:
        return s.decode("utf-8")


def similarity(v1, v2):
    """Returns the cosine similarity of v1 and v2"""
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
