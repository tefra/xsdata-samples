from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_key_element_1 import TypeKeyElement1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass(kw_only=True)
class TypeProviderInfoHistory1(TypeKeyElement1):
    """
    History Element for ProviderInfo Add.

    Parameters
    ----------
    provider_code
        The provider code associated with the Branch.
    pseudo_city_code
        Branch pseudo city code.
    iatacode
        Branch IATA Code.
    """

    class Meta:
        name = "typeProviderInfoHistory"

    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        },
    )
    pseudo_city_code: None | str = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        },
    )
    iatacode: None | str = field(
        default=None,
        metadata={
            "name": "IATACode",
            "type": "Attribute",
            "max_length": 8,
        },
    )
