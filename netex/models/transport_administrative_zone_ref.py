from dataclasses import dataclass
from netex.models.transport_administrative_zone_ref_structure import TransportAdministrativeZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TransportAdministrativeZoneRef(TransportAdministrativeZoneRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
