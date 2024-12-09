from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.port_access_handle import PortAccessHandle
from ipxact.models.port_access_type import PortAccessType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class PortAccessType1:
    """
    :ivar port_access_type: Indicates how a netlister accesses a port.
        'ref' means accessed by reference (default) and 'ptr' means
        accessed through a pointer.
    :ivar access_handles:
    """

    class Meta:
        name = "portAccessType"

    port_access_type: Optional[PortAccessType] = field(
        default=None,
        metadata={
            "name": "portAccessType",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    access_handles: Optional["PortAccessType1.AccessHandles"] = field(
        default=None,
        metadata={
            "name": "accessHandles",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )

    @dataclass
    class AccessHandles:
        access_handle: list[PortAccessHandle] = field(
            default_factory=list,
            metadata={
                "name": "accessHandle",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "min_occurs": 1,
            },
        )
