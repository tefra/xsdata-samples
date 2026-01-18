from __future__ import annotations

from dataclasses import dataclass, field

from .authority_ref import AuthorityRef
from .equipment_places_rel_structure import EquipmentPlacesRelStructure
from .general_organisation_ref import GeneralOrganisationRef
from .levels_rel_structure import LevelsRelStructure
from .local_services_rel_structure import LocalServicesRelStructure
from .locale import Locale
from .management_agent_ref import ManagementAgentRef
from .online_service_operator_ref import OnlineServiceOperatorRef
from .operator_ref import OperatorRef
from .organisation_derived_view_structure import (
    OrganisationDerivedViewStructure,
)
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
from .topographic_place_refs_rel_structure import (
    TopographicPlaceRefsRelStructure,
)
from .topographic_place_view import TopographicPlaceView
from .travel_agent_ref import TravelAgentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteVersionStructure(SiteElementVersionStructure):
    class Meta:
        name = "Site_VersionStructure"

    topographic_place_ref_or_topographic_place_view: (
        None | TopographicPlaceRef | TopographicPlaceView
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TopographicPlaceRef",
                    "type": TopographicPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TopographicPlaceView",
                    "type": TopographicPlaceView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    additional_topographic_places: None | TopographicPlaceRefsRelStructure = (
        field(
            default=None,
            metadata={
                "name": "additionalTopographicPlaces",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    site_type: None | SiteTypeEnumeration = field(
        default=None,
        metadata={
            "name": "SiteType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    at_centre: None | bool = field(
        default=None,
        metadata={
            "name": "AtCentre",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    locale: None | Locale = field(
        default=None,
        metadata={
            "name": "Locale",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice: (
        None
        | RetailConsortiumRef
        | OnlineServiceOperatorRef
        | GeneralOrganisationRef
        | ManagementAgentRef
        | ServicedOrganisationRef
        | TravelAgentRef
        | OtherOrganisationRef
        | AuthorityRef
        | OperatorRef
        | OrganisationRef
        | OrganisationDerivedViewStructure
    ) = field(
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
                    "name": "OnlineServiceOperatorRef",
                    "type": OnlineServiceOperatorRef,
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
                    "name": "OrganisationRef",
                    "type": OrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingOrganisationView",
                    "type": OrganisationDerivedViewStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    parent_site_ref: None | SiteRefStructure = field(
        default=None,
        metadata={
            "name": "ParentSiteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    adjacent_sites: None | SiteRefsRelStructure = field(
        default=None,
        metadata={
            "name": "adjacentSites",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    contained_in_place_ref: None | TopographicPlaceRefStructure = field(
        default=None,
        metadata={
            "name": "ContainedInPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    levels: None | LevelsRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    entrances: None | SiteEntrancesRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    equipment_places: None | EquipmentPlacesRelStructure = field(
        default=None,
        metadata={
            "name": "equipmentPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    place_equipments: None | PlaceEquipmentsRelStructure = field(
        default=None,
        metadata={
            "name": "placeEquipments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    local_services: None | LocalServicesRelStructure = field(
        default=None,
        metadata={
            "name": "localServices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
