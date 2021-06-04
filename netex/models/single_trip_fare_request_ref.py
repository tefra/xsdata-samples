from dataclasses import dataclass
from netex.models.single_trip_fare_request_ref_structure import SingleTripFareRequestRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SingleTripFareRequestRef(SingleTripFareRequestRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
