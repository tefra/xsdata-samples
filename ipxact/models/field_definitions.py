from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.access import Access
from ipxact.models.access_restrictions import AccessRestrictions
from ipxact.models.address_block_ref import AddressBlockRef
from ipxact.models.alternate_register_ref import AlternateRegisterRef
from ipxact.models.bank_ref import BankRef
from ipxact.models.description import Description
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
from ipxact.models.read_action import ReadAction
from ipxact.models.read_response import ReadResponse
from ipxact.models.register_file_ref import RegisterFileRef
from ipxact.models.register_ref import RegisterRef
from ipxact.models.reset import Reset
from ipxact.models.short_description import ShortDescription
from ipxact.models.testable_test_constraint import TestableTestConstraint
from ipxact.models.unsigned_bit_expression import UnsignedBitExpression
from ipxact.models.unsigned_positive_int_expression import (
    UnsignedPositiveIntExpression,
)
from ipxact.models.vendor_extensions import VendorExtensions
from ipxact.models.write_value_constraint import WriteValueConstraint

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class FieldDefinitions:
    class Meta:
        name = "fieldDefinitions"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    field_definition: list[FieldDefinitions.FieldDefinition] = field(
        default_factory=list,
        metadata={
            "name": "fieldDefinition",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class FieldDefinition:
        """
        :ivar name: Unique name
        :ivar display_name:
        :ivar short_description:
        :ivar description:
        :ivar type_identifier: Identifier name used to indicate that
            multiple field elements contain the exact same information
            for the elements in the fieldDefinitionGroup.
        :ivar bit_width: Width of the field in bits.
        :ivar volatile: Indicates whether the data is volatile. The
            presumed value is 'false' if not present.
        :ivar resets:
        :ivar field_access_policies:
        :ivar enumerated_values:
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
        bit_width: UnsignedPositiveIntExpression | None = field(
            default=None,
            metadata={
                "name": "bitWidth",
                "type": "Element",
                "required": True,
            },
        )
        volatile: bool | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        resets: FieldDefinitions.FieldDefinition.Resets | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        field_access_policies: FieldDefinitions.FieldDefinition.FieldAccessPolicies | None = field(
            default=None,
            metadata={
                "name": "fieldAccessPolicies",
                "type": "Element",
            },
        )
        enumerated_values: EnumeratedValues | None = field(
            default=None,
            metadata={
                "name": "enumeratedValues",
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
        class Resets:
            """
            :ivar reset: BitField reset value
            """

            reset: list[Reset] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

        @dataclass
        class FieldAccessPolicies(FieldAccessPropertiesType):
            field_access_policy: list[
                FieldDefinitions.FieldDefinition.FieldAccessPolicies.FieldAccessPolicy
            ] = field(
                default_factory=list,
                metadata={
                    "name": "fieldAccessPolicy",
                    "type": "Element",
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
                :ivar testable: Can the field be tested with an
                    automated register test routine. The presumed value
                    is true if not specified.
                :ivar reserved: Indicates that the field should be
                    documented as reserved. The presumed value is '0' if
                    not present.
                :ivar vendor_extensions:
                :ivar id:
                """

                mode_ref: list[ModeRef] = field(
                    default_factory=list,
                    metadata={
                        "name": "modeRef",
                        "type": "Element",
                    },
                )
                field_access_policy_definition_ref: FieldAccessPolicyDefinitionRef | None = field(
                    default=None,
                    metadata={
                        "name": "fieldAccessPolicyDefinitionRef",
                        "type": "Element",
                    },
                )
                access: Access | None = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                modified_write_value: ModifiedWriteValue | None = field(
                    default=None,
                    metadata={
                        "name": "modifiedWriteValue",
                        "type": "Element",
                    },
                )
                write_value_constraint: WriteValueConstraint | None = field(
                    default=None,
                    metadata={
                        "name": "writeValueConstraint",
                        "type": "Element",
                    },
                )
                read_action: ReadAction | None = field(
                    default=None,
                    metadata={
                        "name": "readAction",
                        "type": "Element",
                    },
                )
                read_response: ReadResponse | None = field(
                    default=None,
                    metadata={
                        "name": "readResponse",
                        "type": "Element",
                    },
                )
                broadcasts: FieldDefinitions.FieldDefinition.FieldAccessPolicies.FieldAccessPolicy.Broadcasts | None = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                access_restrictions: AccessRestrictions | None = field(
                    default=None,
                    metadata={
                        "name": "accessRestrictions",
                        "type": "Element",
                    },
                )
                testable: FieldDefinitions.FieldDefinition.FieldAccessPolicies.FieldAccessPolicy.Testable | None = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                reserved: UnsignedBitExpression | None = field(
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
                class Broadcasts:
                    broadcast_to: list[
                        FieldDefinitions.FieldDefinition.FieldAccessPolicies.FieldAccessPolicy.Broadcasts.BroadcastTo
                    ] = field(
                        default_factory=list,
                        metadata={
                            "name": "broadcastTo",
                            "type": "Element",
                            "min_occurs": 1,
                        },
                    )

                    @dataclass
                    class BroadcastTo:
                        address_space_ref: FieldDefinitions.FieldDefinition.FieldAccessPolicies.FieldAccessPolicy.Broadcasts.BroadcastTo.AddressSpaceRef | None = field(
                            default=None,
                            metadata={
                                "name": "addressSpaceRef",
                                "type": "Element",
                            },
                        )
                        memory_map_ref: FieldDefinitions.FieldDefinition.FieldAccessPolicies.FieldAccessPolicy.Broadcasts.BroadcastTo.MemoryMapRef | None = field(
                            default=None,
                            metadata={
                                "name": "memoryMapRef",
                                "type": "Element",
                            },
                        )
                        memory_remap_ref: MemoryRemapRef | None = field(
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
                        address_block_ref: AddressBlockRef | None = field(
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
                        register_ref: RegisterRef | None = field(
                            default=None,
                            metadata={
                                "name": "registerRef",
                                "type": "Element",
                            },
                        )
                        alternate_register_ref: AlternateRegisterRef | None = field(
                            default=None,
                            metadata={
                                "name": "alternateRegisterRef",
                                "type": "Element",
                            },
                        )
                        field_ref: FieldRef | None = field(
                            default=None,
                            metadata={
                                "name": "fieldRef",
                                "type": "Element",
                                "required": True,
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
                        class AddressSpaceRef:
                            address_space_ref: str | None = field(
                                default=None,
                                metadata={
                                    "name": "addressSpaceRef",
                                    "type": "Attribute",
                                    "required": True,
                                },
                            )

                        @dataclass
                        class MemoryMapRef:
                            memory_map_ref: str | None = field(
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
                        means may read and write all legal values.
                        'restore' means may read and write legal values
                        but the value must be restored to the initially
                        read value before accessing another register.
                        'writeAsRead' has limitations on testability
                        where only the value read before a write may be
                        written to the field. 'readOnly' has limitations
                        on testability where values may only be read
                        from the field.
                    """

                    value: bool | None = field(
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
