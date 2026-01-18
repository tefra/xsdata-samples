from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.parking_site import ParkingSite
from datexii.models.eu.datexii.v2.parking_special_location_enum import (
    ParkingSpecialLocationEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class SpecialLocationParkingSite(ParkingSite):
    """
    A parking site which is located at a special location, often associated
    with some building.

    :ivar parking_special_location: The special location of the parking
        site.
    :ivar parking_other_special_location: A special location not
        available in the enumeration. Use literal 'other' in this case.
    :ivar special_location_parking_site_extension:
    """

    parking_special_location: ParkingSpecialLocationEnum | None = field(
        default=None,
        metadata={
            "name": "parkingSpecialLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    parking_other_special_location: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "parkingOtherSpecialLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    special_location_parking_site_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "specialLocationParkingSiteExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
