from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class ResetTypeLinks:
    """
    A set of links between internal and external resetTypes defined in the
    typeDefinitions document.

    :ivar reset_type_link: A link between one external reset type and
        one internal resetType.
    """

    class Meta:
        name = "resetTypeLinks"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    reset_type_link: list[ResetTypeLinks.ResetTypeLink] = field(
        default_factory=list,
        metadata={
            "name": "resetTypeLink",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class ResetTypeLink:
        """
        :ivar external_reset_type_reference: Reference to a resetType
            defined in the linked external type definitions.
        :ivar reset_type_reference: Reference to a resetType defined
            internally.
        :ivar vendor_extensions:
        :ivar id:
        """

        external_reset_type_reference: ResetTypeLinks.ResetTypeLink.ExternalResetTypeReference | None = field(
            default=None,
            metadata={
                "name": "externalResetTypeReference",
                "type": "Element",
                "required": True,
            },
        )
        reset_type_reference: ResetTypeLinks.ResetTypeLink.ResetTypeReference | None = field(
            default=None,
            metadata={
                "name": "resetTypeReference",
                "type": "Element",
                "required": True,
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
        class ExternalResetTypeReference:
            """
            :ivar reset_type_ref: Reference to a specific resetType.
            """

            reset_type_ref: str | None = field(
                default=None,
                metadata={
                    "name": "resetTypeRef",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class ResetTypeReference:
            """
            :ivar reset_type_ref: Reference to a specific resetType
            """

            reset_type_ref: str | None = field(
                default=None,
                metadata={
                    "name": "resetTypeRef",
                    "type": "Attribute",
                    "required": True,
                },
            )
