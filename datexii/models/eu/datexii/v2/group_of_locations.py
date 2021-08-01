from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class GroupOfLocations:
    """One or more physically separate locations.

    Multiple locations may be related, as in an itinerary (or route), or
    may be unrelated. It is not for identifying the same physical
    location using different Location objects for different referencing
    systems.
    """
    group_of_locations_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "groupOfLocationsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
