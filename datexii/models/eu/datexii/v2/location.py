from dataclasses import dataclass, field
from typing import List, Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.external_referencing import (
    ExternalReferencing,
)
from datexii.models.eu.datexii.v2.group_of_locations import GroupOfLocations
from datexii.models.eu.datexii.v2.point_coordinates import PointCoordinates

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Location(GroupOfLocations):
    """The specification of a location either on a network (as a point or a linear
    location) or as an area.

    This may be provided in one or more referencing systems.

    :ivar external_referencing:
    :ivar location_for_display: A location which may be used by clients
        for visual display on user interfaces.
    :ivar location_extension:
    """

    external_referencing: List[ExternalReferencing] = field(
        default_factory=list,
        metadata={
            "name": "externalReferencing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    location_for_display: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "locationForDisplay",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "locationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
