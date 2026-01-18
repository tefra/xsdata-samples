from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

from .assignment_version_structure_1 import AssignmentVersionStructure1
from .check_constraint_ref import CheckConstraintRef
from .class_of_use_ref import ClassOfUseRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CheckConstraintDelayVersionStructure(AssignmentVersionStructure1):
    class Meta:
        name = "CheckConstraintDelay_VersionStructure"

    check_constraint_ref: CheckConstraintRef | None = field(
        default=None,
        metadata={
            "name": "CheckConstraintRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    class_of_use_ref: ClassOfUseRef | None = field(
        default=None,
        metadata={
            "name": "ClassOfUseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_likely_delay: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "MinimumLikelyDelay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    average_delay: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "AverageDelay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_likely_delay: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "MaximumLikelyDelay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
