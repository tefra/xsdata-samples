from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.address_bank_definition_type import (
    AddressBankDefinitionType,
)
from ipxact.models.address_block import AddressBlock
from ipxact.models.address_unit_bits import AddressUnitBits
from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.short_description import ShortDescription
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class MemoryRemapDefinitions:
    class Meta:
        name = "memoryRemapDefinitions"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    memory_remap_definition: list[
        MemoryRemapDefinitions.MemoryRemapDefinition
    ] = field(
        default_factory=list,
        metadata={
            "name": "memoryRemapDefinition",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class MemoryRemapDefinition:
        """
        :ivar name: Unique name
        :ivar display_name:
        :ivar short_description:
        :ivar description:
        :ivar address_block:
        :ivar bank: An addressable bank of blocks within a bank
            definition.
        :ivar address_unit_bits:
        :ivar vendor_extensions:
        :ivar id:
        """

        name: str = field(
            metadata={
                "type": "Element",
                "required": True,
            }
        )
        display_name: None | DisplayName = field(
            default=None,
            metadata={
                "name": "displayName",
                "type": "Element",
            },
        )
        short_description: None | ShortDescription = field(
            default=None,
            metadata={
                "name": "shortDescription",
                "type": "Element",
            },
        )
        description: None | Description = field(
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
        address_unit_bits: None | AddressUnitBits = field(
            default=None,
            metadata={
                "name": "addressUnitBits",
                "type": "Element",
            },
        )
        vendor_extensions: None | VendorExtensions = field(
            default=None,
            metadata={
                "name": "vendorExtensions",
                "type": "Element",
            },
        )
        id: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )
