#------------------------------------------------------------------------------
# Copyright (c) 2018-2019 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialogButtonBox

from spot_motion_monitor.config import GaussianCameraConfig
from spot_motion_monitor.views import CameraConfigurationDialog

class TestCameraConfigurationDialog:

    def test_parametersAfterConstruction(self, qtbot):
        ccDialog = CameraConfigurationDialog('GaussianCamera')
        qtbot.addWidget(ccDialog)
        ccDialog.show()

        assert ccDialog.tabWidget.count() == 1
        assert ccDialog.tabWidget.currentWidget().name == 'Gaussian'

    def test_setCameraConfiguration(self, qtbot):
        ccDialog = CameraConfigurationDialog('GaussianCamera')
        qtbot.addWidget(ccDialog)
        ccDialog.show()

        truthConfig = GaussianCameraConfig()
        truthConfig.roiSize = 30
        truthConfig.doSpotOscillation = False
        truthConfig.xAmplitude = 2
        truthConfig.xFrequency = 50.0
        truthConfig.yAmplitude = 7
        truthConfig.yFrequency = 25.0

        ccDialog.setCameraConfiguration(truthConfig)
        assert int(ccDialog.cameraConfigTab.roiSizeLineEdit.text()) == truthConfig.roiSize
        state = ccDialog.cameraConfigTab.spotOscillationCheckBox.checkState()
        boolState = True if state == Qt.Checked else False
        assert boolState == truthConfig.doSpotOscillation

    def test_getCameraConfiguration(self, qtbot, mocker):
        ccDialog = CameraConfigurationDialog('GaussianCamera')
        qtbot.addWidget(ccDialog)
        ccDialog.show()
        mockGetConfiguration = mocker.patch.object(ccDialog.cameraConfigTab, 'getConfiguration')

        ccDialog.getCameraConfiguration()
        assert mockGetConfiguration.call_count == 1

    def test_validInputFromTabs(self, qtbot):
        ccDialog = CameraConfigurationDialog('GaussianCamera')
        qtbot.addWidget(ccDialog)
        ccDialog.show()

        ccDialog.cameraConfigTab.roiSizeLineEdit.setText(str(1000))
        assert ccDialog.buttonBox.button(QDialogButtonBox.Ok).isEnabled() is False
