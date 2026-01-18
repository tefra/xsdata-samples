from dataclasses import dataclass, field
from typing import Optional

from .alternative_names_rel_structure import AlternativeNamesRelStructure
from .place_version_structure import PlaceVersionStructure
from .private_code_structure import PrivateCodeStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CountryVersionStructure(PlaceVersionStructure):
    class Meta:
        name = "Country_VersionStructure"

    uic_code: PrivateCodeStructure | None = field(
        default=None,
        metadata={
            "name": "UicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    alternative_names: AlternativeNamesRelStructure | None = field(
        default=None,
        metadata={
            "name": "alternativeNames",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    principality: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
