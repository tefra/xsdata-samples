from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.access_policies import AccessPolicies
from ipxact.models.address_unit_bits import AddressUnitBits
from ipxact.models.alternate_registers import AlternateRegisters
from ipxact.models.array import Array
from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.field_type import FieldType
from ipxact.models.parameters import Parameters
from ipxact.models.register_file import RegisterFile
from ipxact.models.short_description import ShortDescription
from ipxact.models.simple_access_handle import SimpleAccessHandle
from ipxact.models.unsigned_longint_expression import UnsignedLongintExpression
from ipxact.models.unsigned_positive_int_expression import (
    UnsignedPositiveIntExpression,
)
from ipxact.models.unsigned_positive_longint_expression import (
    UnsignedPositiveLongintExpression,
)
from ipxact.models.vendor_extensions import VendorExtensions
from ipxact.models.volatile import Volatile

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class RegisterFileDefinitions:
    class Meta:
        name = "registerFileDefinitions"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    register_file_definition: list[
        RegisterFileDefinitions.RegisterFileDefinition
    ] = field(
        default_factory=list,
        metadata={
            "name": "registerFileDefinition",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class RegisterFileDefinition:
        """
        :ivar name: Unique name
        :ivar display_name:
        :ivar short_description:
        :ivar description:
        :ivar type_identifier: Identifier name used to indicate that
            multiple registerFile elements contain the exact same
            information except for the elements in the
            registerFileInstanceGroup.
        :ivar range: The range of a register file.  Expressed as the
            number of addressable units accessible to the block.
            Specified in units of addressUnitBits.
        :ivar access_policies:
        :ivar register: A single register
        :ivar register_file: A structure of registers and register files
        :ivar address_unit_bits:
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
        type_identifier: str | None = field(
            default=None,
            metadata={
                "name": "typeIdentifier",
                "type": "Element",
            },
        )
        range: UnsignedPositiveLongintExpression | None = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        access_policies: AccessPolicies | None = field(
            default=None,
            metadata={
                "name": "accessPolicies",
                "type": "Element",
            },
        )
        register: list[
            RegisterFileDefinitions.RegisterFileDefinition.Register
        ] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        register_file: list[RegisterFile] = field(
            default_factory=list,
            metadata={
                "name": "registerFile",
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
                baseAddress or the containing register file's
                addressOffset, expressed as the number of
                addressUnitBits from the containing memoryMap or
                localMemoryMap.
            :ivar register_definition_ref:
            :ivar type_identifier: Identifier name used to indicate that
                multiple register elements contain the exact same
                information for the elements in the
                registerDefinitionGroup.
            :ivar size: Width of the register in bits.
            :ivar volatile:
            :ivar access_policies:
            :ivar field_value: Describes individual bit fields within
                the register.
            :ivar alternate_registers:
            :ivar parameters:
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
            access_handles: RegisterFileDefinitions.RegisterFileDefinition.Register.AccessHandles | None = field(
                default=None,
                metadata={
                    "name": "accessHandles",
                    "type": "Element",
                },
            )
            array: Array | None = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            address_offset: UnsignedLongintExpression | None = field(
                default=None,
                metadata={
                    "name": "addressOffset",
                    "type": "Element",
                    "required": True,
                },
            )
            register_definition_ref: RegisterFileDefinitions.RegisterFileDefinition.Register.RegisterDefinitionRef | None = field(
                default=None,
                metadata={
                    "name": "registerDefinitionRef",
                    "type": "Element",
                },
            )
            type_identifier: str | None = field(
                default=None,
                metadata={
                    "name": "typeIdentifier",
                    "type": "Element",
                },
            )
            size: UnsignedPositiveIntExpression | None = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            volatile: Volatile | None = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            access_policies: AccessPolicies | None = field(
                default=None,
                metadata={
                    "name": "accessPolicies",
                    "type": "Element",
                },
            )
            field_value: list[FieldType] = field(
                default_factory=list,
                metadata={
                    "name": "field",
                    "type": "Element",
                },
            )
            alternate_registers: AlternateRegisters | None = field(
                default=None,
                metadata={
                    "name": "alternateRegisters",
                    "type": "Element",
                },
            )
            parameters: Parameters | None = field(
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

            @dataclass
            class AccessHandles:
                access_handle: list[SimpleAccessHandle] = field(
                    default_factory=list,
                    metadata={
                        "name": "accessHandle",
                        "type": "Element",
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
