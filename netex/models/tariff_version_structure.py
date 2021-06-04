from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.alternative_names_rel_structure import AlternativeNamesRelStructure
from netex.models.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.models.authority_ref import AuthorityRef
from netex.models.cell_versioned_child_structure import (
    FareTablesRelStructure,
    PriceGroupsRelStructure,
)
from netex.models.distance_matrix_elements_rel_structure import DistanceMatrixElementsRelStructure
from netex.models.fare_structure_elements_rel_structure import FareStructureElementsRelStructure
from netex.models.flexible_line_ref import FlexibleLineRef
from netex.models.general_organisation_ref import GeneralOrganisationRef
from netex.models.geographical_intervals_rel_structure import GeographicalIntervalsRelStructure
from netex.models.geographical_structure_factors_rel_structure import GeographicalStructureFactorsRelStructure
from netex.models.geographical_unit_ref import GeographicalUnitRef
from netex.models.group_of_lines_ref import GroupOfLinesRef
from netex.models.group_of_operators_ref import GroupOfOperatorsRef
from netex.models.groups_of_distance_matrix_elements_rel_structure import GroupsOfDistanceMatrixElementsRelStructure
from netex.models.info_links_rel_structure import InfoLinksRelStructure
from netex.models.line_ref import LineRef
from netex.models.management_agent_ref import ManagementAgentRef
from netex.models.multilingual_string import MultilingualString
from netex.models.network_ref import NetworkRef
from netex.models.notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from netex.models.operator_ref import OperatorRef
from netex.models.organisation_ref import OrganisationRef
from netex.models.other_organisation_ref import OtherOrganisationRef
from netex.models.price_unit_ref import PriceUnitRef
from netex.models.private_code import PrivateCode
from netex.models.quality_structure_factors_rel_structure import QualityStructureFactorsRelStructure
from netex.models.retail_consortium_ref import RetailConsortiumRef
from netex.models.serviced_organisation_ref import ServicedOrganisationRef
from netex.models.tariff_basis_enumeration import TariffBasisEnumeration
from netex.models.time_intervals_rel_structure import TimeIntervalsRelStructure
from netex.models.time_structure_factors_rel_structure import TimeStructureFactorsRelStructure
from netex.models.time_unit_ref import TimeUnitRef
from netex.models.transport_organisation_ref import TransportOrganisationRef
from netex.models.travel_agent_ref import TravelAgentRef
from netex.models.type_of_tariff_ref import TypeOfTariffRef

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
    retail_consortium_ref: List[RetailConsortiumRef] = field(
        default_factory=list,
        metadata={
            "name": "RetailConsortiumRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    authority_ref: List[AuthorityRef] = field(
        default_factory=list,
        metadata={
            "name": "AuthorityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 6,
            "sequential": True,
        }
    )
    operator_ref: List[OperatorRef] = field(
        default_factory=list,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 6,
            "sequential": True,
        }
    )
    transport_organisation_ref: List[TransportOrganisationRef] = field(
        default_factory=list,
        metadata={
            "name": "TransportOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    general_organisation_ref: List[GeneralOrganisationRef] = field(
        default_factory=list,
        metadata={
            "name": "GeneralOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 6,
            "sequential": True,
        }
    )
    management_agent_ref: List[ManagementAgentRef] = field(
        default_factory=list,
        metadata={
            "name": "ManagementAgentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 6,
            "sequential": True,
        }
    )
    serviced_organisation_ref: List[ServicedOrganisationRef] = field(
        default_factory=list,
        metadata={
            "name": "ServicedOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 6,
            "sequential": True,
        }
    )
    travel_agent_ref: List[TravelAgentRef] = field(
        default_factory=list,
        metadata={
            "name": "TravelAgentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 6,
            "sequential": True,
        }
    )
    other_organisation_ref: List[OtherOrganisationRef] = field(
        default_factory=list,
        metadata={
            "name": "OtherOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    organisation_ref: Optional[OrganisationRef] = field(
        default=None,
        metadata={
            "name": "OrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_operators_ref: Optional[GroupOfOperatorsRef] = field(
        default=None,
        metadata={
            "name": "GroupOfOperatorsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_line_ref: List[FlexibleLineRef] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleLineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
        }
    )
    line_ref: Optional[LineRef] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    network_ref: List[NetworkRef] = field(
        default_factory=list,
        metadata={
            "name": "NetworkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
        }
    )
    group_of_lines_ref: Optional[GroupOfLinesRef] = field(
        default=None,
        metadata={
            "name": "GroupOfLinesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_tariff_ref: Optional[TypeOfTariffRef] = field(
        default=None,
        metadata={
            "name": "TypeOfTariffRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tariff_basis: Optional[TariffBasisEnumeration] = field(
        default=None,
        metadata={
            "name": "TariffBasis",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    return_fare_twice_single: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReturnFareTwiceSingle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_unit_ref: Optional[GeographicalUnitRef] = field(
        default=None,
        metadata={
            "name": "GeographicalUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_intervals: Optional[GeographicalIntervalsRelStructure] = field(
        default=None,
        metadata={
            "name": "geographicalIntervals",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_structure_factors: Optional[GeographicalStructureFactorsRelStructure] = field(
        default=None,
        metadata={
            "name": "geographicalStructureFactors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_unit_ref: Optional[TimeUnitRef] = field(
        default=None,
        metadata={
            "name": "TimeUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_intervals: Optional[TimeIntervalsRelStructure] = field(
        default=None,
        metadata={
            "name": "timeIntervals",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_structure_factors: Optional[TimeStructureFactorsRelStructure] = field(
        default=None,
        metadata={
            "name": "timeStructureFactors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    quality_structure_factors: Optional[QualityStructureFactorsRelStructure] = field(
        default=None,
        metadata={
            "name": "qualityStructureFactors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_structure_elements: Optional[FareStructureElementsRelStructure] = field(
        default=None,
        metadata={
            "name": "fareStructureElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distance_matrix_elements: Optional[DistanceMatrixElementsRelStructure] = field(
        default=None,
        metadata={
            "name": "distanceMatrixElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    groups_of_distance_matrix_elements: Optional[GroupsOfDistanceMatrixElementsRelStructure] = field(
        default=None,
        metadata={
            "name": "groupsOfDistanceMatrixElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    price_unit_ref: Optional[PriceUnitRef] = field(
        default=None,
        metadata={
            "name": "PriceUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    price_groups: Optional[PriceGroupsRelStructure] = field(
        default=None,
        metadata={
            "name": "priceGroups",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_tables: Optional[FareTablesRelStructure] = field(
        default=None,
        metadata={
            "name": "fareTables",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
