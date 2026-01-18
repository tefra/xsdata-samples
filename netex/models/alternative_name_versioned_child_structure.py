from __future__ import annotations

from dataclasses import dataclass, field

from .entity_in_version_structure import VersionedChildStructure
from .multilingual_string import MultilingualString
from .name_type_enumeration import NameTypeEnumeration
from .version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AlternativeNameVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "AlternativeName_VersionedChildStructure"

    named_object_ref: None | VersionOfObjectRefStructure = field(
        default=None,
        metadata={
            "name": "NamedObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    lang: None | str = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name_type: None | NameTypeEnumeration = field(
        default=None,
        metadata={
            "name": "NameType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_name: None | str = field(
        default=None,
        metadata={
            "name": "TypeOfName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    short_name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    abbreviation: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Abbreviation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    qualifier_name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "QualifierName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    order: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
