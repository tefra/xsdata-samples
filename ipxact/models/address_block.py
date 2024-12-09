from dataclasses import dataclass

from ipxact.models.address_block_type import AddressBlockType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class AddressBlock(AddressBlockType):
    """
    This is a single contiguous block of memory inside a memory map.
    """

    class Meta:
        name = "addressBlock"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
