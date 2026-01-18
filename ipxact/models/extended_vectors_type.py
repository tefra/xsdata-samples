from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.left import Left
from ipxact.models.right import Right

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class ExtendedVectorsType:
    """
    :ivar vector: Left and right ranges of the vector.
    """

    class Meta:
        name = "extendedVectorsType"

    vector: list[ExtendedVectorsType.Vector] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class Vector:
        left: Left = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "required": True,
            }
        )
        right: Right = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "required": True,
            }
        )
        vector_id: None | str = field(
            default=None,
            metadata={
                "name": "vectorId",
                "type": "Attribute",
            },
        )
        id: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )
