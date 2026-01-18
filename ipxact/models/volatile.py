from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class Volatile:
    """
    Indicates whether the data is volatile.
    """

    class Meta:
        name = "volatile"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    value: bool = field(
        metadata={
            "required": True,
        }
    )
