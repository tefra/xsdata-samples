from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.api_type import ApiType
from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.generator_type_api_service import GeneratorTypeApiService
from ipxact.models.ipxact_uri import IpxactUri
from ipxact.models.parameters import Parameters
from ipxact.models.phase import Phase
from ipxact.models.short_description import ShortDescription
from ipxact.models.transport_method_type import TransportMethodType
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class GeneratorType:
    """
    Types of generators.

    :ivar name: Unique name
    :ivar display_name:
    :ivar short_description:
    :ivar description:
    :ivar phase:
    :ivar parameters:
    :ivar api_type: Indicates the type of API used by the generator.
        Valid value are TGI_2009, TGI_2014_BASE, TGI_2014_EXTENDED,
        TGI_2022_BASE, TGI_2022_EXTENDED, and none. If this element is
        not present, TGI_2022_BASE is assumed. The type TGI_2009
        indicates a generator using the 1685-2009 version of the TGI
        API. The types TGI_2014_BASE and TGI_2014_EXTENDED indicate a
        generator using the 1685-2014 version of the TGI API. Types
        TGI_2009, TGI_2014_BASE, and TGI_2014_EXTENDED are not part of
        the 1685-2022 version of the standard and may not be supported
        by Design Environments
    :ivar api_service: Communication Mechanism. Can be one of SOAP or
        REST (defaults to SOAP)
    :ivar transport_methods:
    :ivar generator_exe: The pathname to the executable file that
        implements the generator
    :ivar vendor_extensions:
    :ivar hidden: If this attribute is true then the generator should
        not be presented to the user, it may be part of a chain and has
        no useful meaning when invoked standalone.
    :ivar id:
    """

    class Meta:
        name = "generatorType"

    name: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    display_name: DisplayName | None = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    short_description: ShortDescription | None = field(
        default=None,
        metadata={
            "name": "shortDescription",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    description: Description | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    phase: Phase | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    parameters: Parameters | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    api_type: GeneratorType.ApiType | None = field(
        default=None,
        metadata={
            "name": "apiType",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    api_service: GeneratorTypeApiService | None = field(
        default=None,
        metadata={
            "name": "apiService",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    transport_methods: GeneratorType.TransportMethods | None = field(
        default=None,
        metadata={
            "name": "transportMethods",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    generator_exe: IpxactUri | None = field(
        default=None,
        metadata={
            "name": "generatorExe",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    vendor_extensions: VendorExtensions | None = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    hidden: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
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
    class ApiType:
        value: ApiType | None = field(
            default=None,
            metadata={
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

    @dataclass
    class TransportMethods:
        """
        :ivar transport_method: Defines a SOAP transport protocol other
            than HTTP which is supported by this generator. The only
            other currently supported protocol is 'file'.
        :ivar id:
        """

        transport_method: GeneratorType.TransportMethods.TransportMethod | None = field(
            default=None,
            metadata={
                "name": "transportMethod",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
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

        @dataclass
        class TransportMethod:
            value: TransportMethodType | None = field(
                default=None,
                metadata={
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
