from __future__ import annotations

from dataclasses import dataclass, field

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


@dataclass(kw_only=True)
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

    @dataclass(kw_only=True)
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
        access: None | Access = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        modified_write_value: None | ModifiedWriteValue = field(
            default=None,
            metadata={
                "name": "modifiedWriteValue",
                "type": "Element",
            },
        )
        write_value_constraint: None | WriteValueConstraint = field(
            default=None,
            metadata={
                "name": "writeValueConstraint",
                "type": "Element",
            },
        )
        read_action: None | ReadAction = field(
            default=None,
            metadata={
                "name": "readAction",
                "type": "Element",
            },
        )
        read_response: None | ReadResponse = field(
            default=None,
            metadata={
                "name": "readResponse",
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
