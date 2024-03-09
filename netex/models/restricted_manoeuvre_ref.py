from dataclasses import dataclass

from .restricted_manoeuvre_ref_structure import RestrictedManoeuvreRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RestrictedManoeuvreRef(RestrictedManoeuvreRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
