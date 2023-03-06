##
## Proj......... shot-class
## File......... channels.py
## Author....... Toby J. van den Herik
##

class Channel():
    """
    An object that is a channel of data mapped against its own absolute time
    """
    def __init__(self, channel_data, channel_absolute_time, interval_format = "fixed interval"):
        """
        Initialisation takes a set of data, a sampling rate
        """

        # Custom classes are essentially dictionaries with functions. This enables
        # the easy saving and rebuilding of classes to and from JSON format.

        # Note: for fixed interval channel data sets, collapsing and unpacking is not
        #       handled by the class.. it is handled by writer.py and loader.py respectively.
    
        self.data = {
            "class_type"        : "Channel",
            "interval_format"   : interval_format,
            "data"              : channel_data,
            "time"              : channel_absolute_time
        }

        return None