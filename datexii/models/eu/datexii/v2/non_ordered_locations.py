from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.group_of_locations import GroupOfLocations

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class NonOrderedLocations(GroupOfLocations):
    """
    Multiple (i.e. more than one) physically separate locations which have
    no specific order.
    """

    non_ordered_locations_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "nonOrderedLocationsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
