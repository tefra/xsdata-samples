from __future__ import annotations

from dataclasses import dataclass

from ipxact.models.driver_type import DriverType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class Driver(DriverType):
    """
    Wire port driver element.
    """

    class Meta:
        name = "driver"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
