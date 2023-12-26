from dataclasses import dataclass, field
from typing import List, Optional
from .annotation import DocumentationBlock
from .life_cycle_period import LifeCyclePeriod
from .life_cycle_state_subtypes_enum import LifeCycleStateSubtypesEnum
from .ref import Ref
from .referrable_subtypes_enum import ReferrableSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class LifeCycleInfo:
    """
    LifeCycleInfo describes the life cycle state of an element together with
    additional information like what to use instead.

    :ivar lc_object_ref: Element(s) have the life cycle as described in
        lcState.
    :ivar lc_state_ref: This denotes the particular state assigned to
        the object. If no lcState is given then the default life cycle
        state of LifeCycleInfoSet is assumed.
    :ivar period_begin: Starting point of period in which the element
        has the denoted life cycle state lcState. If no periodBegin is
        given then the default period begin of LifeCycleInfoSet is
        assumed.
    :ivar period_end: Expiry date, i.e. end point of period the element
        does not have the denoted life cycle state lcState any more. If
        no periodEnd is given then the default period begin of
        LifeCycleInfoSet is assumed.
    :ivar remark: Remark describing for example * why the element was
        given the specified life cycle * the semantics of useInstead
    :ivar use_instead_refs: Element(s) that should be used instead of
        the one denoted in  referrable. Only relevant in case of life
        cycle states lcState unlike "valid". In case there are multiple
        references the exact semantics shall be individually described
        in the remark.
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
        name = "LIFE-CYCLE-INFO"

    lc_object_ref: Optional["LifeCycleInfo.LcObjectRef"] = field(
        default=None,
        metadata={
            "name": "LC-OBJECT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    lc_state_ref: Optional["LifeCycleInfo.LcStateRef"] = field(
        default=None,
        metadata={
            "name": "LC-STATE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    period_begin: Optional[LifeCyclePeriod] = field(
        default=None,
        metadata={
            "name": "PERIOD-BEGIN",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    period_end: Optional[LifeCyclePeriod] = field(
        default=None,
        metadata={
            "name": "PERIOD-END",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    remark: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "REMARK",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    use_instead_refs: Optional["LifeCycleInfo.UseInsteadRefs"] = field(
        default=None,
        metadata={
            "name": "USE-INSTEAD-REFS",
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
    class LcObjectRef(Ref):
        dest: Optional[ReferrableSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class LcStateRef(Ref):
        dest: Optional[LifeCycleStateSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class UseInsteadRefs:
        use_instead_ref: List[
            "LifeCycleInfo.UseInsteadRefs.UseInsteadRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "USE-INSTEAD-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class UseInsteadRef(Ref):
            dest: Optional[ReferrableSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
