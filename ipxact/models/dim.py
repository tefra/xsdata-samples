from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.unsigned_positive_longint_expression import (
    UnsignedPositiveLongintExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Dim(UnsignedPositiveLongintExpression):
    """
    Dimensions a register array, the semantics for dim elements are the
    same as the C language standard for the layout of memory in
    multidimensional arrays.

    :ivar id:
    :ivar index_var: Name for the index to allow referring to it in
        names and prosa.
    """

    class Meta:
        name = "dim"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    index_var: None | str = field(
        default=None,
        metadata={
            "name": "indexVar",
            "type": "Attribute",
        },
    )
