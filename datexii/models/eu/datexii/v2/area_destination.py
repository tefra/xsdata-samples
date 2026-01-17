from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.area import Area
from datexii.models.eu.datexii.v2.destination import Destination
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class AreaDestination(Destination):
    """
    The specification of the destination of a defined route or itinerary
    which is an area.
    """

    area: Optional[Area] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    area_destination_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "areaDestinationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
