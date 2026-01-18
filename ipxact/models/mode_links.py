from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class ModeLinks:
    """
    A set of links between internal and external modes defined in the
    typeDefinitions document.

    :ivar mode_link: A link between one external mode and one internal
        mode.
    """

    class Meta:
        name = "modeLinks"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    mode_link: list[ModeLinks.ModeLink] = field(
        default_factory=list,
        metadata={
            "name": "modeLink",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class ModeLink:
        """
        :ivar external_mode_reference: Reference to a mode defined in
            the linked external type definitions.
        :ivar mode_reference: Reference to a mode defined internally.
        :ivar vendor_extensions:
        :ivar id:
        """

        external_mode_reference: ModeLinks.ModeLink.ExternalModeReference = (
            field(
                metadata={
                    "name": "externalModeReference",
                    "type": "Element",
                    "required": True,
                }
            )
        )
        mode_reference: ModeLinks.ModeLink.ModeReference = field(
            metadata={
                "name": "modeReference",
                "type": "Element",
                "required": True,
            }
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

        @dataclass(kw_only=True)
        class ExternalModeReference:
            """
            :ivar mode_ref: Reference to a specific mode.
            """

            mode_ref: str = field(
                metadata={
                    "name": "modeRef",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass(kw_only=True)
        class ModeReference:
            """
            :ivar mode_ref: Reference to a specific mode.
            """

            mode_ref: str = field(
                metadata={
                    "name": "modeRef",
                    "type": "Attribute",
                    "required": True,
                }
            )
