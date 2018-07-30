#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from collections import namedtuple

__all__ = ['CameraStatus']

"""Camera related information

Attributes
----------
CameraStatus : collections.namedtuple
    Current values of particular camera information
    * currentFps (int) : The current Frames per Second rate.
    * isRoiMode (bool) : Flag for is the camera is acquiring Full or ROI frames.
    * frameOffset ((float, float)) : The current offset of the frame. Non-zero only in ROI mode.
"""

CameraStatus = namedtuple('CameraStatus', 'currentFps isRoiMode frameOffset')
