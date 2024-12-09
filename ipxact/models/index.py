from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.unsigned_int_expression import UnsignedIntExpression

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Index(UnsignedIntExpression):
    """
    An index into an object in the referenced view.
    """

    class Meta:
        name = "index"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
