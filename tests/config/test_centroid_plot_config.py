#------------------------------------------------------------------------------
# Copyright (c) 2018-2019 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.config import CentroidPlotConfig

class TestCentroidPlotConfig:

    def setup_class(cls):
        cls.config = CentroidPlotConfig()

    def test_parametersAfterConstruction(self):
        assert self.config.autoscaleX is False
        assert self.config.minimumX == 0
        assert self.config.maximumX == 100
        assert self.config.autoscaleY is False
        assert self.config.minimumY == 0
        assert self.config.maximumY == 100
        assert self.config.numHistogramBins == 40

    def test_toDict(self):
        config_dict = self.config.toDict()
        assert config_dict["xCentroid"]["autoscaleY"] is False
        assert config_dict["xCentroid"]["minimumY"] == 0
        assert config_dict["xCentroid"]["maximumY"] == 100
        assert config_dict["yCentroid"]["autoscaleY"] is False
        assert config_dict["yCentroid"]["minimumY"] == 0
        assert config_dict["yCentroid"]["maximumY"] == 100

    def test_fromDict(self):
        config_dict = {"xCentroid": {}, "yCentroid": {}, "scatterPlot": {}}
        config_dict["xCentroid"]["autoscaleY"] = True
        config_dict["xCentroid"]["minimumY"] = 50
        config_dict["xCentroid"]["maximumY"] = 300
        config_dict["yCentroid"]["autoscaleY"] = True
        config_dict["yCentroid"]["minimumY"] = 20
        config_dict["yCentroid"]["maximumY"] = 400
        config_dict["scatterPlot"]["histograms"] = {}
        config_dict["scatterPlot"]["histograms"]["numBins"] = 100
        self.config.fromDict(config_dict)
        assert self.config.autoscaleX is config_dict["xCentroid"]["autoscaleY"]
        assert self.config.minimumX == config_dict["xCentroid"]["minimumY"]
        assert self.config.maximumX == config_dict["xCentroid"]["maximumY"]
        assert self.config.autoscaleY is config_dict["yCentroid"]["autoscaleY"]
        assert self.config.minimumY == config_dict["yCentroid"]["minimumY"]
        assert self.config.maximumY == config_dict["yCentroid"]["maximumY"]
        assert self.config.numHistogramBins == config_dict["scatterPlot"]["histograms"]["numBins"]
