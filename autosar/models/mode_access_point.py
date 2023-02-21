from dataclasses import dataclass, field
from typing import Optional
from .annotation import VariationPoint
from .mode_access_point_ident import ModeAccessPointIdent
from .p_mode_group_in_atomic_swc_instance_ref import PModeGroupInAtomicSwcInstanceRef
from .r_mode_group_in_atomic_swc_instance_ref import RModeGroupInAtomicSwcInstanceRef

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ModeAccessPoint:
    """A ModeAccessPoint is required by a RunnableEntity owned by a Mode Manager or
    Mode User.

    Its semantics implies the ability to access the current mode
    (provided by the RTE)  of a ModeDeclarationGroupPrototype's
    ModeDeclarationGroup.

    :ivar ident: The aggregation in the role ident provides the ability
        to make the ModeAccessPoint identifiable. From the semantical
        point of view, the ModeAccessPoint is considered a first-class
        Identifiable and therefore the aggregation in the role ident
        shall always exist (until it may be possible to let
        ModeAccessPoint directly inherit from Identifiable).
    :ivar mode_group_iref: The mode declaration group that is accessed
        by this runnable.
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
        name = "MODE-ACCESS-POINT"

    ident: Optional[ModeAccessPointIdent] = field(
        default=None,
        metadata={
            "name": "IDENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    mode_group_iref: Optional["ModeAccessPoint.ModeGroupIref"] = field(
        default=None,
        metadata={
            "name": "MODE-GROUP-IREF",
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
    class ModeGroupIref:
        p_mode_group_in_atomic_swc_instance_ref: Optional[PModeGroupInAtomicSwcInstanceRef] = field(
            default=None,
            metadata={
                "name": "P-MODE-GROUP-IN-ATOMIC-SWC-INSTANCE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        r_mode_group_in_atomic_swc_instance_ref: Optional[RModeGroupInAtomicSwcInstanceRef] = field(
            default=None,
            metadata={
                "name": "R-MODE-GROUP-IN-ATOMIC-SWC-INSTANCE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
