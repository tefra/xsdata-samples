from __future__ import annotations

from dataclasses import dataclass, field

from .entity_in_version_structure import DataManagedObjectStructure
from .info_links_rel_structure import InfoLinksRelStructure
from .multilingual_string import MultilingualString
from .private_code import PrivateCode
from .private_code_structure import PrivateCodeStructure
from .type_of_equipment_ref import TypeOfEquipmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EquipmentVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "Equipment_VersionStructure"

    name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: None | PrivateCode = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    public_code: None | PrivateCodeStructure = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    image: None | str = field(
        default=None,
        metadata={
            "name": "Image",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_equipment_ref: None | TypeOfEquipmentRef = field(
        default=None,
        metadata={
            "name": "TypeOfEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    note: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    info_links: None | InfoLinksRelStructure = field(
        default=None,
        metadata={
            "name": "infoLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    out_of_service: None | bool = field(
        default=None,
        metadata={
            "name": "OutOfService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
