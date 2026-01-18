from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.enumerated_value_type import EnumeratedValueType
from ipxact.models.short_description import ShortDescription
from ipxact.models.unsigned_positive_int_expression import (
    UnsignedPositiveIntExpression,
)
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class EnumerationDefinitions:
    class Meta:
        name = "enumerationDefinitions"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    enumeration_definition: list[
        EnumerationDefinitions.EnumerationDefinition
    ] = field(
        default_factory=list,
        metadata={
            "name": "enumerationDefinition",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class EnumerationDefinition:
        """
        :ivar name: Unique name
        :ivar display_name:
        :ivar short_description:
        :ivar description:
        :ivar width: Definition width used to resolve the value.
        :ivar enumerated_value: Enumerates specific values that can be
            assigned to the bit field. The name of this enumerated
            value. This may be used as a token in generating code.
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
        width: UnsignedPositiveIntExpression | None = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        enumerated_value: list[EnumeratedValueType] = field(
            default_factory=list,
            metadata={
                "name": "enumeratedValue",
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
