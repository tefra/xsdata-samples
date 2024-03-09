from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from .entity_in_version_structure import VersionedChildStructure
from .multilingual_string import MultilingualString
from .residence_type_enumeration import ResidenceTypeEnumeration
from .topographic_place_ref import TopographicPlaceRef
from .usage_parameter_ref_structure import UsageParameterRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ResidentialQualificationVersionStructure(VersionedChildStructure):
    class Meta:
        name = "ResidentialQualification_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
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
    parent_ref: Optional[UsageParameterRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    must_reside: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MustReside",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    topographic_place_ref: Optional[TopographicPlaceRef] = field(
        default=None,
        metadata={
            "name": "TopographicPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    residence_type: Optional[ResidenceTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "ResidenceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
