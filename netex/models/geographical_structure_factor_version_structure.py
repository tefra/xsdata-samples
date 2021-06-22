from dataclasses import dataclass, field
from decimal import Decimal
from typing import List
from .cell_versioned_child_structure import FareStructureFactorVersionStructure
from .distance_matrix_element_ref import DistanceMatrixElementRef
from .geographical_interval_ref import GeographicalIntervalRef
from .geographical_unit_ref import GeographicalUnitRef
from .parking_tariff_ref import ParkingTariffRef
from .tariff_ref import TariffRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeographicalStructureFactorVersionStructure(FareStructureFactorVersionStructure):
    class Meta:
        name = "GeographicalStructureFactor_VersionStructure"

    choice_1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParkingTariffRef",
                    "type": ParkingTariffRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TariffRef",
                    "type": TariffRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalIntervalRef",
                    "type": GeographicalIntervalRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementRef",
                    "type": DistanceMatrixElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalUnitRef",
                    "type": GeographicalUnitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NumberOfUnits",
                    "type": int,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AmountFactor",
                    "type": Decimal,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 8,
        }
    )
