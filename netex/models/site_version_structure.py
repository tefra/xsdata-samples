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
    retail_consortium_ref: List[RetailConsortiumRef] = field(
        default_factory=list,
        metadata={
            "name": "RetailConsortiumRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    authority_ref: List[AuthorityRef] = field(
        default_factory=list,
        metadata={
            "name": "AuthorityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    operator_ref: List[OperatorRef] = field(
        default_factory=list,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    transport_organisation_ref: List[TransportOrganisationRef] = field(
        default_factory=list,
        metadata={
            "name": "TransportOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    general_organisation_ref: List[GeneralOrganisationRef] = field(
        default_factory=list,
        metadata={
            "name": "GeneralOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    management_agent_ref: List[ManagementAgentRef] = field(
        default_factory=list,
        metadata={
            "name": "ManagementAgentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    serviced_organisation_ref: List[ServicedOrganisationRef] = field(
        default_factory=list,
        metadata={
            "name": "ServicedOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    travel_agent_ref: List[TravelAgentRef] = field(
        default_factory=list,
        metadata={
            "name": "TravelAgentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    other_organisation_ref: List[OtherOrganisationRef] = field(
        default_factory=list,
        metadata={
            "name": "OtherOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
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
    operating_organisation_view: Optional[OrganisationDerivedViewStructure] = field(
        default=None,
        metadata={
            "name": "OperatingOrganisationView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parent_site_ref: Optional[SiteRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentSiteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    adjacent_sites: Optional[SiteRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "adjacentSites",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    contained_in_place_ref: Optional[TopographicPlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "ContainedInPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    levels: Optional[LevelsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entrances: Optional[SiteEntrancesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    equipment_places: Optional[EquipmentPlacesRelStructure] = field(
        default=None,
        metadata={
            "name": "equipmentPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    place_equipments: Optional[PlaceEquipmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "placeEquipments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    local_services: Optional[LocalServicesRelStructure] = field(
        default=None,
        metadata={
            "name": "localServices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )