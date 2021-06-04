from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FareStructureTypeEnumeration(Enum):
    NETWORK_FLAT_FARE = "networkFlatFare"
    LINE_FLAT_FARE = "lineFlatFare"
    ZONAL_FARE = "zonalFare"
    ZONE_TO_ZONE_FARE = "zoneToZoneFare"
    ZONE_SEQUENCE_FARE = "zoneSequenceFare"
    CAPPED_FLAT_FARE = "cappedFlatFare"
    CAPPED_POINT_TO_POINT_FARE = "cappedPointToPointFare"
    CAPPED_ZONAL_FARE = "cappedZonalFare"
    POINT_TO_POINT_FARE = "pointToPointFare"
    POINT_TO_POINT_DISTANCE_FARE = "pointToPointDistanceFare"
    STAGE_FARE = "stageFare"
    PENALTY_FARE = "penaltyFare"
    OTHER = "other"
