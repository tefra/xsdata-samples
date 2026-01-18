from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from .customer_eligibility_versioned_child_structure import (
    CustomerEligibilityVersionedChildStructure,
)
from .residence_type_enumeration import ResidenceTypeEnumeration
from .residential_qualification_ref import ResidentialQualificationRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ResidentialQualificationEligibilityVersionedChildStructure(
    CustomerEligibilityVersionedChildStructure
):
    class Meta:
        name = "ResidentialQualificationEligibility_VersionedChildStructure"

    residential_qualification_ref: ResidentialQualificationRef | None = field(
        default=None,
        metadata={
            "name": "ResidentialQualificationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    residency_type: ResidenceTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "ResidencyType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    start_date: XmlDate | None = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_date: XmlDate | None = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
