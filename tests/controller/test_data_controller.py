#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
import numpy as np

from spot_motion_monitor.camera import CameraStatus
from spot_motion_monitor.controller import DataController
from spot_motion_monitor.utils import FrameRejected, GenericFrameInformation, RoiFrameInformation
from spot_motion_monitor.views import CameraDataWidget

class TestDataController():

    def setup_class(cls):
        cls.frame = np.ones((3, 5))
        cls.fullFrameStatus = CameraStatus(24, False, (0, 0))
        cls.roiFrameStatus = CameraStatus(40, True, (264, 200))

    def test_parametersAfterConstruction(self, qtbot):
        cdw = CameraDataWidget()
        qtbot.addWidget(cdw)
        dc = DataController(cdw)
        assert dc.cameraDataWidget is not None
        assert dc.updateStatusBar is not None
        assert dc.fullFrameModel is not None
        assert dc.roiFrameModel is not None
        assert dc.bufferModel is not None

    def test_updateFullFrameData(self, qtbot, mocker):
        cdw = CameraDataWidget()
        qtbot.addWidget(cdw)
        dc = DataController(cdw)
        mocker.patch('spot_motion_monitor.views.camera_data_widget.CameraDataWidget.updateFullFrameData')
        dc.fullFrameModel.calculateCentroid = mocker.Mock(return_value=GenericFrameInformation(300.3,
                                                                                               400.2,
                                                                                               32042.42,
                                                                                               145.422,
                                                                                               70,
                                                                                               None))
        dc.passFrame(self.frame, self.fullFrameStatus)
        assert dc.cameraDataWidget.updateFullFrameData.call_count == 1

    def test_failedFrame(self, qtbot, mocker):
        cdw = CameraDataWidget()
        qtbot.addWidget(cdw)
        dc = DataController(cdw)
        mocker.patch('spot_motion_monitor.views.camera_data_widget.CameraDataWidget.updateFullFrameData')
        dc.fullFrameModel.calculateCentroid = mocker.Mock(side_effect=FrameRejected)
        dc.passFrame(self.frame, self.fullFrameStatus)
        assert dc.cameraDataWidget.updateFullFrameData.call_count == 0

    def test_updateRoiFrameData(self, qtbot, mocker):
        cdw = CameraDataWidget()
        qtbot.addWidget(cdw)
        dc = DataController(cdw)
        mocker.patch('spot_motion_monitor.views.camera_data_widget.CameraDataWidget.updateRoiFrameData')
        dc.roiFrameModel.calculateCentroid = mocker.Mock(return_value=GenericFrameInformation(242.3,
                                                                                              286.2,
                                                                                              2519.534,
                                                                                              104.343,
                                                                                              50,
                                                                                              1.532))
        dc.bufferModel.getInformation = mocker.Mock(return_value=RoiFrameInformation(242.5,
                                                                                     286.3,
                                                                                     2501.42,
                                                                                     104.753,
                                                                                     2.5432,
                                                                                     2.2353,
                                                                                     (1000, 25)))
        dc.passFrame(self.frame, self.roiFrameStatus)
        assert dc.cameraDataWidget.updateRoiFrameData.call_count == 1

    def test_getBufferSize(self, qtbot):
        cdw = CameraDataWidget()
        qtbot.addWidget(cdw)
        dc = DataController(cdw)
        bufferSize = dc.getBufferSize()
        assert bufferSize == 1000

    def test_getCentroids(self, qtbot, mocker):
        cdw = CameraDataWidget()
        qtbot.addWidget(cdw)
        dc = DataController(cdw)
        truth_centroids = (241.542, 346.931)
        centroids = dc.getCentroids(False)
        assert centroids == (None, None)
        dc.bufferModel.getCentroids = mocker.Mock(return_value=truth_centroids)
        centroids = dc.getCentroids(True)
        assert centroids == truth_centroids

    def test_getFtf(self, qtbot, mocker):
        cdw = CameraDataWidget()
        qtbot.addWidget(cdw)
        dc = DataController(cdw)
        currentFps = 40
        fft = dc.getFft(currentFps)
        assert fft == (None, None, None)
        dc.bufferModel.rollBuffer = True
        truth_fft = (np.random.random(3), np.random.random(3), np.random.random(3))
        dc.bufferModel.getFft = mocker.Mock(return_value=truth_fft)
        fft = dc.getFft(currentFps)
        dc.bufferModel.getFft.assert_called_with(currentFps)
        assert fft == truth_fft
