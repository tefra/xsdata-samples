from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.access_policies import AccessPolicies
from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.field_type import FieldType
from ipxact.models.short_description import ShortDescription
from ipxact.models.unsigned_positive_int_expression import (
    UnsignedPositiveIntExpression,
)
from ipxact.models.vendor_extensions import VendorExtensions
from ipxact.models.volatile import Volatile

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class RegisterDefinitions:
    class Meta:
        name = "registerDefinitions"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    register_definition: list[RegisterDefinitions.RegisterDefinition] = (
        field(
            default_factory=list,
            metadata={
                "name": "registerDefinition",
                "type": "Element",
                "min_occurs": 1,
            },
        )
    )

    @dataclass
    class RegisterDefinition:
        """
        :ivar name: Unique name
        :ivar display_name:
        :ivar short_description:
        :ivar description:
        :ivar type_identifier: Identifier name used to indicate that
            multiple register elements contain the exact same
            information for the elements in the registerDefinitionGroup.
        :ivar size: Width of the register in bits.
        :ivar volatile:
        :ivar access_policies:
        :ivar field_value: Describes individual bit fields within the
            register.
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
        size: UnsignedPositiveIntExpression | None = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
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
