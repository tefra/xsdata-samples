from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class ImageLocation:
    """
    Parameters
    ----------
    value
    type_value
        Type of Image Location. E.g., "Agent", "Consumer".
    image_width
        The width of the image
    image_height
        The height of the image
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
    image_width: None | int = field(
        default=None,
        metadata={
            "name": "ImageWidth",
            "type": "Attribute",
            "required": True,
        },
    )
    image_height: None | int = field(
        default=None,
        metadata={
            "name": "ImageHeight",
            "type": "Attribute",
            "required": True,
        },
    )
