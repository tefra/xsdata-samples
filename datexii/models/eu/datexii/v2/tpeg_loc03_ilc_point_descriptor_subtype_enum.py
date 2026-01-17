from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class TpegLoc03IlcPointDescriptorSubtypeEnum(Enum):
    """
    Descriptors for describing a junction by identifying the intersecting
    roads at a road junction.

    :cvar TPEG_ILC_NAME1: The name of the road on which the junction
        point is located.
    :cvar TPEG_ILC_NAME2: The name of the first intersecting road at the
        junction.
    :cvar TPEG_ILC_NAME3: The name of the second intersecting road (if
        one exists) at the junction.
    """

    TPEG_ILC_NAME1 = "tpegIlcName1"
    TPEG_ILC_NAME2 = "tpegIlcName2"
    TPEG_ILC_NAME3 = "tpegIlcName3"
