from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class TransparentBridge:
    """If this element is present, it indicates that the bus interface provides a
    transparent bridge to another initiator bus interface on the same component.

    It has a initiatorRef attribute which contains the name of the other
    bus interface. Any target interface can bridge to multiple initiator
    interfaces, and multiple target interfaces can bridge to the same
    initiator interface.

    :ivar vendor_extensions:
    :ivar initiator_ref: The name of the initiator bus interface to
        which this interface bridges.
    :ivar id:
    """

    class Meta:
        name = "transparentBridge"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    vendor_extensions: Optional[VendorExtensions] = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
        },
    )
    initiator_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "initiatorRef",
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
