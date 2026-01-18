from __future__ import annotations

from dataclasses import dataclass

from .country_ref_structure import CountryRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CountryRef(CountryRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
