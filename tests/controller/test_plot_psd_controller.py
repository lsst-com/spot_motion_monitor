#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
import numpy as np

from spot_motion_monitor.controller import PlotPsdController
from spot_motion_monitor.views import PsdWaterfallPlotWidget

class TestPlotPsdController:

    def test_parametersAfterContruction(self, qtbot):
        psdx = PsdWaterfallPlotWidget()
        psdy = PsdWaterfallPlotWidget()
        qtbot.addWidget(psdx)
        qtbot.addWidget(psdy)

        pfc = PlotPsdController(psdx, psdy)
        assert pfc.psdXPlot is not None
        assert pfc.psdYPlot is not None

    def test_parametersAfterSetup(self, qtbot):
        psdx = PsdWaterfallPlotWidget()
        psdy = PsdWaterfallPlotWidget()
        qtbot.addWidget(psdx)
        qtbot.addWidget(psdy)

        arraySize = 5
        pfc = PlotPsdController(psdx, psdy)
        pfc.setup(arraySize)
        assert pfc.psdXPlot.arraySize == arraySize
        assert pfc.psdYPlot.arraySize == arraySize

    def test_update(self, qtbot, mocker):
        psdx = PsdWaterfallPlotWidget()
        psdy = PsdWaterfallPlotWidget()
        qtbot.addWidget(psdx)
        qtbot.addWidget(psdy)

        arraySize = 5
        pfc = PlotPsdController(psdx, psdy)
        pfc.setup(arraySize)

        np.random.seed(3000)
        psdDataX = np.random.random(7)
        psdDataY = np.random.random(7)
        freqs = np.random.random(7)

        mockPsdXPlotUpdatePlot = mocker.patch.object(pfc.psdXPlot, 'updatePlot')
        mockPsdYPlotUpdatePlot = mocker.patch.object(pfc.psdYPlot, 'updatePlot')
        pfc.update(psdDataX, psdDataY, freqs)

        assert mockPsdXPlotUpdatePlot.call_count == 1
        assert mockPsdYPlotUpdatePlot.call_count == 1

    def test_badFftData(self, qtbot, mocker):
        psdx = PsdWaterfallPlotWidget()
        psdy = PsdWaterfallPlotWidget()
        qtbot.addWidget(psdx)
        qtbot.addWidget(psdy)

        arraySize = 5
        pfc = PlotPsdController(psdx, psdy)
        pfc.setup(arraySize)

        mockPsdXPlotUpdatePlot = mocker.patch.object(pfc.psdXPlot, 'updatePlot')
        mockPsdYPlotUpdatePlot = mocker.patch.object(pfc.psdYPlot, 'updatePlot')
        pfc.update(None, None, None)

        assert mockPsdXPlotUpdatePlot.call_count == 0
        assert mockPsdYPlotUpdatePlot.call_count == 0
