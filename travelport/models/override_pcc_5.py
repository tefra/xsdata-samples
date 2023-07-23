from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class OverridePcc5:
    """Used for Host Emulation - If used agent will emulate to this PCC in host and execute the request emulated into this PCC.

    Parameters
    ----------
    provider_code
        The code of the provider (e.g. 1G, 1S)
    pseudo_city_code
        The PCC in the host system.
    """
    class Meta:
        name = "OverridePCC"
        namespace = "http://www.travelport.com/schema/common_v37_0"

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
