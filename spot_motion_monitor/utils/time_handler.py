#------------------------------------------------------------------------------
# Copyright (c) 2019 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
from astropy.time import Time
import pytz

__all__ = ["TimeHandler"]

class TimeHandler():
    """Class that handles timestamps and formatting.

    Attributes
    ----------
    standard_format : str
        The standard time format to return.
    timezone : str
        The current requested timezone. Supports TAI.
    """

    def __init__(self):
        """Initialize the class.
        """
        self.timezone = "UTC"
        self.standard_format = '%Y%m%d_%H%M%S'

    def getTime(self):
        """Get the current timezone aware date/time object.

        Returns
        -------
        datetime.datetime
            The current timezone aware date/time.
        """
        now = Time.now()
        if self.timezone != "UTC":
            if self.timezone == "TAI":
                return now.tai.datetime.replace(tzinfo=pytz.utc)
            else:
                tz = pytz.timezone(self.timezone)
                return now.datetime.replace(tzinfo=pytz.utc).astimezone(tz)
        else:
            return now.datetime.replace(tzinfo=pytz.utc)

    @classmethod
    def getTimezones(cls):
        """Get the list of timezones

        Returns
        -------
        list[str]
            The current list of timezones with TAI added.
        """
        timezones = pytz.all_timezones
        timezones.remove("UTC")
        timezones.insert(0, "TAI")
        timezones.insert(0, "UTC")

        return timezones

    def getFormattedTimeStamp(self, format=None):
        """Get a formatted string of the current timezone aware date/time.

        Parameters
        ----------
        format : str, optional
            Request a specific format.

        Returns
        -------
        str
            The formatted current timezone aware date/time. Default is to
            return %Y%m%d_%H%M%S.
        """
        if format is not None:
            if format == "iso":
                return self.getTime().isoformat()
        else:
            return self.getTime().strftime(self.standard_format)

    def getTimeStamp(self):
        """Get the current timezone aware date/time timestamp.

        Returns
        -------
        float
            The current timezone aware date/time timestamp.
        """
        return self.getTime().timestamp()
