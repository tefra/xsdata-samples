from dataclasses import dataclass
from netex.models.data_supply_request_structure import DataSupplyRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DataSupplyRequest(DataSupplyRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
