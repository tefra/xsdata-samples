from dataclasses import dataclass, field
from typing import Optional

from .admin_data import VariationPoint
from .identifier import Identifier
from .instance_event_in_composition_instance_ref import (
    InstanceEventInCompositionInstanceRef,
)
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class InstantiationTimingEventProps:
    """
    This meta class represents the ability to refine a timing event for
    particular instances of a software component.

    This supports then an instance specific timing.

    :ivar refined_event_iref: This instance ref denotes the Timing Event
        for which the period shall be refined on an instance level.
    :ivar short_label: The main purpose of the shortLabel is to
        contribute to the splitkey of aggregations that are
        &lt;&lt;atpSplitable&gt;&gt;.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar period: This attribute represents the value of the refined
        activation period.
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
        name = "INSTANTIATION-TIMING-EVENT-PROPS"

    refined_event_iref: Optional[InstanceEventInCompositionInstanceRef] = (
        field(
            default=None,
            metadata={
                "name": "REFINED-EVENT-IREF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    short_label: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-LABEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    period: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "PERIOD",
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
