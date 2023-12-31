from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TransportZoneUseEnumeration(Enum):
    ALL_USES_ALLOWED = "allUsesAllowed"
    FORBIDDEN_ZONE = "forbiddenZone"
    CANNOT_PICK_UP_AND_DROP_OFF_IN_SAME_ZONE = (
        "cannotPickUpAndDropOffInSameZone"
    )
    CANNOT_PICK_UP_IN_ZONE = "cannotPickUpInZone"
    CANNOT_DROP_OFF_IN_ZONE = "cannotDropOffInZone"
    MUST_PICK_UP_IN_ZONE = "mustPickUpInZone"
    MUST_DROP_OFF_IN_ZONE = "mustDropOffInZone"
    MUST_PICK_UP_AND_DROP_OFF_IN_SAME_ZONE = "mustPickUpAndDropOffInSameZone"
    NO_PASS_THROUGH = "noPassThrough"
    PASS_THROUGH_USE_ONLY = "passThroughUseOnly"
    OTHER = "other"
