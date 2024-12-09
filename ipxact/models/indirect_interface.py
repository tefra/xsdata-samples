from dataclasses import dataclass

from ipxact.models.indirect_interface_type import IndirectInterfaceType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class IndirectInterface(IndirectInterfaceType):
    """
    Describes one of the bus interfaces supported by this component.
    """

    class Meta:
        name = "indirectInterface"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
