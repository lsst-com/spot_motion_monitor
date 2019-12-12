#------------------------------------------------------------------------------
# Copyright (c) 2018-2019 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.config import BaseConfig

__all__ = ['GaussianCameraConfig']

class GaussianCameraConfig(BaseConfig):
    """Class that handles the configuration of the Gaussian camera.

    Attributes
    ----------
    doSpotOscillation : bool
        Flag tp make the generated spot oscillate.
    roiSize : int
        The size (pixels) of the ROI on the camera.
    xAmplitude : int
        The amplitude of the x component of the spot oscillation.
    xFrequency : float
        The frequency of the x component of the spot oscillation.
    yAmplitude : int
        The amplitude of the y component of the spot oscillation.
    yFrequency : float
        The frequency of the y component of the spot oscillation.
    """

    def __init__(self):
        """Summary
        """
        super().__init__()
        self.roiSize = 50
        self.doSpotOscillation = False
        self.xAmplitude = 10
        self.xFrequency = 5.0
        self.yAmplitude = 5
        self.yFrequency = 10.0

    def fromDict(self, config):
        """Translate config to class attributes.

        Parameters
        ----------
        config : dict
            The configuration to translate.
        """
        self.roiSize = config["roi"]["size"]
        self.doSpotOscillation = config["spotOscillation"]["do"]
        self.xAmplitude = config["spotOscillation"]["x"]["amplitude"]
        self.xFrequency = config["spotOscillation"]["x"]["frequency"]
        self.yAmplitude = config["spotOscillation"]["y"]["amplitude"]
        self.yFrequency = config["spotOscillation"]["y"]["frequency"]

    def toDict(self, writeEmpty=False):
        """Translate class attributes to configuration dict.

        Parameters
        ----------
        writeEmpty : bool
            Flag to write parameters with None as values.

        Returns
        -------
        dict
            The currently stored configuration.
        """
        config = {"roi": {}, "spotOscillation": {"x": {}, "y": {}}}
        config["roi"]["size"] = self.roiSize
        config["spotOscillation"]["do"] = self.doSpotOscillation
        config["spotOscillation"]["x"]["amplitude"] = self.xAmplitude
        config["spotOscillation"]["x"]["frequency"] = self.xFrequency
        config["spotOscillation"]["y"]["amplitude"] = self.yAmplitude
        config["spotOscillation"]["y"]["frequency"] = self.yFrequency
        return config
