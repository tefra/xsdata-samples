from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import ForwardRef

from .containment_aggregation_structure import ContainmentAggregationStructure
from .logical_operation_enumeration import LogicalOperationEnumeration
from .validity_parameter_assignment_version_structure import (
    ValidityParameterAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GenericParameterAssignmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "genericParameterAssignments_RelStructure"

    generic_parameter_assignment_or_generic_parameter_assignment_in_context: Iterable[
        GenericParameterAssignment | GenericParameterAssignmentInContext
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GenericParameterAssignment",
                    "type": ForwardRef("GenericParameterAssignment"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericParameterAssignmentInContext",
                    "type": ForwardRef("GenericParameterAssignmentInContext"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )


@dataclass
class GenericParameterAssignmentVersionStructure(
    ValidityParameterAssignmentVersionStructure
):
    class Meta:
        name = "GenericParameterAssignment_VersionStructure"

    includes_grouping_type: None | LogicalOperationEnumeration = field(
        default=None,
        metadata={
            "name": "IncludesGroupingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    includes: None | GenericParameterAssignmentsRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass
class GenericParameterAssignment(GenericParameterAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class GenericParameterAssignmentInContext(
    GenericParameterAssignmentVersionStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
