from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import VariationPoint
from autosar.models.boolean import Boolean
from autosar.models.flexray_nm_cluster_subtypes_enum import FlexrayNmClusterSubtypesEnum
from autosar.models.flexray_nm_schedule_variant import FlexrayNmScheduleVariant
from autosar.models.ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class FlexrayNmClusterCoupling:
    """
    FlexRay attributes that are valid for each of the referenced (coupled)
    FlexRay clusters.

    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar coupled_cluster_refs: Reference to coupled FlexRay Clusters.
    :ivar nm_control_bit_vector_enabled: Enables control bit vector
        support.
    :ivar nm_data_disabled: Disables the transmission of NM-Data.
    :ivar nm_schedule_variant: FrNm schedule variant according to FrNm
        SWS.
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
        name = "FLEXRAY-NM-CLUSTER-COUPLING"

    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    coupled_cluster_refs: Optional["FlexrayNmClusterCoupling.CoupledClusterRefs"] = field(
        default=None,
        metadata={
            "name": "COUPLED-CLUSTER-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    nm_control_bit_vector_enabled: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "NM-CONTROL-BIT-VECTOR-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    nm_data_disabled: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "NM-DATA-DISABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    nm_schedule_variant: Optional[FlexrayNmScheduleVariant] = field(
        default=None,
        metadata={
            "name": "NM-SCHEDULE-VARIANT",
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
    class CoupledClusterRefs:
        coupled_cluster_ref: List["FlexrayNmClusterCoupling.CoupledClusterRefs.CoupledClusterRef"] = field(
            default_factory=list,
            metadata={
                "name": "COUPLED-CLUSTER-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class CoupledClusterRef(Ref):
            dest: Optional[FlexrayNmClusterSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )
