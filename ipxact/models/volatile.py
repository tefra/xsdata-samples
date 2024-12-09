from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Volatile:
    """
    Indicates whether the data is volatile.
    """

    class Meta:
        name = "volatile"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
