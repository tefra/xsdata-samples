from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_response_image_size_4 import TypeResponseImageSize4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass(kw_only=True)
class MediaItem4:
    """
    Photos and other media urls for the property referenced above.
    """

    class Meta:
        name = "MediaItem"
        namespace = "http://www.travelport.com/schema/common_v37_0"

    caption: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    height: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    width: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    url: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    icon: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    size_code: None | TypeResponseImageSize4 = field(
        default=None,
        metadata={
            "name": "sizeCode",
            "type": "Attribute",
        },
    )
