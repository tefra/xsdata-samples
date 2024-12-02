from dataclasses import dataclass, field
from typing import Optional

from .coupling_port_fifo import CouplingPortFifo
from .coupling_port_rate_policy import CouplingPortRatePolicy
from .coupling_port_scheduler import CouplingPortScheduler
from .coupling_port_scheduler_subtypes_enum import (
    CouplingPortSchedulerSubtypesEnum,
)
from .coupling_port_shaper import CouplingPortShaper
from .coupling_port_traffic_class_assignment import (
    CouplingPortTrafficClassAssignment,
)
from .ethernet_priority_regeneration import EthernetPriorityRegeneration
from .global_time_coupling_port_props import GlobalTimeCouplingPortProps
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CouplingPortDetails:
    """Defines details of a CouplingPort.

    May be used to configure the structures of a switch.

    :ivar coupling_port_structural_elements: Collects all the structural
        parts at which a CouplingPort may be configurable.
    :ivar ethernet_priority_regenerations: Defines a priority
        regeneration where the ingress priority is replaced by
        regenerated priority.
    :ivar ethernet_traffic_class_assignments: Defines the ingress port
        to EthernetTrafficClass assignment.
    :ivar global_time_props: Specifies properties for the usage of the
        CouplingPort in the scope of Global Time Sync.
    :ivar last_egress_scheduler_ref: Defines which CouplingPortScheduler
        is the last in the egress port structure.
    :ivar rate_policys: Rate policies to be applied for this
        CouplingPort.
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
        name = "COUPLING-PORT-DETAILS"

    coupling_port_structural_elements: Optional[
        "CouplingPortDetails.CouplingPortStructuralElements"
    ] = field(
        default=None,
        metadata={
            "name": "COUPLING-PORT-STRUCTURAL-ELEMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ethernet_priority_regenerations: Optional[
        "CouplingPortDetails.EthernetPriorityRegenerations"
    ] = field(
        default=None,
        metadata={
            "name": "ETHERNET-PRIORITY-REGENERATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ethernet_traffic_class_assignments: Optional[
        "CouplingPortDetails.EthernetTrafficClassAssignments"
    ] = field(
        default=None,
        metadata={
            "name": "ETHERNET-TRAFFIC-CLASS-ASSIGNMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    global_time_props: Optional[GlobalTimeCouplingPortProps] = field(
        default=None,
        metadata={
            "name": "GLOBAL-TIME-PROPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    last_egress_scheduler_ref: Optional[
        "CouplingPortDetails.LastEgressSchedulerRef"
    ] = field(
        default=None,
        metadata={
            "name": "LAST-EGRESS-SCHEDULER-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    rate_policys: Optional["CouplingPortDetails.RatePolicys"] = field(
        default=None,
        metadata={
            "name": "RATE-POLICYS",
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
    class CouplingPortStructuralElements:
        coupling_port_fifo: list[CouplingPortFifo] = field(
            default_factory=list,
            metadata={
                "name": "COUPLING-PORT-FIFO",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        coupling_port_scheduler: list[CouplingPortScheduler] = field(
            default_factory=list,
            metadata={
                "name": "COUPLING-PORT-SCHEDULER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        coupling_port_shaper: list[CouplingPortShaper] = field(
            default_factory=list,
            metadata={
                "name": "COUPLING-PORT-SHAPER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class EthernetPriorityRegenerations:
        ethernet_priority_regeneration: list[EthernetPriorityRegeneration] = (
            field(
                default_factory=list,
                metadata={
                    "name": "ETHERNET-PRIORITY-REGENERATION",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                    "max_occurs": 8,
                },
            )
        )

    @dataclass
    class EthernetTrafficClassAssignments:
        coupling_port_traffic_class_assignment: list[
            CouplingPortTrafficClassAssignment
        ] = field(
            default_factory=list,
            metadata={
                "name": "COUPLING-PORT-TRAFFIC-CLASS-ASSIGNMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
                "max_occurs": 8,
            },
        )

    @dataclass
    class LastEgressSchedulerRef(Ref):
        dest: Optional[CouplingPortSchedulerSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class RatePolicys:
        coupling_port_rate_policy: list[CouplingPortRatePolicy] = field(
            default_factory=list,
            metadata={
                "name": "COUPLING-PORT-RATE-POLICY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
