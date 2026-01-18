from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .distribution_assignment_ref import DistributionAssignmentRef
from .logical_operation_enumeration import LogicalOperationEnumeration
from .organisation_ref_structure import OrganisationRefStructure
from .point_ref_structure import PointRefStructure
from .validity_parameter_assignment_version_structure import (
    ValidityParameterAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SpecificParameterAssignmentsRelStructure(
    ContainmentAggregationStructure
):
    class Meta:
        name = "specificParameterAssignments_RelStructure"

    specific_parameter_assignment: Iterable[SpecificParameterAssignment] = (
        field(
            default_factory=list,
            metadata={
                "name": "SpecificParameterAssignment",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            },
        )
    )


@dataclass
class SpecificParameterAssignmentVersionStructure(
    ValidityParameterAssignmentVersionStructure
):
    class Meta:
        name = "SpecificParameterAssignment_VersionStructure"

    access_number: int | None = field(
        default=None,
        metadata={
            "name": "AccessNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    includes_grouping_type: LogicalOperationEnumeration | None = field(
        default=None,
        metadata={
            "name": "IncludesGroupingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    includes: SpecificParameterAssignmentsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distribution_assignment_ref: DistributionAssignmentRef | None = field(
        default=None,
        metadata={
            "name": "DistributionAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    retailing_organization_ref: OrganisationRefStructure | None = field(
        default=None,
        metadata={
            "name": "RetailingOrganizationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    collection_point_ref: PointRefStructure | None = field(
        default=None,
        metadata={
            "name": "CollectionPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass
class SpecificParameterAssignment(SpecificParameterAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
