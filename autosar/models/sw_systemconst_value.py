from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import Annotation
from autosar.models.numerical_value_variation_point import NumericalValueVariationPoint
from autosar.models.ref import Ref
from autosar.models.sw_systemconst_subtypes_enum import SwSystemconstSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SwSystemconstValue:
    """
    This meta-class assigns a particular value to a system constant.

    :ivar sw_systemconst_ref: This is the system constant to which the
        value applies.
    :ivar value: This is the particular value of a system constant. It
        is specified as Numerical. Further restrictions may apply by the
        definition of the system constant. The value attribute defines
        the internal value of the SwSystemconst as it is processed  in
        the Formula Language.
    :ivar annotations: This provides the ability to add information why
        the value is set like it is.
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
        name = "SW-SYSTEMCONST-VALUE"

    sw_systemconst_ref: Optional["SwSystemconstValue.SwSystemconstRef"] = field(
        default=None,
        metadata={
            "name": "SW-SYSTEMCONST-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    value: Optional[NumericalValueVariationPoint] = field(
        default=None,
        metadata={
            "name": "VALUE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    annotations: Optional["SwSystemconstValue.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
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
    class SwSystemconstRef(Ref):
        dest: Optional[SwSystemconstSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class Annotations:
        annotation: List[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
