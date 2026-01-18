from __future__ import annotations

from dataclasses import dataclass, field

from .additional_driver_type_enumeration import AdditionalDriverTypeEnumeration
from .driver_type_fee_basis_enumeration import DriverTypeFeeBasisEnumeration
from .rental_option_version_structure import RentalOptionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AdditionalDriverOptionVersionStructure(RentalOptionVersionStructure):
    class Meta:
        name = "AdditionalDriverOption_VersionStructure"

    additional_driver: None | AdditionalDriverTypeEnumeration = field(
        default=None,
        metadata={
            "name": "AdditionalDriver",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    driver_fee_basis: None | DriverTypeFeeBasisEnumeration = field(
        default=None,
        metadata={
            "name": "DriverFeeBasis",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_ofdrivers: None | int = field(
        default=None,
        metadata={
            "name": "NumberOFDrivers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
