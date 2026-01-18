from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.area import Area
from datexii.models.eu.datexii.v2.destination import Destination
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class AreaDestination(Destination):
    """
    The specification of the destination of a defined route or itinerary
    which is an area.
    """

    area: Area = field(
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    area_destination_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "areaDestinationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
