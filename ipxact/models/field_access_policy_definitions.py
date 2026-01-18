from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.access import Access
from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.modified_write_value import ModifiedWriteValue
from ipxact.models.read_action import ReadAction
from ipxact.models.read_response import ReadResponse
from ipxact.models.short_description import ShortDescription
from ipxact.models.vendor_extensions import VendorExtensions
from ipxact.models.write_value_constraint import WriteValueConstraint

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class FieldAccessPolicyDefinitions:
    class Meta:
        name = "fieldAccessPolicyDefinitions"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    field_access_policy_definition: list[
        FieldAccessPolicyDefinitions.FieldAccessPolicyDefinition
    ] = field(
        default_factory=list,
        metadata={
            "name": "fieldAccessPolicyDefinition",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class FieldAccessPolicyDefinition:
        """
        :ivar name: Unique name
        :ivar display_name:
        :ivar short_description:
        :ivar description:
        :ivar access:
        :ivar modified_write_value:
        :ivar write_value_constraint:
        :ivar read_action:
        :ivar read_response:
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
