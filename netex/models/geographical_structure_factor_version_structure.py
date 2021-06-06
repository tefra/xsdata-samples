from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
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

    parking_tariff_ref: List[ParkingTariffRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingTariffRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
        }
    )
    tariff_ref: Optional[TariffRef] = field(
        default=None,
        metadata={
            "name": "TariffRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_interval_ref: Optional[GeographicalIntervalRef] = field(
        default=None,
        metadata={
            "name": "GeographicalIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distance_matrix_element_ref: Optional[DistanceMatrixElementRef] = field(
        default=None,
        metadata={
            "name": "DistanceMatrixElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_unit_ref: Optional[GeographicalUnitRef] = field(
        default=None,
        metadata={
            "name": "GeographicalUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    number_of_units: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfUnits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    amount_factor: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AmountFactor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
