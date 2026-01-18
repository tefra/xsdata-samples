from __future__ import annotations

from dataclasses import dataclass, field

from .ecuc_container_value_subtypes_enum import EcucContainerValueSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class RtePluginProps:
    """
    The properties of a communication graph with respect to the utilization
    of RTE Implementation Plug-in.

    :ivar associated_cross_sw_cluster_com_rte_plugin_ref: This
        associates a communication graph to a specific RTE
        Implementation Plug-in handling cross Software Cluster
        communication.
    :ivar associated_rte_plugin_ref: This associates a communication
        graph to a specific RTE Implementation Plug-in handling local
        Software Cluster communication or communication in a non-cluster
        ECU.
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
        name = "RTE-PLUGIN-PROPS"

    associated_cross_sw_cluster_com_rte_plugin_ref: (
        RtePluginProps.AssociatedCrossSwClusterComRtePluginRef | None
    ) = field(
        default=None,
        metadata={
            "name": "ASSOCIATED-CROSS-SW-CLUSTER-COM-RTE-PLUGIN-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    associated_rte_plugin_ref: RtePluginProps.AssociatedRtePluginRef | None = (
        field(
            default=None,
            metadata={
                "name": "ASSOCIATED-RTE-PLUGIN-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
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
    class AssociatedCrossSwClusterComRtePluginRef(Ref):
        dest: EcucContainerValueSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class AssociatedRtePluginRef(Ref):
        dest: EcucContainerValueSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
