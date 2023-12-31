from dataclasses import dataclass
from .car_model_profile_ref_structure import CarModelProfileRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CarModelProfileRef(CarModelProfileRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
