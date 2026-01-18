from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.clock_driver_type import ClockDriverType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class ClockDriver(ClockDriverType):
    """
    Describes a driven clock port.

    :ivar clock_name: Indicates the name of the cllock. If not specified
        the name is assumed to be the name of the containing port.
    """

    class Meta:
        name = "clockDriver"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    clock_name: None | str = field(
        default=None,
        metadata={
            "name": "clockName",
            "type": "Attribute",
        },
    )
