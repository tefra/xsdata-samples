from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.address_block_ref import AddressBlockRef
from ipxact.models.alternate_register_ref import AlternateRegisterRef
from ipxact.models.bank_ref import BankRef
from ipxact.models.field_ref import FieldRef
from ipxact.models.memory_remap_ref import MemoryRemapRef
from ipxact.models.register_file_ref import RegisterFileRef
from ipxact.models.register_ref import RegisterRef

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class IndirectDataRef:
    """
    A reference to a field used for read/write access to the indirectly
    accessible memoryMap.
    """

    class Meta:
        name = "indirectDataRef"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    address_space_ref: None | IndirectDataRef.AddressSpaceRef = field(
        default=None,
        metadata={
            "name": "addressSpaceRef",
            "type": "Element",
        },
    )
    memory_map_ref: None | IndirectDataRef.MemoryMapRef = field(
        default=None,
        metadata={
            "name": "memoryMapRef",
            "type": "Element",
        },
    )
    memory_remap_ref: None | MemoryRemapRef = field(
        default=None,
        metadata={
            "name": "memoryRemapRef",
            "type": "Element",
        },
    )
    bank_ref: list[BankRef] = field(
        default_factory=list,
        metadata={
            "name": "bankRef",
            "type": "Element",
        },
    )
    address_block_ref: None | AddressBlockRef = field(
        default=None,
        metadata={
            "name": "addressBlockRef",
            "type": "Element",
        },
    )
    register_file_ref: list[RegisterFileRef] = field(
        default_factory=list,
        metadata={
            "name": "registerFileRef",
            "type": "Element",
        },
    )
    register_ref: None | RegisterRef = field(
        default=None,
        metadata={
            "name": "registerRef",
            "type": "Element",
        },
    )
    alternate_register_ref: None | AlternateRegisterRef = field(
        default=None,
        metadata={
            "name": "alternateRegisterRef",
            "type": "Element",
        },
    )
    field_ref: FieldRef = field(
        metadata={
            "name": "fieldRef",
            "type": "Element",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class AddressSpaceRef:
        address_space_ref: str = field(
            metadata={
                "name": "addressSpaceRef",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class MemoryMapRef:
        memory_map_ref: str = field(
            metadata={
                "name": "memoryMapRef",
                "type": "Attribute",
                "required": True,
            }
        )
