from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.access_policies import AccessPolicies
from ipxact.models.alternate_registers import AlternateRegisters
from ipxact.models.array import Array
from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.field_type import FieldType
from ipxact.models.parameters import Parameters
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


@dataclass(kw_only=True)
class RegisterFile:
    """
    A structure of registers and register files.

    :ivar name: Unique name
    :ivar display_name:
    :ivar short_description:
    :ivar description:
    :ivar access_handles:
    :ivar array:
    :ivar address_offset: Offset from the address block's baseAddress or
        the containing register file's addressOffset, expressed as the
        number of addressUnitBits from the containing memoryMap or
        localMemoryMap.
    :ivar register_file_definition_ref:
    :ivar type_identifier: Identifier name used to indicate that
        multiple registerFile elements contain the exact same
        information except for the elements in the
        registerFileInstanceGroup.
    :ivar range: The range of a register file.  Expressed as the number
        of addressable units accessible to the block. Specified in units
        of addressUnitBits.
    :ivar access_policies:
    :ivar register: A single register
    :ivar register_file: A structure of registers and register files
    :ivar parameters:
    :ivar vendor_extensions:
    :ivar id:
    """

    class Meta:
        name = "registerFile"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

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
    access_handles: None | RegisterFile.AccessHandles = field(
        default=None,
        metadata={
            "name": "accessHandles",
            "type": "Element",
        },
    )
    array: None | Array = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    address_offset: UnsignedLongintExpression = field(
        metadata={
            "name": "addressOffset",
            "type": "Element",
            "required": True,
        }
    )
    register_file_definition_ref: (
        None | RegisterFile.RegisterFileDefinitionRef
    ) = field(
        default=None,
        metadata={
            "name": "registerFileDefinitionRef",
            "type": "Element",
        },
    )
    type_identifier: None | str = field(
        default=None,
        metadata={
            "name": "typeIdentifier",
            "type": "Element",
        },
    )
    range: None | UnsignedPositiveLongintExpression = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    access_policies: None | AccessPolicies = field(
        default=None,
        metadata={
            "name": "accessPolicies",
            "type": "Element",
        },
    )
    register: list[RegisterFile.Register] = field(
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
    parameters: None | Parameters = field(
        default=None,
        metadata={
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

    @dataclass(kw_only=True)
    class AccessHandles:
        access_handle: list[SimpleAccessHandle] = field(
            default_factory=list,
            metadata={
                "name": "accessHandle",
                "type": "Element",
                "min_occurs": 1,
            },
        )

    @dataclass(kw_only=True)
    class RegisterFileDefinitionRef:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        type_definitions: str = field(
            metadata={
                "name": "typeDefinitions",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
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
        access_handles: None | RegisterFile.Register.AccessHandles = field(
            default=None,
            metadata={
                "name": "accessHandles",
                "type": "Element",
            },
        )
        array: None | Array = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        address_offset: UnsignedLongintExpression = field(
            metadata={
                "name": "addressOffset",
                "type": "Element",
                "required": True,
            }
        )
        register_definition_ref: (
            None | RegisterFile.Register.RegisterDefinitionRef
        ) = field(
            default=None,
            metadata={
                "name": "registerDefinitionRef",
                "type": "Element",
            },
        )
        type_identifier: None | str = field(
            default=None,
            metadata={
                "name": "typeIdentifier",
                "type": "Element",
            },
        )
        size: None | UnsignedPositiveIntExpression = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        volatile: None | Volatile = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        access_policies: None | AccessPolicies = field(
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
        alternate_registers: None | AlternateRegisters = field(
            default=None,
            metadata={
                "name": "alternateRegisters",
                "type": "Element",
            },
        )
        parameters: None | Parameters = field(
            default=None,
            metadata={
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

        @dataclass(kw_only=True)
        class AccessHandles:
            access_handle: list[SimpleAccessHandle] = field(
                default_factory=list,
                metadata={
                    "name": "accessHandle",
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

        @dataclass(kw_only=True)
        class RegisterDefinitionRef:
            value: str = field(
                default="",
                metadata={
                    "required": True,
                },
            )
            type_definitions: str = field(
                metadata={
                    "name": "typeDefinitions",
                    "type": "Attribute",
                    "required": True,
                }
            )
