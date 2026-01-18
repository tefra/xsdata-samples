from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.bits_in_lau import BitsInLau
from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.endianess_type import EndianessType
from ipxact.models.indirect_address_ref import IndirectAddressRef
from ipxact.models.indirect_data_ref import IndirectDataRef
from ipxact.models.parameters import Parameters
from ipxact.models.short_description import ShortDescription
from ipxact.models.transparent_bridge import TransparentBridge
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class IndirectInterfaceType:
    """
    Type definition for a indirectInterface in a component.

    :ivar name: Unique name
    :ivar display_name:
    :ivar short_description:
    :ivar description:
    :ivar indirect_address_ref:
    :ivar indirect_data_ref:
    :ivar memory_map_ref: A reference to a memoryMap. This memoryMap is
        indirectly accessible through this interface.
    :ivar transparent_bridge:
    :ivar bits_in_lau:
    :ivar endianness: 'big': means the most significant element of any
        multi-element  data field is stored at the lowest memory
        address. 'little' means the least significant element of any
        multi-element data field is stored at the lowest memory address.
        If this element is not present the default is 'little' endian.
    :ivar parameters:
    :ivar vendor_extensions:
    :ivar id:
    :ivar any_attributes:
    """

    class Meta:
        name = "indirectInterfaceType"

    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        }
    )
    display_name: None | DisplayName = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    short_description: None | ShortDescription = field(
        default=None,
        metadata={
            "name": "shortDescription",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    description: None | Description = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    indirect_address_ref: IndirectAddressRef = field(
        metadata={
            "name": "indirectAddressRef",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        }
    )
    indirect_data_ref: IndirectDataRef = field(
        metadata={
            "name": "indirectDataRef",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        }
    )
    memory_map_ref: None | str = field(
        default=None,
        metadata={
            "name": "memoryMapRef",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    transparent_bridge: list[TransparentBridge] = field(
        default_factory=list,
        metadata={
            "name": "transparentBridge",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    bits_in_lau: None | BitsInLau = field(
        default=None,
        metadata={
            "name": "bitsInLau",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    endianness: None | EndianessType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    parameters: None | Parameters = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    vendor_extensions: None | VendorExtensions = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )
