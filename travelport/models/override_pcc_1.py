from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class OverridePcc1:
    """Used to emulate to another PCC or SID.

    Providers: 1G, 1V, 1P.

    Parameters
    ----------
    provider_code
        The code of the provider (e.g. 1G, 1S)
    pseudo_city_code
        The PCC in the host system.
    """

    class Meta:
        name = "OverridePCC"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        },
    )
    pseudo_city_code: None | str = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 10,
        },
    )
