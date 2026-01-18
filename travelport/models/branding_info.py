from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.image_location import ImageLocation
from travelport.models.price_range import PriceRange
from travelport.models.service_group import ServiceGroup
from travelport.models.text import Text
from travelport.models.title import Title
from travelport.models.type_segment_ref_1 import TypeSegmentRef1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class BrandingInfo:
    """
    Branding information for the Ancillary Service.

    Returned in Seat Map only. Providers: 1G, 1V, 1P, ACH.

    Parameters
    ----------
    price_range
        The price range of the Ancillary Service.  Providers: 1G, 1V, 1P,
        ACH
    text
    title
        The additional titles associated to the brand or optional service.
        Providers: ACH, 1G, 1V, 1P
    image_location
    service_group
    air_segment_ref
        Specifies the AirSegment the branding information is for. Providers:
        ACH, 1G, 1V, 1P
    key
    service_sub_code
        The Service Sub Code of the Ancillary Service.  Providers: 1G, 1V,
        1P, ACH
    external_service_name
        The external name of the Ancillary Service.  Providers: 1G, 1V, 1P,
        ACH
    service_type
        The type of Ancillary Service.  Providers: 1G, 1V, 1P, ACH
    commercial_name
        The commercial name of the Ancillary Service.  Providers: 1G, 1V,
        1P, ACH
    chargeable
        Indicates if the optional service is not offered, is available for a
        charge, or is included in the brand.  Providers: 1G, 1V, 1P, ACH
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    price_range: list[PriceRange] = field(
        default_factory=list,
        metadata={
            "name": "PriceRange",
            "type": "Element",
            "max_occurs": 5,
        },
    )
    text: list[Text] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "max_occurs": 99,
        },
    )
    title: list[Title] = field(
        default_factory=list,
        metadata={
            "name": "Title",
            "type": "Element",
            "max_occurs": 2,
        },
    )
    image_location: list[ImageLocation] = field(
        default_factory=list,
        metadata={
            "name": "ImageLocation",
            "type": "Element",
            "max_occurs": 3,
        },
    )
    service_group: None | ServiceGroup = field(
        default=None,
        metadata={
            "name": "ServiceGroup",
            "type": "Element",
        },
    )
    air_segment_ref: list[TypeSegmentRef1] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentRef",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 99,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    service_sub_code: None | str = field(
        default=None,
        metadata={
            "name": "ServiceSubCode",
            "type": "Attribute",
        },
    )
    external_service_name: None | str = field(
        default=None,
        metadata={
            "name": "ExternalServiceName",
            "type": "Attribute",
        },
    )
    service_type: None | str = field(
        default=None,
        metadata={
            "name": "ServiceType",
            "type": "Attribute",
        },
    )
    commercial_name: str = field(
        metadata={
            "name": "CommercialName",
            "type": "Attribute",
            "required": True,
        }
    )
    chargeable: None | str = field(
        default=None,
        metadata={
            "name": "Chargeable",
            "type": "Attribute",
        },
    )
