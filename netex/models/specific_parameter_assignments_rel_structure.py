from __future__ import annotations

from collections.abc import Sequence
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


@dataclass(kw_only=True)
class SpecificParameterAssignmentsRelStructure(
    ContainmentAggregationStructure
):
    class Meta:
        name = "specificParameterAssignments_RelStructure"

    specific_parameter_assignment: Sequence[SpecificParameterAssignment] = (
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


@dataclass(kw_only=True)
class SpecificParameterAssignmentVersionStructure(
    ValidityParameterAssignmentVersionStructure
):
    class Meta:
        name = "SpecificParameterAssignment_VersionStructure"

    access_number: None | int = field(
        default=None,
        metadata={
            "name": "AccessNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    includes_grouping_type: None | LogicalOperationEnumeration = field(
        default=None,
        metadata={
            "name": "IncludesGroupingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    includes: None | SpecificParameterAssignmentsRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distribution_assignment_ref: None | DistributionAssignmentRef = field(
        default=None,
        metadata={
            "name": "DistributionAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    retailing_organization_ref: None | OrganisationRefStructure = field(
        default=None,
        metadata={
            "name": "RetailingOrganizationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    collection_point_ref: None | PointRefStructure = field(
        default=None,
        metadata={
            "name": "CollectionPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass(kw_only=True)
class SpecificParameterAssignment(SpecificParameterAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
