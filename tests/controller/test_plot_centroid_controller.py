#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from spot_motion_monitor.controller import PlotCentroidController
from spot_motion_monitor.views import Centroid1dPlotWidget, CentroidScatterPlotWidget

class TestPlotCentroidController:

    def setup_class(cls):
        cls.bufferSize = 3
        cls.roiFps = 2

    def test_parametersAfterConstruction(self, qtbot):
        cxp = Centroid1dPlotWidget()
        cyp = Centroid1dPlotWidget()
        csp = CentroidScatterPlotWidget()
        qtbot.addWidget(cxp)
        qtbot.addWidget(cyp)
        qtbot.addWidget(csp)

        p1cc = PlotCentroidController(cxp, cyp, csp)
        assert p1cc.x1dPlot is not None
        assert p1cc.y1dPlot is not None
        assert p1cc.scatterPlot is not None

    def test_parametersAfterSetup(self, qtbot):
        cxp = Centroid1dPlotWidget()
        cyp = Centroid1dPlotWidget()
        csp = CentroidScatterPlotWidget()
        qtbot.addWidget(cxp)
        qtbot.addWidget(cyp)
        qtbot.addWidget(csp)

        p1cc = PlotCentroidController(cxp, cyp, csp)
        p1cc.setup(self.bufferSize, self.roiFps)

        assert p1cc.x1dPlot.dataSize == self.bufferSize
        assert p1cc.y1dPlot.dataSize == self.bufferSize
        assert p1cc.scatterPlot.dataSize == self.bufferSize

    def test_update(self, qtbot):
        cxp = Centroid1dPlotWidget()
        cyp = Centroid1dPlotWidget()
        csp = CentroidScatterPlotWidget()
        qtbot.addWidget(cxp)
        qtbot.addWidget(cyp)
        qtbot.addWidget(csp)

        p1cc = PlotCentroidController(cxp, cyp, csp)
        p1cc.setup(self.bufferSize, self.roiFps)
        centroidX = 253.543
        centroidY = 313.683
        p1cc.update(centroidX, centroidY)

        assert p1cc.x1dPlot.data[0] == centroidX
        assert p1cc.y1dPlot.data[0] == centroidY
        assert p1cc.scatterPlot.xData[0] == centroidX
        assert p1cc.scatterPlot.yData[0] == centroidY

    def test_badCentroidsUpdate(self, qtbot, mocker):
        cxp = Centroid1dPlotWidget()
        cyp = Centroid1dPlotWidget()
        csp = CentroidScatterPlotWidget()
        qtbot.addWidget(cxp)
        qtbot.addWidget(cyp)
        qtbot.addWidget(csp)
        mocker.patch('spot_motion_monitor.views.centroid_1d_plot_widget.Centroid1dPlotWidget.updatePlot')
        mocker.patch('spot_motion_monitor.views.centroid_scatter_plot_widget.'
                     'CentroidScatterPlotWidget.updateData')

        p1cc = PlotCentroidController(cxp, cyp, csp)
        p1cc.setup(self.bufferSize, self.roiFps)
        p1cc.update(None, None)
        assert p1cc.x1dPlot.updatePlot.call_count == 0
        assert p1cc.y1dPlot.updatePlot.call_count == 0
        assert p1cc.scatterPlot.updateData.call_count == 0

    def test_showScatterPlots(self, qtbot, mocker):
        cxp = Centroid1dPlotWidget()
        cyp = Centroid1dPlotWidget()
        csp = CentroidScatterPlotWidget()
        qtbot.addWidget(cxp)
        qtbot.addWidget(cyp)
        qtbot.addWidget(csp)
        mocker.patch('spot_motion_monitor.views.centroid_scatter_plot_widget.'
                     'CentroidScatterPlotWidget.showPlot')
        p1cc = PlotCentroidController(cxp, cyp, csp)
        p1cc.setup(self.bufferSize, self.roiFps)
        centroidX = 253.543
        centroidY = 313.683
        p1cc.update(centroidX, centroidY)
        p1cc.showScatterPlots(False)
        assert p1cc.scatterPlot.showPlot.call_count == 0
        p1cc.showScatterPlots(True)
        assert p1cc.scatterPlot.showPlot.call_count == 1

    def test_updateRoiFps(self, qtbot, mocker):
        cxp = Centroid1dPlotWidget()
        cyp = Centroid1dPlotWidget()
        csp = CentroidScatterPlotWidget()
        qtbot.addWidget(cxp)
        qtbot.addWidget(cyp)
        qtbot.addWidget(csp)
        p1cc = PlotCentroidController(cxp, cyp, csp)
        mockXSetRoiFps = mocker.patch.object(p1cc.x1dPlot, 'setRoiFps')
        mockYSetRoiFps = mocker.patch.object(p1cc.y1dPlot, 'setRoiFps')
        p1cc.setup(self.bufferSize, self.roiFps)
        p1cc.updateRoiFps(20)
        assert mockXSetRoiFps.call_count == 1
        assert mockYSetRoiFps.call_count == 1
