from __future__ import annotations

from dataclasses import dataclass

from ipxact.models.instance_generator_type import InstanceGeneratorType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class ComponentGenerator(InstanceGeneratorType):
    """
    Specifies a set of component generators.

    The scope attribute applies to component generators and specifies
    whether the generator should be run for each instance of the entity (or
    module) or just once for all instances of the entity.
    """

    class Meta:
        name = "componentGenerator"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
