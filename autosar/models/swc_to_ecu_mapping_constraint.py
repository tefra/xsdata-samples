from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import (
    DocumentationBlock,
    VariationPoint,
)
from autosar.models.component_in_system_instance_ref import ComponentInSystemInstanceRef
from autosar.models.ecu_instance_subtypes_enum import EcuInstanceSubtypesEnum
from autosar.models.ref import Ref
from autosar.models.swc_to_ecu_mapping_constraint_type import SwcToEcuMappingConstraintType

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SwcToEcuMappingConstraint:
    """The System Constraint Description has to describe dedicated and
    exclusive mapping of SW-Cs to one or more ECUs.

    Dedicated mapping means that the SW-C can only be mapped to the ECUs
    it is dedicated to. Exclusive Mapping means that the SW-C cannot be
    mapped to the ECUs it is excluded from.

    :ivar introduction: This represents introductory documentation about
        the mapping constraint.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar component_iref: Reference to SwComponentPrototypes for which
        the dedicated or exclusive mapping is defined.
    :ivar ecu_instance_refs: If the dedicated mapping is described, the
        SwComponentPrototypes can only be mapped to these referenced
        ECUInstances. If the exclusive mapping is described, the
        SwComponentPrototypes cannot be mapped to these referenced
        ECUInstances.
    :ivar swc_to_ecu_mapping_constraint_type: This attribute determines
        if dedicated or exclusive mapping is used.
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
        name = "SWC-TO-ECU-MAPPING-CONSTRAINT"

    introduction: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
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
    component_iref: Optional[ComponentInSystemInstanceRef] = field(
        default=None,
        metadata={
            "name": "COMPONENT-IREF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    ecu_instance_refs: Optional["SwcToEcuMappingConstraint.EcuInstanceRefs"] = field(
        default=None,
        metadata={
            "name": "ECU-INSTANCE-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    swc_to_ecu_mapping_constraint_type: Optional[SwcToEcuMappingConstraintType] = field(
        default=None,
        metadata={
            "name": "SWC-TO-ECU-MAPPING-CONSTRAINT-TYPE",
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
    class EcuInstanceRefs:
        ecu_instance_ref: List["SwcToEcuMappingConstraint.EcuInstanceRefs.EcuInstanceRef"] = field(
            default_factory=list,
            metadata={
                "name": "ECU-INSTANCE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class EcuInstanceRef(Ref):
            dest: Optional[EcuInstanceSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )
