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
        o = Threaded(hole)
        # o = Hole(hole) #for simple hole
        o.inspection()
        # print(o.extract_data()) #return a dictionnary of holes data #debugging
        print('...')
        db = Threaded.equivalence(o)
        o.inject(db)
        o.inspection()
        print('Inch -> mm\n')
        raw_input("\n(Press any key to exit ;)")


if __name__ == "__main__":
    main()