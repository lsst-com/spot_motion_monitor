#------------------------------------------------------------------------------
# Copyright (c) 2019 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from datetime import datetime

from freezegun import freeze_time
import pytz

from spot_motion_monitor.utils import TimeHandler

class TestTimeHandler():

    def test_parametersAfterConstruction(self):
        th = TimeHandler()
        th.timezone == "UTC"
        assert th.standard_format == "%Y%m%d_%H%M%S"

    @freeze_time("2019-11-26 13:45:23")
    def test_utc_timezone(self):
        th = TimeHandler()
        assert th.getTime() == datetime(2019, 11, 26, 13, 45, 23, tzinfo=pytz.utc)
        assert th.getTimeStamp() == 1574775923
        assert th.getFormattedTimeStamp() == "20191126_134523"
        assert th.getFormattedTimeStamp(format="iso") == "2019-11-26T13:45:23+00:00"

    @freeze_time("2019-11-26 13:45:23")
    def test_tai_timezone(self):
        th = TimeHandler()
        th.timezone = "TAI"
        assert th.getTime() == datetime(2019, 11, 26, 13, 46, 00, tzinfo=pytz.utc)
        assert th.getTimeStamp() == 1574775960
        assert th.getFormattedTimeStamp() == "20191126_134600"
        assert th.getFormattedTimeStamp(format="iso") == "2019-11-26T13:46:00+00:00"

    @freeze_time("2019-11-26 13:45:23")
    def test_arizona_timezone(self):
        th = TimeHandler()
        th.timezone = "US/Arizona"
        dt = datetime(2019, 11, 26, 13, 45, 23).replace(tzinfo=pytz.utc)
        tz = pytz.timezone(th.timezone)
        dtl = dt.astimezone(tz)
        assert th.getTime() == dtl
        assert th.getTimeStamp() == 1574775923
        assert th.getFormattedTimeStamp() == "20191126_064523"
        assert th.getFormattedTimeStamp(format="iso") == "2019-11-26T06:45:23-07:00"

    @freeze_time("2019-11-26 13:45:23")
    def test_chile_timezone(self):
        th = TimeHandler()
        th.timezone = "America/Santiago"
        dt = datetime(2019, 11, 26, 13, 45, 23).replace(tzinfo=pytz.utc)
        tz = pytz.timezone(th.timezone)
        dtl = dt.astimezone(tz)
        assert th.getTime() == dtl
        assert th.getTimeStamp() == 1574775923
        assert th.getFormattedTimeStamp() == "20191126_104523"
        assert th.getFormattedTimeStamp(format="iso") == "2019-11-26T10:45:23-03:00"
