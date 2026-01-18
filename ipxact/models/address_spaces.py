from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.address_unit_bits import AddressUnitBits
from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.local_memory_map_type import LocalMemoryMapType
from ipxact.models.parameters import Parameters
from ipxact.models.short_description import ShortDescription
from ipxact.models.unsigned_longint_expression import UnsignedLongintExpression
from ipxact.models.unsigned_positive_int_expression import (
    UnsignedPositiveIntExpression,
)
from ipxact.models.unsigned_positive_longint_expression import (
    UnsignedPositiveLongintExpression,
)
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class AddressSpaces:
    """
    If this component is a bus initiator, this lists all the address spaces
    defined by the component.

    :ivar address_space: This defines a logical space, referenced by a
        bus initiator.
    """

    class Meta:
        name = "addressSpaces"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    address_space: list[AddressSpaces.AddressSpace] = field(
        default_factory=list,
        metadata={
            "name": "addressSpace",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class AddressSpace:
        """
        :ivar name: Unique name
        :ivar display_name:
        :ivar short_description:
        :ivar description:
        :ivar range: The address range of an address block.  Expressed
            as the number of addressable units accessible to the block.
            The range and the width are related by the following
            formulas: number_of_bits_in_block = ipxact:addressUnitBits *
            ipxact:range number_of_rows_in_block =
            number_of_bits_in_block / ipxact:width
        :ivar width: The bit width of a row in the address block. The
            range and the width are related by the following formulas:
            number_of_bits_in_block = ipxact:addressUnitBits *
            ipxact:range number_of_rows_in_block =
            number_of_bits_in_block / ipxact:width
        :ivar segments: Address segments withing an addressSpace
        :ivar address_unit_bits:
        :ivar local_memory_map: Provides the local memory map of an
            address space.  Blocks in this memory map are accessable to
            initiator interfaces on this component that reference this
            address space.   They are not accessable to any external
            initiator interface.
        :ivar parameters: Data specific to this address space.
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
        range: UnsignedPositiveLongintExpression = field(
            metadata={
                "type": "Element",
                "required": True,
            }
        )
        width: UnsignedPositiveIntExpression = field(
            metadata={
                "type": "Element",
                "required": True,
            }
        )
        segments: None | AddressSpaces.AddressSpace.Segments = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        address_unit_bits: None | AddressUnitBits = field(
            default=None,
            metadata={
                "name": "addressUnitBits",
                "type": "Element",
            },
        )
        local_memory_map: None | LocalMemoryMapType = field(
            default=None,
            metadata={
                "name": "localMemoryMap",
                "type": "Element",
            },
        )
        parameters: None | Parameters = field(
            default=None,
            metadata={
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

        @dataclass(kw_only=True)
        class Segments:
            """
            :ivar segment: Address segment withing an addressSpace
            """

            segment: list[AddressSpaces.AddressSpace.Segments.Segment] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

            @dataclass(kw_only=True)
            class Segment:
                """
                :ivar name: Unique name
                :ivar display_name:
                :ivar short_description:
                :ivar description:
                :ivar address_offset: Address offset of the segment
                    within the containing address space.
                :ivar range: The address range of asegment.  Expressed
                    as the number of addressable units accessible to the
                    segment.
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
                address_offset: UnsignedLongintExpression = field(
                    metadata={
                        "name": "addressOffset",
                        "type": "Element",
                        "required": True,
                    }
                )
                range: UnsignedPositiveLongintExpression = field(
                    metadata={
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
