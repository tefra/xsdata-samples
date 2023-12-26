from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class TypeNativeSearchModifier:
    """
    Parameters
    ----------
    value
    provider_code
        The host for which the NativeModfier being added to
    """

    class Meta:
        name = "typeNativeSearchModifier"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
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
