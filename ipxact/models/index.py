from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.unsigned_int_expression import UnsignedIntExpression

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class Index(UnsignedIntExpression):
    """
    An index into an object in the referenced view.
    """

    class Meta:
        name = "index"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
