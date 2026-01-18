from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.address_bank_definition_type import (
    AddressBankDefinitionType,
)
from ipxact.models.address_block import AddressBlock
from ipxact.models.address_unit_bits import AddressUnitBits
from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.memory_remap_definition_type import (
    MemoryRemapDefinitionType,
)
from ipxact.models.shared_type import SharedType
from ipxact.models.short_description import ShortDescription
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class MemoryMapDefinitions:
    class Meta:
        name = "memoryMapDefinitions"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    memory_map_definition: list[MemoryMapDefinitions.MemoryMapDefinition] = (
        field(
            default_factory=list,
            metadata={
                "name": "memoryMapDefinition",
                "type": "Element",
                "min_occurs": 1,
            },
        )
    )

    @dataclass
    class MemoryMapDefinition:
        """
        :ivar name: Unique name
        :ivar display_name:
        :ivar short_description:
        :ivar description:
        :ivar address_block:
        :ivar bank: An addressable bank of blocks within a bank
            definition.
        :ivar memory_remap:
        :ivar address_unit_bits:
        :ivar shared: When the value is 'yes', the contents of the
            memoryMap are shared by all the references to this
            memoryMap, when the value is 'no' the contents of the
            memoryMap is not shared and when the value is 'undefined'
            (default) the sharing of the memoryMap is undefined.
        :ivar vendor_extensions:
        :ivar id:
        """

        name: str | None = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        display_name: DisplayName | None = field(
            default=None,
            metadata={
                "name": "displayName",
                "type": "Element",
            },
        )
        short_description: ShortDescription | None = field(
            default=None,
            metadata={
                "name": "shortDescription",
                "type": "Element",
            },
        )
        description: Description | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        address_block: list[AddressBlock] = field(
            default_factory=list,
            metadata={
                "name": "addressBlock",
                "type": "Element",
            },
        )
        bank: list[AddressBankDefinitionType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        memory_remap: list[MemoryRemapDefinitionType] = field(
            default_factory=list,
            metadata={
                "name": "memoryRemap",
                "type": "Element",
            },
        )
        address_unit_bits: AddressUnitBits | None = field(
            default=None,
            metadata={
                "name": "addressUnitBits",
                "type": "Element",
            },
        )
        shared: SharedType | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        vendor_extensions: VendorExtensions | None = field(
            default=None,
            metadata={
                "name": "vendorExtensions",
                "type": "Element",
            },
        )
        id: str | None = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )
