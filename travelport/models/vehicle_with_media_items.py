from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.media_item_1 import MediaItem1
from travelport.models.type_result_message_1 import TypeResultMessage1
from travelport.models.vehicle import Vehicle

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class VehicleWithMediaItems:
    """
    A container for displaying vehicle details,media urls and errors.

    Parameters
    ----------
    vehicle
    media_item
        Photos and other media urls for the item referenced above.
    media_result_message
        Errors, Warnings and informational messages for the property
        referenced above.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    vehicle: None | Vehicle = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "required": True,
        },
    )
    media_item: list[MediaItem1] = field(
        default_factory=list,
        metadata={
            "name": "MediaItem",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    media_result_message: list[TypeResultMessage1] = field(
        default_factory=list,
        metadata={
            "name": "MediaResultMessage",
            "type": "Element",
            "max_occurs": 999,
        },
    )
