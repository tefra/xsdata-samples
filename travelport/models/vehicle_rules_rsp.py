from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_search_rsp_1 import BaseSearchRsp1
from travelport.models.marketing_information_1 import MarketingInformation1
from travelport.models.policy import Policy
from travelport.models.type_deposit_guarantee import TypeDepositGuarantee
from travelport.models.type_rental_period import TypeRentalPeriod
from travelport.models.type_start_end_time import TypeStartEndTime
from travelport.models.type_vehicle_charge import TypeVehicleCharge
from travelport.models.type_vehicle_location_information import (
    TypeVehicleLocationInformation,
)
from travelport.models.vehicle import Vehicle

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class VehicleRulesRsp(BaseSearchRsp1):
    """
    The rules associated with a vehicle rental rate.

    Parameters
    ----------
    vehicle
    operation_time
    start_end_times
        The earliest and latest pickup and dropoff times for this vehicle
        rental rate.
    rental_period_rules
        The maximum and minimum rental periods.
    pre_pay_cancel_info
        PrePayment cancellation Advisory Values use to construct custom
        Advisory text. 1P only.
    payment_rule
        The Deposit, Guarantee or PrePayment rule for the vehicle rental.
    payment_credit_card
        The two character code of a credit card accepted for payment.
    vehicle_charge
        Charges associated with the vehicle rental.
    marketing_information
    policy
    pickup_location_information
        Pickup Location  Information ,  1P only.
    return_location_information
        Return Location  Information ,  1P only.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    vehicle: None | Vehicle = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "required": True,
        },
    )
    operation_time: list[str] = field(
        default_factory=list,
        metadata={
            "name": "OperationTime",
            "type": "Element",
            "max_occurs": 2,
        },
    )
    start_end_times: None | VehicleRulesRsp.StartEndTimes = field(
        default=None,
        metadata={
            "name": "StartEndTimes",
            "type": "Element",
        },
    )
    rental_period_rules: None | VehicleRulesRsp.RentalPeriodRules = field(
        default=None,
        metadata={
            "name": "RentalPeriodRules",
            "type": "Element",
        },
    )
    pre_pay_cancel_info: list[VehicleRulesRsp.PrePayCancelInfo] = field(
        default_factory=list,
        metadata={
            "name": "PrePayCancelInfo",
            "type": "Element",
            "max_occurs": 99,
        },
    )
    payment_rule: list[VehicleRulesRsp.PaymentRule] = field(
        default_factory=list,
        metadata={
            "name": "PaymentRule",
            "type": "Element",
            "max_occurs": 2,
        },
    )
    payment_credit_card: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PaymentCreditCard",
            "type": "Element",
            "max_occurs": 13,
            "length": 2,
        },
    )
    vehicle_charge: list[TypeVehicleCharge] = field(
        default_factory=list,
        metadata={
            "name": "VehicleCharge",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    marketing_information: None | MarketingInformation1 = field(
        default=None,
        metadata={
            "name": "MarketingInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    policy: list[Policy] = field(
        default_factory=list,
        metadata={
            "name": "Policy",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    pickup_location_information: None | TypeVehicleLocationInformation = field(
        default=None,
        metadata={
            "name": "PickupLocationInformation",
            "type": "Element",
        },
    )
    return_location_information: None | TypeVehicleLocationInformation = field(
        default=None,
        metadata={
            "name": "ReturnLocationInformation",
            "type": "Element",
        },
    )

    @dataclass
    class StartEndTimes:
        """
        Parameters
        ----------
        earliest_start
            The earliest a vehicle may be picked up.
        latest_start
            The latest a vehicle may be picked up.
        latest_end
            The latest a vehicle may be dropped off.
        """

        earliest_start: None | TypeStartEndTime = field(
            default=None,
            metadata={
                "name": "EarliestStart",
                "type": "Element",
            },
        )
        latest_start: None | TypeStartEndTime = field(
            default=None,
            metadata={
                "name": "LatestStart",
                "type": "Element",
            },
        )
        latest_end: None | TypeStartEndTime = field(
            default=None,
            metadata={
                "name": "LatestEnd",
                "type": "Element",
            },
        )

    @dataclass
    class RentalPeriodRules:
        """
        Parameters
        ----------
        max_rental
            The maximum rental period for this rate.
        min_rental
            The minimum rental period for this rate.
        absolute_max
            The absolute maximum rental period for this rate.
        """

        max_rental: None | TypeRentalPeriod = field(
            default=None,
            metadata={
                "name": "MaxRental",
                "type": "Element",
            },
        )
        min_rental: None | TypeRentalPeriod = field(
            default=None,
            metadata={
                "name": "MinRental",
                "type": "Element",
            },
        )
        absolute_max: None | TypeRentalPeriod = field(
            default=None,
            metadata={
                "name": "AbsoluteMax",
                "type": "Element",
            },
        )

    @dataclass
    class PrePayCancelInfo:
        """
        Parameters
        ----------
        code
            Code value associated to policy line advisory cancellation text
            (values 001 up to 999) 1P only.
        amount
            Rate amount preceded by the ISO currency code charged to cancel,
            e.g. USD25.00 1P only.
        percent
            Percentage value (e.g. 010=10%     025=25%      050=50%
            100) 1P only.
        number_of_days_hours
            Number of Days or Hours (e.g. 002 days  024 hours), 1P only.
        rental_days
            Number of rental days (e.g. 001 up to 365), 1P only.
        """

        code: None | int = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
                "required": True,
            },
        )
        amount: None | str = field(
            default=None,
            metadata={
                "name": "Amount",
                "type": "Attribute",
            },
        )
        percent: None | int = field(
            default=None,
            metadata={
                "name": "Percent",
                "type": "Attribute",
            },
        )
        number_of_days_hours: None | int = field(
            default=None,
            metadata={
                "name": "NumberOfDaysHours",
                "type": "Attribute",
            },
        )
        rental_days: None | int = field(
            default=None,
            metadata={
                "name": "RentalDays",
                "type": "Attribute",
            },
        )

    @dataclass
    class PaymentRule(TypeDepositGuarantee):
        """
        Parameters
        ----------
        credit_card
            The two character credit card code.
        """

        credit_card: list[str] = field(
            default_factory=list,
            metadata={
                "name": "CreditCard",
                "type": "Element",
                "max_occurs": 13,
                "length": 2,
            },
        )
