from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.generator_type import GeneratorType
from ipxact.models.instance_generator_type_scope import (
    InstanceGeneratorTypeScope,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class InstanceGeneratorType(GeneratorType):
    """
    :ivar group: An identifier to specify the generator group. This is
        used by generator chains for selecting which generators to run.
    :ivar scope: The scope attribute applies to component generators and
        specifies whether the generator should be run for each instance
        of the entity (or module) or just once for all instances of the
        entity.
    """

    class Meta:
        name = "instanceGeneratorType"

    group: list[InstanceGeneratorType.Group] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    scope: InstanceGeneratorTypeScope = field(
        default=InstanceGeneratorTypeScope.INSTANCE,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class Group:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        id: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )
