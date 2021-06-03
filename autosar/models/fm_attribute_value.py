from dataclasses import dataclass, field
from typing import Optional
from autosar.models.fm_attribute_def_subtypes_enum import FmAttributeDefSubtypesEnum
from autosar.models.numerical_value import NumericalValue
from autosar.models.ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class FmAttributeValue:
    """
    This defines a value for the attribute that is referred to in the role
    definition.

    :ivar definition_ref: This refers to the definition of this
        attribute.
    :ivar value: This represents the value of this attribute.
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
        name = "FM-ATTRIBUTE-VALUE"

    definition_ref: Optional["FmAttributeValue.DefinitionRef"] = field(
        default=None,
        metadata={
            "name": "DEFINITION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    value: Optional[NumericalValue] = field(
        default=None,
        metadata={
            "name": "VALUE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        }
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        }
    )

    @dataclass
    class DefinitionRef(Ref):
        dest: Optional[FmAttributeDefSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
