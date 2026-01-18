from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.string_expression import StringExpression

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class PortPathSegmentType(StringExpression):
    """
    Identifies one level of hierarchy in the view specifed by viewNameRef.

    This is a simple name and optionally some indices into a multi
    dimensional element.
    """

    class Meta:
        name = "portPathSegmentType"

    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
