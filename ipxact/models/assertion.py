from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.short_description import ShortDescription
from ipxact.models.unsigned_bit_expression import UnsignedBitExpression

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Assertion:
    """
    Provides an expression for describing valid parameter value settings.

    If a assertion assert expression evaluates false, the name, displayName
    and/or description can be used to communicate the assertion failure.

    :ivar name: Unique name
    :ivar display_name:
    :ivar short_description:
    :ivar description:
    :ivar assert_value:
    :ivar id:
    """

    class Meta:
        name = "assertion"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    name: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    display_name: DisplayName | None = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
        },
    )
    short_description: ShortDescription | None = field(
        default=None,
        metadata={
            "name": "shortDescription",
            "type": "Element",
        },
    )
    description: Description | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    assert_value: UnsignedBitExpression | None = field(
        default=None,
        metadata={
            "name": "assert",
            "type": "Element",
            "required": True,
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
