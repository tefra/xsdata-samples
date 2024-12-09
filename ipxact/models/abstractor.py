from dataclasses import dataclass

from ipxact.models.abstractor_type import AbstractorType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Abstractor(AbstractorType):
    """
    This is the root element for abstractors.
    """

    class Meta:
        name = "abstractor"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
