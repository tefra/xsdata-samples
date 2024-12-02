from dataclasses import dataclass, field
from typing import Optional

from .boolean import Boolean
from .integer import Integer
from .nm_node_subtypes_enum import NmNodeSubtypesEnum
from .ref import Ref
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class NmCoordinator:
    """
    A NM coordinator is an ECU, which is connected to at least two busses, and
    where the requirement exists that shutdown of NM of at least two of these
    busses (also referred to as coordinated busses) has to be performed
    synchronously.

    :ivar index: Identification of the NMCoordinator.
    :ivar nm_active_coordinator: Please note that this attribute is
        obsolete and is no longer supported. It is replaced by the
        attribute NmCoordinatorRole in NmNode. Old description: This
        attribute indicates whether a NM Coordinator is an active
        gateway (true) or a passive gateway (false).
    :ivar nm_coord_sync_support: Switch for enabling NmCoordinatorSync
        (coordination of nested busses) support.
    :ivar nm_global_coordinator_time: This attribute defines the maximum
        shutdown time (in seconds) of a connected and coordinated NM-
        Cluster.
    :ivar nm_node_refs: reference to busses (via NmNodes) that are
        coordinated by the NmCoordinator.
    :ivar nm_shutdown_delay_timer: Please note that this attribute is
        obsolete and is no longer supported. Old description: This
        parameter defines the time in seconds which the NM Coordination
        algorithm shall delay the release of the referenced cluster.
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
        name = "NM-COORDINATOR"

    index: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "INDEX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_active_coordinator: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "NM-ACTIVE-COORDINATOR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_coord_sync_support: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "NM-COORD-SYNC-SUPPORT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_global_coordinator_time: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "NM-GLOBAL-COORDINATOR-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_node_refs: Optional["NmCoordinator.NmNodeRefs"] = field(
        default=None,
        metadata={
            "name": "NM-NODE-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_shutdown_delay_timer: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "NM-SHUTDOWN-DELAY-TIMER",
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
    class NmNodeRefs:
        nm_node_ref: list["NmCoordinator.NmNodeRefs.NmNodeRef"] = field(
            default_factory=list,
            metadata={
                "name": "NM-NODE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class NmNodeRef(Ref):
            dest: Optional[NmNodeSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
