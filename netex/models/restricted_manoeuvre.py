from dataclasses import dataclass
from .restricted_manoeuvre_version_structure import (
    RestrictedManoeuvreVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RestrictedManoeuvre(RestrictedManoeuvreVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
