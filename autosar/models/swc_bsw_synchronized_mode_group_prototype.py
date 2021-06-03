from dataclasses import dataclass, field
from typing import Optional
from autosar.models.annotation import VariationPoint
from autosar.models.mode_declaration_group_prototype_subtypes_enum import ModeDeclarationGroupPrototypeSubtypesEnum
from autosar.models.p_mode_group_in_atomic_swc_instance_ref import PModeGroupInAtomicSwcInstanceRef
from autosar.models.ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SwcBswSynchronizedModeGroupPrototype:
    """
    Synchronizes a mode group provided by a component via a port with a mode
    group provided by a BSW module or cluster.

    :ivar bsw_mode_group_ref: The BSW mode group prototype.
    :ivar swc_mode_group_iref: The SWC mode group prototype provided by
        a particular port.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
        name = "SWC-BSW-SYNCHRONIZED-MODE-GROUP-PROTOTYPE"

    bsw_mode_group_ref: Optional["SwcBswSynchronizedModeGroupPrototype.BswModeGroupRef"] = field(
        default=None,
        metadata={
            "name": "BSW-MODE-GROUP-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    swc_mode_group_iref: Optional[PModeGroupInAtomicSwcInstanceRef] = field(
        default=None,
        metadata={
            "name": "SWC-MODE-GROUP-IREF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
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
    class BswModeGroupRef(Ref):
        dest: Optional[ModeDeclarationGroupPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
