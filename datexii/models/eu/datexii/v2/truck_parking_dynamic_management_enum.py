from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class TruckParkingDynamicManagementEnum(Enum):
    """
    Dynamic parking mode enum.

    :cvar COMPACT_PARKING: Lorries are parking one after the other in
        different lanes; each lane has a dedicated time of departure
        (which might be displayed on a sign gantry).
    :cvar QUEUE_PARKING: Lorries are parking in queues, one after the
        other. Each lorry must have an earlier time of departure than
        all the lorries behind it.
    :cvar NO_DYNAMIC_PARKING_MANAGEMENT: No dynamic parking management.
    :cvar OTHER: Some other type of dynamic parking management.
    """

    COMPACT_PARKING = "compactParking"
    QUEUE_PARKING = "queueParking"
    NO_DYNAMIC_PARKING_MANAGEMENT = "noDynamicParkingManagement"
    OTHER = "other"
