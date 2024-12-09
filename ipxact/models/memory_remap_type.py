from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.address_block import AddressBlock
from ipxact.models.bank import Bank
from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.mode_ref import ModeRef
from ipxact.models.short_description import ShortDescription
from ipxact.models.subspace_map import SubspaceMap
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class MemoryRemapType:
    """
    Map of address space blocks on a target bus interface in a specific remap
    state.

    :ivar name: Unique name
    :ivar display_name:
    :ivar short_description:
    :ivar description:
    :ivar mode_ref:
    :ivar remap_definition_ref:
    :ivar address_block:
    :ivar bank:
    :ivar subspace_map:
    :ivar vendor_extensions:
    :ivar id:
    """

    class Meta:
        name = "memoryRemapType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    display_name: Optional[DisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    short_description: Optional[ShortDescription] = field(
        default=None,
        metadata={
            "name": "shortDescription",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    mode_ref: list[ModeRef] = field(
        default_factory=list,
        metadata={
            "name": "modeRef",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "min_occurs": 1,
        },
    )
    remap_definition_ref: Optional["MemoryRemapType.RemapDefinitionRef"] = (
        field(
            default=None,
            metadata={
                "name": "remapDefinitionRef",
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
    vendor_extensions: Optional[VendorExtensions] = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )

    @dataclass
    class RemapDefinitionRef:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        type_definitions: Optional[str] = field(
            default=None,
            metadata={
                "name": "typeDefinitions",
                "type": "Attribute",
                "required": True,
            },
        )
