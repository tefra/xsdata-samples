from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ReroutingManagementTypeEnum(Enum):
    """
    Management actions relating to rerouting.

    :cvar DO_NOT_FOLLOW_DIVERSION_SIGNS: Do not follow diversion signs.
    :cvar DO_NOT_USE_ENTRY: Rerouted traffic is not to use the specified
        entry onto the identified road to commence the alternative
        route.
    :cvar DO_NOT_USE_EXIT: Rerouted traffic is not to use the specified
        exit from the identified road to commence the alternative route.
    :cvar DO_NOT_USE_INTERSECTION_OR_JUNCTION: Rerouted traffic is not
        to use the specified intersection or junction.
    :cvar FOLLOW_DIVERSION_SIGNS: Rerouted traffic is to follow the
        diversion signs.
    :cvar FOLLOW_LOCAL_DIVERSION: Rerouted traffic is to follow local
        diversion.
    :cvar FOLLOW_SPECIAL_MARKERS: Rerouted traffic is to follow the
        special diversion markers.
    :cvar USE_ENTRY: Rerouted traffic is to use the specified entry onto
        the identified road to commence the alternative route.
    :cvar USE_EXIT: Rerouted traffic is to use the specified exit from
        the identified road to commence the alternative route.
    :cvar USE_INTERSECTION_OR_JUNCTION: Rerouted traffic is to use the
        specified intersection or junction to commence the alternative
        route.
    """

    DO_NOT_FOLLOW_DIVERSION_SIGNS = "doNotFollowDiversionSigns"
    DO_NOT_USE_ENTRY = "doNotUseEntry"
    DO_NOT_USE_EXIT = "doNotUseExit"
    DO_NOT_USE_INTERSECTION_OR_JUNCTION = "doNotUseIntersectionOrJunction"
    FOLLOW_DIVERSION_SIGNS = "followDiversionSigns"
    FOLLOW_LOCAL_DIVERSION = "followLocalDiversion"
    FOLLOW_SPECIAL_MARKERS = "followSpecialMarkers"
    USE_ENTRY = "useEntry"
    USE_EXIT = "useExit"
    USE_INTERSECTION_OR_JUNCTION = "useIntersectionOrJunction"
