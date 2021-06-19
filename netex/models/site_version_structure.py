from dataclasses import dataclass, field
from typing import List, Optional
from .authority_ref import AuthorityRef
from .equipment_places_rel_structure import EquipmentPlacesRelStructure
from .general_organisation_ref import GeneralOrganisationRef
from .levels_rel_structure import LevelsRelStructure
from .local_services_rel_structure import LocalServicesRelStructure
from .locale import Locale
from .management_agent_ref import ManagementAgentRef
from .operator_ref import OperatorRef
from .organisation_derived_view_structure import OrganisationDerivedViewStructure
from .organisation_ref import OrganisationRef
from .other_organisation_ref import OtherOrganisationRef
from .place_equipments_rel_structure import PlaceEquipmentsRelStructure
from .retail_consortium_ref import RetailConsortiumRef
from .serviced_organisation_ref import ServicedOrganisationRef
from .site_element_version_structure import SiteElementVersionStructure
from .site_entrances_rel_structure import SiteEntrancesRelStructure
from .site_ref_structure import SiteRefStructure
from .site_refs_rel_structure import SiteRefsRelStructure
from .site_type_enumeration import SiteTypeEnumeration
from .topographic_place_ref import TopographicPlaceRef
from .topographic_place_ref_structure import TopographicPlaceRefStructure
from .topographic_place_refs_rel_structure import TopographicPlaceRefsRelStructure
from .topographic_place_view import TopographicPlaceView
from .transport_organisation_ref import TransportOrganisationRef
from .travel_agent_ref import TravelAgentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SiteVersionStructure(SiteElementVersionStructure):
    class Meta:
        name = "Site_VersionStructure"

    topographic_place_ref: Optional[TopographicPlaceRef] = field(
        default=None,
        metadata={
            "name": "TopographicPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    topographic_place_view: Optional[TopographicPlaceView] = field(
        default=None,
        metadata={
            "name": "TopographicPlaceView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    additional_topographic_places: Optional[TopographicPlaceRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "additionalTopographicPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    site_type: Optional[SiteTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "SiteType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    at_centre: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AtCentre",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    locale: Optional[Locale] = field(
        default=None,
        metadata={
            "name": "Locale",
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
                    "name": "OperatingOrganisationView",
                    "type": OrganisationDerivedViewStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParentSiteRef",
                    "type": SiteRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "adjacentSites",
                    "type": SiteRefsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ContainedInPlaceRef",
                    "type": TopographicPlaceRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "levels",
                    "type": LevelsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "entrances",
                    "type": SiteEntrancesRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "equipmentPlaces",
                    "type": EquipmentPlacesRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "placeEquipments",
                    "type": PlaceEquipmentsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "localServices",
                    "type": LocalServicesRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 34,
        }
    )
