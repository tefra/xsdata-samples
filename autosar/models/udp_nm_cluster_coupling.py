from dataclasses import dataclass, field
from typing import List, Optional

from .admin_data import VariationPoint
from .boolean import Boolean
from .ref import Ref
from .udp_nm_cluster_subtypes_enum import UdpNmClusterSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class UdpNmClusterCoupling:
    """
    Udp attributes that are valid for each of the referenced (coupled) UdpNm
    clusters.

    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar coupled_cluster_refs: Reference to coupled UdpNm Clusters.
    :ivar nm_bus_load_reduction_enabled: Enables busload reduction
        support
    :ivar nm_immediate_restart_enabled: Enables the asynchronous
        transmission of a CanNm PDU upon bus-communication request in
        Prepare-Bus-Sleep mode.
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
        name = "UDP-NM-CLUSTER-COUPLING"

    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    coupled_cluster_refs: Optional[
        "UdpNmClusterCoupling.CoupledClusterRefs"
    ] = field(
        default=None,
        metadata={
            "name": "COUPLED-CLUSTER-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_bus_load_reduction_enabled: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "NM-BUS-LOAD-REDUCTION-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_immediate_restart_enabled: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "NM-IMMEDIATE-RESTART-ENABLED",
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
    class CoupledClusterRefs:
        coupled_cluster_ref: List[
            "UdpNmClusterCoupling.CoupledClusterRefs.CoupledClusterRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "COUPLED-CLUSTER-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class CoupledClusterRef(Ref):
            dest: Optional[UdpNmClusterSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
