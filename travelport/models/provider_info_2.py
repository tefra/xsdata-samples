from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_key_element_2 import TypeKeyElement2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProviderInfo2(TypeKeyElement2):
    """
    A representation of the Provider Information (e.g. PCC, IATA, Provider Code)
    given to a Branch profile.

    Parameters
    ----------
    provider_code
        The provider code associated with the PCC/IATA.
    pseudo_city_code
        Branch pseudo city code.
    iatacode
        Branch IATA Code.
    """
    class Meta:
        name = "ProviderInfo"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    pseudo_city_code: None | str = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 10,
        }
    )
    iatacode: None | str = field(
        default=None,
        metadata={
            "name": "IATACode",
            "type": "Attribute",
            "max_length": 8,
        }
    )
