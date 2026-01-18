from __future__ import annotations

from dataclasses import dataclass, field

from .fare_structure_type_enumeration import FareStructureTypeEnumeration
from .operator_restrictions_enumeration import OperatorRestrictionsEnumeration
from .tariff_basis_enumeration import TariffBasisEnumeration
from .train_restrictions_enumeration import TrainRestrictionsEnumeration
from .vehicle_collection_enumeration import VehicleCollectionEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ConditionSummaryStructure:
    fare_structure_type: None | FareStructureTypeEnumeration = field(
        default=None,
        metadata={
            "name": "FareStructureType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tariff_basis: None | TariffBasisEnumeration = field(
        default=None,
        metadata={
            "name": "TariffBasis",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_notices: None | bool = field(
        default=None,
        metadata={
            "name": "HasNotices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    provides_card: None | bool = field(
        default=None,
        metadata={
            "name": "ProvidesCard",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    goes_on_card: None | bool = field(
        default=None,
        metadata={
            "name": "GoesOnCard",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_personal: None | bool = field(
        default=None,
        metadata={
            "name": "IsPersonal",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    requires_photo: None | bool = field(
        default=None,
        metadata={
            "name": "RequiresPhoto",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    must_carry: None | bool = field(
        default=None,
        metadata={
            "name": "MustCarry",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    requires_account: None | bool = field(
        default=None,
        metadata={
            "name": "RequiresAccount",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_supplement: None | bool = field(
        default=None,
        metadata={
            "name": "IsSupplement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    requires_entitlement: None | bool = field(
        default=None,
        metadata={
            "name": "RequiresEntitlement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gives_entitlement: None | bool = field(
        default=None,
        metadata={
            "name": "GivesEntitlement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_operator_restrictions: None | OperatorRestrictionsEnumeration = field(
        default=None,
        metadata={
            "name": "HasOperatorRestrictions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_travel_time_restrictions: None | bool = field(
        default=None,
        metadata={
            "name": "HasTravelTimeRestrictions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_route_restrictions: None | bool = field(
        default=None,
        metadata={
            "name": "HasRouteRestrictions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    train_restrictions: None | TrainRestrictionsEnumeration = field(
        default=None,
        metadata={
            "name": "TrainRestrictions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_zone_restrictions: None | bool = field(
        default=None,
        metadata={
            "name": "HasZoneRestrictions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    can_break_journey: None | bool = field(
        default=None,
        metadata={
            "name": "CanBreakJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    return_trips_only: None | bool = field(
        default=None,
        metadata={
            "name": "ReturnTripsOnly",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    night_train: None | bool = field(
        default=None,
        metadata={
            "name": "NightTrain",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    can_change_class: None | bool = field(
        default=None,
        metadata={
            "name": "CanChangeClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_refundable: None | bool = field(
        default=None,
        metadata={
            "name": "IsRefundable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_exchangable: None | bool = field(
        default=None,
        metadata={
            "name": "IsExchangable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_exchange_fee: None | bool = field(
        default=None,
        metadata={
            "name": "HasExchangeFee",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_discounted_fares: None | bool = field(
        default=None,
        metadata={
            "name": "HasDiscountedFares",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    allow_additional_discounts: None | bool = field(
        default=None,
        metadata={
            "name": "AllowAdditionalDiscounts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    allow_companion_discounts: None | bool = field(
        default=None,
        metadata={
            "name": "AllowCompanionDiscounts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_minimum_price: None | bool = field(
        default=None,
        metadata={
            "name": "HasMinimumPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    requires_positive_balance: None | bool = field(
        default=None,
        metadata={
            "name": "RequiresPositiveBalance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    requires_deposit: None | bool = field(
        default=None,
        metadata={
            "name": "RequiresDeposit",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    no_cash_payment: None | bool = field(
        default=None,
        metadata={
            "name": "NoCashPayment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_purchase_conditions: None | bool = field(
        default=None,
        metadata={
            "name": "HasPurchaseConditions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_dynamic_pricing: None | bool = field(
        default=None,
        metadata={
            "name": "HasDynamicPricing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    requires_reservation: None | bool = field(
        default=None,
        metadata={
            "name": "RequiresReservation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_reservation_fee: None | bool = field(
        default=None,
        metadata={
            "name": "HasReservationFee",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_quota: None | bool = field(
        default=None,
        metadata={
            "name": "HasQuota",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    penalty_if_without_ticket: None | bool = field(
        default=None,
        metadata={
            "name": "PenaltyIfWithoutTicket",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    available_on_subscription: None | bool = field(
        default=None,
        metadata={
            "name": "AvailableOnSubscription",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    unlimited_mileage: None | bool = field(
        default=None,
        metadata={
            "name": "UnlimitedMileage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    like_for_like_refuelling: None | bool = field(
        default=None,
        metadata={
            "name": "LikeForLikeRefuelling",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_collection: None | VehicleCollectionEnumeration = field(
        default=None,
        metadata={
            "name": "VehicleCollection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
