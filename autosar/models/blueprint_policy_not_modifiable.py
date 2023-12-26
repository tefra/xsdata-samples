from dataclasses import dataclass, field
from typing import Optional
from .string import String

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class BlueprintPolicyNotModifiable:
    """
    The class represents that the related attribute is not modifiable during the
    blueprinting.

    :ivar attribute_name: This identifies the related attribute of a
        BlueprintPolicy. For navigation over the model a subset of xpath
        expressions is used.
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
        name = "BLUEPRINT-POLICY-NOT-MODIFIABLE"

    attribute_name: Optional[String] = field(
        default=None,
        metadata={
            "name": "ATTRIBUTE-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
