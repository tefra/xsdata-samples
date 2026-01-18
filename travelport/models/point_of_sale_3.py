from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass(kw_only=True)
class PointOfSale3:
    """
    User can use this node to send a specific PCC to access fares allowed
    only for that PCC.

    This node gives the capability for fare redistribution at UR level. For
    fare redistribution at the stored fare level see
    AirPricingSolution/AirPricingInfo/AirPricingModifiers/PointOfSale.

    Parameters
    ----------
    provider_code
        The provider in which the PCC is defined.
    pseudo_city_code
        The PCC in the host system.
    key
    iata
        Used for rapid reprice. This field is the IATA associated to this
        Point of Sale PCC. Providers: 1G/1V
    """

    class Meta:
        name = "PointOfSale"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    provider_code: str = field(
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    pseudo_city_code: str = field(
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 10,
        }
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    iata: None | str = field(
        default=None,
        metadata={
            "name": "IATA",
            "type": "Attribute",
            "max_length": 8,
        },
    )
