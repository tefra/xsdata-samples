from __future__ import annotations

from dataclasses import dataclass

from .restricted_manoeuvre_ref_structure import RestrictedManoeuvreRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RestrictedManoeuvreRef(RestrictedManoeuvreRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
