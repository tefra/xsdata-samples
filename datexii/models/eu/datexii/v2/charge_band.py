from dataclasses import dataclass, field
from typing import List, Optional
from datexii.models.eu.datexii.v2.charge import Charge
from datexii.models.eu.datexii.v2.currency_enum import CurrencyEnum
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.overall_period import OverallPeriod
from datexii.models.eu.datexii.v2.parking_permit import ParkingPermit
from datexii.models.eu.datexii.v2.user_type_enum import UserTypeEnum
from datexii.models.eu.datexii.v2.vehicle_characteristics import VehicleCharacteristics

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ChargeBand:
    """
    A charge band in accordance with the specified conditions, possibly up to a
    maximum duration, during a specified period and for a vehicle of specified
    characteristics (in case of parking).

    :ivar charge_currency: A three-character code according to ISO 4217
        for the currency in which the parking charge is specified (e.g.
        EUR, GBP, SEK, CZK).
    :ivar maximum_duration: The maximum duration (e.g. of parking) for
        which the specified charge is applicable.
    :ivar charge_band_name: Name for this charge band.
    :ivar applicable_for_user: Limitation to a set of special users.
    :ivar charge:
    :ivar applicable_for_period: Charge band limitation on a (complex)
        period, described by the validity model.
    :ivar applicable_for_vehicles: Charge band limitation on a set of
        vehicles described by their characteristics.
    :ivar parking_permit:
    :ivar charge_band_extension:
    :ivar id:
    :ivar version:
    """
    charge_currency: Optional[CurrencyEnum] = field(
        default=None,
        metadata={
            "name": "chargeCurrency",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    maximum_duration: Optional[float] = field(
        default=None,
        metadata={
            "name": "maximumDuration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    charge_band_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "chargeBandName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    applicable_for_user: List[UserTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "applicableForUser",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    charge: List[Charge] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    applicable_for_period: Optional[OverallPeriod] = field(
        default=None,
        metadata={
            "name": "applicableForPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    applicable_for_vehicles: List[VehicleCharacteristics] = field(
        default_factory=list,
        metadata={
            "name": "applicableForVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_permit: List[ParkingPermit] = field(
        default_factory=list,
        metadata={
            "name": "parkingPermit",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    charge_band_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "chargeBandExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
