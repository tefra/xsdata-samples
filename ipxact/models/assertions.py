from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.assertion import Assertion

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class Assertions:
    """
    List of assertions about allowed parameter values.
    """

    class Meta:
        name = "assertions"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    assertion: list[Assertion] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
