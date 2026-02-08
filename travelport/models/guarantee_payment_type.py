from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass(kw_only=True)
class GuaranteePaymentType:
    """
    Accepted payment types.

    Applicable only for HotelSupershopper, Hotel Details and Hotel rules.

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

    value: str = field(default="")
    type_value: str = field(
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
        },
    )
