from __future__ import annotations

from dataclasses import dataclass

from .country_version_structure import CountryVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Country(CountryVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
