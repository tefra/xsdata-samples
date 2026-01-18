from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class BrandModifiers:
    """
    Used to specify the level of branding requested.

    Parameters
    ----------
    fare_family_display
        Used to request a fare family display.
    basic_details_only
        Used to request basic details of the brand.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    fare_family_display: None | BrandModifiers.FareFamilyDisplay = field(
        default=None,
        metadata={
            "name": "FareFamilyDisplay",
            "type": "Element",
        },
    )
    basic_details_only: None | BrandModifiers.BasicDetailsOnly = field(
        default=None,
        metadata={
            "name": "BasicDetailsOnly",
            "type": "Element",
        },
    )

    @dataclass(kw_only=True)
    class FareFamilyDisplay:
        """
        Parameters
        ----------
        modifier_type
            "FareFamily" returns the lowest branded fares in a fare family.
            "MaintainBookingCode" attempts to return the lowest branded fare
            in a fare family display based on the permitted booking code.
            Any brand that does not have a fare for the permitted booking
            code will then have the lowest fare returned.
            "LowestFareInBrand" returns the lowest fare within each branded
            fare in a fare family display.
        """

        modifier_type: str = field(
            metadata={
                "name": "ModifierType",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BasicDetailsOnly:
        return_basic_details: bool = field(
            metadata={
                "name": "ReturnBasicDetails",
                "type": "Attribute",
                "required": True,
            }
        )
