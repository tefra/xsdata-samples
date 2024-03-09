from dataclasses import dataclass, field
from typing import Optional

from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .private_code import PrivateCode

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfValueVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "TypeOfValue_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    image: Optional[str] = field(
        default=None,
        metadata={
            "name": "Image",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "Url",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
