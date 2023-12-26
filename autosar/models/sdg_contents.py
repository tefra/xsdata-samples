from dataclasses import dataclass, field
from typing import List, Optional
from .annotation import (
    ReferrableRefConditional,
    Sdg,
)
from .ref import Ref
from .referrable_subtypes_enum import ReferrableSubtypesEnum
from .sd import Sd
from .sdf import Sdf

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SdgContents:
    """This meta-class represents the possible contents of a special data group.

    It can be an arbitrary mix of references, of primitive special data
    and nested special data groups.

    :ivar sdx_ref: Reference to any identifiable element. This allows to
        use Sdg even to establish arbitrary relationships.
    :ivar sdxf: Additional reference with variant support. This property
        was modified due to atpVariation (DirectedAssociationPattern).
    :ivar sd: This is one particular special data element.
    :ivar sdg: This aggregation allows to express nested special data
        groups. By this, any structure can be represented in
        SpeicalData. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was 1.
    :ivar sdf: This is one particular special data element.
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
        name = "SDG-CONTENTS"

    sdx_ref: List["SdgContents.SdxRef"] = field(
        default_factory=list,
        metadata={
            "name": "SDX-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sdxf: List[ReferrableRefConditional] = field(
        default_factory=list,
        metadata={
            "name": "SDXF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sd: List[Sd] = field(
        default_factory=list,
        metadata={
            "name": "SD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sdg: List[Sdg] = field(
        default_factory=list,
        metadata={
            "name": "SDG",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sdf: List[Sdf] = field(
        default_factory=list,
        metadata={
            "name": "SDF",
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

    @dataclass
    class SdxRef(Ref):
        dest: Optional[ReferrableSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
