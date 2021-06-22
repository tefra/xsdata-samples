from dataclasses import dataclass, field
from typing import List, Optional
from .alternative_names_rel_structure import AlternativeNamesRelStructure
from .alternative_texts_rel_structure import DataManagedObjectStructure
from .authority_ref import AuthorityRef
from .cell_versioned_child_structure import (
    FareTablesRelStructure,
    PriceGroupsRelStructure,
)
from .distance_matrix_elements_rel_structure import DistanceMatrixElementsRelStructure
from .fare_structure_elements_rel_structure import FareStructureElementsRelStructure
from .flexible_line_ref import FlexibleLineRef
from .general_organisation_ref import GeneralOrganisationRef
from .geographical_intervals_rel_structure import GeographicalIntervalsRelStructure
from .geographical_structure_factors_rel_structure import GeographicalStructureFactorsRelStructure
from .geographical_unit_ref import GeographicalUnitRef
from .group_of_lines_ref import GroupOfLinesRef
from .group_of_operators_ref import GroupOfOperatorsRef
from .groups_of_distance_matrix_elements_rel_structure import GroupsOfDistanceMatrixElementsRelStructure
from .info_links_rel_structure import InfoLinksRelStructure
from .line_ref import LineRef
from .management_agent_ref import ManagementAgentRef
from .multilingual_string import MultilingualString
from .network_ref import NetworkRef
from .notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from .operator_ref import OperatorRef
from .organisation_ref import OrganisationRef
from .other_organisation_ref import OtherOrganisationRef
from .price_unit_ref import PriceUnitRef
from .private_code import PrivateCode
from .quality_structure_factors_rel_structure import QualityStructureFactorsRelStructure
from .retail_consortium_ref import RetailConsortiumRef
from .serviced_organisation_ref import ServicedOrganisationRef
from .tariff_basis_enumeration import TariffBasisEnumeration
from .time_intervals_rel_structure import TimeIntervalsRelStructure
from .time_structure_factors_rel_structure import TimeStructureFactorsRelStructure
from .time_unit_ref import TimeUnitRef
from .transport_organisation_ref import TransportOrganisationRef
from .travel_agent_ref import TravelAgentRef
from .type_of_tariff_ref import TypeOfTariffRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TariffVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "Tariff_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    alternative_names: Optional[AlternativeNamesRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeNames",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice_assignments: Optional[NoticeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    document_links: Optional[InfoLinksRelStructure] = field(
        default=None,
        metadata={
            "name": "documentLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    choice: List[object] = field(
        default_factory=list,
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
                    "name": "TransportOrganisationRef",
                    "type": TransportOrganisationRef,
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
                {
                    "name": "GroupOfOperatorsRef",
                    "type": GroupOfOperatorsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleLineRef",
                    "type": FlexibleLineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineRef",
                    "type": LineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NetworkRef",
                    "type": NetworkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfLinesRef",
                    "type": GroupOfLinesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTariffRef",
                    "type": TypeOfTariffRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TariffBasis",
                    "type": TariffBasisEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReturnFareTwiceSingle",
                    "type": bool,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalUnitRef",
                    "type": GeographicalUnitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "geographicalIntervals",
                    "type": GeographicalIntervalsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "geographicalStructureFactors",
                    "type": GeographicalStructureFactorsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeUnitRef",
                    "type": TimeUnitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "timeIntervals",
                    "type": TimeIntervalsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "timeStructureFactors",
                    "type": TimeStructureFactorsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "qualityStructureFactors",
                    "type": QualityStructureFactorsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "fareStructureElements",
                    "type": FareStructureElementsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "distanceMatrixElements",
                    "type": DistanceMatrixElementsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "groupsOfDistanceMatrixElements",
                    "type": GroupsOfDistanceMatrixElementsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PriceUnitRef",
                    "type": PriceUnitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "priceGroups",
                    "type": PriceGroupsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "fareTables",
                    "type": FareTablesRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 71,
        }
    )
