from dataclasses import dataclass, field
from typing import Optional

from .multilingual_string import MultilingualString
from .sign_content_enumeration import SignContentEnumeration
from .sign_equipment_version_structure import SignEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeneralSignStructure(SignEquipmentVersionStructure):
    content: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Content",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sign_content_type: SignContentEnumeration | None = field(
        default=None,
        metadata={
            "name": "SignContentType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
