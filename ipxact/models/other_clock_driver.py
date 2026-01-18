from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.clock_driver_type import ClockDriverType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class OtherClockDriver(ClockDriverType):
    """
    Describes a clock not directly associated with an input port.

    The clockSource attribute can be used on these clocks to indicate the
    actual clock source (e.g. an output port of a clock generator cell).

    :ivar clock_name: Indicates the name of the clock.
    :ivar clock_source: Indicates the name of the actual clock source
        (e.g. an output pin of a clock generator cell).
    """

    class Meta:
        name = "otherClockDriver"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    clock_name: str | None = field(
        default=None,
        metadata={
            "name": "clockName",
            "type": "Attribute",
            "required": True,
        },
    )
    clock_source: str | None = field(
        default=None,
        metadata={
            "name": "clockSource",
            "type": "Attribute",
        },
    )
