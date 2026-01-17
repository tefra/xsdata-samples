from dataclasses import dataclass

from ipxact.models.subspace_ref_type import SubspaceRefType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class SubspaceMap(SubspaceRefType):
    """
    Maps in an address subspace from across a bus bridge.

    Its initiatorRef attribute refers by name to the initiator bus
    interface on the other side of the bridge. It must match the
    initiatorRef attribute of a bridge element on the target interface, and
    that bridge element must be designated as opaque.
    """

    class Meta:
        name = "subspaceMap"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
