from dataclasses import dataclass, field
from typing import Optional
from netex.models.multilingual_string import MultilingualString
from netex.models.sign_content_enumeration import SignContentEnumeration
from netex.models.sign_equipment_version_structure import SignEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeneralSignStructure(SignEquipmentVersionStructure):
    content: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Content",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sign_content_type: Optional[SignContentEnumeration] = field(
        default=None,
        metadata={
            "name": "SignContentType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
