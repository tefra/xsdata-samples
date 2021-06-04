from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MobilityFacilityEnumeration(Enum):
    UNKNOWN = "unknown"
    LOW_FLOOR = "lowFloor"
    STEP_FREE_ACCESS = "stepFreeAccess"
    SUITABLE_FOR_WHEELCHAIRS = "suitableForWheelchairs"
    SUITABLE_FOR_HEAVILIY_DISABLED = "suitableForHeaviliyDisabled"
    BOARDING_ASSISTANCE = "boardingAssistance"
    ONBOARD_ASSISTANCE = "onboardAssistance"
    UNACCOMPANIED_MINOR_ASSISTANCE = "unaccompaniedMinorAssistance"
    TACTILE_PLATFORM_EDGES = "tactilePlatformEdges"
    TACTILE_GUIDING_STRIPS = "tactileGuidingStrips"
