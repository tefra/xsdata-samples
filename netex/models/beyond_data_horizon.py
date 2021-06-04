from dataclasses import dataclass
from netex.models.beyond_data_horizon_error_structure import BeyondDataHorizonErrorStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class BeyondDataHorizon(BeyondDataHorizonErrorStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
