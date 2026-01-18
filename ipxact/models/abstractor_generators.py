from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.abstractor_generator import AbstractorGenerator

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class AbstractorGenerators:
    """
    List of abstractor generators.
    """

    class Meta:
        name = "abstractorGenerators"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    abstractor_generator: list[AbstractorGenerator] = field(
        default_factory=list,
        metadata={
            "name": "abstractorGenerator",
            "type": "Element",
            "min_occurs": 1,
        },
    )
