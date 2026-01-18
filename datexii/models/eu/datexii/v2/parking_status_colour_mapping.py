from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.parking_site_status_enum import (
    ParkingSiteStatusEnum,
)
from datexii.models.eu.datexii.v2.rgbcolour import RGBColour

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingStatusColourMapping:
    """
    Defines a pair of 'parkingSiteStatus' and a corresponding colour.

    :ivar parking_site_status: The status of the parking site (spaces
        available or not).
    :ivar rgb_colour:
    :ivar parking_status_colour_mapping_extension:
    """

    parking_site_status: ParkingSiteStatusEnum | None = field(
        default=None,
        metadata={
            "name": "parkingSiteStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    rgb_colour: RGBColour | None = field(
        default=None,
        metadata={
            "name": "rgbColour",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    parking_status_colour_mapping_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "parkingStatusColourMappingExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
