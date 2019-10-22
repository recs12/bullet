#!python3
# Units: 0 (inch) & 1 (mm)
from standards import drillsize, standard_thread


class Simple(object):
    """Access the propeties and methodes of holes in Solidedge."""

    def __init__(self, hole):
        self.hole = hole
        self.family = 'Simple'

    def extract_data(self):
        params = {"Standard": self.hole.Standard,
            "Sub Type": self.hole.SubType,
            "Size": self.hole.Size,
            "Fit": self.hole.Fit,
            "Hole Diameter": self.hole.HoleDiameter,
        }
        print(params)

    def inject(self, db):
        if db:
            self.hole.Units = 1
            self.hole.Standard = db.get("Standard",'')
            self.hole.SubType = db.get("Sub Type",'')
            self.hole.Size = db.get("Size", '')
            self.hole.Fit = db.get("Fit", '')
            self.hole.HoleDiameter = db.get("Hole Diameter",'')
        else:
            print('[-] hole unchanged')

    def inspection(self):
        print('---')
        print('Name         : %s' %self.hole.Name)
        print('Family       : %s' %self.family)
        print('Standard     : %s' %self.hole.Standard)
        print('SubType      : %s' %self.hole.SubType)
        print('Size         : %s' %self.hole.Size)
        print('Fit          : %s' %self.hole.Fit)
        print('H.Diam       : %s' %self.hole.HoleDiameter)

    def equivalence(self):
        if not self.hole.SubType:
            raise Exception('[-] SubType unknown')
        else:
            if self.hole.Standard == 'ANSI Metric - PT':
                print('[-] %s is already metric' %self.hole.Name)
            else:
                sz = self.hole.Size
                hole_data = drillsize.get('%s' %sz)
                return hole_data


class Threaded():

    def __init__(self, hole):
        self.hole = hole
        self.family = 'Threaded'

    def inspection(self):
        print('Nominal.Diam  : %s' %self.hole.ThreadNominalDiameter)
        print('Tap.drill.Diam  : %s' %self.hole.ThreadTapDrillDiameter)
        print('Int.Diam  : %s' %self.hole.ThreadMinorDiameter)
        print('Ext.Diam  : %s' %self.hole.ThreadExternalDiameter)
        print('Pitch  : %s' %self.hole.ThreadDepth)
        print('Units  : %s' %self.hole.Units)
        print('SystemName  : %s' %self.hole.SystemName)
        print('Taper  : %s' %self.hole.Taper)
        print('ThreadDepthMethod   : %s' %self.hole.ThreadDepthMethod )
        print('ThreadDescription   : %s' %self.hole.ThreadDescription )
        print('ThreadHeight   : %s' %self.hole.ThreadHeight )
        print('ThreadSetting   : %s' %self.hole.ThreadSetting )

    def inject(self, db):
        if db:
            self.hole.Units= db.get("Units", None)
            self.hole.BottomAngle = db.get("BottomAngle", None)
            self.hole.CounterboreDepth = db.get("CounterboreDepth", None)
            self.hole.CounterboreDiameter = db.get("CounterboreDiameter", None)
            self.hole.CounterboreProfileLocationType = db.get("CounterboreProfileLocationType", None)
            self.hole.CountersinkAngle = db.get("CountersinkAngle", None)
            self.hole.CountersinkDiameter = db.get("CountersinkDiameter", None)
            self.hole.HeadClearance = db.get("HeadClearance", None)
            self.hole.HoleDiameter = db.get("HoleDiameter", None)
            self.hole.HoleType = db.get("HoleType", None)
            # self.hole.InsideEffectiveThreadLength = db.get("InsideEffectiveThreadLength", None)
            # self.hole.Name = db.get("Name", None)
            # self.hole.OutsideEffectiveThreadLength = db.get("OutsideEffectiveThreadLength", None)
            self.hole.Size = db.get("Size", None)
            self.hole.Standard = db.get("Standard", None)
            self.hole.SubType = db.get("SubType", None)
            self.hole.Taper = db.get("Taper", None)
            self.hole.TaperDimType = db.get("TaperDimType", None)
            self.hole.TaperLValue = db.get("TaperLValue", None)
            self.hole.TaperMethod = db.get("TaperMethod", None)
            self.hole.TaperRValue = db.get("TaperRValue", None)
            self.hole.ThreadDepth = db.get("ThreadDepth", None)
            self.hole.ThreadDepthMethod = db.get("ThreadDepthMethod", None)
            self.hole.ThreadDescription = db.get("ThreadDescription", None)
            self.hole.ThreadDiameterOption= db.get("ThreadDiameterOption", None)
            self.hole.ThreadExternalDiameter= db.get("ThreadExternalDiameter", None)
            # self.hole.ThreadHeight= db.get("ThreadHeight", None)
            self.hole.ThreadMinorDiameter= db.get("ThreadMinorDiameter", None)
            self.hole.ThreadNominalDiameter= db.get("ThreadNominalDiameter", None)
            self.hole.ThreadSetting= db.get("ThreadSetting", None)
            self.hole.ThreadTapDrillDiameter= db.get("ThreadTapDrillDiameter", None)
            self.hole.ThreadTaperAngle= db.get("ThreadTaperAngle", None)
            self.hole.TreatmentType= db.get("TreatmentType", None)
            self.hole.VBottomDimType= db.get("VBottomDimType", None)
        else:
            print('[-] Unchanged')

    def equivalence(self):
        if not self.hole.SubType:
            raise Exception('[-] SubType unknown')
        else:
            if self.hole.Standard == 'ANSI Metric - PT':
                print('[-] %s is already metric' %self.hole.Name)
            else:
                sz = self.hole.Size #check for size
                hole_data = standard_thread.get('%s' %sz)
                return hole_data