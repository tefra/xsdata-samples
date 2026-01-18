from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from .customer_eligibility_versioned_child_structure import (
    CustomerEligibilityVersionedChildStructure,
)
from .residence_type_enumeration import ResidenceTypeEnumeration
from .residential_qualification_ref import ResidentialQualificationRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ResidentialQualificationEligibilityVersionedChildStructure(
    CustomerEligibilityVersionedChildStructure
):
    class Meta:
        name = "ResidentialQualificationEligibility_VersionedChildStructure"

    residential_qualification_ref: None | ResidentialQualificationRef = field(
        default=None,
        metadata={
            "name": "ResidentialQualificationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    residency_type: None | ResidenceTypeEnumeration = field(
        default=None,
        metadata={
            "name": "ResidencyType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    start_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
