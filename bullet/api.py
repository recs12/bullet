"""
SolidEdge API 
=======================
"""

import clr
import System.Runtime.InteropServices as SRI

clr.AddReference("Interop.SolidEdge")
clr.AddReference("System.Runtime.InteropServices")


class Api:
    def __init__(self):
        # Connect to a running instance of Solid Edge
        self.api = SRI.Marshal.GetActiveObject("SolidEdge.Application")

    def check_valid_version(self, *valid_version):
        # validate solidedge version - 'Solid Edge ST7'
        print("* version: %s" % self.api.Value)
        assert self.api.Value in valid_version, "Unvalid version of solidedge"

    def active_document(self):
        return self.api.ActiveDocument

    @property
    def name(cls, part):
        return cls.part.Name


class HoleCollection:
    def __init__(self, doc):
        self.holes = doc.HoleDataCollection
        self.count = self.holes.Count

    def threaded(self):
        return (hole for hole in self.holes if hole.SubType == "Standard Thread")

    @property
    def count_imperial(self):
        imperial_collection = [o for o in self.holes if o.Units == 0]
        return len(imperial_collection)

    @property
    def count_metric(self):
        metric_collection = [o for o in self.holes if o.Units == 1]
        return len(metric_collection)

    @property
    def count_imperial_threaded(self):
        imperial_collection = [
            o for o in self.holes if o.Units == 0 and o.Subtype == "Standard Thread"
        ]
        return len(imperial_collection)

    @property
    def count_metric_threaded(self):
        metric_collection = [
            o for o in self.holes if o.Units == 1 and o.Subtype == "Standard Thread"
        ]
        return len(metric_collection)

    @property
    def count_threaded(self):
        total_collection = [o for o in self.holes if o.Subtype == "Standard Thread"]
        return len(total_collection)
