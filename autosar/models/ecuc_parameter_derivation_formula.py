from dataclasses import dataclass, field
from typing import List, Optional, Type
from .ecuc_query_subtypes_enum import EcucQuerySubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EcucParameterDerivationFormula:
    """
    This formula is intended to specify how an ecu parameter can be derived
    from other information in the Autosar Templates.

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
    :ivar content:
    """
    class Meta:
        name = "ECUC-PARAMETER-DERIVATION-FORMULA"

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
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ECUC-QUERY-REF",
                    "type": Type["EcucParameterDerivationFormula.EcucQueryRef"],
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "ECUC-QUERY-STRING-REF",
                    "type": Type["EcucParameterDerivationFormula.EcucQueryStringRef"],
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            ),
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
