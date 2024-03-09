from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.media_item_5 import MediaItem5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class ServiceInfo5:
    """
    Parameters
    ----------
    description
        Description of the Service.  Usually used in tandem with  one or
        more media items.
    media_item
    """

    class Meta:
        name = "ServiceInfo"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    description: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    media_item: list[MediaItem5] = field(
        default_factory=list,
        metadata={
            "name": "MediaItem",
            "type": "Element",
            "max_occurs": 3,
        },
    )
