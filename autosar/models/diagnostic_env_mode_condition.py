from dataclasses import dataclass, field
from typing import Optional
from .diagnostic_compare_type_enum import DiagnosticCompareTypeEnum
from .diagnostic_env_mode_element_subtypes_enum import DiagnosticEnvModeElementSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DiagnosticEnvModeCondition:
    """DiagnosticEnvModeCondition are atomic condition based on the comparison
    of the active ModeDeclaration in a ModeDeclarationGroupProtoype with the
    constant value of a ModeDeclaration.

    The formulation of this condition uses only one
    DiagnosticEnvElement, which contains enough information to deduce
    the variable part (i.e. the part that changes at runtime) as well as
    the constant part of the comparison. Only
    DiagnosticCompareTypeEnum.isEqual or
    DiagnosticCompareTypeEnum.isNotEqual are eligible values for
    DiagnosticAtomicCondition.compareType.

    :ivar compare_type: This attributes represents the concrete type of
        the comparison.
    :ivar mode_element_ref: This reference represents both the
        ModeDeclarationGroupPrototype and the ModeDeclaration relevant
        for the mode comparison.
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
        name = "DIAGNOSTIC-ENV-MODE-CONDITION"

    compare_type: Optional[DiagnosticCompareTypeEnum] = field(
        default=None,
        metadata={
            "name": "COMPARE-TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    mode_element_ref: Optional["DiagnosticEnvModeCondition.ModeElementRef"] = field(
        default=None,
        metadata={
            "name": "MODE-ELEMENT-REF",
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
    class ModeElementRef(Ref):
        dest: Optional[DiagnosticEnvModeElementSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
