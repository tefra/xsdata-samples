from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Volatile:
    """
    Indicates whether the data is volatile.
    """

    class Meta:
        name = "volatile"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    value: None | bool = field(
        default=None,
        metadata={
            "required": True,
        },
    )
