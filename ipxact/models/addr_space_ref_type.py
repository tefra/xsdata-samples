from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class AddrSpaceRefType:
    """
    Base type for an element which references an address space.

    Reference is kept in an attribute rather than the text value, so that
    the type may be extended with child elements if necessary.

    :ivar vendor_extensions:
    :ivar address_space_ref: A reference to a unique address space.
    :ivar id:
    """

    class Meta:
        name = "addrSpaceRefType"

    vendor_extensions: None | VendorExtensions = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    address_space_ref: None | str = field(
        default=None,
        metadata={
            "name": "addressSpaceRef",
            "type": "Attribute",
            "required": True,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
