from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.company_name import CompanyName

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class PrePayId:
    """
    Pre pay unique identifier , example Flight Pass Number.

    Parameters
    ----------
    company_name
        Supplier info that is specific to the pre pay Id
    id
        This is the exact pre pay number. Example flight pass number
    type_value
        Type of pre pay unique identifier,presently only available value is
        FlightPass.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    company_name: None | CompanyName = field(
        default=None,
        metadata={
            "name": "CompanyName",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 36,
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
