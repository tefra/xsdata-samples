from __future__ import annotations

from dataclasses import dataclass

from ipxact.models.port_type import PortType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Port(PortType):
    """
    Describes port characteristics.
    """

    class Meta:
        name = "port"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
