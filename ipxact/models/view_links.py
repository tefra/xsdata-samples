from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class ViewLinks:
    """
    A set of links between internal and external views defined in the
    typeDefinitions document.

    :ivar view_link: A link between one external view and one internal
        view.
    """

    class Meta:
        name = "viewLinks"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    view_link: list[ViewLinks.ViewLink] = field(
        default_factory=list,
        metadata={
            "name": "viewLink",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class ViewLink:
        """
        :ivar external_view_reference: Reference to a view defined in
            the linked external type definitions.
        :ivar view_reference: Reference to a view defined internally.
        :ivar vendor_extensions:
        :ivar id:
        """

        external_view_reference: (
            ViewLinks.ViewLink.ExternalViewReference | None
        ) = field(
            default=None,
            metadata={
                "name": "externalViewReference",
                "type": "Element",
                "required": True,
            },
        )
        view_reference: ViewLinks.ViewLink.ViewReference | None = field(
            default=None,
            metadata={
                "name": "viewReference",
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
        class ExternalViewReference:
            """
            :ivar view_ref: Reference to a specific view.
            """

            view_ref: str | None = field(
                default=None,
                metadata={
                    "name": "viewRef",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class ViewReference:
            """
            :ivar view_ref: Reference to a specific view.
            """

            view_ref: str | None = field(
                default=None,
                metadata={
                    "name": "viewRef",
                    "type": "Attribute",
                    "required": True,
                },
            )
