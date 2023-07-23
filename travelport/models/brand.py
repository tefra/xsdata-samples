from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.default_brand_detail import DefaultBrandDetail
from travelport.models.image_location import ImageLocation
from travelport.models.optional_services import OptionalServices
from travelport.models.rules import Rules
from travelport.models.service_associations import ServiceAssociations
from travelport.models.text import Text
from travelport.models.title import Title
from travelport.models.type_applicable_segment import TypeApplicableSegment
from travelport.models.upsell_brand import UpsellBrand

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Brand:
    """
    Commercially recognized product offered by an airline.

    Parameters
    ----------
    title
        The additional titles associated to the brand
    text
        Text associated to the brand
    image_location
        Images associated to the brand
    optional_services
    rules
        Brand rules
    service_associations
        Service associated with this brand
    upsell_brand
        The unique identifier of the Upsell brand
    applicable_segment
    default_brand_detail
        Default brand details.
    key
        Brand Key
    brand_id
        The unique identifier of the brand
    name
        The Title of the brand
    air_itinerary_details_ref
        AirItinerary associated with this brand
    up_sell_brand_id
    brand_found
        Indicates whether brand for the fare was found for carrier or not
    up_sell_brand_found
        Indicates whether upsell brand for the fare was found for carrier or
        not
    branded_details_available
        Indicates if full details of the brand is available
    carrier
    brand_tier
        Modifier to price by specific brand tier number.
    brand_maintained
        Indicates whether the brand was maintained from the original ticket.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    title: list[Title] = field(
        default_factory=list,
        metadata={
            "name": "Title",
            "type": "Element",
            "max_occurs": 2,
        }
    )
    text: list[Text] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "max_occurs": 5,
        }
    )
    image_location: list[ImageLocation] = field(
        default_factory=list,
        metadata={
            "name": "ImageLocation",
            "type": "Element",
            "max_occurs": 3,
        }
    )
    optional_services: None | OptionalServices = field(
        default=None,
        metadata={
            "name": "OptionalServices",
            "type": "Element",
        }
    )
    rules: list[Rules] = field(
        default_factory=list,
        metadata={
            "name": "Rules",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    service_associations: None | ServiceAssociations = field(
        default=None,
        metadata={
            "name": "ServiceAssociations",
            "type": "Element",
        }
    )
    upsell_brand: None | UpsellBrand = field(
        default=None,
        metadata={
            "name": "UpsellBrand",
            "type": "Element",
        }
    )
    applicable_segment: list[TypeApplicableSegment] = field(
        default_factory=list,
        metadata={
            "name": "ApplicableSegment",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    default_brand_detail: list[DefaultBrandDetail] = field(
        default_factory=list,
        metadata={
            "name": "DefaultBrandDetail",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    brand_id: None | str = field(
        default=None,
        metadata={
            "name": "BrandID",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 19,
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        }
    )
    air_itinerary_details_ref: None | str = field(
        default=None,
        metadata={
            "name": "AirItineraryDetailsRef",
            "type": "Attribute",
        }
    )
    up_sell_brand_id: None | str = field(
        default=None,
        metadata={
            "name": "UpSellBrandID",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 19,
        }
    )
    brand_found: None | bool = field(
        default=None,
        metadata={
            "name": "BrandFound",
            "type": "Attribute",
        }
    )
    up_sell_brand_found: None | bool = field(
        default=None,
        metadata={
            "name": "UpSellBrandFound",
            "type": "Attribute",
        }
    )
    branded_details_available: None | bool = field(
        default=None,
        metadata={
            "name": "BrandedDetailsAvailable",
            "type": "Attribute",
        }
    )
    carrier: None | str = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    brand_tier: None | str = field(
        default=None,
        metadata={
            "name": "BrandTier",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 10,
        }
    )
    brand_maintained: None | str = field(
        default=None,
        metadata={
            "name": "BrandMaintained",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 99,
        }
    )
