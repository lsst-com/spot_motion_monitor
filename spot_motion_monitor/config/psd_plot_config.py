#------------------------------------------------------------------------------
# Copyright (c) 2018-2019 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.config import BaseConfig

__all__ = ['PsdPlotConfig']

class PsdPlotConfig(BaseConfig):
    """Class that handles the configuration of the Power Spectrum Distribution
       plots (1D and waterfall).

    Attributes
    ----------
    autoscaleX1d : bool
        Set autoscaling on the x component 1D PSD plot.
    autoscaleY1d : bool
        Set autoscaling on the y component 1D PSD plot.
    numWaterfallBins : int
        Set the number of vertical bins for the waterfall PSD plots.
    waterfallColorMap : str
        Set the color map for the waterfall PSD plots.
    x1dMaximum : int
        Set the maximum y axis value for on the x component 1D PSD plot.
    y1dMaximum : int
        Set the maximum y axis value for on the y component 1D PSD plot.
    """

    def __init__(self):
        """Initialize the class.
        """
        super().__init__()
        self.autoscaleX1d = False
        self.x1dMaximum = 1000
        self.autoscaleY1d = False
        self.y1dMaximum = 1000
        self.numWaterfallBins = 25
        self.waterfallColorMap = "viridis"

    def fromDict(self, config):
        """Translate config to class attributes.

        Parameters
        ----------
        config : dict
            The configuration to translate.
        """
        self.autoscaleX1d = config["xPSD"]["autoscaleY"]
        self.x1dMaximum = config["xPSD"]["maximumY"]
        self.autoscaleY1d = config["yPSD"]["autoscaleY"]
        self.y1dMaximum = config["yPSD"]["maximumY"]
        self.numWaterfallBins = config["waterfall"]["numBins"]
        self.waterfallColorMap = config["waterfall"]["colorMap"]

    def toDict(self):
        """Translate class attributes to configuration dict.

        Returns
        -------
        dict
            The currently stored configuration.
        """
        config = {"xPSD": {}, "yPSD": {}, "waterfall": {}}
        config["xPSD"]["autoscaleY"] = self.autoscaleX1d
        config["xPSD"]["maximumY"] = self.x1dMaximum
        config["yPSD"]["autoscaleY"] = self.autoscaleY1d
        config["yPSD"]["maximumY"] = self.y1dMaximum
        config["waterfall"]["numBins"] = self.numWaterfallBins
        config["waterfall"]["colorMap"] = self.waterfallColorMap
        return config
