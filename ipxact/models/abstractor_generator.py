from dataclasses import dataclass

from ipxact.models.instance_generator_type import InstanceGeneratorType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class AbstractorGenerator(InstanceGeneratorType):
    """
    Specifies a set of abstractor generators.

    The scope attribute applies to abstractor generators and specifies
    whether the generator should be run for each instance of the entity (or
    module) or just once for all instances of the entity.
    """

    class Meta:
        name = "abstractorGenerator"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
