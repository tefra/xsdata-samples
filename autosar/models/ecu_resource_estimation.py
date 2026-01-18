from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    DocumentationBlock,
    VariationPoint,
)
from .ecu_instance_subtypes_enum import EcuInstanceSubtypesEnum
from .ref import Ref
from .resource_consumption import ResourceConsumption
from .swc_to_ecu_mapping_subtypes_enum import SwcToEcuMappingSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EcuResourceEstimation:
    """
    Resource estimations for RTE and BSW of a single ECU instance.

    :ivar introduction: This represents introductory documentation about
        the ecu resource estimation
    :ivar bsw_resource_estimation: Estimation for the resource
        consumption of the basic software.
    :ivar ecu_instance_ref: Reference to the ECU this estimation is done
        for.
    :ivar rte_resource_estimation: Estimation for the resource
        consumption of the run time environment.
    :ivar sw_comp_to_ecu_mapping_refs: References to  SwcToEcuMappings
        that have been taken into account for the resource estimations.
        This way it is possible to define dfferent
        EcuResourceEstimations with diifferent mappings, e.g. before and
        after mapping an additional SW component.
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
        name = "ECU-RESOURCE-ESTIMATION"

    introduction: DocumentationBlock | None = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    bsw_resource_estimation: ResourceConsumption | None = field(
        default=None,
        metadata={
            "name": "BSW-RESOURCE-ESTIMATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ecu_instance_ref: EcuResourceEstimation.EcuInstanceRef | None = field(
        default=None,
        metadata={
            "name": "ECU-INSTANCE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    rte_resource_estimation: ResourceConsumption | None = field(
        default=None,
        metadata={
            "name": "RTE-RESOURCE-ESTIMATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_comp_to_ecu_mapping_refs: EcuResourceEstimation.SwCompToEcuMappingRefs | None = field(
        default=None,
        metadata={
            "name": "SW-COMP-TO-ECU-MAPPING-REFS",
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
    class EcuInstanceRef(Ref):
        dest: EcuInstanceSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class SwCompToEcuMappingRefs:
        sw_comp_to_ecu_mapping_ref: list[
            EcuResourceEstimation.SwCompToEcuMappingRefs.SwCompToEcuMappingRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "SW-COMP-TO-ECU-MAPPING-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class SwCompToEcuMappingRef(Ref):
            dest: SwcToEcuMappingSubtypesEnum | None = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
