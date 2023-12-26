from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class TravelArranger:
    """
    Details of Travel Arranger.

    Parameters
    ----------
    value
    company_short_name
        Company Name
    code
        IATA Code for Arranger
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

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
        },
    )
    code: None | str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        },
    )
