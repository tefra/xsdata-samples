from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.ecuc_query_subtypes_enum import EcucQuerySubtypesEnum
from autosar.models.ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EcucConditionFormula:
    """This formula shall yield a boolean expression depending on ecuc queries.

    Note that the EcucConditionFormula is a mixed string. Therefore, the
    properties have the upper multiplicity 1.

    :ivar content:
    :ivar ecuc_query_ref: The EcucQuery serves as a argument for the
        formula.
    :ivar ecuc_query_string_ref: This indicates that the referenced
        query shall return a string.
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
        name = "ECUC-CONDITION-FORMULA"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    ecuc_query_ref: List["EcucConditionFormula.EcucQueryRef"] = field(
        default_factory=list,
        metadata={
            "name": "ECUC-QUERY-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    ecuc_query_string_ref: List["EcucConditionFormula.EcucQueryStringRef"] = field(
        default_factory=list,
        metadata={
            "name": "ECUC-QUERY-STRING-REF",
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
    class EcucQueryRef(Ref):
        dest: Optional[EcucQuerySubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class EcucQueryStringRef(Ref):
        dest: Optional[EcucQuerySubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )