from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.configurable_element_values import ConfigurableElementValues

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class ConfigurableLibraryRefType:
    """
    Base IP-XACT document reference type for configurable top-level
    objects.

    Contains vendor, library, name and version attributes along with
    configurable element values.
    """

    class Meta:
        name = "configurableLibraryRefType"

    configurable_element_values: ConfigurableElementValues | None = field(
        default=None,
        metadata={
            "name": "configurableElementValues",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    vendor: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    library: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
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
