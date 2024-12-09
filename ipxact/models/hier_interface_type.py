from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.description import Description
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class HierInterfaceType:
    """A representation of an exported interface.

    The busRef indicates the name of the interface in the containing
    component.

    :ivar description:
    :ivar vendor_extensions:
    :ivar bus_ref: Reference to the components  bus interface
    :ivar id:
    """

    class Meta:
        name = "hierInterfaceType"

    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    vendor_extensions: Optional[VendorExtensions] = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    bus_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "busRef",
            "type": "Attribute",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
