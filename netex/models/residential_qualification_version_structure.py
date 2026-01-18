from dataclasses import dataclass, field

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

    name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parent_ref: UsageParameterRefStructure | None = field(
        default=None,
        metadata={
            "name": "ParentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    must_reside: bool | None = field(
        default=None,
        metadata={
            "name": "MustReside",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    topographic_place_ref: TopographicPlaceRef | None = field(
        default=None,
        metadata={
            "name": "TopographicPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    residence_type: ResidenceTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "ResidenceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_duration: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "MinimumDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
