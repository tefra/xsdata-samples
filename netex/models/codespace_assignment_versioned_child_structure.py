from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from netex.models.administrative_zone_ref import AdministrativeZoneRef
from netex.models.alternative_texts_rel_structure import VersionedChildStructure
from netex.models.codespace import Codespace
from netex.models.codespace_ref import CodespaceRef
from netex.models.multilingual_string import MultilingualString
from netex.models.type_of_codespace_assignment_ref import TypeOfCodespaceAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CodespaceAssignmentVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "CodespaceAssignment_VersionedChildStructure"

    codespace_ref: Optional[CodespaceRef] = field(
        default=None,
        metadata={
            "name": "CodespaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    codespace: Optional[Codespace] = field(
        default=None,
        metadata={
            "name": "Codespace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    administrative_zone_ref: Optional[AdministrativeZoneRef] = field(
        default=None,
        metadata={
            "name": "AdministrativeZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    name_of_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "NameOfClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    code_prefix: List[str] = field(
        default_factory=list,
        metadata={
            "name": "CodePrefix",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_length: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumLength",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_codespace_assignment_ref: Optional[TypeOfCodespaceAssignmentRef] = field(
        default=None,
        metadata={
            "name": "TypeOfCodespaceAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
