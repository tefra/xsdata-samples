from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.allowance_unit import AllowanceUnit

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class BaggageInformationType:
    """
    Information about baggage.
    """

    segment: list[BaggageInformationType.Segment] = field(
        default_factory=list,
        metadata={
            "name": "Segment",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
        },
    )
    allowance: None | BaggageInformationType.Allowance = field(
        default=None,
        metadata={
            "name": "Allowance",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        },
    )

    @dataclass
    class Segment:
        """
        Attributes:
            id: Id of segment that current baggage information applies
                to.
        """

        id: None | int = field(
            default=None,
            metadata={
                "name": "Id",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class Allowance:
        """
        Attributes:
            pieces: Number of Pieces
            weight: Weight Limit
            unit: Units of the Weight Limit
        """

        pieces: None | int = field(
            default=None,
            metadata={
                "name": "Pieces",
                "type": "Attribute",
            },
        )
        weight: None | int = field(
            default=None,
            metadata={
                "name": "Weight",
                "type": "Attribute",
            },
        )
        unit: None | AllowanceUnit = field(
            default=None,
            metadata={
                "name": "Unit",
                "type": "Attribute",
            },
        )
