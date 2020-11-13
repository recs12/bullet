""" Convert threads in holes from imperial to metric and reverse.
"""


import sys
sys.path.append("C:\IronPython 2.7\Lib")
from collections import Counter

from api import Api, HoleCollection
from equivalences import equivalences
from holes import Hole

mappingToImp = equivalences.get("mappingToImp")
mappingToMetric = equivalences.get("mappingToMetric")


__project__ = "threaded_hole_conversion"
__author__ = "recs"
__version__ = "0.0.1"
__update__ = "2020-11-13"


def main():
    """Convert holes in plate to metric (by default) or imperial."""
    try:
        session = Api()
        plate = session.active_document()
        print("Part: {:^30s}\n".format(plate.name))

        # Check if part is sheetmetal.
        assert plate.name.endswith(
            ".psm"
        ), "This macro only works on .psm not {:^30s}".format(plate.name[-4:])

        # Get a reference to the variables collection.
        holes = HoleCollection(plate)

        # Display the quantites of different types of holes.
        quantites(
            holes.count,
            holes.count_threaded,
            holes.count_imperial_threaded,
            holes.count_metric_threaded,
        )

        # Prototyping table of holes. (helper for drafter)
        qty_size = dict(Counter(holes.all_holes()))  # >>> 'M6x1':3
        print_table(qty_size)

        # Prompt user selection
        units = prompt_units_selection()

        if units == "metric":  # if metric
            for hole in holes.threaded():
                o = Hole(hole)
                if o.is_metric():
                    continue
                imperial = o.size
                holedata = Hole.get_equivalence(o, mapping=mappingToMetric)
                o.conversion_to_metric(holedata)
                metric = o.size
                header()
                print(" {:<30s} {:<30s}".format(imperial, metric))
                footer()

        elif units == "imperial":  # if imperial
            for hole in holes.threaded():
                o = Hole(hole)
                if o.is_imperial():
                    continue
                metric = o.size
                holedata = Hole.get_equivalence(o, mapping=mappingToImp)  # correction
                o.conversion_to_metric(holedata)  # correction
                imperial = o.size
                header()
                print(" {:<30s} {:<30s}".format(metric, imperial))
                footer()

        elif units == "debug":
            for hole in holes.threaded():
                o = Hole(hole)
                print(o.__repr__())

        else:
            sys.exit()

        # Display a second time the quantites of different types of holes.
        quantites(
            holes.count,
            holes.count_threaded,
            holes.count_imperial_threaded,
            holes.count_metric_threaded,
            state="(Changed state)",
        )

    except AssertionError as err:
        print(err.args)

    except Exception as ex:
        print(ex.args)

    else:
        pass

    finally:
        raw_input("\nPress any key to exit...")
        sys.exit()


def quantites(
    count, count_threaded, imperial_threaded, metric_threaded, state="(Current state)"
):
    print("{}".format(state))
    print("- Total number of holes: ...................... {}".format(count))
    print("- Total threaded: ............................. {}".format(count_threaded))
    print("  - imperial: ................................. {}".format(imperial_threaded))
    print("  - metric: ................................... {} \n".format(metric_threaded))


def prompt_units_selection():
    # TODO: add a lowercase convertor for m and i.
    sys_metric = raw_input("select: [M]etric/[I]mperial, (press any key to cancel):\n>")
    sys_metric = sys_metric.lower()
    return {"m": "metric", "i": "imperial", "?": "debug"}.get(sys_metric)


# Display a table of content
# hole sizes before and after macro process.
def header(col1="current", col2="changed to"):
    print(" " + 60 * "-")
    print("{:^30s}->{:^30s}".format(col1, col2))
    print(" " + 60 * "=")


def footer():
    print(" " + 60 * "-")
    print("\n")


def print_table(_dict):
    print("{:<8} {:<15}".format('Size','Qty'))
    for s, q in _dict.iteritems():
        print("{:<8} {:<15}".format(s, q))
    print("\n")


def confirmation(func):
    response = raw_input(
        """Would you like to convert theaded hole to metric or imperial? (Press y/[Y] to proceed.): """
    )
    if response.lower() not in ["y"]:
        print("Process canceled")
        sys.exit()
    else:
        func()


if __name__ == "__main__":
    print(
        "%s\n--author: %s  --version: %s  --last-update : %s"
        % (__project__, __author__, __version__, __update__)
    )
    confirmation(main)
