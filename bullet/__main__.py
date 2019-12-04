""" Convert threads in holes from imperial to metric.
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
from api import Api, HoleCollection

def main():
    try:
        session = Api()
        print("Author: recs")
        print("Last update: 2019-12-3")
        session.check_valid_version('Solid Edge ST7','Solid Edge 2019')
        plate = session.active_document()
        print("part: %s\n" % plate.name)

        # Check if part is sheetmetal.
        assert plate.name.endswith(".psm"), "This macro only works on .psm not %s" %plate.name[-4:]

        # Get a reference to the variables collection.
        holes = HoleCollection(plate)

        print("Total of holes: %s" %holes.count)
        print("|\timperial\t|\tmetric\t\t|")
        print(48 * "=")
        for hole in holes.threaded():
            o = Hole(hole)
            imperial = o.size
            holedata = Hole.get_equivalence(o)
            o.conversion_to_metric(holedata)
            metric = o.size
            print("|\t%s\t|\t%s\t\t|" %(imperial, metric))
        print(48 * "-")
    except AssertionError as err:
        print(err.args)
    except Exception as ex:
        print(ex.args)
    else:
        pass
    finally:
        raw_input("\n(Press any key to exit ;)")
        sys.exit()

if __name__ == "__main__":
    main()
