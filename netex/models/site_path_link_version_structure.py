from __future__ import annotations

from dataclasses import dataclass, field

from .check_constraints_rel_structure import CheckConstraintsRelStructure
from .class_of_use_ref import ClassOfUseRef
from .equipment_places_rel_structure import EquipmentPlacesRelStructure
from .level_ref import LevelRef
from .local_services_rel_structure import LocalServicesRelStructure
from .multilingual_string import MultilingualString
from .path_link_version_structure import PathLinkVersionStructure
from .place_equipments_rel_structure import PlaceEquipmentsRelStructure
from .site_ref_structure import SiteRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SitePathLinkVersionStructure(PathLinkVersionStructure):
    class Meta:
        name = "SitePathLink_VersionStructure"

    site_ref: None | SiteRefStructure = field(
        default=None,
        metadata={
            "name": "SiteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    level_ref: None | LevelRef = field(
        default=None,
        metadata={
            "name": "LevelRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    class_of_use_ref: None | ClassOfUseRef = field(
        default=None,
        metadata={
            "name": "ClassOfUseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    check_constraints: None | CheckConstraintsRelStructure = field(
        default=None,
        metadata={
            "name": "checkConstraints",
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
    label: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
