from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.access import Access
from ipxact.models.access_restrictions import AccessRestrictions
from ipxact.models.address_block_ref import AddressBlockRef
from ipxact.models.alternate_register_ref import AlternateRegisterRef
from ipxact.models.bank_ref import BankRef
from ipxact.models.bit_stride import BitStride
from ipxact.models.description import Description
from ipxact.models.dim import Dim
from ipxact.models.display_name import DisplayName
from ipxact.models.enumerated_values import EnumeratedValues
from ipxact.models.field_access_policy_definition_ref import (
    FieldAccessPolicyDefinitionRef,
)
from ipxact.models.field_access_properties_type import (
    FieldAccessPropertiesType,
)
from ipxact.models.field_ref import FieldRef
from ipxact.models.memory_remap_ref import MemoryRemapRef
from ipxact.models.mode_ref import ModeRef
from ipxact.models.modified_write_value import ModifiedWriteValue
from ipxact.models.parameters import Parameters
from ipxact.models.read_action import ReadAction
from ipxact.models.read_response import ReadResponse
from ipxact.models.register_file_ref import RegisterFileRef
from ipxact.models.register_ref import RegisterRef
from ipxact.models.reset import Reset
from ipxact.models.short_description import ShortDescription
from ipxact.models.sliced_access_handle import SlicedAccessHandle
from ipxact.models.testable_test_constraint import TestableTestConstraint
from ipxact.models.unsigned_bit_expression import UnsignedBitExpression
from ipxact.models.unsigned_int_expression import UnsignedIntExpression
from ipxact.models.unsigned_positive_int_expression import (
    UnsignedPositiveIntExpression,
)
from ipxact.models.vendor_extensions import VendorExtensions
from ipxact.models.write_value_constraint import WriteValueConstraint

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class FieldType:
    """
    A field within a register.

    :ivar name: Unique name
    :ivar display_name:
    :ivar short_description:
    :ivar description:
    :ivar access_handles:
    :ivar array:
    :ivar bit_offset: Offset of this field's bit 0 from bit 0 of the
        register.
    :ivar field_definition_ref:
    :ivar type_identifier: Identifier name used to indicate that
        multiple field elements contain the exact same information for
        the elements in the fieldDefinitionGroup.
    :ivar bit_width: Width of the field in bits.
    :ivar volatile: Indicates whether the data is volatile. The presumed
        value is 'false' if not present.
    :ivar resets:
    :ivar alias_of:
    :ivar field_access_policies:
    :ivar enumerated_values:
    :ivar parameters:
    :ivar vendor_extensions:
    :ivar id:
    """

    class Meta:
        name = "fieldType"

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
    access_handles: Optional["FieldType.AccessHandles"] = field(
        default=None,
        metadata={
            "name": "accessHandles",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    array: Optional["FieldType.Array"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    bit_offset: Optional[UnsignedIntExpression] = field(
        default=None,
        metadata={
            "name": "bitOffset",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    field_definition_ref: Optional["FieldType.FieldDefinitionRef"] = field(
        default=None,
        metadata={
            "name": "fieldDefinitionRef",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    type_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "typeIdentifier",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    bit_width: Optional[UnsignedPositiveIntExpression] = field(
        default=None,
        metadata={
            "name": "bitWidth",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    volatile: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    resets: Optional["FieldType.Resets"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    alias_of: Optional["FieldType.AliasOf"] = field(
        default=None,
        metadata={
            "name": "aliasOf",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    field_access_policies: Optional["FieldType.FieldAccessPolicies"] = field(
        default=None,
        metadata={
            "name": "fieldAccessPolicies",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    enumerated_values: Optional[EnumeratedValues] = field(
        default=None,
        metadata={
            "name": "enumeratedValues",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    parameters: Optional[Parameters] = field(
        default=None,
        metadata={
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
    class Array:
        dim: list[Dim] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "min_occurs": 1,
            },
        )
        bit_stride: Optional[BitStride] = field(
            default=None,
            metadata={
                "name": "bitStride",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )

    @dataclass
    class FieldDefinitionRef:
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

    @dataclass
    class Resets:
        """
        :ivar reset: BitField reset value
        """

        reset: list[Reset] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "min_occurs": 1,
            },
        )

    @dataclass
    class AliasOf:
        address_space_ref: Optional["FieldType.AliasOf.AddressSpaceRef"] = (
            field(
                default=None,
                metadata={
                    "name": "addressSpaceRef",
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                },
            )
        )
        memory_map_ref: Optional["FieldType.AliasOf.MemoryMapRef"] = field(
            default=None,
            metadata={
                "name": "memoryMapRef",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )
        memory_remap_ref: Optional[MemoryRemapRef] = field(
            default=None,
            metadata={
                "name": "memoryRemapRef",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )
        bank_ref: list[BankRef] = field(
            default_factory=list,
            metadata={
                "name": "bankRef",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )
        address_block_ref: Optional[AddressBlockRef] = field(
            default=None,
            metadata={
                "name": "addressBlockRef",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )
        register_file_ref: list[RegisterFileRef] = field(
            default_factory=list,
            metadata={
                "name": "registerFileRef",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )
        register_ref: Optional[RegisterRef] = field(
            default=None,
            metadata={
                "name": "registerRef",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )
        alternate_register_ref: Optional[AlternateRegisterRef] = field(
            default=None,
            metadata={
                "name": "alternateRegisterRef",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )
        field_ref: Optional[FieldRef] = field(
            default=None,
            metadata={
                "name": "fieldRef",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "required": True,
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
    class FieldAccessPolicies(FieldAccessPropertiesType):
        field_access_policy: list[
            "FieldType.FieldAccessPolicies.FieldAccessPolicy"
        ] = field(
            default_factory=list,
            metadata={
                "name": "fieldAccessPolicy",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "min_occurs": 1,
            },
        )

        @dataclass
        class FieldAccessPolicy:
            """
            :ivar mode_ref:
            :ivar field_access_policy_definition_ref:
            :ivar access:
            :ivar modified_write_value:
            :ivar write_value_constraint:
            :ivar read_action:
            :ivar read_response:
            :ivar broadcasts:
            :ivar access_restrictions: Access restrictions
            :ivar testable: Can the field be tested with an automated
                register test routine. The presumed value is true if not
                specified.
            :ivar reserved: Indicates that the field should be
                documented as reserved. The presumed value is '0' if not
                present.
            :ivar vendor_extensions:
            :ivar id:
            """

            mode_ref: list[ModeRef] = field(
                default_factory=list,
                metadata={
                    "name": "modeRef",
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                },
            )
            field_access_policy_definition_ref: Optional[
                FieldAccessPolicyDefinitionRef
            ] = field(
                default=None,
                metadata={
                    "name": "fieldAccessPolicyDefinitionRef",
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                },
            )
            access: Optional[Access] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                },
            )
            modified_write_value: Optional[ModifiedWriteValue] = field(
                default=None,
                metadata={
                    "name": "modifiedWriteValue",
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                },
            )
            write_value_constraint: Optional[WriteValueConstraint] = field(
                default=None,
                metadata={
                    "name": "writeValueConstraint",
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                },
            )
            read_action: Optional[ReadAction] = field(
                default=None,
                metadata={
                    "name": "readAction",
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                },
            )
            read_response: Optional[ReadResponse] = field(
                default=None,
                metadata={
                    "name": "readResponse",
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                },
            )
            broadcasts: Optional[
                "FieldType.FieldAccessPolicies.FieldAccessPolicy.Broadcasts"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                },
            )
            access_restrictions: Optional[AccessRestrictions] = field(
                default=None,
                metadata={
                    "name": "accessRestrictions",
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                },
            )
            testable: Optional[
                "FieldType.FieldAccessPolicies.FieldAccessPolicy.Testable"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                },
            )
            reserved: Optional[UnsignedBitExpression] = field(
                default=None,
                metadata={
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
            class Broadcasts:
                broadcast_to: list[
                    "FieldType.FieldAccessPolicies.FieldAccessPolicy.Broadcasts.BroadcastTo"
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "broadcastTo",
                        "type": "Element",
                        "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                        "min_occurs": 1,
                    },
                )

                @dataclass
                class BroadcastTo:
                    address_space_ref: Optional[
                        "FieldType.FieldAccessPolicies.FieldAccessPolicy.Broadcasts.BroadcastTo.AddressSpaceRef"
                    ] = field(
                        default=None,
                        metadata={
                            "name": "addressSpaceRef",
                            "type": "Element",
                            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                        },
                    )
                    memory_map_ref: Optional[
                        "FieldType.FieldAccessPolicies.FieldAccessPolicy.Broadcasts.BroadcastTo.MemoryMapRef"
                    ] = field(
                        default=None,
                        metadata={
                            "name": "memoryMapRef",
                            "type": "Element",
                            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                        },
                    )
                    memory_remap_ref: Optional[MemoryRemapRef] = field(
                        default=None,
                        metadata={
                            "name": "memoryRemapRef",
                            "type": "Element",
                            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                        },
                    )
                    bank_ref: list[BankRef] = field(
                        default_factory=list,
                        metadata={
                            "name": "bankRef",
                            "type": "Element",
                            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                        },
                    )
                    address_block_ref: Optional[AddressBlockRef] = field(
                        default=None,
                        metadata={
                            "name": "addressBlockRef",
                            "type": "Element",
                            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                        },
                    )
                    register_file_ref: list[RegisterFileRef] = field(
                        default_factory=list,
                        metadata={
                            "name": "registerFileRef",
                            "type": "Element",
                            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                        },
                    )
                    register_ref: Optional[RegisterRef] = field(
                        default=None,
                        metadata={
                            "name": "registerRef",
                            "type": "Element",
                            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                        },
                    )
                    alternate_register_ref: Optional[AlternateRegisterRef] = (
                        field(
                            default=None,
                            metadata={
                                "name": "alternateRegisterRef",
                                "type": "Element",
                                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                            },
                        )
                    )
                    field_ref: Optional[FieldRef] = field(
                        default=None,
                        metadata={
                            "name": "fieldRef",
                            "type": "Element",
                            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
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
            class Testable:
                """
                :ivar value:
                :ivar test_constraint: Constraint for an automated
                    register test routine. 'unconstrained' (default)
                    means may read and write all legal values. 'restore'
                    means may read and write legal values but the value
                    must be restored to the initially read value before
                    accessing another register. 'writeAsRead' has
                    limitations on testability where only the value read
                    before a write may be written to the field.
                    'readOnly' has limitations on testability where
                    values may only be read from the field.
                """

                value: Optional[bool] = field(
                    default=None,
                    metadata={
                        "required": True,
                    },
                )
                test_constraint: TestableTestConstraint = field(
                    default=TestableTestConstraint.UNCONSTRAINED,
                    metadata={
                        "name": "testConstraint",
                        "type": "Attribute",
                    },
                )
