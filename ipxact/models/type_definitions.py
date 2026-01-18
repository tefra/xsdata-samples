from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.address_block_definitions import AddressBlockDefinitions
from ipxact.models.assertions import Assertions
from ipxact.models.bank_definitions import BankDefinitions
from ipxact.models.choices import Choices
from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.enumeration_definitions import EnumerationDefinitions
from ipxact.models.external_type_definitions import ExternalTypeDefinitions
from ipxact.models.field_access_policy_definitions import (
    FieldAccessPolicyDefinitions,
)
from ipxact.models.field_definitions import FieldDefinitions
from ipxact.models.memory_map_definitions import MemoryMapDefinitions
from ipxact.models.memory_remap_definitions import MemoryRemapDefinitions
from ipxact.models.parameters import Parameters
from ipxact.models.register_definitions import RegisterDefinitions
from ipxact.models.register_file_definitions import RegisterFileDefinitions
from ipxact.models.short_description import ShortDescription
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class TypeDefinitions:
    """
    :ivar vendor: Name of the vendor who supplies this file.
    :ivar library: Name of the logical library this element belongs to.
    :ivar name: The name of the object.
    :ivar version: Indicates the version of the named element.
    :ivar display_name: Name for display purposes. Typically a few words
        providing a more detailed and/or user-friendly name than the
        vlnv.
    :ivar short_description:
    :ivar description:
    :ivar external_type_definitions:
    :ivar modes: A list of user defined component modes.
    :ivar views: A list of user defined views.
    :ivar field_access_policy_definitions:
    :ivar enumeration_definitions:
    :ivar field_definitions:
    :ivar register_definitions:
    :ivar register_file_definitions:
    :ivar address_block_definitions:
    :ivar bank_definitions:
    :ivar memory_map_definitions:
    :ivar memory_remap_definitions:
    :ivar reset_types: A list of user defined resetTypes applicable to
        this component.
    :ivar choices:
    :ivar parameters:
    :ivar assertions:
    :ivar vendor_extensions:
    :ivar id:
    """

    class Meta:
        name = "typeDefinitions"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    vendor: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    library: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    name: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    version: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    display_name: str | None = field(
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
    external_type_definitions: list[ExternalTypeDefinitions] = field(
        default_factory=list,
        metadata={
            "name": "externalTypeDefinitions",
            "type": "Element",
        },
    )
    modes: TypeDefinitions.Modes | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    views: TypeDefinitions.Views | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    field_access_policy_definitions: FieldAccessPolicyDefinitions | None = (
        field(
            default=None,
            metadata={
                "name": "fieldAccessPolicyDefinitions",
                "type": "Element",
            },
        )
    )
    enumeration_definitions: EnumerationDefinitions | None = field(
        default=None,
        metadata={
            "name": "enumerationDefinitions",
            "type": "Element",
        },
    )
    field_definitions: FieldDefinitions | None = field(
        default=None,
        metadata={
            "name": "fieldDefinitions",
            "type": "Element",
        },
    )
    register_definitions: RegisterDefinitions | None = field(
        default=None,
        metadata={
            "name": "registerDefinitions",
            "type": "Element",
        },
    )
    register_file_definitions: RegisterFileDefinitions | None = field(
        default=None,
        metadata={
            "name": "registerFileDefinitions",
            "type": "Element",
        },
    )
    address_block_definitions: AddressBlockDefinitions | None = field(
        default=None,
        metadata={
            "name": "addressBlockDefinitions",
            "type": "Element",
        },
    )
    bank_definitions: BankDefinitions | None = field(
        default=None,
        metadata={
            "name": "bankDefinitions",
            "type": "Element",
        },
    )
    memory_map_definitions: MemoryMapDefinitions | None = field(
        default=None,
        metadata={
            "name": "memoryMapDefinitions",
            "type": "Element",
        },
    )
    memory_remap_definitions: MemoryRemapDefinitions | None = field(
        default=None,
        metadata={
            "name": "memoryRemapDefinitions",
            "type": "Element",
        },
    )
    reset_types: TypeDefinitions.ResetTypes | None = field(
        default=None,
        metadata={
            "name": "resetTypes",
            "type": "Element",
        },
    )
    choices: Choices | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    parameters: Parameters | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    assertions: Assertions | None = field(
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
    class Modes:
        mode: list[TypeDefinitions.Modes.Mode] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            },
        )

        @dataclass
        class Mode:
            """
            :ivar name: Unique name
            :ivar display_name:
            :ivar short_description:
            :ivar description:
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
    class Views:
        view: list[TypeDefinitions.Views.View] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            },
        )

        @dataclass
        class View:
            """
            :ivar name: Unique name
            :ivar display_name:
            :ivar short_description:
            :ivar description:
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
    class ResetTypes:
        """
        :ivar reset_type: A user defined reset policy
        """

        reset_type: list[TypeDefinitions.ResetTypes.ResetType] = field(
            default_factory=list,
            metadata={
                "name": "resetType",
                "type": "Element",
                "min_occurs": 1,
            },
        )

        @dataclass
        class ResetType:
            """
            :ivar name: Unique name
            :ivar display_name:
            :ivar short_description:
            :ivar description:
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
