from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class ComplexBaseExpression:
    """
    Represents the base-type for an expressions.
    """

    class Meta:
        name = "complexBaseExpression"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
