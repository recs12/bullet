#!python3
#2019-11-20 by: recs
"""Macro convertor imperial to metric on solidedge.
"""

import clr

clr.AddReference("Interop.SolidEdge")
clr.AddReference("System.Runtime.InteropServices")

import sys
import SolidEdgeFramework as SEFramework
import SolidEdgePart as SEPart
import SolidEdgeConstants as SEConstants
import System.Runtime.InteropServices as SRI

from holes import Hole


def main():
    # Connect to a running instance of Solid Edge
    objApplication = SRI.Marshal.GetActiveObject("SolidEdge.Application")
    print("version solidedge: %s" %objApplication.Value)

    # Get a reference to the active document
    objPart = objApplication.ActiveDocument
    print("part: %s" %objPart.Name) #partnumber
    print("\n")
    
    if not objPart.Name.endswith('.psm'):
        print('Warning: This Macro only works on plates.')
    else:
        # Get a reference to the variables collection
        holes = objPart.HoleDataCollection
        if holes.Count == 0:
            print('No hole detected on this plate.')
        else:
            for hole in holes:
                # print(hole.SubType)
                if hole.SubType =="Standard Thread": #perform action only on the threaded ones
                    o = Hole(hole)
                    ## print(repr(o))
                    o.inspection_hole()
                    holedata = Hole.get_equivalence(o)
                    o.conversion_to_metric(holedata)
                    o.inspection_hole()
                    print("\n\t***")
    raw_input("\n(Press any key to exit ;)") #gui with OK button


if __name__ == "__main__":
    main()


#TODO: [1] functional programming instead of OO.
#TODO: [0] allow macro only on version ST7.
#TODO: [0] check if solidedge open before starting macro
