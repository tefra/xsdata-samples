from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.inter_urban_parking_site_location_enum import InterUrbanParkingSiteLocationEnum
from datexii.models.eu.datexii.v2.parking_site import ParkingSite

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class InterUrbanParkingSite(ParkingSite):
    """
    A parking site in an interurban context.

    :ivar inter_urban_parking_site_location: Defines whether the
        interurban parking site is located in or nearby a motorway
        context, is a layby or on-street parking.
    :ivar inter_urban_parking_site_extension:
    """
    inter_urban_parking_site_location: Optional[InterUrbanParkingSiteLocationEnum] = field(
        default=None,
        metadata={
            "name": "interUrbanParkingSiteLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    inter_urban_parking_site_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "interUrbanParkingSiteExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
