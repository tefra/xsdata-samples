from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.saved_trip_activity_type import SavedTripActivityType

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class SavedTripActivity:
    """
    This element ties together related objects for a saved trip.

    Parameters
    ----------
    booking_traveler_ref
        Reference to the associated travelers.
    search_passenger_ref
        Reference to the associated travelers.
    point_of_sale_ref
        Reference to the point of sale present in the saved trip.
    accounting_remark_ref
        Reference to the AccountingRemark present in the saved trip.
    general_remark_ref
        Reference to the GeneralRemark present in the saved trip.
    air_pricing_modifier_ref
        Reference to the Air Pricing modifier present in the saved trip.
    air_pricing_solution_ref
        Reference to the air pricing solution present in the saved trip.
    vehicle_search_modifiers_ref
        Reference to the VehicleSearchModifiers present in the saved trip.
    vehicle_date_location_ref
        Reference to the VehicleDateLocation present in the saved trip.
    special_equipment_ref
        Reference to the SpecialEquipment present in the saved trip.
    vehicle_special_request_ref
        Reference to the VehicleSpecialRequest present in the saved trip.
    payment_information_ref
        Reference to the PaymentInformation present in the saved trip.
    delivery_address_ref
        Reference to the DeliveryAddress present in the saved trip.
    collection_address_ref
        Reference to the CollectionAddress present in the saved trip.
    flight_arrival_information_ref
        Reference to the FlightArrivalInformation present in the saved trip.
    vehicle_ref
        Reference to the Vehicle present in the saved trip.
    vendor_location_ref
        Reference to the VendorLocation present in the saved trip.
    hotel_property_ref
        Reference to the HotelProperty present in the saved trip.
    hotel_stay_ref
        Reference to the HotelStay present in the saved trip.
    hotel_rules_modifiers_ref
        Reference to the HotelRulesModifiers present in the saved trip.
    hotel_details_modifiers_ref
        Reference to the HotelDetailsModifiers present in the saved trip.
    hotel_rate_detail_ref
        Reference to the HotelRateDetail present in the saved trip.
    promotion_code_ref
        Reference to the PromotionCode present in the saved trip.
    rail_pricing_solution_ref
        Reference to the rail pricing solution present in the saved trip.
    type_value
        Service which is the source for the references present in this
        element.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    booking_traveler_ref: list[SavedTripActivity.BookingTravelerRef] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    search_passenger_ref: list[SavedTripActivity.SearchPassengerRef] = field(
        default_factory=list,
        metadata={
            "name": "SearchPassengerRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    point_of_sale_ref: list[SavedTripActivity.PointOfSaleRef] = field(
        default_factory=list,
        metadata={
            "name": "PointOfSaleRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    accounting_remark_ref: list[SavedTripActivity.AccountingRemarkRef] = field(
        default_factory=list,
        metadata={
            "name": "AccountingRemarkRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    general_remark_ref: list[SavedTripActivity.GeneralRemarkRef] = field(
        default_factory=list,
        metadata={
            "name": "GeneralRemarkRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_pricing_modifier_ref: list[SavedTripActivity.AirPricingModifierRef] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingModifierRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_pricing_solution_ref: list[SavedTripActivity.AirPricingSolutionRef] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingSolutionRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    vehicle_search_modifiers_ref: list[SavedTripActivity.VehicleSearchModifiersRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleSearchModifiersRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    vehicle_date_location_ref: list[SavedTripActivity.VehicleDateLocationRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleDateLocationRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    special_equipment_ref: list[SavedTripActivity.SpecialEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "SpecialEquipmentRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    vehicle_special_request_ref: list[SavedTripActivity.VehicleSpecialRequestRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleSpecialRequestRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    payment_information_ref: list[SavedTripActivity.PaymentInformationRef] = field(
        default_factory=list,
        metadata={
            "name": "PaymentInformationRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    delivery_address_ref: list[SavedTripActivity.DeliveryAddressRef] = field(
        default_factory=list,
        metadata={
            "name": "DeliveryAddressRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    collection_address_ref: list[SavedTripActivity.CollectionAddressRef] = field(
        default_factory=list,
        metadata={
            "name": "CollectionAddressRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    flight_arrival_information_ref: list[SavedTripActivity.FlightArrivalInformationRef] = field(
        default_factory=list,
        metadata={
            "name": "FlightArrivalInformationRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    vehicle_ref: list[SavedTripActivity.VehicleRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    vendor_location_ref: list[SavedTripActivity.VendorLocationRef] = field(
        default_factory=list,
        metadata={
            "name": "VendorLocationRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    hotel_property_ref: list[SavedTripActivity.HotelPropertyRef] = field(
        default_factory=list,
        metadata={
            "name": "HotelPropertyRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    hotel_stay_ref: list[SavedTripActivity.HotelStayRef] = field(
        default_factory=list,
        metadata={
            "name": "HotelStayRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    hotel_rules_modifiers_ref: list[SavedTripActivity.HotelRulesModifiersRef] = field(
        default_factory=list,
        metadata={
            "name": "HotelRulesModifiersRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    hotel_details_modifiers_ref: list[SavedTripActivity.HotelDetailsModifiersRef] = field(
        default_factory=list,
        metadata={
            "name": "HotelDetailsModifiersRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    hotel_rate_detail_ref: list[SavedTripActivity.HotelRateDetailRef] = field(
        default_factory=list,
        metadata={
            "name": "HotelRateDetailRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    promotion_code_ref: list[SavedTripActivity.PromotionCodeRef] = field(
        default_factory=list,
        metadata={
            "name": "PromotionCodeRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    rail_pricing_solution_ref: list[SavedTripActivity.RailPricingSolutionRef] = field(
        default_factory=list,
        metadata={
            "name": "RailPricingSolutionRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    type_value: None | SavedTripActivityType = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class BookingTravelerRef:
        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class SearchPassengerRef:
        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class PointOfSaleRef:
        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class AccountingRemarkRef:
        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class GeneralRemarkRef:
        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class AirPricingModifierRef:
        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class AirPricingSolutionRef:
        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class VehicleSearchModifiersRef:
        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class VehicleDateLocationRef:
        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class SpecialEquipmentRef:
        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class VehicleSpecialRequestRef:
        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class PaymentInformationRef:
        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class DeliveryAddressRef:
        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class CollectionAddressRef:
        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class FlightArrivalInformationRef:
        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class VehicleRef:
        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class VendorLocationRef:
        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class HotelPropertyRef:
        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class HotelStayRef:
        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class HotelRulesModifiersRef:
        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class HotelDetailsModifiersRef:
        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class HotelRateDetailRef:
        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class PromotionCodeRef:
        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class RailPricingSolutionRef:
        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )
