from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.address_block_ref import AddressBlockRef
from ipxact.models.alternate_register_ref import AlternateRegisterRef
from ipxact.models.bank_ref import BankRef
from ipxact.models.field_ref import FieldRef
from ipxact.models.memory_remap_ref import MemoryRemapRef
from ipxact.models.part_select import PartSelect
from ipxact.models.range import Range
from ipxact.models.register_file_ref import RegisterFileRef
from ipxact.models.register_ref import RegisterRef
from ipxact.models.sub_port_reference import SubPortReference

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class FieldMap:
    """
    Maps slices of this port to component field slices.

    :ivar field_slice: Reference to a register field slice
    :ivar sub_port_reference:
    :ivar part_select:
    :ivar mode_ref: A reference to a mode.
    :ivar id:
    """

    class Meta:
        name = "fieldMap"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    field_slice: Optional["FieldMap.FieldSlice"] = field(
        default=None,
        metadata={
            "name": "fieldSlice",
            "type": "Element",
            "required": True,
        },
    )
    sub_port_reference: list[SubPortReference] = field(
        default_factory=list,
        metadata={
            "name": "subPortReference",
            "type": "Element",
        },
    )
    part_select: Optional[PartSelect] = field(
        default=None,
        metadata={
            "name": "partSelect",
            "type": "Element",
        },
    )
    mode_ref: list["FieldMap.ModeRef"] = field(
        default_factory=list,
        metadata={
            "name": "modeRef",
            "type": "Element",
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
    class FieldSlice:
        address_space_ref: Optional["FieldMap.FieldSlice.AddressSpaceRef"] = (
            field(
                default=None,
                metadata={
                    "name": "addressSpaceRef",
                    "type": "Element",
                },
            )
        )
        memory_map_ref: Optional["FieldMap.FieldSlice.MemoryMapRef"] = field(
            default=None,
            metadata={
                "name": "memoryMapRef",
                "type": "Element",
            },
        )
        memory_remap_ref: Optional[MemoryRemapRef] = field(
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
        address_block_ref: Optional[AddressBlockRef] = field(
            default=None,
            metadata={
                "name": "addressBlockRef",
                "type": "Element",
                "required": True,
            },
        )
        register_file_ref: list[RegisterFileRef] = field(
            default_factory=list,
            metadata={
                "name": "registerFileRef",
                "type": "Element",
            },
        )
        register_ref: Optional[RegisterRef] = field(
            default=None,
            metadata={
                "name": "registerRef",
                "type": "Element",
                "required": True,
            },
        )
        alternate_register_ref: Optional[AlternateRegisterRef] = field(
            default=None,
            metadata={
                "name": "alternateRegisterRef",
                "type": "Element",
            },
        )
        field_ref: Optional[FieldRef] = field(
            default=None,
            metadata={
                "name": "fieldRef",
                "type": "Element",
                "required": True,
            },
        )
        range: Optional[Range] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

        @dataclass
        class AddressSpaceRef:
            address_space_ref: Optional[str] = field(
                default=None,
                metadata={
                    "name": "addressSpaceRef",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class MemoryMapRef:
            memory_map_ref: Optional[str] = field(
                default=None,
                metadata={
                    "name": "memoryMapRef",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class ModeRef:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        priority: Optional[int] = field(
            default=None,
            metadata={
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
