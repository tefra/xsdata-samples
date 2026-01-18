from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.parameter import Parameter

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Parameters:
    """
    A collection of parameters and associated value assertions.
    """

    class Meta:
        name = "parameters"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    parameter: list[Parameter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
