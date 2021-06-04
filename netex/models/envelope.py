from dataclasses import dataclass
from netex.models.envelope_type import EnvelopeType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Envelope(EnvelopeType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
