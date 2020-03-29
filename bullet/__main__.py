""" Convert threads in holes from imperial to metric.
"""
import sys

from api import Api, HoleCollection
from holes import Hole
from bullet.equivalences import mappingToMetric, mappingToImp


def conversion_metric():
    cad_conversion(option=1)


def conversion_imperial():
    cad_conversion(option=2)


def cad_conversion(option):
    try:
        session = Api()
        print("* Author: recs")
        print("* Last update: 2019-12-3")
        session.check_valid_version("Solid Edge ST7", "Solid Edge 2019")
        plate = session.active_document()
        print("* part-number: {:^30s}\n".format(plate.name))

        # Check if part is sheetmetal.
        # TODO: Change the old formated string system for the more recent .format(?)
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

        # Display a table of content
        # hole sizes before and after macro process.
        print(" " + 60 * "-")
        print("{:^30s}->{:^30s}".format("current", "changed to"))
        print(" " + 60 * "=")
        #

        if option == 1:  # if metric
            for hole in holes.threaded():
                o = Hole(hole)
                if o.is_metric():
                    continue
                imperial = o.size
                holedata = Hole.get_equivalence(o)
                o.conversion_to_metric(holedata)
                metric = o.size
                print(" {:<30s} {:<30s}".format(imperial, metric))
        elif option == 2:  # if imperial
            for hole in holes.threaded():
                o = Hole(hole)
                if o.is_metric():  # correction
                    continue
                imperial = o.size  # correstion
                holedata = Hole.get_equivalence(o)  # correction
                o.conversion_to_metric(holedata)  # correction
                metric = o.size  # correction
                print(" {:<30s} {:<30s}".format(imperial, metric))  # correction
        #
        print(" " + 60 * "-")
        print("\n")

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
        raw_input("\n(Press any key to exit ;)")
        sys.exit()


def quantites(
    count, count_threaded, imperial_threaded, metric_threaded, state="(Current state)"
):
    print("{}".format(state))
    print("- Total number of holes: {}".format(count))
    print("- Total threaded: ...... {}".format(count_threaded))
    print("  - imperial: .......... {}".format(imperial_threaded))
    print("  - metric: ............ {} \n".format(metric_threaded))


# Replace confirmation by multi choice option 1 or 2. + switcher
def confirmation(func):
    response = raw_input(
        """Bullet converts holes from imperial to metric, (Press y/[Y] to proceed.): """
    )
    if response.lower() not in ["y"]:
        print("Process canceled")
        sys.exit()
    else:
        func()


if __name__ == "__main__":
    confirmation(main)
