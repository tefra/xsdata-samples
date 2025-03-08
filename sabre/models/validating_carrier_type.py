from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.validating_carrier_prefer_level_type import (
    ValidatingCarrierPreferLevelType,
)

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class ValidatingCarrierType:
    """
    Attributes:
        preference:
        code: Validating Carrier code
    """

    preference: list[ValidatingCarrierType.Preference] = field(
        default_factory=list,
        metadata={
            "name": "Preference",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    code: None | str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "pattern": r"[0-9A-Z]{2,3}",
        },
    )

    @dataclass
    class Preference:
        code: None | str = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
                "required": True,
                "pattern": r"[0-9A-Z]{2,3}",
            },
        )
        level: None | ValidatingCarrierPreferLevelType = field(
            default=None,
            metadata={
                "name": "Level",
                "type": "Attribute",
                "required": True,
            },
        )
