from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.applicable_segment import ApplicableSegment
from travelport.models.image_location import ImageLocation
from travelport.models.text import Text

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class TypeDefaultBrandDetail:
    """
    Parameters
    ----------
    text
        Text associated to the brand
    image_location
        Images associated to the brand
    applicable_segment
        Defines for which air segment the brand is applicable.
    brand_id
        The unique identifier of the brand
    """

    class Meta:
        name = "typeDefaultBrandDetail"

    text: list[Text] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 4,
        },
    )
    image_location: list[ImageLocation] = field(
        default_factory=list,
        metadata={
            "name": "ImageLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 3,
        },
    )
    applicable_segment: list[ApplicableSegment] = field(
        default_factory=list,
        metadata={
            "name": "ApplicableSegment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 99,
        },
    )
    brand_id: None | str = field(
        default=None,
        metadata={
            "name": "BrandID",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 19,
        },
    )
