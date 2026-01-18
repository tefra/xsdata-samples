from dataclasses import dataclass, field
from decimal import Decimal

from datexii.models.eu.datexii.v2.charge_type_enum import ChargeTypeEnum
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.time_period_of_day import TimePeriodOfDay

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Charge:
    """
    A particular charge for a specified interval belonging a charge band.

    :ivar charge: Charge for the specified interval (for vehicle of
        defined characteristics, if any specified) up to the maximum
        defined duration and during the defined period(s).
    :ivar charge_interval: Interval for which the charge applies (e.g.
        charge applies for 2 hours (to specify in seconds)). If no
        interval is specified, the price is valid for the whole period
        (kind of flat fee).
    :ivar charge_type: The type of charge. Day- week- month- and year-
        charges can be specified without this enumeration by specifying
        the interval.
    :ivar charge_type_description: Additional description for this kind
        of charge type, especially if the enumeration does not fit.
    :ivar max_iterations_of_charge: This charge must not be applied more
        often within this charge band than specified in this attribute.
        Thus it is possible to specify the first hour for free, for
        example.
    :ivar min_iterations_of_charge: This charge must be applied within
        this charge band at least as often as specified in this
        attribute. Thus it is possible to specify the first hour in an
        expensive manner, for example.
    :ivar charge_order_index: A non-unique index which forms an order
        for applying charges, i.e. a charge may never be applied
        afterwards a charge with a higher index. For same indices there
        is no order-restriction. You can skip charges unless their
        'minIterationsOfCharge' is not &gt; 0.
    :ivar time_period_of_day: The TimePeriodOfDay limits the validity of
        the charge to this period (e.g. night-tariffs).
    :ivar charge_extension:
    """

    charge: Decimal | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "total_digits": 8,
            "fraction_digits": 2,
        },
    )
    charge_interval: float | None = field(
        default=None,
        metadata={
            "name": "chargeInterval",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    charge_type: ChargeTypeEnum | None = field(
        default=None,
        metadata={
            "name": "chargeType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    charge_type_description: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "chargeTypeDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    max_iterations_of_charge: int | None = field(
        default=None,
        metadata={
            "name": "maxIterationsOfCharge",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    min_iterations_of_charge: int | None = field(
        default=None,
        metadata={
            "name": "minIterationsOfCharge",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    charge_order_index: int | None = field(
        default=None,
        metadata={
            "name": "chargeOrderIndex",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    time_period_of_day: TimePeriodOfDay | None = field(
        default=None,
        metadata={
            "name": "timePeriodOfDay",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    charge_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "chargeExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
