from dataclasses import dataclass, field
from typing import List, Optional
from .fm_feature_subtypes_enum import FmFeatureSubtypesEnum
from .ref import Ref
from .sw_systemconst_subtypes_enum import SwSystemconstSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class FmConditionByFeaturesAndSwSystemconsts:
    """
    A boolean expression that has the syntax of the AUTOSAR formula language
    and may use references to features or system constants as operands.

    :ivar content:
    :ivar sysc_string_ref: syscString indicates that the referenced
        system constant shall be evaluated as a string according to
        [TPS_SWCT_01431].
    :ivar sysc_ref: This refers to a system constant. The internal
        (coded) value of the system constant shall be used.
    :ivar feature_ref: An expression of type
        FMFormulaByFeaturesAndSwSystemconsts may refer to FMFeatures.
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
        name = "FM-CONDITION-BY-FEATURES-AND-SW-SYSTEMCONSTS"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    sysc_string_ref: List["FmConditionByFeaturesAndSwSystemconsts.SyscStringRef"] = field(
        default_factory=list,
        metadata={
            "name": "SYSC-STRING-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sysc_ref: List["FmConditionByFeaturesAndSwSystemconsts.SyscRef"] = field(
        default_factory=list,
        metadata={
            "name": "SYSC-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    feature_ref: List["FmConditionByFeaturesAndSwSystemconsts.FeatureRef"] = field(
        default_factory=list,
        metadata={
            "name": "FEATURE-REF",
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

    @dataclass
    class FeatureRef(Ref):
        dest: Optional[FmFeatureSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
