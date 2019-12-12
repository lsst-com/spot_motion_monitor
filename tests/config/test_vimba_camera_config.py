#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.config import VimbaCameraConfig

class TestVimbaCameraConfig:

    def setup_class(cls):
        cls.config = VimbaCameraConfig()

    def test_parametersAfterConstruction(self):
        assert self.config.modelName is None
        assert self.config.roiSize == 50
        assert self.config.roiFluxMinimum == 2000
        assert self.config.roiExposureTime == 3000
        assert self.config.fullExposureTime == 3000

    def test_toDict(self):
        config_dict = self.config.toDict()
        assert ("modelName" in config_dict) is False
        assert config_dict["roi"]["size"] == 50
        assert config_dict["roi"]["fluxMin"] == 2000
        assert config_dict["roi"]["exposureTime"] == 3000
        assert config_dict["full"]["exposureTime"] == 3000

    def test_fromDict(self):
        config_dict = {"roi": {}, "full": {}}
        config_dict["modelName"] = "GT-3300"
        config_dict["roi"]["size"] = 75
        config_dict["roi"]["fluxMin"] = 1000
        config_dict["roi"]["exposureTime"] = 8000
        config_dict["full"]["exposureTime"] = 8000
        self.config.fromDict(config_dict)
        assert self.config.modelName == config_dict["modelName"]
        assert self.config.roiSize == config_dict["roi"]["size"]
        assert self.config.roiFluxMinimum == config_dict["roi"]["fluxMin"]
        assert self.config.roiExposureTime == config_dict["roi"]["exposureTime"]
        assert self.config.fullExposureTime == config_dict["full"]["exposureTime"]
