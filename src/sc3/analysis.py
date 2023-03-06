##
## Proj......... shot-class
## File......... analysis.py
## Author....... Toby J. van den Herik
##

class Analysis():
    """
    An object that is a channel of data mapped against its own absolute time
    """
    def __init__(self, title):
        """
        Initialisation of an Analysis class.
        """

        # stores channels as classes but code is smart enough
        # to convert them to jsons on write and rebuild them as 
        # Channel classes on read.

        self.data = {
            "name"          : title,
            "channels"      : {}
        }

        return None
    
    def add_channel(self, name, channel):
        """
        Add a channel to an analysis
        """
        self.data["channels"][name] = channel

        return None