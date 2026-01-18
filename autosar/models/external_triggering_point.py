from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import VariationPoint
from .external_triggering_point_ident import ExternalTriggeringPointIdent
from .p_trigger_in_atomic_swc_type_instance_ref import (
    PTriggerInAtomicSwcTypeInstanceRef,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ExternalTriggeringPoint:
    """
    If a RunnableEntity owns an ExternalTriggeringPoint it is entitled to
    raise an ExternalTriggerOccurredEvent.

    :ivar ident: The aggregation in the role ident provides the ability
        to make the ExternalTriggeringPoint identifiable. From the
        semantical point of view, the ExternalTriggeringPoint is
        considered a first-class Identifiable and therefore the
        aggregation in the role ident shall always exist (until it may
        be possible to let ModeAccessPoint directly inherit from
        Identifiable).
    :ivar trigger_iref: The trigger taken for the
        ExternalTriggeringPoint.
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
        name = "EXTERNAL-TRIGGERING-POINT"

    ident: ExternalTriggeringPointIdent | None = field(
        default=None,
        metadata={
            "name": "IDENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    trigger_iref: ExternalTriggeringPoint.TriggerIref | None = field(
        default=None,
        metadata={
            "name": "TRIGGER-IREF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: VariationPoint | None = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: str | None = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: str | None = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class TriggerIref:
        p_trigger_in_atomic_swc_type_instance_ref: (
            PTriggerInAtomicSwcTypeInstanceRef | None
        ) = field(
            default=None,
            metadata={
                "name": "P-TRIGGER-IN-ATOMIC-SWC-TYPE-INSTANCE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
