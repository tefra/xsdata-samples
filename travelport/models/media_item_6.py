from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_response_image_size_6 import TypeResponseImageSize6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class MediaItem6:
    """
    Photos and other media urls for the property referenced above.
    """
    class Meta:
        name = "MediaItem"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    caption: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    height: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    width: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        }
    )
    url: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    icon: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    size_code: None | TypeResponseImageSize6 = field(
        default=None,
        metadata={
            "name": "sizeCode",
            "type": "Attribute",
        }
    )
