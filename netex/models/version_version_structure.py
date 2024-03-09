from dataclasses import dataclass, field
from typing import Optional

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

    start_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    status: Optional[VersionStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "Status",
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
    version_type: Optional[VersionTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "VersionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_version_ref: Optional[TypeOfVersionRef] = field(
        default=None,
        metadata={
            "name": "TypeOfVersionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    derived_from_version_ref: Optional[VersionRefStructure] = field(
        default=None,
        metadata={
            "name": "DerivedFromVersionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
