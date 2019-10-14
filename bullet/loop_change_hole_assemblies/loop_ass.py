import clr

clr.AddReference("Interop.SolidEdge")
clr.AddReference("System.Runtime.InteropServices")

import SolidEdgeFramework as SEFramework
import SolidEdgePart as SEPart
import SolidEdgeConstants as SEConstants
import System.Runtime.InteropServices as SRI


if __name__ == "__main__":
    # Connect to a running instance of Solid Edge
    objApplication = SRI.Marshal.GetActiveObject("SolidEdge.Application")
    # Get a reference to the active document
    objAss = objApplication.ActiveDocument
    print(dir(objAss))
    print([p.name for p in objAss.Occurrences])
    

