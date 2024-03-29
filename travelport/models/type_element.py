from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class TypeElement(Enum):
    """
    Defines the list of available data types for modifications.
    """

    PAYMENT = "Payment"
    CREDIT_CARD_AUTHORIZATION = "CreditCardAuthorization"
    DELIVERY_INFO = "DeliveryInfo"
    FORM_OF_PAYMENT = "FormOfPayment"
    ACTION_STATUS = "ActionStatus"
    OSI = "OSI"
    GENERAL_REMARK = "GeneralRemark"
    UNASSOCIATED_REMARK = "UnassociatedRemark"
    ACCOUNTING_REMARK = "AccountingRemark"
    POST_SCRIPT = "PostScript"
    AIR_RESERVATION_AIR_SEGMENT_UPDATE = "AirReservationAirSegmentUpdate"
    AIR_SEGMENT = "AirSegment"
    PHONE_NUMBER = "PhoneNumber"
    EMAIL = "Email"
    LOYALTY_CARD = "LoyaltyCard"
    SSR = "SSR"
    SEAT_ASSIGNMENT = "SeatAssignment"
    SPECIFIC_SEAT_ASSIGNMENT = "SpecificSeatAssignment"
    AUTO_SEAT_ASSIGNMENT = "AutoSeatAssignment"
    AIR_PRICING_INFO = "AirPricingInfo"
    VEHICLE_SPECIAL_REQUEST = "VehicleSpecialRequest"
    SPECIAL_EQUIPMENT = "SpecialEquipment"
    XMLREMARK = "XMLRemark"
    ADDRESS = "Address"
    TICKETING_MODIFIERS = "TicketingModifiers"
    GUARANTEE = "Guarantee"
    DELIVERY_ADDRESS = "DeliveryAddress"
    SERVICE_FEE_INFO = "ServiceFeeInfo"
    LINKED_UNIVERSAL_RECORD = "LinkedUniversalRecord"
    NAME_REMARK = "NameRemark"
    PASSIVE_SEGMENT = "PassiveSegment"
    PAYMENT_INFORMATION = "PaymentInformation"
    CUSTOMER_ID = "CustomerID"
    DRIVERS_LICENSE = "DriversLicense"
    ASSOCIATED_REMARK = "AssociatedRemark"
    COLLECTION_ADDRESS = "CollectionAddress"
    HOTEL_SPECIAL_REQUEST = "HotelSpecialRequest"
    CORPORATE_DISCOUNT_ID = "CorporateDiscountID"
    COMMISSION_REMARK = "CommissionRemark"
    POCKET_ITINERARY_REMARK = "PocketItineraryRemark"
    CUSTOMIZED_NAME_DATA = "CustomizedNameData"
    INVOICE_REMARK = "InvoiceRemark"
    THIRD_PARTY_INFORMATION = "ThirdPartyInformation"
    TRAVEL_COMPLIANCE = "TravelCompliance"
    REVIEW_BOOKING = "ReviewBooking"
    CONSOLIDATOR_REMARK = "ConsolidatorRemark"
    BOOKING_TRAVELER = "BookingTraveler"
    APPLIED_PROFILE = "AppliedProfile"
    TRIP_NAME = "TripName"
    TRAVEL_PURPOSE = "TravelPurpose"
    BOOKING_CONFIRMATION = "BookingConfirmation"
    BRAND = "Brand"
