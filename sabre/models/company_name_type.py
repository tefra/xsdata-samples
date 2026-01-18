from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class CompanyNameType:
    """
    Identifies a company by name.

    Attributes:
        value:
        company_short_name:
        travel_sector: Refer to OTA Code List Travel Sector (TVS).
        code: Identifies a company by the company code.
        code_context: Identifies the context of the identifying code,
            such as DUNS, IATA or internal code, etc.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    company_short_name: None | str = field(
        default=None,
        metadata={
            "name": "CompanyShortName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 64,
        },
    )
    travel_sector: None | str = field(
        default=None,
        metadata={
            "name": "TravelSector",
            "type": "Attribute",
        },
    )
    code: None | str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 8,
        },
    )
    code_context: None | str = field(
        default=None,
        metadata={
            "name": "CodeContext",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        },
    )
