from dataclasses import dataclass, field
from typing import List, Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.location import Location
from datexii.models.eu.datexii.v2.non_ordered_locations import (
    NonOrderedLocations,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class NonOrderedLocationGroupByList(NonOrderedLocations):
    """
    A group of (i.e. more than one) physically separate locations which have no
    specific order and where each location is explicitly listed.

    :ivar location_contained_in_group: A location contained in a non
        ordered group of locations.
    :ivar non_ordered_location_group_by_list_extension:
    """

    location_contained_in_group: List[Location] = field(
        default_factory=list,
        metadata={
            "name": "locationContainedInGroup",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 2,
        },
    )
    non_ordered_location_group_by_list_extension: Optional[ExtensionType] = (
        field(
            default=None,
            metadata={
                "name": "nonOrderedLocationGroupByListExtension",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
            },
        )
    )
