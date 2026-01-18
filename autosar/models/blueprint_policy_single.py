from dataclasses import dataclass, field
from typing import Optional

from .admin_data import DocumentationBlock
from .string import String

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class BlueprintPolicySingle:
    """
    The class represents that the related attribute is modifiable during
    the blueprinting.

    It applies only to attribute with upper multiplicity equal 1.

    :ivar attribute_name: This identifies the related attribute of a
        BlueprintPolicy. For navigation over the model a subset of xpath
        expressions is used.
    :ivar blueprint_derivation_guide: This role offers the possibility
        to give addtional information to the policy.
    :ivar s: Checksum calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine if
        an ArObject has changed. The checksum has no semantic meaning
        for an AUTOSAR model and there is no requirement for AUTOSAR
        tools to manage the checksum.
    :ivar t: Timestamp calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine
        the last change of an ArObject. The timestamp has no semantic
        meaning for an AUTOSAR model and there is no requirement for
        AUTOSAR tools to manage the timestamp.
    """

    class Meta:
        name = "BLUEPRINT-POLICY-SINGLE"

    attribute_name: String | None = field(
        default=None,
        metadata={
            "name": "ATTRIBUTE-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    blueprint_derivation_guide: DocumentationBlock | None = field(
        default=None,
        metadata={
            "name": "BLUEPRINT-DERIVATION-GUIDE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: str | None = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: str | None = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
