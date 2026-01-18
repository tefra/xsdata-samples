from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.included_in_base_1 import IncludedInBase1
from travelport.models.tax_detail_1 import TaxDetail1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass(kw_only=True)
class TypeTaxInfo1:
    """
    Parameters
    ----------
    tax_detail
    included_in_base
    key
        The tax key represents a valid key of tax
    category
        The tax category represents a valid IATA tax code.
    carrier_defined_category
        Optional category, where a carrier has used a non-standard IATA tax
        category. The tax category will be set to "DU"
    segment_ref
        The segment to which that tax is relative (if applicable)
    flight_details_ref
        The flight details that this tax is relative to (if applicable)
    coupon_ref
        The coupon to which that tax is relative (if applicable)
    amount
    origin_airport
    destination_airport
    country_code
    fare_info_ref
    tax_exempted
        This indicates whether the tax specified by tax category is
        exempted.
    provider_code
        Code of the provider returning this TaxInfo.
    supplier_code
        Code of the supplier returning this TaxInfo.
    text
        Additional Information returned from Supplier.(ACH  only)
    """

    class Meta:
        name = "typeTaxInfo"

    tax_detail: list[TaxDetail1] = field(
        default_factory=list,
        metadata={
            "name": "TaxDetail",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    included_in_base: None | IncludedInBase1 = field(
        default=None,
        metadata={
            "name": "IncludedInBase",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    category: str = field(
        metadata={
            "name": "Category",
            "type": "Attribute",
            "required": True,
        }
    )
    carrier_defined_category: None | str = field(
        default=None,
        metadata={
            "name": "CarrierDefinedCategory",
            "type": "Attribute",
        },
    )
    segment_ref: None | str = field(
        default=None,
        metadata={
            "name": "SegmentRef",
            "type": "Attribute",
        },
    )
    flight_details_ref: None | str = field(
        default=None,
        metadata={
            "name": "FlightDetailsRef",
            "type": "Attribute",
        },
    )
    coupon_ref: None | str = field(
        default=None,
        metadata={
            "name": "CouponRef",
            "type": "Attribute",
        },
    )
    amount: str = field(
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
        }
    )
    origin_airport: None | str = field(
        default=None,
        metadata={
            "name": "OriginAirport",
            "type": "Attribute",
            "length": 3,
        },
    )
    destination_airport: None | str = field(
        default=None,
        metadata={
            "name": "DestinationAirport",
            "type": "Attribute",
            "length": 3,
        },
    )
    country_code: None | str = field(
        default=None,
        metadata={
            "name": "CountryCode",
            "type": "Attribute",
        },
    )
    fare_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "FareInfoRef",
            "type": "Attribute",
        },
    )
    tax_exempted: None | bool = field(
        default=None,
        metadata={
            "name": "TaxExempted",
            "type": "Attribute",
        },
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        },
    )
    supplier_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        },
    )
    text: None | str = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
