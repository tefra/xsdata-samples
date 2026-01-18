from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.access_policies import AccessPolicies
from ipxact.models.alternate_registers import AlternateRegisters
from ipxact.models.array import Array
from ipxact.models.base_address import BaseAddress
from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.field_type import FieldType
from ipxact.models.parameters import Parameters
from ipxact.models.register_file import RegisterFile
from ipxact.models.short_description import ShortDescription
from ipxact.models.simple_access_handle import SimpleAccessHandle
from ipxact.models.sliced_access_handle import SlicedAccessHandle
from ipxact.models.unsigned_longint_expression import UnsignedLongintExpression
from ipxact.models.unsigned_positive_int_expression import (
    UnsignedPositiveIntExpression,
)
from ipxact.models.unsigned_positive_longint_expression import (
    UnsignedPositiveLongintExpression,
)
from ipxact.models.usage_type import UsageType
from ipxact.models.vendor_extensions import VendorExtensions
from ipxact.models.volatile import Volatile

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class AddressBlockType:
    """
    Top level address block that specify an address.

    :ivar name: Unique name
    :ivar display_name:
    :ivar short_description:
    :ivar description:
    :ivar access_handles:
    :ivar array:
    :ivar base_address:
    :ivar address_block_definition_ref:
    :ivar type_identifier: Identifier name used to indicate that
        multiple addressBlock elements contain the exact same
        information except for the elements in the
        addressBlockInstanceGroup.
    :ivar range: The address range of an address block.  Expressed as
        the number of addressable units accessible to the block. The
        range and the width are related by the following formulas:
        number_of_bits_in_block = ipxact:addressUnitBits * ipxact:range
        number_of_rows_in_block = number_of_bits_in_block / ipxact:width
    :ivar width: The bit width of a row in the address block. The range
        and the width are related by the following formulas:
        number_of_bits_in_block = ipxact:addressUnitBits * ipxact:range
        number_of_rows_in_block = number_of_bits_in_block / ipxact:width
    :ivar usage: Indicates the usage of this block.  Possible values are
        'memory', 'register' and 'reserved'.
    :ivar volatile:
    :ivar access_policies:
    :ivar parameters: Any additional parameters needed to describe this
        address block to the generators.
    :ivar register: A single register
    :ivar register_file: A structure of registers and register files
    :ivar vendor_extensions:
    :ivar id:
    :ivar misalignment_allowed: If true, register alignment is not
        restricted to register size. Defaults to false.
    """

    class Meta:
        name = "addressBlockType"

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
    access_handles: AddressBlockType.AccessHandles | None = field(
        default=None,
        metadata={
            "name": "accessHandles",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    array: Array | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    base_address: BaseAddress | None = field(
        default=None,
        metadata={
            "name": "baseAddress",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    address_block_definition_ref: AddressBlockType.AddressBlockDefinitionRef | None = field(
        default=None,
        metadata={
            "name": "addressBlockDefinitionRef",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    type_identifier: str | None = field(
        default=None,
        metadata={
            "name": "typeIdentifier",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    range: UnsignedPositiveLongintExpression | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    width: UnsignedPositiveIntExpression | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    usage: UsageType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    volatile: Volatile | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    access_policies: AccessPolicies | None = field(
        default=None,
        metadata={
            "name": "accessPolicies",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    parameters: Parameters | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    register: list[AddressBlockType.Register] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    register_file: list[RegisterFile] = field(
        default_factory=list,
        metadata={
            "name": "registerFile",
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
    misalignment_allowed: bool = field(
        default=True,
        metadata={
            "name": "misalignmentAllowed",
            "type": "Attribute",
        },
    )

    @dataclass
    class AccessHandles:
        access_handle: list[SlicedAccessHandle] = field(
            default_factory=list,
            metadata={
                "name": "accessHandle",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "min_occurs": 1,
            },
        )

    @dataclass
    class AddressBlockDefinitionRef:
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

    @dataclass
    class Register:
        """
        :ivar name: Unique name
        :ivar display_name:
        :ivar short_description:
        :ivar description:
        :ivar access_handles:
        :ivar array:
        :ivar address_offset: Offset from the address block's
            baseAddress or the containing register file's addressOffset,
            expressed as the number of addressUnitBits from the
            containing memoryMap or localMemoryMap.
        :ivar register_definition_ref:
        :ivar type_identifier: Identifier name used to indicate that
            multiple register elements contain the exact same
            information for the elements in the registerDefinitionGroup.
        :ivar size: Width of the register in bits.
        :ivar volatile:
        :ivar access_policies:
        :ivar field_value: Describes individual bit fields within the
            register.
        :ivar alternate_registers:
        :ivar parameters:
        :ivar vendor_extensions:
        :ivar id:
        """

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
        access_handles: AddressBlockType.Register.AccessHandles | None = (
            field(
                default=None,
                metadata={
                    "name": "accessHandles",
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                },
            )
        )
        array: Array | None = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )
        address_offset: UnsignedLongintExpression | None = field(
            default=None,
            metadata={
                "name": "addressOffset",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "required": True,
            },
        )
        register_definition_ref: AddressBlockType.Register.RegisterDefinitionRef | None = field(
            default=None,
            metadata={
                "name": "registerDefinitionRef",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )
        type_identifier: str | None = field(
            default=None,
            metadata={
                "name": "typeIdentifier",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )
        size: UnsignedPositiveIntExpression | None = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )
        volatile: Volatile | None = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )
        access_policies: AccessPolicies | None = field(
            default=None,
            metadata={
                "name": "accessPolicies",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )
        field_value: list[FieldType] = field(
            default_factory=list,
            metadata={
                "name": "field",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )
        alternate_registers: AlternateRegisters | None = field(
            default=None,
            metadata={
                "name": "alternateRegisters",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )
        parameters: Parameters | None = field(
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
        class AccessHandles:
            access_handle: list[SimpleAccessHandle] = field(
                default_factory=list,
                metadata={
                    "name": "accessHandle",
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                    "min_occurs": 1,
                },
            )

        @dataclass
        class RegisterDefinitionRef:
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
