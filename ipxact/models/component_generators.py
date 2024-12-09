from dataclasses import dataclass, field

from ipxact.models.component_generator import ComponentGenerator

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class ComponentGenerators:
    """
    List of component generators.
    """

    class Meta:
        name = "componentGenerators"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    component_generator: list[ComponentGenerator] = field(
        default_factory=list,
        metadata={
            "name": "componentGenerator",
            "type": "Element",
            "min_occurs": 1,
        },
    )
