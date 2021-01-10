from dataclasses import dataclass
from datexii.models.datexii_3_common import PayloadPublication

__NAMESPACE__ = "http://datex2.eu/schema/3/d2Payload"


@dataclass
class Payload(PayloadPublication):
    class Meta:
        name = "payload"
        namespace = "http://datex2.eu/schema/3/d2Payload"
