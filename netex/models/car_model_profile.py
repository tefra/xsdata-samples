from dataclasses import dataclass
from .car_model_profile_version_structure import (
    CarModelProfileVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CarModelProfile(CarModelProfileVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
