from dataclasses import dataclass

from ipxact.models.generator_type import GeneratorType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Generator(GeneratorType):
    """
    Specifies a set of generators.
    """

    class Meta:
        name = "generator"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
