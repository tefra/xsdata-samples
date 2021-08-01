from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.parking_access_reference import ParkingAccessReference

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class DedicatedAccess:
    """
    Reference to an access of any type (vehicles, pedestrian, ...).

    :ivar dedicated_access: Specifies a reference to an access, object
        (i.e. an entrance, an exit or both). A Point location and
        further characteristics can be specified for those objects.
    :ivar distance_from_parking_space: Distance from this access to the
        parking space or group of parking spaces. Especially interesting
        for handicapped people on the one hand or in case of the need of
        changing the side of a motorway.
    :ivar dedicated_access_extension:
    """
    dedicated_access: Optional[ParkingAccessReference] = field(
        default=None,
        metadata={
            "name": "dedicatedAccess",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    distance_from_parking_space: Optional[int] = field(
        default=None,
        metadata={
            "name": "distanceFromParkingSpace",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    dedicated_access_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "dedicatedAccessExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
