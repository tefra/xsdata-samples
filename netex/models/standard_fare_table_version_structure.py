from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from xsdata.models.datatype import XmlDate
from .authority_ref import AuthorityRef
from .general_organisation_ref import GeneralOrganisationRef
from .group_of_entities_version_structure import GroupOfEntitiesVersionStructure
from .management_agent_ref import ManagementAgentRef
from .operator_ref import OperatorRef
from .organisation_ref import OrganisationRef
from .other_organisation_ref import OtherOrganisationRef
from .priceable_object_refs_rel_structure import PriceableObjectRefsRelStructure
from .retail_consortium_ref import RetailConsortiumRef
from .rounding_ref import RoundingRef
from .serviced_organisation_ref import ServicedOrganisationRef
from .travel_agent_ref import TravelAgentRef
from .type_of_fare_table_ref import TypeOfFareTableRef
from .used_in_refs_rel_structure import UsedInRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StandardFareTableVersionStructure(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "StandardFareTable_VersionStructure"

    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    rounding_ref: Optional[RoundingRef] = field(
        default=None,
        metadata={
            "name": "RoundingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_table_ref: Optional[TypeOfFareTableRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFareTableRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    prices_for: Optional[PriceableObjectRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "pricesFor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    used_in: Optional[UsedInRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "usedIn",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    choice: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RetailConsortiumRef",
                    "type": RetailConsortiumRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AuthorityRef",
                    "type": AuthorityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatorRef",
                    "type": OperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralOrganisationRef",
                    "type": GeneralOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ManagementAgentRef",
                    "type": ManagementAgentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicedOrganisationRef",
                    "type": ServicedOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelAgentRef",
                    "type": TravelAgentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OtherOrganisationRef",
                    "type": OtherOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationRef",
                    "type": OrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    first_class_single: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FirstClassSingle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    second_class_single: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SecondClassSingle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    first_class_return: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FirstClassReturn",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    second_class_return: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SecondClassReturn",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
