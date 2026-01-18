from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.access_policies import AccessPolicies
from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.field_type import FieldType
from ipxact.models.mode_ref import ModeRef
from ipxact.models.parameters import Parameters
from ipxact.models.short_description import ShortDescription
from ipxact.models.simple_access_handle import SimpleAccessHandle
from ipxact.models.vendor_extensions import VendorExtensions
from ipxact.models.volatile import Volatile

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class AlternateRegisters:
    """
    Alternate definitions for the current register.

    :ivar alternate_register: Alternate definition for the current
        register
    """

    class Meta:
        name = "alternateRegisters"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    alternate_register: list[AlternateRegisters.AlternateRegister] = field(
        default_factory=list,
        metadata={
            "name": "alternateRegister",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class AlternateRegister:
        """
        :ivar name: Unique name
        :ivar display_name:
        :ivar short_description:
        :ivar description:
        :ivar access_handles:
        :ivar mode_ref:
        :ivar type_identifier: Identifier name used to indicate that
            multiple register elements contain the exact same
            information for the elements in the
            alternateRegisterDefinitionGroup.
        :ivar volatile:
        :ivar access_policies:
        :ivar field_value: Describes individual bit fields within the
            register.
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
        access_handles: (
            AlternateRegisters.AlternateRegister.AccessHandles | None
        ) = field(
            default=None,
            metadata={
                "name": "accessHandles",
                "type": "Element",
            },
        )
        mode_ref: list[ModeRef] = field(
            default_factory=list,
            metadata={
                "name": "modeRef",
                "type": "Element",
                "min_occurs": 1,
            },
        )
        type_identifier: str | None = field(
            default=None,
            metadata={
                "name": "typeIdentifier",
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
                "min_occurs": 1,
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
