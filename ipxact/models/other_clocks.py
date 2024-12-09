from dataclasses import dataclass, field

from ipxact.models.other_clock_driver import OtherClockDriver

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class OtherClocks:
    """List of clocks associated with the component that are not associated with
    ports.

    Set the clockSource attribute on the clockDriver to indicate the
    source of a clock not associated with a particular component port.
    """

    class Meta:
        name = "otherClocks"

    other_clock_driver: list[OtherClockDriver] = field(
        default_factory=list,
        metadata={
            "name": "otherClockDriver",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "min_occurs": 1,
        },
    )
