from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class ValidatingCarrierInfoType:
    """
    Attributes:
        default: Default validating carrier code
        alternate: Alternate validating carrier code
        settlement_method:
        new_vcx_process:
    """

    default: None | ValidatingCarrierInfoType.Default = field(
        default=None,
        metadata={
            "name": "Default",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    alternate: list[ValidatingCarrierInfoType.Alternate] = field(
        default_factory=list,
        metadata={
            "name": "Alternate",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 24,
        },
    )
    settlement_method: None | str = field(
        default=None,
        metadata={
            "name": "SettlementMethod",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 3,
        },
    )
    new_vcx_process: None | bool = field(
        default=None,
        metadata={
            "name": "NewVcxProcess",
            "type": "Attribute",
        },
    )

    @dataclass
    class Default:
        country: list[ValidatingCarrierInfoType.Default.Country] = field(
            default_factory=list,
            metadata={
                "name": "Country",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        code: None | str = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
                "pattern": r"[A-Z][0-9A-Z]|[0-9A-Z][A-Z][0-9A-Z]?|[A-Za-z]{0}",
            },
        )

        @dataclass
        class Country:
            code: None | str = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"[a-zA-Z]{2}",
                },
            )

    @dataclass
    class Alternate:
        country: list[ValidatingCarrierInfoType.Alternate.Country] = field(
            default_factory=list,
            metadata={
                "name": "Country",
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
        class Country:
            code: None | str = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"[a-zA-Z]{2}",
                },
            )
