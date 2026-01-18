from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.address_block import AddressBlock
from ipxact.models.address_unit_bits import AddressUnitBits
from ipxact.models.bank import Bank
from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.memory_remap import MemoryRemap
from ipxact.models.shared_type import SharedType
from ipxact.models.short_description import ShortDescription
from ipxact.models.subspace_map import SubspaceMap
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class MemoryMapType:
    """
    Map of address space blocks on target target bus interface.

    :ivar name: Unique name
    :ivar display_name:
    :ivar short_description:
    :ivar description:
    :ivar memory_map_definition_ref:
    :ivar address_block:
    :ivar bank:
    :ivar subspace_map:
    :ivar memory_remap:
    :ivar address_unit_bits:
    :ivar shared: When the value is 'yes', the contents of the memoryMap
        are shared by all the references to this memoryMap, when the
        value is 'no' the contents of the memoryMap is not shared and
        when the value is 'undefined' (default) the sharing of the
        memoryMap is undefined.
    :ivar vendor_extensions:
    :ivar id:
    """

    class Meta:
        name = "memoryMapType"

    name: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    display_name: DisplayName | None = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    short_description: ShortDescription | None = field(
        default=None,
        metadata={
            "name": "shortDescription",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    description: Description | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    memory_map_definition_ref: MemoryMapType.MemoryMapDefinitionRef | None = (
        field(
            default=None,
            metadata={
                "name": "memoryMapDefinitionRef",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )
    )
    address_block: list[AddressBlock] = field(
        default_factory=list,
        metadata={
            "name": "addressBlock",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    bank: list[Bank] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    subspace_map: list[SubspaceMap] = field(
        default_factory=list,
        metadata={
            "name": "subspaceMap",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    memory_remap: list[MemoryRemap] = field(
        default_factory=list,
        metadata={
            "name": "memoryRemap",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    address_unit_bits: AddressUnitBits | None = field(
        default=None,
        metadata={
            "name": "addressUnitBits",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    shared: SharedType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    vendor_extensions: VendorExtensions | None = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )

    @dataclass
    class MemoryMapDefinitionRef:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        type_definitions: str | None = field(
            default=None,
            metadata={
                "name": "typeDefinitions",
                "type": "Attribute",
                "required": True,
            },
        )
