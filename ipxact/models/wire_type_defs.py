from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.wire_type_def import WireTypeDef

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class WireTypeDefs:
    """
    The group of wire type definitions.

    If no match to a viewName is found then the default language types are
    to be used. See the User Guide for these default types.
    """

    class Meta:
        name = "wireTypeDefs"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    wire_type_def: list[WireTypeDef] = field(
        default_factory=list,
        metadata={
            "name": "wireTypeDef",
            "type": "Element",
            "min_occurs": 1,
        },
    )
