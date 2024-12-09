from dataclasses import dataclass

from ipxact.models.component_type import ComponentType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Component(ComponentType):
    """
    This is the root element for all non platform-core components.
    """

    class Meta:
        name = "component"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
