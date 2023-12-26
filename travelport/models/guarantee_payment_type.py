from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class GuaranteePaymentType:
    """Accepted payment types.

    Applicable only for HotelSupershopper, Hotel Details and Hotel
    rules.

    Parameters
    ----------
    value
    type_value
        Accepted payment types: CreditCard, AgencyIATA/ARC, FrequentGuest,
        SpecialIndustry, CDNumber, HomeAddress, CompanyAddress, Override,
        Other, or None
    description
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

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
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
        },
    )
