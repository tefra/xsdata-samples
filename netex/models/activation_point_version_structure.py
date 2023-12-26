from dataclasses import dataclass, field
from typing import Optional
from .multilingual_string import MultilingualString
from .point_version_structure import PointVersionStructure
from .private_code import PrivateCode
from .type_of_activation_ref import TypeOfActivationRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ActivationPointVersionStructure(PointVersionStructure):
    class Meta:
        name = "ActivationPoint_VersionStructure"

    activation_point_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ActivationPointNumber",
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
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_activation_ref: Optional[TypeOfActivationRef] = field(
        default=None,
        metadata={
            "name": "TypeOfActivationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
