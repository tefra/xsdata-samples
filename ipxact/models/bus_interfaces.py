from dataclasses import dataclass, field

from ipxact.models.bus_interface import BusInterface

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class BusInterfaces:
    """
    A list of bus interfaces supported by this component.
    """

    class Meta:
        name = "busInterfaces"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    bus_interface: list[BusInterface] = field(
        default_factory=list,
        metadata={
            "name": "busInterface",
            "type": "Element",
            "min_occurs": 1,
        },
    )
