from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.parking_site import ParkingSite
from datexii.models.eu.datexii.v2.urban_parking_site_type_enum import (
    UrbanParkingSiteTypeEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class UrbanParkingSite(ParkingSite):
    """
    A parking site in an urban context.

    :ivar urban_parking_site_type: The type of urban parking site.
    :ivar parking_zone: Name or identifier of a parking zone this
        parking site belongs to. To be filled with the string value
        'True', if there is a parking zone with unknown name.
    :ivar urban_parking_site_extension:
    """

    urban_parking_site_type: UrbanParkingSiteTypeEnum | None = field(
        default=None,
        metadata={
            "name": "urbanParkingSiteType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    parking_zone: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "parkingZone",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    urban_parking_site_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "urbanParkingSiteExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
