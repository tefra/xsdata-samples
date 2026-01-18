from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.complex_tied_value_expression import (
    ComplexTiedValueExpression,
)
from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.external_port_reference import ExternalPortReference
from ipxact.models.part_select import PartSelect
from ipxact.models.short_description import ShortDescription
from ipxact.models.sub_port_reference import SubPortReference
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class AdHocConnection:
    """
    Represents an ad-hoc connection between component ports.

    :ivar name: Unique name
    :ivar display_name:
    :ivar short_description:
    :ivar description:
    :ivar tied_value: The logic value of this connection. The value can
        be an unsigned bit vector expression or the string values 'open'
        or 'default'. Only valid for ports of style wire.
    :ivar port_references: Liist of internal and external port
        references involved in the adhocConnection
    :ivar vendor_extensions:
    :ivar id:
    """

    class Meta:
        name = "adHocConnection"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    name: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "collapse",
            "pattern": r"\i[\p{L}\p{N}\.\-:_]*",
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
    tied_value: ComplexTiedValueExpression | None = field(
        default=None,
        metadata={
            "name": "tiedValue",
            "type": "Element",
        },
    )
    port_references: AdHocConnection.PortReferences | None = field(
        default=None,
        metadata={
            "name": "portReferences",
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
    class PortReferences:
        """
        :ivar internal_port_reference: Defines a reference to a port on
            a component contained within the design.
        :ivar external_port_reference:
        """

        internal_port_reference: list[
            AdHocConnection.PortReferences.InternalPortReference
        ] = field(
            default_factory=list,
            metadata={
                "name": "internalPortReference",
                "type": "Element",
                "min_occurs": 1,
            },
        )
        external_port_reference: list[ExternalPortReference] = field(
            default_factory=list,
            metadata={
                "name": "externalPortReference",
                "type": "Element",
                "min_occurs": 1,
                "sequence": 1,
            },
        )

        @dataclass
        class InternalPortReference:
            """
            :ivar sub_port_reference:
            :ivar part_select:
            :ivar vendor_extensions:
            :ivar port_ref: A port on the on the referenced component
                from componentInterfaceRef.
            :ivar component_instance_ref: A reference to the
                instanceName element of a component in this design.
            :ivar id:
            """

            sub_port_reference: list[SubPortReference] = field(
                default_factory=list,
                metadata={
                    "name": "subPortReference",
                    "type": "Element",
                },
            )
            part_select: PartSelect | None = field(
                default=None,
                metadata={
                    "name": "partSelect",
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
            port_ref: str | None = field(
                default=None,
                metadata={
                    "name": "portRef",
                    "type": "Attribute",
                    "required": True,
                    "white_space": "collapse",
                    "pattern": r"\i[\p{L}\p{N}\.\-:_]*",
                },
            )
            component_instance_ref: str | None = field(
                default=None,
                metadata={
                    "name": "componentInstanceRef",
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
