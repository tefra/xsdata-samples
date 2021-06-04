from dataclasses import dataclass, field
from typing import Optional
from netex.models.alternative_names_rel_structure import AlternativeNamesRelStructure
from netex.models.place_version_structure import PlaceVersionStructure
from netex.models.private_code_structure import PrivateCodeStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CountryVersionStructure(PlaceVersionStructure):
    class Meta:
        name = "Country_VersionStructure"

    uic_code: Optional[PrivateCodeStructure] = field(
        default=None,
        metadata={
            "name": "UicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    alternative_names: Optional[AlternativeNamesRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeNames",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    principality: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
