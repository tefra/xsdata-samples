from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class ComplexTiedValueExpression:
    """
    An unsigned bit vector expression that resolves to the value set {0, 1,
    ...} or or the string values 'open' or 'default'.

    It is derived from simpleUnsignedBitVectorExpression and it supports an
    expression value.

    :ivar value:
    :ivar other_attributes:
    :ivar minimum: For elements which can be specified using expression
        which are supposed to be resolved to a long value, this
        indicates the minimum value allowed.
    :ivar maximum: For elements which can be specified using expression
        which are supposed to be resolved to a long value, this
        indicates the maximum value allowed.
    """

    class Meta:
        name = "complexTiedValueExpression"

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
    minimum: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    maximum: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
