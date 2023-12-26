from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class ExemptTaxes:
    """
    Request tax exemption for specific tax category and/or all taxes of a specific
    country.

    Parameters
    ----------
    country_code
        Specify ISO country code for which tax exemption is requested.
    tax_category
        Specify tax category for which tax exemption is requested.
    all_taxes
        Request exemption of all taxes.
    tax_territory
        exemption is achieved by sending in the TaxTerritory in the tax
        exempt price request.
    company_name
        The federal government body name must be provided in this element.
        This field is required by AC
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    country_code: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CountryCode",
            "type": "Element",
            "max_occurs": 999,
            "length": 2,
        },
    )
    tax_category: list[str] = field(
        default_factory=list,
        metadata={
            "name": "TaxCategory",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    all_taxes: None | bool = field(
        default=None,
        metadata={
            "name": "AllTaxes",
            "type": "Attribute",
        },
    )
    tax_territory: None | str = field(
        default=None,
        metadata={
            "name": "TaxTerritory",
            "type": "Attribute",
            "length": 2,
        },
    )
    company_name: None | str = field(
        default=None,
        metadata={
            "name": "CompanyName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 24,
        },
    )
