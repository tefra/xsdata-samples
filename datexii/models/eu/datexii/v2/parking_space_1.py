from dataclasses import dataclass, field
from typing import List, Optional

from datexii.models.eu.datexii.v2.dimension import Dimension
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.location import Location
from datexii.models.eu.datexii.v2.parking_space_basics import (
    ParkingSpaceBasics,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingSpace1(ParkingSpaceBasics):
    """A single parking space.

    It is possible to define the same parking space more than once with
    different properties, e.g. when there is a different parking
    assignment for different times.

    :ivar identical_to_parking_space: Points to another instance of
        'ParkingSpace', which is identical from a local point of view
        (i.e. which is the same parking space). To be used when defining
        mixed parking areas (with using different time slots).
    :ivar location:
    :ivar parking_space_dimension: Dimension of the parking space (not
        all dimension attributes need to be provided). If the parking
        space is not rectangular, its dimension is specified as the
        smallest rectangle fitting inside its shape.
    :ivar parking_space_extension:
    """

    class Meta:
        name = "ParkingSpace"

    identical_to_parking_space: List[str] = field(
        default_factory=list,
        metadata={
            "name": "identicalToParkingSpace",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    location: Optional[Location] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_space_dimension: Optional[Dimension] = field(
        default=None,
        metadata={
            "name": "parkingSpaceDimension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_space_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingSpaceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
