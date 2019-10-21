#!python3
import clr

clr.AddReference("Interop.SolidEdge")
clr.AddReference("System.Runtime.InteropServices")

import sys
import SolidEdgeFramework as SEFramework
import SolidEdgePart as SEPart
import SolidEdgeConstants as SEConstants
import System.Runtime.InteropServices as SRI

from holes import Simple, Threaded
from standards import drillsize, stdthread


def main():
    # Connect to a running instance of Solid Edge
    objApplication = SRI.Marshal.GetActiveObject("SolidEdge.Application")
    print(objApplication.Value)
    # Get a reference to the active document
    objPart = objApplication.ActiveDocument
    print(objPart.Name) #partnumber
    # Get a reference to the variables collection
    holes = objPart.HoleDataCollection
    for hole in holes:
        # o = Simple(hole) #for simple hole
        o = Threaded(hole)
        o.inspection()
        # print(o.extract_data()) #return a dictionnary of holes data #debugging
        db = Simple.equivalence(o)
        db = Threaded.equivalence(o)
        o.inject(db)
        o.inspection()
        # raw_input("\n(Press any key to exit ;)")


if __name__ == "__main__":
    main()


#TODO: [3] process only parts. or assemblies.