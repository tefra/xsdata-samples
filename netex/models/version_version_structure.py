from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .type_of_version_ref import TypeOfVersionRef
from .version_ref_structure import VersionRefStructure
from .version_status_enumeration import VersionStatusEnumeration
from .version_type_enumeration import VersionTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VersionVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "Version_VersionStructure"

    start_date: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_date: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    status: None | VersionStatusEnumeration = field(
        default=None,
        metadata={
            "name": "Status",
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
    version_type: None | VersionTypeEnumeration = field(
        default=None,
        metadata={
            "name": "VersionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_version_ref: None | TypeOfVersionRef = field(
        default=None,
        metadata={
            "name": "TypeOfVersionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    derived_from_version_ref: None | VersionRefStructure = field(
        default=None,
        metadata={
            "name": "DerivedFromVersionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
