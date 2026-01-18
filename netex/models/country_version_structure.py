from __future__ import annotations

from dataclasses import dataclass, field

from .alternative_names_rel_structure import AlternativeNamesRelStructure
from .place_version_structure import PlaceVersionStructure
from .private_code_structure import PrivateCodeStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CountryVersionStructure(PlaceVersionStructure):
    class Meta:
        name = "Country_VersionStructure"

    uic_code: None | PrivateCodeStructure = field(
        default=None,
        metadata={
            "name": "UicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    alternative_names: None | AlternativeNamesRelStructure = field(
        default=None,
        metadata={
            "name": "alternativeNames",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    principality: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
