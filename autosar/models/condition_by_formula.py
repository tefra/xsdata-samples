from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.binding_time_enum_simple import BindingTimeEnumSimple
from autosar.models.ref import Ref
from autosar.models.sw_systemconst_subtypes_enum import SwSystemconstSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ConditionByFormula:
    """This class represents a condition which is computed based on system
    constants according to the specified expression. The expected result is
    considered as boolean value. The result of the expression is interpreted as
    a condition.

    * "0" represents "false";
    * a value other than zero is considered "true"

    :ivar content:
    :ivar sysc_string_ref: syscString indicates that the referenced
        system constant shall be evaluated as a string according to
        [TPS_SWCT_01431].
    :ivar sysc_ref: This refers to a system constant. The internal
        (coded) value of the system constant shall be used.
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
    :ivar binding_time: This attribute specifies the point in time when
        condition may be evaluated at earliest. At this point in time
        all referenced system constants shall have a value.
    """
    class Meta:
        name = "CONDITION-BY-FORMULA"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    sysc_string_ref: List["ConditionByFormula.SyscStringRef"] = field(
        default_factory=list,
        metadata={
            "name": "SYSC-STRING-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sysc_ref: List["ConditionByFormula.SyscRef"] = field(
        default_factory=list,
        metadata={
            "name": "SYSC-REF",
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
    binding_time: Optional[BindingTimeEnumSimple] = field(
        default=None,
        metadata={
            "name": "BINDING-TIME",
            "type": "Attribute",
        }
    )

    @dataclass
    class SyscStringRef(Ref):
        dest: Optional[SwSystemconstSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class SyscRef(Ref):
        dest: Optional[SwSystemconstSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
