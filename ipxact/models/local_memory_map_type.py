from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.address_block import AddressBlock
from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.local_address_bank_type import LocalAddressBankType
from ipxact.models.short_description import ShortDescription
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class LocalMemoryMapType:
    """
    Map of address space blocks on the local memory map of a initiator bus
    interface.

    :ivar name: Unique name
    :ivar display_name:
    :ivar short_description:
    :ivar description:
    :ivar address_block:
    :ivar bank: Represents a bank of memory made up of address blocks or
        other banks.  It has a bankAlignment attribute indicating
        whether its blocks are aligned in 'parallel' (occupying adjacent
        bit fields) or 'serial' (occupying contiguous addresses). Its
        child blocks do not contain addresses or bit offsets.
    :ivar vendor_extensions:
    :ivar id:
    """

    class Meta:
        name = "localMemoryMapType"

    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        }
    )
    display_name: None | DisplayName = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    short_description: None | ShortDescription = field(
        default=None,
        metadata={
            "name": "shortDescription",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    description: None | Description = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    address_block: list[AddressBlock] = field(
        default_factory=list,
        metadata={
            "name": "addressBlock",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    bank: list[LocalAddressBankType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    vendor_extensions: None | VendorExtensions = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
