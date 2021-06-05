from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlDuration
from netex.models.assignment_version_structure_1 import AssignmentVersionStructure1
from netex.models.journey_accounting_enumeration import JourneyAccountingEnumeration
from netex.models.organisation_ref_structure import OrganisationRefStructure
from netex.models.supply_contract_ref import SupplyContractRef
from netex.models.version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyAccountingVersionStructure(AssignmentVersionStructure1):
    class Meta:
        name = "JourneyAccounting_VersionStructure"

    accounted_object_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "AccountedObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    organisation_ref: Optional[OrganisationRefStructure] = field(
        default=None,
        metadata={
            "name": "OrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    supply_contract_ref: Optional[SupplyContractRef] = field(
        default=None,
        metadata={
            "name": "SupplyContractRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    accounting_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountingCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    accounting_type: Optional[JourneyAccountingEnumeration] = field(
        default=None,
        metadata={
            "name": "AccountingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    partial: List[bool] = field(
        default_factory=list,
        metadata={
            "name": "Partial",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
