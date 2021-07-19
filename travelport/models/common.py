from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration, XmlPeriod

__NAMESPACE__ = "http://www.travelport.com/schema/common_v48_0"


@dataclass
class Arcpayment:
    """
    ARC form of payment.ACH Only.

    Parameters
    ----------
    arcidentifier: Value of the ARC Direct Bill id
    arcpassword: Value of the ARC Direct Bill id password
    """
    class Meta:
        name = "ARCPayment"
        namespace = "http://www.travelport.com/schema/common_v48_0"

    arcidentifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "ARCIdentifier",
            "type": "Attribute",
            "required": True,
            "max_length": 128,
        }
    )
    arcpassword: Optional[str] = field(
        default=None,
        metadata={
            "name": "ARCPassword",
            "type": "Attribute",
            "max_length": 128,
        }
    )


@dataclass
class AccountCode:
    """
    Account Code is used to get Private Fares.If ProviderCode or SupplierCode
    is not specified, it will be considered a default AccounCode to be sent to
    all the Providers or Suppliers.

    Parameters
    ----------
    code:
    provider_code:
    supplier_code:
    type: An identifier to categorize this account code. For example,
        FlightPass for AC Flight Pass or RFB for AC corporate Rewards
        for Business.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "max_length": 36,
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )


class ActionStatusType(Enum):
    """
    Properties
    ----------
    TAW:
    TTL:
    TLCXL:
    ACTIVE:
    CXL:
    TAU: Equivalent to TAX in Worldspan
    TRH:
    """
    TAW = "TAW"
    TTL = "TTL"
    TLCXL = "TLCXL"
    ACTIVE = "ACTIVE"
    CXL = "CXL"
    TAU = "TAU"
    TRH = "TRH"


@dataclass
class AddSvc:
    """1P - Add SVC segments to collect additional fee

    Parameters
    ----------
    rfic: 1P - Reason for issuance
    rfisc: 1P - Resaon for issuance sub-code
    svc_description: 1P - SVC fee description
    origin: Origin location - Airport code. If this value not provided,
        the last air segment arrival location is taken as default. 1P
        only.
    destination: Destination location - Airport code.
    start_date: The start date of the SVC segment. If the value not
        specified, the default value is set as the date next to the last
        airsegment arrival date. 1P only
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    rfic: Optional[str] = field(
        default=None,
        metadata={
            "name": "RFIC",
            "type": "Attribute",
        }
    )
    rfisc: Optional[str] = field(
        default=None,
        metadata={
            "name": "RFISC",
            "type": "Attribute",
        }
    )
    svc_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "SvcDescription",
            "type": "Attribute",
        }
    )
    origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Attribute",
        }
    )


@dataclass
class AgencySellInfo:
    """
    Information about the agency selling the reservation.

    Parameters
    ----------
    iata_code: The IATA code that pertains to this Agency and Branch.
    country: The country code of the requesting agency.
    currency_code: The currency code in which the reservation will be
        ticketed.
    provider_code: The IATA assigned airline/GDS code.
    pseudo_city_code: The PCC in the host system.
    city_code: IATA code of "home" city or airport.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    iata_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "IataCode",
            "type": "Attribute",
            "max_length": 8,
        }
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Attribute",
            "length": 2,
        }
    )
    currency_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurrencyCode",
            "type": "Attribute",
            "length": 3,
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        }
    )
    city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityCode",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )


class AgentActionActionType(Enum):
    CREATED = "Created"
    MODIFIED = "Modified"
    TICKETED = "Ticketed"


@dataclass
class AgentIdoverride:
    """
    Vendor specific agent identifier overrides to be used to access vendor
    systems.

    Parameters
    ----------
    supplier_code: Supplier code to determine which vendor this AgentId
        belongs to.
    provider_code: Provider code to route the AgentId to proper
        provider.
    agent_id: The Agent ID for the applicable supplier/vendor
    """
    class Meta:
        name = "AgentIDOverride"
        namespace = "http://www.travelport.com/schema/common_v48_0"

    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    agent_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgentID",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 32,
        }
    )


@dataclass
class AgentVoucher:
    """
    Agent Voucher Form of Payments.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class AirSearchParameters:
    """
    Search Parameters.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    no_advance_purchase: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoAdvancePurchase",
            "type": "Attribute",
        }
    )
    refundable_fares: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RefundableFares",
            "type": "Attribute",
        }
    )
    non_penalty_fares: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NonPenaltyFares",
            "type": "Attribute",
        }
    )
    un_restricted_fares: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UnRestrictedFares",
            "type": "Attribute",
        }
    )


@dataclass
class Auxdata:
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    entry: List["Auxdata.Entry"] = field(
        default_factory=list,
        metadata={
            "name": "Entry",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )

    @dataclass
    class Entry:
        reason: Optional[str] = field(
            default=None,
            metadata={
                "name": "Reason",
                "type": "Element",
                "required": True,
            }
        )
        description: Optional[str] = field(
            default=None,
            metadata={
                "name": "Description",
                "type": "Element",
                "required": True,
            }
        )


@dataclass
class Bsppayment:
    """
    BSP form of payment.ACH Only.

    Parameters
    ----------
    bspidentifier: Value of the BSP Direct Bill id
    bsppassword: Value of the BSP Direct Bill id password
    """
    class Meta:
        name = "BSPPayment"
        namespace = "http://www.travelport.com/schema/common_v48_0"

    bspidentifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "BSPIdentifier",
            "type": "Attribute",
            "required": True,
            "max_length": 128,
        }
    )
    bsppassword: Optional[str] = field(
        default=None,
        metadata={
            "name": "BSPPassword",
            "type": "Attribute",
            "max_length": 128,
        }
    )


@dataclass
class BaseAsyncProviderSpecificResponse:
    """
    Identifies pending responses from a specific provider using MoreResults
    attribute.

    Parameters
    ----------
    provider_code: Provider code of a specific host
    more_results: Identifies whether more results are available for
        specific host or not.
    """
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    more_results: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MoreResults",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class BillingPointOfSaleInfo:
    """
    Point of Sale information for Billing.

    Parameters
    ----------
    origin_application: Name of the Point of Sale application which
        initiated the Request.This information will be provided as part
        of the provisioning of the user.
    cidbnumber: A 10 Digit customer number generated by CIDB system.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    origin_application: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginApplication",
            "type": "Attribute",
            "required": True,
        }
    )
    cidbnumber: Optional[str] = field(
        default=None,
        metadata={
            "name": "CIDBNumber",
            "type": "Attribute",
            "pattern": r"\d{10}",
        }
    )


@dataclass
class BookingDates:
    """
    Check in and Check out Date information.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    check_in_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "CheckInDate",
            "type": "Attribute",
            "pattern": r"[^:Z].*",
        }
    )
    check_out_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "CheckOutDate",
            "type": "Attribute",
            "pattern": r"[^:Z].*",
        }
    )


class BookingSourceType(Enum):
    """
    Properties
    ----------
    PSEUDO_CITY_CODE:
    ARC_NUMBER:
    IATA_NUMBER:
    CUSTOMER_ID:
    BOOKING_SOURCE_OVERRIDE: The Booking Source Override is usually used
        when the car supplier has assigned a number (which can be
        alpha/numeric) to the agency/e-commerce to use in place of an
        IATA number. Supported provider(s) : 1P/1J
    """
    PSEUDO_CITY_CODE = "PseudoCityCode"
    ARC_NUMBER = "ArcNumber"
    IATA_NUMBER = "IataNumber"
    CUSTOMER_ID = "CustomerId"
    BOOKING_SOURCE_OVERRIDE = "BookingSourceOverride"


@dataclass
class BookingTravelerName:
    """
    Complete name fields.

    Parameters
    ----------
    prefix: Name prefix.
    first: First Name.
    middle: Midle name.
    last: Last Name.
    suffix: Name suffix.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    prefix: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prefix",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 20,
        }
    )
    first: Optional[str] = field(
        default=None,
        metadata={
            "name": "First",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        }
    )
    middle: Optional[str] = field(
        default=None,
        metadata={
            "name": "Middle",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 256,
        }
    )
    last: Optional[str] = field(
        default=None,
        metadata={
            "name": "Last",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        }
    )
    suffix: Optional[str] = field(
        default=None,
        metadata={
            "name": "Suffix",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 256,
        }
    )


@dataclass
class CabinClass:
    """
    Requests cabin class (First, Business and Economy, etc.) as supported by
    the provider or supplier.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Carrier:
    """
    Carrier identifier.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )


@dataclass
class Certificate:
    """
    Certificate Form of Payment.

    Parameters
    ----------
    number: The Certificate number
    amount: The monetary value of the certificate.
    discount_amount: The monetary discount amount of this certificate.
    discount_percentage: The percentage discount value of this
        certificate.
    not_valid_before: The date that this certificate becomes valid.
    not_valid_after: The date that this certificate expires.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
        }
    )
    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        }
    )
    discount_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "DiscountAmount",
            "type": "Attribute",
        }
    )
    discount_percentage: Optional[int] = field(
        default=None,
        metadata={
            "name": "DiscountPercentage",
            "type": "Attribute",
        }
    )
    not_valid_before: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NotValidBefore",
            "type": "Attribute",
        }
    )
    not_valid_after: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NotValidAfter",
            "type": "Attribute",
        }
    )


@dataclass
class Characteristic:
    """
    Identifies the characteristics of the seat with seat type, value and
    description.

    Parameters
    ----------
    seat_type: Indicates codeset of values such as Seat Type like
        Place,Position, Smoking Choice, Place Arrangement, Place
        Direction, Compartment.
    seat_description: Description of the seat type.
    seat_value: Indicates the value specific to the selected type.
    seat_value_description: Description of the seat value.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    seat_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeatType",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 255,
        }
    )
    seat_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeatDescription",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 255,
        }
    )
    seat_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeatValue",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 255,
        }
    )
    seat_value_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeatValueDescription",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 255,
        }
    )


@dataclass
class Check:
    """
    Check Form of Payment.

    Parameters
    ----------
    micrnumber: Magnetic Ink Character Reader Number of check.
    routing_number: The bank routing number of the check.
    account_number: The account number of the check
    check_number: The sequential check number of the check.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    micrnumber: Optional[str] = field(
        default=None,
        metadata={
            "name": "MICRNumber",
            "type": "Attribute",
            "max_length": 29,
        }
    )
    routing_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "RoutingNumber",
            "type": "Attribute",
        }
    )
    account_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountNumber",
            "type": "Attribute",
        }
    )
    check_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "CheckNumber",
            "type": "Attribute",
        }
    )


@dataclass
class ContinuityCheckOverride:
    """
    Parameters
    ----------
    value:
    key: Will use key to map continuity remark to a particular segment
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    value: Optional[str] = field(
        default=None,
        metadata={
            "min_length": 1,
            "white_space": "collapse",
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )


@dataclass
class CorporateDiscountId:
    """
    These are zero or more negotiated rate codes.

    Parameters
    ----------
    value:
    negotiated_rate_code: When set to true, the data in the
        CorporateDiscountID is a negotiated rate code. Otherwise, this
        data is a Corporate Discount ID rate.
    """
    class Meta:
        name = "CorporateDiscountID"
        namespace = "http://www.travelport.com/schema/common_v48_0"

    value: Optional[str] = field(
        default=None
    )
    negotiated_rate_code: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NegotiatedRateCode",
            "type": "Attribute",
        }
    )


@dataclass
class Credentials:
    """
    Container to send login id and password on each request.

    Parameters
    ----------
    user_id: The UserID associated with the entity using this request
        withing this BranchCode.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    user_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "UserId",
            "type": "Attribute",
            "required": True,
            "max_length": 36,
        }
    )


@dataclass
class CreditCardAuth:
    """The result of a Credit Auth Request.

    Will contain all the authorization info and result codes.

    Parameters
    ----------
    key:
    payment_ref:
    trans_id: The transaction id from the credit processing system
    number:
    amount: The amount that was authorized.
    auth_code: The authorization code to confirm card acceptance
    auth_result_code: The result code of the authorization command.
    avsresult_code: The address verification result code (if AVS was
        requested)
    message: The message explains the result of the authorization
        command.
    provider_reservation_info_ref:
    form_of_payment_ref:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    payment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentRef",
            "type": "Attribute",
        }
    )
    trans_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransId",
            "type": "Attribute",
        }
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "min_length": 13,
            "max_length": 128,
        }
    )
    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
        }
    )
    auth_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthCode",
            "type": "Attribute",
        }
    )
    auth_result_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthResultCode",
            "type": "Attribute",
            "required": True,
        }
    )
    avsresult_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AVSResultCode",
            "type": "Attribute",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "name": "Message",
            "type": "Attribute",
        }
    )
    provider_reservation_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        }
    )
    form_of_payment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FormOfPaymentRef",
            "type": "Attribute",
        }
    )


@dataclass
class CustomProfileInformation:
    """
    Custom Profile Field Data required for File Finishing.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"


@dataclass
class CustomizedNameData:
    """
    Customized Name Data is used to print customized name on the different
    documents.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    value: Optional[str] = field(
        default=None
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    provider_reservation_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        }
    )


@dataclass
class DirectPayment:
    """
    Direct Payment Form of Payments.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    text: Optional[str] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Attribute",
        }
    )


@dataclass
class DiscountCardRef:
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


class DistanceUnits(Enum):
    MI = "MI"
    KM = "KM"


@dataclass
class DriversLicenseRef:
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


class EmailNotificationRecipients(Enum):
    ALL = "All"
    DEFAULT = "Default"
    SPECIFIC = "Specific"


@dataclass
class Endorsement:
    """
    Restrictions or instructions about the fare or ticket.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        }
    )


@dataclass
class EnettVan:
    """
    Container for all eNett Van information.

    Parameters
    ----------
    min_percentage: The minimum percentage that will be applied on the
        Total price and sent to enett,which will denote the minimum
        authorized amount approved by eNett.uApi will default this to
        zero for multi-use Van's.
    max_percentage: The maximum percentage that will be applied on the
        Total price and sent to enett, which will denote the maximum
        authorized amount as approved by eNett. This value will be
        ignored and not used for Multi-Use VAN’s.
    expiry_days: The number of days from the VAN generation date that
        the VAN will be active for, after which the VAN cannot be used.
    multi_use: Acceptable values are true or false. If set to true it
        will denote that the VAN being requested is multi-use else it
        will indicate a single -use VAN.A Single use VAN can only be
        debited once while the multiple use VAN's can be debited
        multiple times subjected to the maximum value it has been
        authorized for. The default value will be TRUE to indicate a
        multi-use VAN is being issued.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    min_percentage: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinPercentage",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 100,
        }
    )
    max_percentage: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxPercentage",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 100,
        }
    )
    expiry_days: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ExpiryDays",
            "type": "Attribute",
            "min_inclusive": XmlDuration("P1D"),
            "max_inclusive": XmlDuration("P366D"),
        }
    )
    multi_use: bool = field(
        default=True,
        metadata={
            "name": "MultiUse",
            "type": "Attribute",
        }
    )


@dataclass
class ExchangedCoupon:
    """
    The coupon numbers that were used in the exchange process to create the
    MCO.

    Parameters
    ----------
    ticket_number: The ticket number for which the exchange coupons are
        present.
    coupon_number: Coupon numbers that were exchanged specific to this
        ticket
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    ticket_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Attribute",
            "required": True,
            "length": 13,
        }
    )
    coupon_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "CouponNumber",
            "type": "Attribute",
        }
    )


@dataclass
class FormOfPaymentRef:
    """
    A reference to a Form of Payment in the existing UR.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


class FormattedTextTextTypeTextFormat(Enum):
    """
    Properties
    ----------
    PLAIN_TEXT: Textual data that is in ASCII format.
    HTML: HTML formatted text.
    """
    PLAIN_TEXT = "PlainText"
    HTML = "HTML"


@dataclass
class GuaranteeType:
    """
    A type of guarantee i.e.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    value: Optional[str] = field(
        default=None,
        metadata={
            "max_length": 250,
        }
    )


@dataclass
class IncludedInBase:
    """Shows the taxes and fees included in the base fare.

    (ACH only)

    Parameters
    ----------
    amount: this attribute shows the amount included in the base fare
        for the specific fee or tax
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        }
    )


@dataclass
class IndustryStandardSsr:
    """
    Indicates Carrier Supports this industry standard.

    Parameters
    ----------
    code: This code indicates which Standard of SSR's they support.
        Sucha as the 'AIRIMP' standard identified by 'IATA.org'
    """
    class Meta:
        name = "IndustryStandardSSR"
        namespace = "http://www.travelport.com/schema/common_v48_0"

    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        }
    )


@dataclass
class KeyMapping:
    """
    Element for which mapping key sent in the request is different from the
    mapping key comes in the response.

    Parameters
    ----------
    element_name: Name of the element.
    original_key: The mapping key which is sent in the request.
    new_key: The mapping key that comes in the response.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    element_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ElementName",
            "type": "Attribute",
            "required": True,
        }
    )
    original_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginalKey",
            "type": "Attribute",
            "required": True,
        }
    )
    new_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "NewKey",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Location:
    """
    Used during search to specify an origin or destination location.
    """


@dataclass
class LocatorCode:
    """
    A locator code that identifies a PNR or searches for one.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    value: Optional[str] = field(
        default=None,
        metadata={
            "min_length": 1,
        }
    )


@dataclass
class LoyaltyCardRef:
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


class McofeeInfoFeeAppliesToInd(Enum):
    PER_PERSON = "Per-Person"
    PER_MCO = "Per-MCO"


@dataclass
class Mcoremark:
    """Information related to fare construction, free form text etc.

    of the MCO

    Parameters
    ----------
    value:
    additional_rmk: Indicates if the remark is additional remark or not.
    """
    class Meta:
        name = "MCORemark"
        namespace = "http://www.travelport.com/schema/common_v48_0"

    value: Optional[str] = field(
        default=None
    )
    additional_rmk: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AdditionalRmk",
            "type": "Attribute",
        }
    )


@dataclass
class Mcotext:
    """All type of free format text messages related to MCO like - Command Text, Agent Entry, MCO Modifiers, Text Message

    Parameters
    ----------
    value:
    type: The type of text. Possible values: Command Text, Agent Entry,
        MCO Modifiers, Text Message
    """
    class Meta:
        name = "MCOText"
        namespace = "http://www.travelport.com/schema/common_v48_0"

    value: Optional[str] = field(
        default=None
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )


@dataclass
class MarketingInformation:
    """
    Marketing text or Notices for Suppliers.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    text: List[object] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class MealRequest:
    """
    Special meal requests like Vegetarian.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
            "length": 4,
        }
    )


@dataclass
class MetaData:
    """Extra data to elaborate the parent element.

    This data is primarily informative and is not persisted.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 10,
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 50,
        }
    )


@dataclass
class MiscFormOfPayment:
    """
    Miscellaneous Form of Payments.

    Parameters
    ----------
    credit_card_type: The 2 letter credit/ debit card type or code which
        may not have been issued using the standard bank card types  -
        i.e. an airline issued card
    credit_card_number:
    exp_date: The Expiration date of this card in YYYY-MM format.
    text: Any free form text which may be associated with the
        Miscellaneous Form of Payment. This text may be provider or GDS
        specific
    category: Indicates what Category the Miscellaneous Form Of Payment
        is being used for payment - The category may vary by GDS.
        Allowable values are "Text" "Credit" "CreditCard"
        "FreeFormCreditCard" "Invoice" "NonRefundable"
        "MultipleReceivables" "Exchange" "Cash"
    acceptance_override: Override airline restriction on the credit
        card.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    credit_card_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "CreditCardType",
            "type": "Attribute",
            "length": 2,
        }
    )
    credit_card_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "CreditCardNumber",
            "type": "Attribute",
            "min_length": 13,
            "max_length": 128,
        }
    )
    exp_date: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "ExpDate",
            "type": "Attribute",
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Attribute",
        }
    )
    category: Optional[str] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
            "required": True,
        }
    )
    acceptance_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AcceptanceOverride",
            "type": "Attribute",
        }
    )


class ModificationType(Enum):
    """
    The modification types supported.

    Properties
    ----------
    ADD_SEGMENT: Add a segment to the itinerary
    REMOVE_SEGMENT: Delete a segment from the itinerary
    REPLACE_SEGMENT: Replace a segment in the itinerary with a new
        segment
    ADD_PASSENGER: Add a passenger to the itinerary
    REMOVE_PASSENGER: Remove a passenger from the itinerary
    OPTIONS_ONLY: Modification where only options are added / removed
        from the itinerary
    OTHER: Other modification types
    """
    ADD_SEGMENT = "AddSegment"
    REMOVE_SEGMENT = "RemoveSegment"
    REPLACE_SEGMENT = "ReplaceSegment"
    ADD_PASSENGER = "AddPassenger"
    REMOVE_PASSENGER = "RemovePassenger"
    OPTIONS_ONLY = "OptionsOnly"
    OTHER = "Other"


@dataclass
class Name:
    """
    Complete name fields.

    Parameters
    ----------
    prefix: Name prefix. Size can be up to 20 characters
    first: First Name. Size can be up to 256 characters
    middle: Midle name. Size can be up to 256 characters
    last: Last Name. Size can be up to 256 characters
    suffix: Name suffix. Size can be up to 256 characters
    traveler_profile_id: Traveler Applied Profile ID.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    prefix: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prefix",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 20,
        }
    )
    first: Optional[str] = field(
        default=None,
        metadata={
            "name": "First",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        }
    )
    middle: Optional[str] = field(
        default=None,
        metadata={
            "name": "Middle",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 256,
        }
    )
    last: Optional[str] = field(
        default=None,
        metadata={
            "name": "Last",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        }
    )
    suffix: Optional[str] = field(
        default=None,
        metadata={
            "name": "Suffix",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 256,
        }
    )
    traveler_profile_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "TravelerProfileId",
            "type": "Attribute",
        }
    )


@dataclass
class NameOverride:
    """
    To be used if the name is different from booking travelers in the PNR.

    Parameters
    ----------
    first: First Name.
    last: Last Name.
    age: Age.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    first: Optional[str] = field(
        default=None,
        metadata={
            "name": "First",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        }
    )
    last: Optional[str] = field(
        default=None,
        metadata={
            "name": "Last",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        }
    )
    age: Optional[int] = field(
        default=None,
        metadata={
            "name": "Age",
            "type": "Attribute",
        }
    )


@dataclass
class NextResultReference:
    """
    Container to return/send additional retrieve/request additional search
    results.

    Parameters
    ----------
    value:
    provider_code: The code of the Provider (e.g 1G,1S)
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    value: Optional[str] = field(
        default=None,
        metadata={
            "min_length": 1,
            "white_space": "collapse",
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )


@dataclass
class OperatedBy:
    """
    This is the carrier code to support Cross Accrual.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    value: Optional[str] = field(
        default=None,
        metadata={
            "min_length": 1,
            "white_space": "collapse",
        }
    )


class OptionalServiceApplicabilityType(Enum):
    """
    The different levels at which an optional service may be applied.

    Properties
    ----------
    ITINERARY:
    PASSENGER:
    SEGMENT:
    PASSENGER_SEGMENT:
    PASSENGER_OD: PassengerOD stands for passenger origin destination.
    OTHER:
    """
    ITINERARY = "Itinerary"
    PASSENGER = "Passenger"
    SEGMENT = "Segment"
    PASSENGER_SEGMENT = "PassengerSegment"
    PASSENGER_OD = "PassengerOD"
    OTHER = "Other"


class OptionalServicesTypeCodeGroupType(Enum):
    """
    Properties
    ----------
    ADDITIONAL_OPTION: Identifies an additional option which has to be
        paid for.
    FREE_OPTION: Identifies an additional option which can be selected
        without additional charge
    DISCOUNT_OPTION: Identifies an option included in the base fare, and
        can be de-selected by the user resulting in a discount in the
        price
    """
    ADDITIONAL_OPTION = "AdditionalOption"
    FREE_OPTION = "FreeOption"
    DISCOUNT_OPTION = "DiscountOption"


class OtherGuaranteeInfoType(Enum):
    IATA_ARC_NUMBER = "IATA/ARC Number"
    AGENCY_ADDRESS = "Agency Address"
    DEPOSIT_TAKEN = "Deposit Taken"
    OTHERS = "Others"


@dataclass
class OverridePcc:
    """Used to emulate to another PCC or SID.

    Providers: 1G, 1V, 1P, 1J.

    Parameters
    ----------
    provider_code: The code of the provider (e.g. 1G, 1S)
    pseudo_city_code: The PCC in the host system.
    """
    class Meta:
        name = "OverridePCC"
        namespace = "http://www.travelport.com/schema/common_v48_0"

    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 10,
        }
    )


@dataclass
class OwnershipChange:
    """Element to change the ownership of the PNR in the UR.

    PROVIDER SUPPORTED: Worldspan and JAL.

    Parameters
    ----------
    owning_pcc: New owning PCC of the PNR.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    owning_pcc: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwningPCC",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PaymentAdvice:
    """
    Contains other form of payment for Cruise Reservations.

    Parameters
    ----------
    type: Other Payment Yype. Possible Values: AGC - Agency Check, AGG -
        Agency Guarantee, AWC - Award Check, CSH - Cash Equivalent, DBC
        - Denied Boarding Compensation, MCO - Miscellaneous Charge
        Order, TOO - Tour Order, TOV - Tour Voucher
    document_number: Payment Document Number Examples: 1234567890, R7777
    issue_date: Document Issuance date
    issue_city: City code of document issuance
    original_fop: Original form of payment Examples: CHECK 3500
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
            "max_length": 3,
        }
    )
    document_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocumentNumber",
            "type": "Attribute",
            "required": True,
            "max_length": 22,
        }
    )
    issue_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Attribute",
            "required": True,
        }
    )
    issue_city: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssueCity",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    original_fop: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginalFOP",
            "type": "Attribute",
            "max_length": 19,
        }
    )


@dataclass
class PaymentRef:
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


class PaymentType(Enum):
    """
    Properties
    ----------
    AIRLINE_FEE: Payment for all airline based fees (paper ticket fee,
        SSR, etc.)
    DELIVERY_FEE: Payment for agency ticket delivery fee
    ITINERARY: Payment for all passengers
    PASSENGER: Payment for a single passenger. The BookingTravelerRef
        attribute must be set.
    SERVICE_FEE: Payment for a service fee other than an MCO
    OPTIONAL_SERVICE: Payment for an optional service
    TICKET_FEE: Deprecated
    """
    AIRLINE_FEE = "AirlineFee"
    DELIVERY_FEE = "DeliveryFee"
    ITINERARY = "Itinerary"
    PASSENGER = "Passenger"
    SERVICE_FEE = "ServiceFee"
    OPTIONAL_SERVICE = "OptionalService"
    TICKET_FEE = "TicketFee"


@dataclass
class Penalty:
    """
    Exchange penalty information.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    cancel_refund: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CancelRefund",
            "type": "Attribute",
        }
    )
    non_refundable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NonRefundable",
            "type": "Attribute",
        }
    )
    non_exchangeable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NonExchangeable",
            "type": "Attribute",
        }
    )
    cancelation_penalty: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CancelationPenalty",
            "type": "Attribute",
        }
    )
    reissue_penalty: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReissuePenalty",
            "type": "Attribute",
        }
    )
    non_reissue_penalty: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NonReissuePenalty",
            "type": "Attribute",
        }
    )
    ticket_refund_penalty: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TicketRefundPenalty",
            "type": "Attribute",
        }
    )
    charge_applicable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ChargeApplicable",
            "type": "Attribute",
        }
    )
    charge_portion: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ChargePortion",
            "type": "Attribute",
        }
    )
    penalty_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "PenaltyAmount",
            "type": "Attribute",
        }
    )


@dataclass
class PersonalGeography:
    """
    Personal geography details of the associated passenger.

    Parameters
    ----------
    country_code: Passenger country code.
    state_province_code: Passenger state/province code.
    city_code: Passenger city code.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    country_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CountryCode",
            "type": "Element",
            "length": 2,
        }
    )
    state_province_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "StateProvinceCode",
            "type": "Element",
            "max_length": 6,
        }
    )
    city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityCode",
            "type": "Element",
            "length": 3,
        }
    )


class PhoneNumberType(Enum):
    AGENCY = "Agency"
    BUSINESS = "Business"
    MOBILE = "Mobile"
    HOME = "Home"
    FAX = "Fax"
    HOTEL = "Hotel"
    OTHER = "Other"
    NONE = "None"
    EMAIL = "Email"
    RESERVATIONS = "Reservations"


@dataclass
class PointOfCommencement:
    """Point of Commencement is optional.

    CityOrAirportCode and date portion of the Time attribute is
    mandatory.

    Parameters
    ----------
    city_or_airport_code: Three digit Airport or City code that would be
        the Point of Commencement location for the trips/legs mentioned.
    time: Specify a date or date and time
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    city_or_airport_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOrAirportCode",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    time: Optional[str] = field(
        default=None,
        metadata={
            "name": "Time",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PointOfSale:
    """User can use this node to send a specific PCC to access fares allowed
    only for that PCC.

    This node gives the capability for fare redistribution at UR level.  For fare redistribution at the stored fare level see AirPricingSolution/AirPricingInfo/AirPricingModifiers/PointOfSale.

    Parameters
    ----------
    provider_code: The provider in which the PCC is defined.
    pseudo_city_code: The PCC in the host system.
    key:
    iata: Used for rapid reprice. This field is the IATA associated to
        this Point of Sale PCC. Providers: 1G/1V
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 10,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    iata: Optional[str] = field(
        default=None,
        metadata={
            "name": "IATA",
            "type": "Attribute",
            "max_length": 8,
        }
    )


@dataclass
class PriceMatchError:
    """
    Parameters
    ----------
    error_message:
    vendor_code: The code of the vendor (e.g.  HZ, etc.)
    hotel_chain: 2 Letter Hotel Chain Code
    hotel_code: Unique hotel identifier for the channel.
    req_base: BaseRate in the request.
    rsp_base: BaseRate retruned from the supplier.
    base_diff: BaseRate Difference.
    req_total: Estimated Total Amount in the request.
    rsp_total: Estimated Total Amount returned from the supplier.
    total_diff: Estimated Total Amount difference.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    error_message: Optional[str] = field(
        default=None,
        metadata={
            "name": "ErrorMessage",
            "type": "Element",
            "required": True,
        }
    )
    vendor_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "VendorCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        }
    )
    hotel_chain: Optional[str] = field(
        default=None,
        metadata={
            "name": "HotelChain",
            "type": "Attribute",
            "length": 2,
        }
    )
    hotel_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "HotelCode",
            "type": "Attribute",
            "max_length": 32,
        }
    )
    req_base: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ReqBase",
            "type": "Attribute",
        }
    )
    rsp_base: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RspBase",
            "type": "Attribute",
        }
    )
    base_diff: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BaseDiff",
            "type": "Attribute",
        }
    )
    req_total: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ReqTotal",
            "type": "Attribute",
        }
    )
    rsp_total: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RspTotal",
            "type": "Attribute",
        }
    )
    total_diff: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TotalDiff",
            "type": "Attribute",
        }
    )


@dataclass
class Provider:
    """
    Provider identifier.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )


@dataclass
class ProviderReservationInfoRef:
    """
    Container for Provider reservation reference key.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PseudoCityCode:
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    value: Optional[str] = field(
        default=None,
        metadata={
            "min_length": 2,
            "max_length": 10,
        }
    )


@dataclass
class QueueSelector:
    """
    Identifies the Queue with Queue Number , Category and Date Range.

    Parameters
    ----------
    queue: Queue Number . Possible values are 01, AA , A1 etc.
    category: Queue Category Number. 2 Character Alpha or Numeric
        Number. Either Alpha or Numeric Number is allowed. If using for
        Sabre is mandatory and is Prefatory Instruction Code value of
        0-999.
    date_range: Date range number where the PNR should be queued.
        Possible values are 1,2,1-4 etc.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    queue: Optional[str] = field(
        default=None,
        metadata={
            "name": "Queue",
            "type": "Attribute",
        }
    )
    category: Optional[str] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
        }
    )
    date_range: Optional[str] = field(
        default=None,
        metadata={
            "name": "DateRange",
            "type": "Attribute",
        }
    )


@dataclass
class ReferencePoint:
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    value: Optional[str] = field(
        default=None,
        metadata={
            "max_length": 30,
        }
    )


@dataclass
class RefundRemark:
    """
    A textual remark displayed in Refund Quote and Refund response.

    Parameters
    ----------
    remark_data: Actual remark data.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    remark_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "RemarkData",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Remark:
    """A textual remark container to hold any printable text.

    (max 512 chars)
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    value: Optional[str] = field(
        default=None
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )


class RequiredFieldName(Enum):
    CARD_TYPE = "CardType"
    NUMBER = "Number"
    CUSTOMER_REFERENCE = "CustomerReference"
    ISSUE_NUMBER = "IssueNumber"
    START_DATE = "StartDate"
    NAME_ON_CARD = "NameOnCard"
    EXPIRATION_DATE = "ExpirationDate"
    CVV = "CVV"
    ADDRESS_LINE1 = "AddressLine1"
    ADDRESS_LINE2 = "AddressLine2"
    CITY = "City"
    STATE = "State"
    POSTAL_CODE = "PostalCode"


class RequisitionCategory(Enum):
    GOVERNMENT = "Government"
    OTHER = "Other"


class RequisitionType(Enum):
    CASH = "Cash"
    CREDIT = "Credit"


class ResponseMessageType(Enum):
    WARNING = "Warning"
    ERROR = "Error"
    INFO = "Info"


@dataclass
class Restriction:
    """
    Which activities are supported for a particular element.

    Parameters
    ----------
    operation: The operation that is restricted
    reason: The reason it is restricted
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    operation: Optional[str] = field(
        default=None,
        metadata={
            "name": "Operation",
            "type": "Attribute",
            "required": True,
        }
    )
    reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reason",
            "type": "Attribute",
        }
    )


@dataclass
class RoleInfo:
    """
    Container to specify the role of the agent.

    Parameters
    ----------
    id: Unique identifier of the role.
    name: Agent's role name
    source: Role inheritance level. Needed in the response, not in the
        request
    description: Description of role
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "required": True,
            "max_length": 19,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "max_length": 128,
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Attribute",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "max_length": 1024,
        }
    )


class SearchTicketingReservationStatus(Enum):
    ON_HOLD = "OnHold"
    SET_FOR_TICKETING = "SetForTicketing"
    BOTH = "Both"


class SearchTicketingTicketStatus(Enum):
    TICKETED = "Ticketed"
    UNTICKETED = "Unticketed"
    BOTH = "Both"


@dataclass
class SeatAttribute:
    """
    Identifies the seat attribute of the service.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 2,
        }
    )


@dataclass
class SegmentRemark:
    """A textual remark container to hold any printable text.

    (max 512 chars)
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    value: Optional[str] = field(
        default=None
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class SellMessage:
    """Sell Message from Vendor.

    This is applicable in response messages only, any input in request
    message will be ignored.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    value: Optional[str] = field(
        default=None
    )


@dataclass
class ServiceFeeTaxInfo:
    """
    The taxes associated to a particular Service Fee.

    Parameters
    ----------
    category: The tax category represents a valid IATA tax code.
    amount:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    category: Optional[str] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
            "required": True,
        }
    )
    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ShopInformation:
    """
    Shopping Information required for File Finishing.

    Parameters
    ----------
    search_request: Search parameters that were used in LFS request
    flights_offered: Flights with lowest logical airfare returned as
        response to LFS request
    cabin_shopped:
    cabin_selected:
    lowest_fare_offered:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    search_request: List["ShopInformation.SearchRequest"] = field(
        default_factory=list,
        metadata={
            "name": "SearchRequest",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    flights_offered: List["ShopInformation.FlightsOffered"] = field(
        default_factory=list,
        metadata={
            "name": "FlightsOffered",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    cabin_shopped: Optional[str] = field(
        default=None,
        metadata={
            "name": "CabinShopped",
            "type": "Attribute",
        }
    )
    cabin_selected: Optional[str] = field(
        default=None,
        metadata={
            "name": "CabinSelected",
            "type": "Attribute",
        }
    )
    lowest_fare_offered: Optional[str] = field(
        default=None,
        metadata={
            "name": "LowestFareOffered",
            "type": "Attribute",
        }
    )

    @dataclass
    class SearchRequest:
        """
        Parameters
        ----------
        origin:
        destination:
        departure_time: Date and Time at which this entity departs. This
            does not include Time Zone information since it can be
            derived from origin location
        class_of_service:
        """
        origin: Optional[str] = field(
            default=None,
            metadata={
                "name": "Origin",
                "type": "Attribute",
                "length": 3,
                "white_space": "collapse",
            }
        )
        destination: Optional[str] = field(
            default=None,
            metadata={
                "name": "Destination",
                "type": "Attribute",
                "length": 3,
                "white_space": "collapse",
            }
        )
        departure_time: Optional[str] = field(
            default=None,
            metadata={
                "name": "DepartureTime",
                "type": "Attribute",
            }
        )
        class_of_service: Optional[str] = field(
            default=None,
            metadata={
                "name": "ClassOfService",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 2,
            }
        )

    @dataclass
    class FlightsOffered:
        """
        Parameters
        ----------
        origin:
        destination:
        departure_time: Date and Time at which this entity departs. This
            does not include Time Zone information since it can be
            derived from origin location
        travel_order:
        carrier:
        flight_number:
        class_of_service:
        stop_over:
        connection:
        """
        origin: Optional[str] = field(
            default=None,
            metadata={
                "name": "Origin",
                "type": "Attribute",
                "length": 3,
                "white_space": "collapse",
            }
        )
        destination: Optional[str] = field(
            default=None,
            metadata={
                "name": "Destination",
                "type": "Attribute",
                "length": 3,
                "white_space": "collapse",
            }
        )
        departure_time: Optional[str] = field(
            default=None,
            metadata={
                "name": "DepartureTime",
                "type": "Attribute",
            }
        )
        travel_order: Optional[int] = field(
            default=None,
            metadata={
                "name": "TravelOrder",
                "type": "Attribute",
            }
        )
        carrier: Optional[str] = field(
            default=None,
            metadata={
                "name": "Carrier",
                "type": "Attribute",
                "length": 2,
            }
        )
        flight_number: Optional[str] = field(
            default=None,
            metadata={
                "name": "FlightNumber",
                "type": "Attribute",
                "max_length": 5,
            }
        )
        class_of_service: Optional[str] = field(
            default=None,
            metadata={
                "name": "ClassOfService",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 2,
            }
        )
        stop_over: bool = field(
            default=False,
            metadata={
                "name": "StopOver",
                "type": "Attribute",
            }
        )
        connection: bool = field(
            default=False,
            metadata={
                "name": "Connection",
                "type": "Attribute",
            }
        )


@dataclass
class SimpleName:
    """
    Free text name.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    value: Optional[str] = field(
        default=None
    )


@dataclass
class State:
    """
    Container to house the state code for an address.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    value: Optional[str] = field(
        default=None
    )


@dataclass
class StockControl:
    """
    The Stock Control Numbers related details of the MCO.

    Parameters
    ----------
    type: Stock control type valid options include: Pending, Failed,
        Plain Paper, Blank, Suppressed.
    number: Stock control number.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
        }
    )


@dataclass
class TaxDetail:
    """
    The tax idetail nformation for a fare quote tax.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
        }
    )
    origin_airport: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginAirport",
            "type": "Attribute",
            "length": 3,
        }
    )
    destination_airport: Optional[str] = field(
        default=None,
        metadata={
            "name": "DestinationAirport",
            "type": "Attribute",
            "length": 3,
        }
    )
    country_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CountryCode",
            "type": "Attribute",
        }
    )
    fare_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareInfoRef",
            "type": "Attribute",
        }
    )


@dataclass
class TerminalSessionInfo:
    """Travelport use only.

    This element contains CDATA information representing existing GDS
    session data or ACH credentials information of the terminal user
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    value: Optional[str] = field(
        default=None
    )


@dataclass
class TicketNumber:
    """
    The identifying number for the actual ticket.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    value: Optional[str] = field(
        default=None,
        metadata={
            "min_length": 1,
            "max_length": 13,
        }
    )


@dataclass
class TravelInfo:
    """
    Traveler information details like Travel Purpose and Trip Name.

    Parameters
    ----------
    trip_name: Trip Name
    travel_purpose: Purpose of the trip
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    trip_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "TripName",
            "type": "Attribute",
            "max_length": 50,
        }
    )
    travel_purpose: Optional[str] = field(
        default=None,
        metadata={
            "name": "TravelPurpose",
            "type": "Attribute",
            "max_length": 50,
        }
    )


@dataclass
class TravelerType:
    """
    The 3-char IATA traveler type code.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 3,
            "max_length": 5,
        }
    )


class UrticketStatus(Enum):
    """
    Information on whether the Universal Record ticket status is Ticketed,
    Unticketed , Partially Ticketed or Not Applicable status.
    """
    TICKETED = "Ticketed"
    UNTICKETED = "Unticketed"
    PARTIALLY_TICKETED = "Partially Ticketed"
    NOT_APPLICABLE = "Not Applicable"


@dataclass
class UnitedNations:
    """
    United Nations Form of Payments.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
        }
    )


class AttrDocumentDocumentType(Enum):
    SERVICE_FEE = "Service Fee"
    PAPER_TICKET = "Paper Ticket"
    MCO = "MCO"
    E_TICKET = "E-Ticket"


class AttrFlexShoppingTier(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class TypeAdjustmentTarget(Enum):
    BASE = "Base"
    TOTAL = "Total"
    OTHER = "Other"


class TypeAdjustmentType(Enum):
    AMOUNT = "Amount"
    PERCENTAGE = "Percentage"


@dataclass
class TypeAgencyPayment:
    """
    Type for Agency Payment.

    Parameters
    ----------
    agency_billing_identifier: Value of the billing id
    agency_billing_number: Value of billing number
    agency_billing_password: Value of billing password
    """
    class Meta:
        name = "typeAgencyPayment"

    agency_billing_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgencyBillingIdentifier",
            "type": "Attribute",
            "required": True,
            "max_length": 128,
        }
    )
    agency_billing_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgencyBillingNumber",
            "type": "Attribute",
            "max_length": 128,
        }
    )
    agency_billing_password: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgencyBillingPassword",
            "type": "Attribute",
            "max_length": 128,
        }
    )


class TypeAgencyProfileLevel(Enum):
    """
    Profile levels in the Agency Hierarchy.
    """
    AGENCY = "Agency"
    BRANCH = "Branch"
    BRANCH_GROUP = "BranchGroup"
    AGENT = "Agent"


@dataclass
class TypeAgentInfo:
    class Meta:
        name = "typeAgentInfo"


@dataclass
class TypeBookingTransactionsAllowed:
    """
    Parameters
    ----------
    booking_enabled: Allow or prohibit booking transaction for the given
        product type on this Provider/Supplier. Inheritable.
    """
    class Meta:
        name = "typeBookingTransactionsAllowed"

    booking_enabled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BookingEnabled",
            "type": "Attribute",
        }
    )


class TypeCommissionLevel(Enum):
    """
    ATA/IATA Standard commission level.
    """
    RECALLED = "Recalled"
    FARE = "Fare"
    PENALTY = "Penalty"


class TypeCommissionModifier(Enum):
    """
    Optional commission modifier.

    Properties
    ----------
    FARE_PERCENT: Commission percentage applied to the fare
    FARE_AMOUNT: Commission amount applied to the fare
    COMMISSION_AMOUNT: Specific commission amount to be applied
    LESS_STANDARD_COMMISSION: Indicates commission percentage applied to
        the fare less the standard commission
    STANDARD_PLUS_SUPPLEMENTARY_PERCENT: Indicates commission percentage
        includes standard and supplementary commission
    SUPPLEMENTARY_PERCENT: Supplementary commission percent which is
        applied to the fare
    SUPPLEMENTARY_AMOUNT: Supplementary commission amount which is
        applied to the fare
    """
    FARE_PERCENT = "FarePercent"
    FARE_AMOUNT = "FareAmount"
    COMMISSION_AMOUNT = "CommissionAmount"
    LESS_STANDARD_COMMISSION = "LessStandardCommission"
    STANDARD_PLUS_SUPPLEMENTARY_PERCENT = "StandardPlusSupplementaryPercent"
    SUPPLEMENTARY_PERCENT = "SupplementaryPercent"
    SUPPLEMENTARY_AMOUNT = "SupplementaryAmount"


class TypeCommissionType(Enum):
    """
    Types of possible commission.
    """
    FLAT = "Flat"
    PERCENT_BASE = "PercentBase"
    PERCENT_TOTAL = "PercentTotal"


@dataclass
class TypeDateRange:
    """
    Specify a range of dates.
    """
    class Meta:
        name = "typeDateRange"

    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Attribute",
            "required": True,
        }
    )
    end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Attribute",
            "required": True,
        }
    )


class TypeDirection(Enum):
    """
    Defines the Direction for Incoming or Outgoing.
    """
    INCOMING = "Incoming"
    OUTGOING = "Outgoing"


class TypeDistance(Enum):
    """
    2 Letter distance unit code.
    """
    MI = "MI"
    KM = "KM"


class TypeDoorCount(Enum):
    TWO_TO_THREE_DOORS = "TwoToThreeDoors"
    TWO_TO_FOUR_DOORS = "TwoToFourDoors"
    FOUR_TO_FIVE_DOORS = "FourToFiveDoors"


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


class TypeElementStatus(Enum):
    """Values to specify the state of the element.

    "A" refers to "Add" , "M" refers to "Modified" and "C" refers to
    error conditions when value provided in "Key" attribute is not
    retained in response
    """
    A = "A"
    M = "M"
    C = "C"


class TypeEventType(Enum):
    """
    The various reservation events (book, cancel, void, etc)
    """
    CREATE = "Create"
    CANCEL = "Cancel"
    TICKET = "Ticket"
    REFUND = "Refund"
    EXCHANGE = "Exchange"
    VOID = "Void"


class TypeFarePull(Enum):
    REVERSE_OF_ORIGIN_DESTINATION = "ReverseOfOriginDestination"
    SAME_AS_ORIGIN_DESTINATION = "SameAsOriginDestination"


@dataclass
class TypeFormOfPaymentPnrreference:
    """
    Parameters
    ----------
    key: Unique ID to identify a ProviderReservationInfo
    provider_reservation_level: It means that the form of payment is
        applied at ProviderReservation level.
    """
    class Meta:
        name = "typeFormOfPaymentPNRReference"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    provider_reservation_level: bool = field(
        default=True,
        metadata={
            "name": "ProviderReservationLevel",
            "type": "Attribute",
        }
    )


class TypeFormOfRefund(Enum):
    MCO = "MCO"
    FORM_OF_PAYMENT = "FormOfPayment"


class TypeFuel(Enum):
    PETROL = "Petrol"
    DIESEL = "Diesel"
    HYBRID = "Hybrid"
    ELECTRIC = "Electric"
    LPGCNG = "LPGCNG"
    HYDROGEN = "Hydrogen"
    MULTI_FUEL = "MultiFuel"
    ETHANOL = "Ethanol"


class TypeFulfillmentIdtype(Enum):
    """
    IdentificationType to define how the customer will identify himself when
    collecting the ticket.
    """
    BAHN_CARD = "Bahn Card"
    CREDIT_CARD = "Credit Card"
    EURO_CHEQUE_CARD = "Euro Cheque Card"
    COLLECTION_REFERENCE = "Collection Reference"


class TypeFulfillmentType(Enum):
    """
    Defines how the client wishes to receive travel documents, e.g. collect
    ticket at a kiosk, print in agency.
    """
    KIOSK = "Kiosk"
    TRAVEL_AGENCY = "Travel Agency"
    COURIER = "Courier"
    STANDARD_MAIL = "Standard Mail"
    TICKETLESS = "Ticketless"
    TICKET_OFFICE = "Ticket Office"
    EXPRESS_MAIL = "Express Mail"
    CORPORATE_KIOSK = "Corporate Kiosk"
    TRAIN_STATION_SERVICE_DESK = "Train Station Service Desk"
    DIRECT_PRINTING_OF_TICKET = "Direct Printing of Ticket"
    PRINTING_OF_TICKET_AT_HOME = "Printing of Ticket at Home"
    DIGITAL_PRINTING_OF_TICKET_AT_HOME = "Digital Printing of Ticket at Home"
    RETRIEVE_TICKET_AT_EUROSTAR_IN_LONDON = "Retrieve Ticket at Eurostar in London"


@dataclass
class TypeGeneralReference:
    class Meta:
        name = "typeGeneralReference"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


class TypeGuaranteeInformationAgencyType(Enum):
    AGENCY_IATA = "AgencyIATA"
    OTHER_AGENCY_IATA = "OtherAgencyIATA"


class TypeGuaranteeInformationType(Enum):
    GUARANTEE = "Guarantee"
    DEPOSIT = "Deposit"


class TypeImageSize(Enum):
    """The image size.

    T - Thumbnail
    I - Minimum
    S - Small
    M - Medium
    L - Large
    E - Extra Large
    G - Guaranteed
    F - Forced
    B - Big
    J - Jumbo
    O - Original
    H - Huge
    C - Colossal
    """
    T = "T"
    I = "I"
    S = "S"
    M = "M"
    L = "L"
    E = "E"
    G = "G"
    F = "F"
    B = "B"
    J = "J"
    O = "O"
    H = "H"
    C = "C"


class TypeInvoiceRecordCategory(Enum):
    """
    Invoice record type: Invoice, Void, Refund, Manual.
    """
    INVOICE = "Invoice"
    VOID = "Void"
    REFUND = "Refund"
    MANUAL = "Manual"


class TypeItineraryCode(Enum):
    """
    Properties
    ----------
    INTERNATIONAL: Indicates the itinerary is International
    DOMESTIC: Indicates the itinerary is domestic
    """
    INTERNATIONAL = "International"
    DOMESTIC = "Domestic"


class TypeItineraryType(Enum):
    """
    Properties
    ----------
    NEW: Indicates the itinerary is New
    ORIGINAL: Indicates the itinerary is Original
    """
    NEW = "New"
    ORIGINAL = "Original"


@dataclass
class TypeKeyBasedReference:
    """
    Generic type to be used for Key based reference.
    """
    class Meta:
        name = "typeKeyBasedReference"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


class TypeLicenseCode(Enum):
    """
    The type of license assigned to an agent.
    """
    STANDARD = "Standard"
    STANDARD_PLUS = "Standard Plus"
    ENTERPRISE = "Enterprise"
    TE_ONLY = "TE Only"
    U_API = "uAPI"


class TypeLoggingLevel(Enum):
    """
    The type of various Logging levels.
    """
    TRACE = "TRACE"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    FATAL = "FATAL"


class TypeMcofeeType(Enum):
    """
    The available Airline service fee types for an MCO.
    """
    CURRENTLY = "CURRENTLY"
    UNDEFINED = "UNDEFINED"


class TypeMcostatus(Enum):
    """
    The available status codes for an MCO.
    """
    OPEN = "Open"
    USED = "Used"
    REFUNDED = "Refunded"
    VOIDED = "Voided"
    EXPIRED = "Expired"


class TypeMcotype(Enum):
    """
    The available types for an MCO.
    """
    AGENCY_SERVICE_FEE = "AgencyServiceFee"
    EXCHANGE_RESIDUAL = "ExchangeResidual"
    AIRLINE_SERVICE_FEE = "AirlineServiceFee"


@dataclass
class TypeNonAirReservationRef:
    class Meta:
        name = "typeNonAirReservationRef"

    locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )


@dataclass
class TypeOtasubKey:
    """
    The attributes and elements in a SubKey.

    Parameters
    ----------
    text: Information for a sub key.
    name: A subkey to identify the special equipment codes. Applicable
        when Policy/@Name is EQUIP. Uses OTA CODE "EQP". 1P/1J.
    description: A brief description of a subkey.
    """
    class Meta:
        name = "typeOTASubKey"

    text: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    name: Optional[int] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
        }
    )


class TypeOtherImageSize(Enum):
    """
    Other unknown image sizes.
    """
    X = "X"


class TypePolicy(Enum):
    """
    Available product types.
    """
    AIR = "Air"
    VEHICLE = "Vehicle"
    HOTEL = "Hotel"
    RAIL = "Rail"
    TICKETING = "Ticketing"


@dataclass
class TypePolicyCodesList:
    """
    Parameters
    ----------
    policy_code: A code that indicates why an item was determined to be
        ‘out of policy’.
    min_policy_code: A code that indicates why the minimum fare or rate
        was determined to be ‘out of policy’.
    max_policy_code: A code that indicates why the maximum fare or rate
        was determined to be ‘out of policy’.
    """
    class Meta:
        name = "typePolicyCodesList"

    policy_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PolicyCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 10,
        }
    )
    min_policy_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MinPolicyCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 10,
        }
    )
    max_policy_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MaxPolicyCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 10,
        }
    )


class TypePriceClassOfService(Enum):
    CLASS_BOOKED = "ClassBooked"
    LOWEST_CLASS = "LowestClass"


class TypePricingType(Enum):
    CLASS_BOOKED = "ClassBooked"
    LOWEST_CLASS = "LowestClass"
    LOWEST_QUOTE = "LowestQuote"


class TypeProduct(Enum):
    """
    Available product types.
    """
    AIR = "Air"
    VEHICLE = "Vehicle"
    HOTEL = "Hotel"
    RAIL = "Rail"
    CRUISE = "Cruise"
    OTHER = "Other"


class TypeProfileApplicability(Enum):
    """
    The applicability of the profile or profile template value.
    """
    ALWAYS = "Always"
    OPTIONAL = "Optional"
    NEVER = "Never"


class TypeProfileEntityStatus(Enum):
    """Status of the given profile/entity.

    Any profile with a status other than Active cannot perform most
    transactions.
    """
    ACTIVE = "Active"
    INACTIVE = "Inactive"


class TypeProfileEntityStatusWithDelete(Enum):
    """
    Specify whether the change is to update or delete the field.
    """
    DELETED = "Deleted"
    ACTIVE = "Active"
    INACTIVE = "Inactive"


class TypeProfileLevel(Enum):
    """
    The type of the profile or profile template.
    """
    AGENCY = "Agency"
    BRANCH = "Branch"
    BRANCH_GROUP = "BranchGroup"
    AGENT = "Agent"
    ACCOUNT = "Account"
    TRAVELER_GROUP = "TravelerGroup"
    TRAVELER = "Traveler"


class TypeProfileLevelWithCredential(Enum):
    """
    The "profile level" used for association of workflow etc.
    """
    AGENCY = "Agency"
    BRANCH = "Branch"
    AGENT = "Agent"


class TypeProfileLevelWithSystem(Enum):
    """
    The "profile level" used for association of workflow etc.
    """
    SYSTEM = "System"
    AGENCY = "Agency"
    BRANCH = "Branch"
    BRANCH_GROUP = "BranchGroup"
    AGENT = "Agent"
    ACCOUNT = "Account"
    TRAVELER_GROUP = "TravelerGroup"
    TRAVELER = "Traveler"


class TypeProfileType(Enum):
    """
    A type for unique party identifiers of any party role.
    """
    AGENCY_GROUP = "AgencyGroup"
    AGENCY = "Agency"
    BRANCH_GROUP = "BranchGroup"
    BRANCH = "Branch"
    AGENT = "Agent"
    ACCOUNT = "Account"
    TRAVELER_GROUP = "TravelerGroup"
    TRAVELER = "Traveler"


@dataclass
class TypeProviderReservationDetail:
    """Details of a provider reservation locator consisting of provider locator
    code and provider code.

    To be used as a request element type while accessing a specific PNR
    """
    class Meta:
        name = "typeProviderReservationDetail"

    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    provider_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "required": True,
            "max_length": 15,
        }
    )


class TypeProviderToken(Enum):
    """
    List of known hosts with terminal access.
    """
    SABRE = "Sabre"


class TypePurchaseWindow(Enum):
    """
    The purchase windows available for merchandising service.
    """
    BOOKING_ONLY = "BookingOnly"
    TICKETING_ONLY = "TicketingOnly"
    CHECK_IN_ONLY = "CheckInOnly"
    ANYTIME = "Anytime"
    POST_TICKETING = "PostTicketing"


class TypeQueueModifyAction(Enum):
    """
    Queue action: remove, requeue, move, add, unlock.
    """
    REMOVE = "Remove"
    REQUEUE = "Requeue"
    MOVE = "Move"
    ADD = "Add"
    UNLOCK = "Unlock"


class TypeRateCategory(Enum):
    """
    The category of the rate (Best, etc)
    """
    ASSOCIATION = "Association"
    BUSINESS = "Business"
    CORPORATE = "Corporate"
    GOVERNMENT = "Government"
    INDUSTRY = "Industry"
    PACKAGE = "Package"
    INCLUSIVE = "Inclusive"
    PROMOTIONAL = "Promotional"
    CREDENTIAL = "Credential"
    STANDARD = "Standard"
    CONSORTIUM = "Consortium"
    CONVENTION = "Convention"
    NEGOTIATED = "Negotiated"
    PREPAY = "Prepay"


@dataclass
class TypeRateDescription:
    """
    Parameters
    ----------
    text:
    name: Optional context name of the text block being returned i.e.
        Room details
    """
    class Meta:
        name = "typeRateDescription"

    text: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        }
    )


class TypeRateGuarantee(Enum):
    """
    The guarantee for this rate.
    """
    RATE_GUARANTEED = "Rate Guaranteed"
    RATE_QUOTED = "Rate Quoted"
    AGENT_ENTERED = "Agent Entered"


class TypeRateTimePeriod(Enum):
    """
    The period for the rate code (daily, weekly, etc)
    """
    HOURLY = "Hourly"
    DAILY = "Daily"
    WEEKLY = "Weekly"
    MONTHLY = "Monthly"
    WEEKEND_DAY = "WeekendDay"
    OTHER = "Other"
    PACKAGE = "Package"
    BUNDLE = "Bundle"
    TOTAL = "Total"


class TypeRecordStatus(Enum):
    """
    Information on whether the Universal Record is Current, Past , Cancelled or
    Any status.
    """
    ALL = "All"
    PAST = "Past"
    CURRENT = "Current"
    CANCELED = "Canceled"
    UNKNOWN = "Unknown"


@dataclass
class TypeRemark:
    """
    Parameters
    ----------
    value:
    provider_reservation_info_ref: Provider reservation reference key.
    provider_code: Contains the Provider Code of the provider for which
        this element is used
    """
    class Meta:
        name = "typeRemark"

    value: Optional[str] = field(
        default=None
    )
    provider_reservation_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )


@dataclass
class TypeRemarkWithTravelerRef:
    """
    Parameters
    ----------
    remark_data: Actual remarks data.
    booking_traveler_ref: Reference to Booking Traveler.
    provider_reservation_info_ref: Provider reservation reference key.
    provider_code: Contains the Provider Code of the provider for which
        this element is used
    """
    class Meta:
        name = "typeRemarkWithTravelerRef"

    remark_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "RemarkData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "required": True,
        }
    )
    booking_traveler_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    provider_reservation_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )


class TypeReqSeat(Enum):
    ANY = "Any"
    AISLE = "Aisle"
    BULKHEAD = "Bulkhead"
    EXIT = "Exit"
    WINDOW = "Window"
    MIDDLE = "Middle"


class TypeReserveRequirement(Enum):
    """
    Type of payment required to reserve travel i.e. Hotel Reservation
    requirement.
    """
    DEPOSIT = "Deposit"
    GUARANTEE = "Guarantee"
    PREPAYMENT = "Prepayment"
    OTHER = "Other"


class TypeResidency(Enum):
    """
    The passenger residency type.Residence Type can be Employee, National or
    Resident.
    """
    EMPLOYEE = "Employee"
    NATIONAL = "National"
    RESIDENT = "Resident"


class TypeResponseImageSize(Enum):
    """
    Allowable images sizes in response.
    """
    T = "T"
    I = "I"
    S = "S"
    M = "M"
    L = "L"
    E = "E"
    G = "G"
    F = "F"
    B = "B"
    J = "J"
    O = "O"
    H = "H"
    C = "C"
    X = "X"


class TypeResultMessageType(Enum):
    WARNING = "Warning"
    ERROR = "Error"
    INFO = "Info"


@dataclass
class TypeSearchTimeSpec:
    class Meta:
        name = "typeSearchTimeSpec"


@dataclass
class TypeSegmentRef:
    class Meta:
        name = "typeSegmentRef"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


class TypeSource(Enum):
    """
    The source/level at which is item is defined (available through
    inheritance)
    """
    AGENCY = "Agency"
    BRANCH_GROUP = "BranchGroup"
    BRANCH = "Branch"
    AGENT = "Agent"


@dataclass
class TypeSpecificTime:
    """Specify exact times.

    System will automatically convert to a range according to agency
    configuration.
    """
    class Meta:
        name = "typeSpecificTime"

    time: Optional[str] = field(
        default=None,
        metadata={
            "name": "Time",
            "type": "Attribute",
            "required": True,
        }
    )


class TypeStatus(Enum):
    """
    The status of the service fees.

    Properties
    ----------
    ISSUED: The service fee has been issued.
    READY_TO_ISSUE: The service fee is ready to be issued.
    ISSUE_LATER: The service fee can be issued later.
    """
    ISSUED = "Issued"
    READY_TO_ISSUE = "ReadyToIssue"
    ISSUE_LATER = "IssueLater"


@dataclass
class TypeSubKey:
    """
    The attributes and elements in a SubKey.

    Parameters
    ----------
    text: Information for a sub key.
    name: A subkey to identify the specific information within this
        keyword
    description: A brief description of a subkey.
    """
    class Meta:
        name = "typeSubKey"

    text: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
        }
    )


@dataclass
class TypeTax:
    class Meta:
        name = "typeTax"

    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        }
    )


class TypeTicketStatus(Enum):
    """
    Status for the ticket (Ticketed, Voided, etc)

    Properties
    ----------
    U: Code="U" Description="Unticketed"
    T: Code="T" Description="Ticketed"
    V: Code="V" Description="Voided"
    R: Code="R" Description="Refunded"
    X: Code="X" Description="eXchanged"
    Z: Code="Z" Description="Unknown/Archived/Carrier Modified"
    N: Code="N" Description="Unused"
    S: Code="S" Description="Used"
    """
    U = "U"
    T = "T"
    V = "V"
    R = "R"
    X = "X"
    Z = "Z"
    N = "N"
    S = "S"


@dataclass
class TypeTimeRange:
    """
    Specify a range of times.
    """
    class Meta:
        name = "typeTimeRange"

    earliest_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "EarliestTime",
            "type": "Attribute",
            "required": True,
        }
    )
    latest_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "LatestTime",
            "type": "Attribute",
            "required": True,
        }
    )


class TypeTrinary(Enum):
    """
    Extension of boolean, that allows for unknown values.
    """
    TRUE = "true"
    FALSE = "false"
    UNKNOWN = "unknown"


class TypeVehicleCategory(Enum):
    """
    The category of vehicle.
    """
    CAR = "Car"
    VAN = "Van"
    SUV = "SUV"
    CONVERTIBLE = "Convertible"
    TRUCK = "Truck"
    STATION_WAGON = "StationWagon"
    PICKUP = "Pickup"
    ALL_TERRAIN = "AllTerrain"
    RECREATIONAL = "Recreational"
    SPORT = "Sport"
    SPECIAL = "Special"
    EXTENDED_CAB_PICKUP = "ExtendedCabPickup"
    REGULAR_CAB_PICKUP = "RegularCabPickup"
    SPECIAL_OFFER = "SpecialOffer"
    COUPE = "Coupe"
    MONOSPACE = "Monospace"
    ROADSTER = "Roadster"
    CROSSOVER = "Crossover"
    MOTORCYCLE = "Motorcycle"
    LIMO = "Limo"
    MOTORHOME = "Motorhome"
    TWO_WHEEL_VEHICLE = "TwoWheelVehicle"
    COMMERCIAL_VAN_OR_TRUCK = "CommercialVanOrTruck"


class TypeVehicleClass(Enum):
    """
    The class of vehicle.
    """
    MINI = "Mini"
    ECONOMY = "Economy"
    COMPACT = "Compact"
    INTERMEDIATE = "Intermediate"
    STANDARD = "Standard"
    FULLSIZE = "Fullsize"
    LUXURY = "Luxury"
    PREMIUM = "Premium"
    SPECIAL = "Special"
    MINI_ELITE = "MiniElite"
    ECONOMY_ELITE = "EconomyElite"
    COMPACT_ELITE = "CompactElite"
    INTERMEDIATE_ELITE = "IntermediateElite"
    STANDARD_ELITE = "StandardElite"
    FULLSIZE_ELITE = "FullsizeElite"
    PREMIUM_ELITE = "PremiumElite"
    LUXURY_ELITE = "LuxuryElite"
    OVERSIZE = "Oversize"
    SUBCOMPACT = "Subcompact"
    MINIVAN = "Minivan"
    TWELVE_PASSENGER_VAN = "TwelvePassengerVan"
    MOVING_VAN = "MovingVan"
    FIFTEEN_PASSENGER_VAN = "FifteenPassengerVan"
    CARGO_VAN = "CargoVan"
    TWELVE_FOOT_TRUCK = "TwelveFootTruck"
    TWENTY_FOOT_TRUCK = "TwentyFootTruck"
    TWENTYFOUR_FOOT_TRUCK = "TwentyfourFootTruck"
    TWENTYSIX_FOOT_TRUCK = "TwentysixFootTruck"
    MOPED = "Moped"
    STRETCH = "Stretch"
    REGULAR = "Regular"
    UNIQUE = "Unique"
    EXOTIC = "Exotic"
    SMALL_OR_MEDIUM_TRUCK = "SmallOrMediumTruck"
    LARGE_TRUCK = "LargeTruck"
    SMALL_SUV = "SmallSUV"
    MEDIUM_SUV = "MediumSUV"
    LARGE_SUV = "LargeSUV"
    EXOTIC_SUV = "ExoticSUV"
    FOUR_WHEEL_DRIVE = "FourWheelDrive"


class TypeVehicleLocation(Enum):
    """
    The type of location requested, such as resort, city center.
    """
    TERMINAL = "Terminal"
    SHUTTLE_ON_AIRPORT = "ShuttleOnAirport"
    SHUTTLE_OFF_AIRPORT = "ShuttleOffAirport"
    RAILWAY_STATION = "RailwayStation"
    HOTEL = "Hotel"
    CAR_DEALER = "CarDealer"
    CITY_CENTER_DOWNTOWN = "CityCenterDowntown"
    EAST_OF_CITY_CENTER = "EastOfCityCenter"
    SOUTH_OF_CITY_CENTER = "SouthOfCityCenter"
    WEST_OF_CITY_CENTER = "WestOfCityCenter"
    NORTH_OF_CITY_CENTER = "NorthOfCityCenter"
    PORT_OR_FERRY = "PortOrFerry"
    NEAR_RESORT = "NearResort"
    AIRPORT = "Airport"
    UNKNOWN = "Unknown"


class TypeVehicleTransmission(Enum):
    AUTOMATIC = "Automatic"
    AUTOMATIC4_WD = "Automatic4WD"
    AUTOMATIC_AWD = "AutomaticAWD"
    MANUAL = "Manual"
    MANUAL4_WD = "Manual4WD"
    MANUAL_AWD = "ManualAWD"


@dataclass
class TypeVendorLocation:
    """
    Parameters
    ----------
    provider_code: The code of the provider (e.g. 1G, 1S)
    vendor_code: The code of the vendor (e.g.  HZ, etc.)
    preferred_option: Preferred Option marker for Location.
    vendor_location_id: Location identifier
    key: Key which maps vendor location with vehicles
    more_rates_token: Enter the Token when provided by hotel property,
        more rates exist. HADS/HSS  support only.
    """
    class Meta:
        name = "typeVendorLocation"

    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    vendor_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "VendorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        }
    )
    preferred_option: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PreferredOption",
            "type": "Attribute",
        }
    )
    vendor_location_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "VendorLocationID",
            "type": "Attribute",
            "min_length": 1,
            "white_space": "collapse",
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    more_rates_token: Optional[str] = field(
        default=None,
        metadata={
            "name": "MoreRatesToken",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 30,
        }
    )


class TypeVoucherType(Enum):
    FULL_CREDIT = "FullCredit"
    GROUP_OR_DAY = "GroupOrDay"
    SPECIFIC_VALUE = "SpecificValue"
    REGULAR_VOUCHER = "RegularVoucher"


@dataclass
class AccountingRemark:
    """
    An accounting remark container to hold any printable text.

    Parameters
    ----------
    remark_data: Actual remarks data.
    booking_traveler_ref: Reference to Booking Traveler.
    key:
    category: A category to group and organize the various remarks. This
        is not required, but it is recommended.
    type_in_gds:
    provider_reservation_info_ref: Provider reservation reference key.
    provider_code: Contains the Provider Code of the provider for which
        this accounting remark is used
    use_provider_native_mode: Will be true when terminal process
        required, else false
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    remark_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "RemarkData",
            "type": "Element",
            "required": True,
        }
    )
    booking_traveler_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    category: Optional[str] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
            "max_length": 14,
        }
    )
    type_in_gds: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeInGds",
            "type": "Attribute",
            "max_length": 30,
        }
    )
    provider_reservation_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    use_provider_native_mode: bool = field(
        default=False,
        metadata={
            "name": "UseProviderNativeMode",
            "type": "Attribute",
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class ActionStatus:
    """Status of the action that will happen or has happened to the air
    reservation.

    One Action status for each provider reservation

    Parameters
    ----------
    remark:
    type: Identifies the type of action (if any) to take on this air
        reservation. Only TTL, TAU, TAX and TAW can be set by the user.
    ticket_date: Identifies when the action type will happen, or has
        happened according to the type.
    key: Identifies when the action type will happen, or has happened
        according to the type.
    provider_reservation_info_ref: Provider reservation reference key.
    queue_category: Add Category placement to ticketing queue (required
        in 1P - default is 00)
    airport_code: Used with Time Limit to specify the airport location
        where the ticket is to be issued.
    provider_code:
    supplier_code:
    pseudo_city_code: The Branch PCC in the host system where PNR can be
        queued for ticketing. When used with TAU it will auto queue to
        Q10. When used with TAW agent performs manual move to Q.
    account_code: Used with TAW. Used to specify a corporate or in house
        account code to the PNR as part of ticketing arrangement field.
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    remark: Optional[Remark] = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
        }
    )
    type: Optional[ActionStatusType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    ticket_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketDate",
            "type": "Attribute",
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    provider_reservation_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        }
    )
    queue_category: Optional[str] = field(
        default=None,
        metadata={
            "name": "QueueCategory",
            "type": "Attribute",
            "min_length": 1,
            "white_space": "collapse",
        }
    )
    airport_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirportCode",
            "type": "Attribute",
            "length": 3,
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        }
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        }
    )
    account_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Attribute",
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class AgencyPayment(TypeAgencyPayment):
    """
    Container for Agency Payment.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"


@dataclass
class AgentAction:
    """
    Depending on context, this will represent information about which agent
    perform different actions.

    Parameters
    ----------
    action_type: The type of action the agent performed.
    agent_code: The AgenctCode who performed the action.
    branch_code: The BranchCode of the branch (working branch,
        branchcode used for the request. If nothing specified,
        branchcode for the agent) who performed the action.
    agency_code: The AgencyCode of the agent who performed the action.
    agent_sine: The sign in user name of the agent logged into the
        terminal. PROVIDER SUPPORTED: ACH
    event_time: Date and time at which this event took place.
    agent_override: AgentSine value that was used during PNR creation or
        End Transact.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    action_type: Optional[AgentActionActionType] = field(
        default=None,
        metadata={
            "name": "ActionType",
            "type": "Attribute",
            "required": True,
        }
    )
    agent_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgentCode",
            "type": "Attribute",
            "required": True,
        }
    )
    branch_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "BranchCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 25,
        }
    )
    agency_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgencyCode",
            "type": "Attribute",
            "required": True,
        }
    )
    agent_sine: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgentSine",
            "type": "Attribute",
        }
    )
    event_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EventTime",
            "type": "Attribute",
            "required": True,
        }
    )
    agent_override: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgentOverride",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        }
    )


@dataclass
class Airport(Location):
    """
    Airport identifier.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )


@dataclass
class AppliedProfile:
    """
    A simple container to specify the profiles that were applied to a
    reservation.

    Parameters
    ----------
    key: Key for update/delete of the element
    traveler_id: The ID of the TravelerProfile that was applied
    traveler_name: The name from the TravelerProfile that was applied
    account_id: The ID of the AccountProfile that was applied
    account_name: The name from the AccountProfile that was applied
    immediate_parent_id: The ID of the immediate parent that was applied
    immediate_parent_name: The name of the immediate parent that was
        applied
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    traveler_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TravelerID",
            "type": "Attribute",
        }
    )
    traveler_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "TravelerName",
            "type": "Attribute",
        }
    )
    account_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountID",
            "type": "Attribute",
        }
    )
    account_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountName",
            "type": "Attribute",
        }
    )
    immediate_parent_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ImmediateParentID",
            "type": "Attribute",
        }
    )
    immediate_parent_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ImmediateParentName",
            "type": "Attribute",
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class BaseCoreReq:
    """
    Parameters
    ----------
    billing_point_of_sale_info:
    agent_idoverride:
    terminal_session_info:
    trace_id: Unique identifier for this atomic transaction traced by
        the user. Use is optional.
    token_id: Authentication Token ID used when running in statefull
        operation. Obtained from the LoginRsp. Use is optional.
    authorized_by: Used in showing who authorized the request. Use is
        optional.
    target_branch: Used for Emulation - If authorised will execute the
        request as if the agent's parent branch is the TargetBranch
        specified.
    override_logging: Use to override the default logging level
    language_code: ISO 639 two-character language codes are used to
        retrieve specific information in the requested language. For
        Rich Content and Branding, language codes ZH-HANT (Chinese
        Traditional), ZH-HANS (Chinese Simplified), FR-CA (French
        Canadian) and PT-BR (Portuguese Brazil) can also be used. For
        RCH, language codes ENGB, ENUS, DEDE, DECH can also be used.
        Only certain services support this attribute. Providers: ACH,
        RCH, 1G, 1V, 1P, 1J.
    """
    billing_point_of_sale_info: Optional[BillingPointOfSaleInfo] = field(
        default=None,
        metadata={
            "name": "BillingPointOfSaleInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "required": True,
        }
    )
    agent_idoverride: List[AgentIdoverride] = field(
        default_factory=list,
        metadata={
            "name": "AgentIDOverride",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    terminal_session_info: Optional[str] = field(
        default=None,
        metadata={
            "name": "TerminalSessionInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    trace_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TraceId",
            "type": "Attribute",
        }
    )
    token_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TokenId",
            "type": "Attribute",
        }
    )
    authorized_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthorizedBy",
            "type": "Attribute",
        }
    )
    target_branch: Optional[str] = field(
        default=None,
        metadata={
            "name": "TargetBranch",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 25,
        }
    )
    override_logging: Optional[TypeLoggingLevel] = field(
        default=None,
        metadata={
            "name": "OverrideLogging",
            "type": "Attribute",
        }
    )
    language_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LanguageCode",
            "type": "Attribute",
        }
    )


@dataclass
class BookingSource:
    """
    Parameters
    ----------
    code: Alternate booking source code or number.
    type: Type of booking source sent in the Code attribute. Possible
        values are “PseudoCityCode”,” ArcNumber”,” IataNumber”,
        “CustomerId” and “BookingSourceOverrride”.
        “BookingSourceOverrride” is only applicable in
        VehicleCreateReservationReq. 1P/1J.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
        }
    )
    type: Optional[BookingSourceType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class BookingTravelerInformation:
    """
    Booking Traveler information tied to invoice.

    Parameters
    ----------
    name:
    booking_traveler_ref: A reference to a passenger related to a
        ticket.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        }
    )
    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        }
    )


@dataclass
class BookingTravelerRef:
    """
    Reference Element for Booking Traveler and Loyalty cards.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    loyalty_card_ref: List[LoyaltyCardRef] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCardRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    drivers_license_ref: Optional[DriversLicenseRef] = field(
        default=None,
        metadata={
            "name": "DriversLicenseRef",
            "type": "Element",
        }
    )
    discount_card_ref: List[DiscountCardRef] = field(
        default_factory=list,
        metadata={
            "name": "DiscountCardRef",
            "type": "Element",
            "max_occurs": 9,
        }
    )
    payment_ref: List[PaymentRef] = field(
        default_factory=list,
        metadata={
            "name": "PaymentRef",
            "type": "Element",
            "max_occurs": 3,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )


@dataclass
class City(Location):
    """
    City identifier.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )


@dataclass
class CityOrAirport(Location):
    """
    This element can be used when it is not known whether the value is an
    airport or a city code.

    Parameters
    ----------
    code: The airport or city IATA code.
    prefer_city: Indicates that the search should prefer city results
        over airport results.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    prefer_city: bool = field(
        default=False,
        metadata={
            "name": "PreferCity",
            "type": "Attribute",
        }
    )


@dataclass
class Commission:
    """
    Identifies the agency commission.

    Parameters
    ----------
    key:
    level: The commission percentage level.
    type: The commission type.
    modifier: Optional commission modifier.
    amount: The monetary amount of the commission.
    value: Contains alphanumeric or alpha characters intended as 1G
        Value Code as applicable by BSP of client.
    percentage: The percent of the commission.
    booking_traveler_ref: A reference to a passenger.
    commission_override: This is enabled to override CAT-35 commission
        error during air ticketing. PROVIDER SUPPORTED:Worldspan and JAL
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    level: Optional[TypeCommissionLevel] = field(
        default=None,
        metadata={
            "name": "Level",
            "type": "Attribute",
            "required": True,
        }
    )
    type: Optional[TypeCommissionType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    modifier: Optional[TypeCommissionModifier] = field(
        default=None,
        metadata={
            "name": "Modifier",
            "type": "Attribute",
        }
    )
    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 15,
        }
    )
    percentage: Optional[str] = field(
        default=None,
        metadata={
            "name": "Percentage",
            "type": "Attribute",
            "pattern": r"([0-9]{1,2}|100)\.[0-9]{1,2}",
        }
    )
    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        }
    )
    commission_override: bool = field(
        default=False,
        metadata={
            "name": "CommissionOverride",
            "type": "Attribute",
        }
    )


@dataclass
class CommissionRemark:
    """Identifies the agency commision remarks.

    Specifically used for Worldspan.

    Parameters
    ----------
    provider_reservation_level: Specify commission which is applicable
        to PNR level.
    passenger_type_level: Specify commission which is applicable to per
        PTC level.
    key: Key to be used for internal processing.
    provider_reservation_info_ref: Provider reservation reference key.
    provider_code: Contains the Provider Code of the provider for which
        this accounting remark is used
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    provider_reservation_level: Optional["CommissionRemark.ProviderReservationLevel"] = field(
        default=None,
        metadata={
            "name": "ProviderReservationLevel",
            "type": "Element",
        }
    )
    passenger_type_level: List["CommissionRemark.PassengerTypeLevel"] = field(
        default_factory=list,
        metadata={
            "name": "PassengerTypeLevel",
            "type": "Element",
            "max_occurs": 4,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    provider_reservation_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )

    @dataclass
    class ProviderReservationLevel:
        """
        Parameters
        ----------
        amount: The monetary amount of the commission.
        percentage: The percent of the commission.
        commission_cap: Commission cap for the Airline.
        """
        amount: Optional[str] = field(
            default=None,
            metadata={
                "name": "Amount",
                "type": "Attribute",
            }
        )
        percentage: Optional[str] = field(
            default=None,
            metadata={
                "name": "Percentage",
                "type": "Attribute",
                "pattern": r"([0-9]{1,2}|100)\.[0-9]{1,2}",
            }
        )
        commission_cap: Optional[str] = field(
            default=None,
            metadata={
                "name": "CommissionCap",
                "type": "Attribute",
            }
        )

    @dataclass
    class PassengerTypeLevel:
        """
        Parameters
        ----------
        traveler_type:
        amount: The monetary amount of the commission.
        percentage: The percent of the commission.
        commission_cap: Commission cap for the Airline.
        """
        traveler_type: Optional[str] = field(
            default=None,
            metadata={
                "name": "TravelerType",
                "type": "Attribute",
                "required": True,
                "min_length": 3,
                "max_length": 5,
            }
        )
        amount: Optional[str] = field(
            default=None,
            metadata={
                "name": "Amount",
                "type": "Attribute",
            }
        )
        percentage: Optional[str] = field(
            default=None,
            metadata={
                "name": "Percentage",
                "type": "Attribute",
                "pattern": r"([0-9]{1,2}|100)\.[0-9]{1,2}",
            }
        )
        commission_cap: Optional[str] = field(
            default=None,
            metadata={
                "name": "CommissionCap",
                "type": "Attribute",
            }
        )


@dataclass
class ConsolidatorRemark:
    """Authorization remark for Consolidator access to a PNR .

    Contains PCC information created by retail agent to  allow a
    consolidator or other Axess users to service their PNR. PROVIDER
    SUPPORTED: Worldspan and JAL.

    Parameters
    ----------
    pseudo_city_code:
    key: Key to be used for internal processing.
    provider_reservation_info_ref: Provider reservation reference key.
    provider_code: Contains the Provider Code of the provider for which
        this element is used
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    pseudo_city_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PseudoCityCode",
            "type": "Element",
            "max_occurs": 5,
            "min_length": 2,
            "max_length": 10,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    provider_reservation_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class CoordinateLocation(Location):
    """
    Specific lat/long location, usually associated with a Distance.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    latitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    longitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CustomerId(TypeRemark):
    """A provider reservation field used to store customer information.

    It may be used to identify reservations which will/will not be
    available for access.
    """
    class Meta:
        name = "CustomerID"
        namespace = "http://www.travelport.com/schema/common_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )


@dataclass
class DiscountCard:
    """
    Rail Discount Card Information.

    Parameters
    ----------
    key:
    code:
    description:
    number:
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 8,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 36,
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class Distance:
    """
    Container to encapsulate the a distance value with its unit of measure.

    Parameters
    ----------
    units:
    value:
    direction: Directions: S, N, E, W, SE, NW, ...
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    units: DistanceUnits = field(
        default=DistanceUnits.MI,
        metadata={
            "name": "Units",
            "type": "Attribute",
            "length": 2,
        }
    )
    value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        }
    )
    direction: Optional[str] = field(
        default=None,
        metadata={
            "name": "Direction",
            "type": "Attribute",
            "max_length": 2,
        }
    )


@dataclass
class DriversLicense:
    """
    Details of drivers license.

    Parameters
    ----------
    key:
    license_number: The driving license number of the booking traveler.
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    license_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "LicenseNumber",
            "type": "Attribute",
            "required": True,
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class Email:
    """
    Container for an email address with a type specifier (max 128 chars)

    Parameters
    ----------
    provider_reservation_info_ref: Tagging provider reservation info
        with Email.
    key:
    type:
    comment:
    email_id:
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    provider_reservation_info_ref: List[ProviderReservationInfoRef] = field(
        default_factory=list,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    email_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailID",
            "type": "Attribute",
            "required": True,
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class EmailNotification:
    """Send Email Notification to the emails specified in Booking Traveler.

    Supported Provider : 1G/1V

    Parameters
    ----------
    email_ref: Reference to Booking Traveler Email.
    recipients: Indicates the recipients of the mail addresses for which
        the user requires the system to send the itinerary.List of
        Possible Values: All = Send Email to All addresses Default =
        Send Email to Primary Booking Traveler Specific = Send Email to
        specific address Referred in EmailRef.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    email_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "EmailRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    recipients: Optional[EmailNotificationRecipients] = field(
        default=None,
        metadata={
            "name": "Recipients",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class FormattedTextTextType:
    """
    Provides text and indicates whether it is formatted or not.

    Parameters
    ----------
    value:
    formatted: Textual information, which may be formatted as a line of
        information, or unformatted, as a paragraph of text.
    language: Language identification.
    text_format: Indicates the format of text used in the description
        e.g. unformatted  or html.
    """
    value: Optional[str] = field(
        default=None
    )
    formatted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Formatted",
            "type": "Attribute",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Attribute",
        }
    )
    text_format: Optional[FormattedTextTextTypeTextFormat] = field(
        default=None,
        metadata={
            "name": "TextFormat",
            "type": "Attribute",
        }
    )


@dataclass
class GeneralRemark:
    """A textual remark container to hold any printable text.

    (max 512 chars)

    Parameters
    ----------
    remark_data: Actual remarks data.
    booking_traveler_ref: Reference to Booking Traveler.
    key:
    category: A category to group and organize the various remarks. This
        is not required, but it is recommended.
    type_in_gds:
    supplier_type: The type of product this reservation is relative to
    provider_reservation_info_ref: Provider reservation reference key.
    provider_code:
    supplier_code:
    direction: Direction Incoming or Outgoing of the GeneralRemark.
    create_date: The date and time that this GeneralRemark was created.
    use_provider_native_mode: Will be true when terminal process
        required, else false
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    remark_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "RemarkData",
            "type": "Element",
            "required": True,
        }
    )
    booking_traveler_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    category: Optional[str] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
            "max_length": 20,
        }
    )
    type_in_gds: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeInGds",
            "type": "Attribute",
            "max_length": 30,
        }
    )
    supplier_type: Optional[TypeProduct] = field(
        default=None,
        metadata={
            "name": "SupplierType",
            "type": "Attribute",
        }
    )
    provider_reservation_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        }
    )
    direction: Optional[TypeDirection] = field(
        default=None,
        metadata={
            "name": "Direction",
            "type": "Attribute",
        }
    )
    create_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreateDate",
            "type": "Attribute",
        }
    )
    use_provider_native_mode: bool = field(
        default=False,
        metadata={
            "name": "UseProviderNativeMode",
            "type": "Attribute",
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class HostToken:
    """This is a host token.

    It contains some kind of payload we got from a host that must be
    passed in on successive calls they know who you are as our system
    does not maintain state. The format of this string isn't important
    as long as it is not altered in any way between calls. Since a host
    token is only valid on the host it is assocated with, there is also
    an attribute called Host so we know how to route the command(s). You
    can have multiple active sessions between one or more hosts

    Parameters
    ----------
    value:
    host: The host associated with this token
    key: Unique identifier for this token - use this key when a single
        HostToken is shared by multiple elements.
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    value: Optional[str] = field(
        default=None
    )
    host: Optional[str] = field(
        default=None,
        metadata={
            "name": "Host",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class LinkedUniversalRecord:
    """
    Parameters
    ----------
    locator_code: A Universal Record that need to be linked to the
        current Universal Record.
    key:
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class LoyaltyProgram:
    """
    Parameters
    ----------
    key:
    supplier_code: The code used to identify the Loyalty supplier, e.g.
        AA, ZE, MC
    alliance_level:
    membership_program: Loyalty Program membership Id of the traveler
        specific to Amtrak(2V) Guest Rewards
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    level:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )
    alliance_level: Optional[str] = field(
        default=None,
        metadata={
            "name": "AllianceLevel",
            "type": "Attribute",
        }
    )
    membership_program: Optional[str] = field(
        default=None,
        metadata={
            "name": "MembershipProgram",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )
    level: Optional[str] = field(
        default=None,
        metadata={
            "name": "Level",
            "type": "Attribute",
        }
    )


@dataclass
class McofeeInfo:
    """
    Information related to the PTA/TOD (Prepaid Ticket Advice / Ticket on
    Departure) related to the MCO.

    Parameters
    ----------
    amount: The monetary amount.
    percentage: The percentage.
    fee_applies_to_ind: Indicates if PTA/TOD fee is for the entire MCO
        or is per person.
    """
    class Meta:
        name = "MCOFeeInfo"
        namespace = "http://www.travelport.com/schema/common_v48_0"

    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        }
    )
    percentage: Optional[str] = field(
        default=None,
        metadata={
            "name": "Percentage",
            "type": "Attribute",
            "pattern": r"([0-9]{1,2}|100)\.[0-9]{1,2}",
        }
    )
    fee_applies_to_ind: Optional[McofeeInfoFeeAppliesToInd] = field(
        default=None,
        metadata={
            "name": "FeeAppliesToInd",
            "type": "Attribute",
        }
    )


@dataclass
class MediaItem:
    """
    Photos and other media urls for the property referenced above.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    caption: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    height: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    width: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    icon: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    size_code: Optional[TypeResponseImageSize] = field(
        default=None,
        metadata={
            "name": "sizeCode",
            "type": "Attribute",
        }
    )


@dataclass
class NameRemark:
    """
    Text that support Name Remarks.

    Parameters
    ----------
    remark_data: Actual remarks data.
    provider_reservation_info_ref: Tagging provider reservation info
        with NameRemark.
    key:
    category: A category to group and organize the various remarks. This
        is not required, but it is recommended.
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    remark_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "RemarkData",
            "type": "Element",
            "required": True,
        }
    )
    provider_reservation_info_ref: List[ProviderReservationInfoRef] = field(
        default_factory=list,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    category: Optional[str] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class Osi:
    """
    Other Service information sent to the carriers during air bookings.

    Parameters
    ----------
    key:
    carrier:
    code:
    text:
    provider_reservation_info_ref: Provider reservation reference key.
    provider_code: Contains the Provider Code of the provider for which
        this OSI is used
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        name = "OSI"
        namespace = "http://www.travelport.com/schema/common_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "max_length": 4,
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Attribute",
            "required": True,
            "max_length": 256,
        }
    )
    provider_reservation_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class OptionalServiceApplicationLimitType:
    """
    The optional service application limit.

    Parameters
    ----------
    applicable_level: Indicates the applicable level for the option
    provider_defined_applicable_levels: Indicates the actual provider
        defined ApplicableLevels which is mapped to Other
    maximum_quantity: The maximum quantity allowed for the type
    minimum_quantity: Indicates the minimum number of the option that
        can be selected.
    """
    applicable_level: Optional[OptionalServiceApplicabilityType] = field(
        default=None,
        metadata={
            "name": "ApplicableLevel",
            "type": "Attribute",
            "required": True,
        }
    )
    provider_defined_applicable_levels: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderDefinedApplicableLevels",
            "type": "Attribute",
        }
    )
    maximum_quantity: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumQuantity",
            "type": "Attribute",
            "required": True,
        }
    )
    minimum_quantity: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinimumQuantity",
            "type": "Attribute",
        }
    )


@dataclass
class OtherGuaranteeInfo:
    """
    Parameters
    ----------
    value:
    type: 1) IATA/ARC Number 2) Agency Address 2) Deposit Taken 3)
        Others
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    value: Optional[str] = field(
        default=None
    )
    type: Optional[OtherGuaranteeInfoType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PassengerInfo:
    """
    Booking Traveler information tied to invoice.

    Parameters
    ----------
    name:
    booking_traveler_ref: A reference to a passenger related to a
        ticket.
    passenger_type: Passenger Type Code.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        }
    )
    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        }
    )
    passenger_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "PassengerType",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 5,
        }
    )


@dataclass
class Payment:
    """Payment information - must be used in conjunction with credit card info

    Parameters
    ----------
    key:
    type: Identifies the type of payment. This can be for an itinerary,
        a traveler, or a service fee for example.
    form_of_payment_ref: The credit card that is will be used to make
        this payment.
    booking_traveler_ref: If the type represents a per traveler payment,
        then this will reference the traveler this payment refers to.
    amount:
    amount_type: This field displays type of payment amount when it is
        non-monetary. Presently available/supported value is "Flight
        Pass Credits".
    approximate_amount: It stores the converted payment amount in
        agency's default currency
    status: Status to indicate the business association of the payment
        element.
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    type: Optional[PaymentType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    form_of_payment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FormOfPaymentRef",
            "type": "Attribute",
            "required": True,
        }
    )
    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        }
    )
    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
        }
    )
    amount_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "AmountType",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        }
    )
    approximate_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateAmount",
            "type": "Attribute",
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class PermittedProviders:
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    provider: Optional[Provider] = field(
        default=None,
        metadata={
            "name": "Provider",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PhoneNumber:
    """
    Consists of type (office, home, fax), location (city code), the country
    code, the number, and an extension.

    Parameters
    ----------
    provider_reservation_info_ref:
    key:
    type:
    location: IATA code for airport or city
    country_code: Hosts/providers will expect this to be international
        dialing digits
    area_code:
    number: The local phone number
    extension:
    text:
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    provider_reservation_info_ref: List[ProviderReservationInfoRef] = field(
        default_factory=list,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    type: Optional[PhoneNumberType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Attribute",
            "max_length": 10,
        }
    )
    country_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CountryCode",
            "type": "Attribute",
            "max_length": 5,
        }
    )
    area_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AreaCode",
            "type": "Attribute",
            "max_length": 10,
        }
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 83,
        }
    )
    extension: Optional[str] = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Attribute",
            "max_length": 10,
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Attribute",
            "max_length": 1024,
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class PolicyInformation:
    """
    Policy Information required for File Finishing.

    Parameters
    ----------
    reason_code: Reason Code
    type: Policy Type - Air, Hotel, Car, Rail, Ticketing
    name: Policy Name
    out_of_policy: In Policy / Out of Policy Indicator
    segment_ref:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    reason_code: Optional["PolicyInformation.ReasonCode"] = field(
        default=None,
        metadata={
            "name": "ReasonCode",
            "type": "Element",
        }
    )
    type: Optional[TypePolicy] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        }
    )
    out_of_policy: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OutOfPolicy",
            "type": "Attribute",
        }
    )
    segment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SegmentRef",
            "type": "Attribute",
        }
    )

    @dataclass
    class ReasonCode:
        """
        Parameters
        ----------
        out_of_policy: Reason Code - Out of Policy
        purpose_of_trip: Reason Code -Purpose of Trip
        remark:
        """
        out_of_policy: Optional[str] = field(
            default=None,
            metadata={
                "name": "OutOfPolicy",
                "type": "Element",
            }
        )
        purpose_of_trip: Optional[str] = field(
            default=None,
            metadata={
                "name": "PurposeOfTrip",
                "type": "Element",
            }
        )
        remark: Optional[Remark] = field(
            default=None,
            metadata={
                "name": "Remark",
                "type": "Element",
            }
        )


@dataclass
class Postscript(TypeRemark):
    """
    Postscript Notes.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )


@dataclass
class ProviderArnksegment:
    """
    Represents host ARNK segments.

    Parameters
    ----------
    previous_segment:
    next_segment:
    key:
    provider_reservation_info_ref: Provider reservation reference key.
    provider_segment_order: To identify the appropriate travel sequence
        for Air/Car/Hotel/Rail segments/reservations in the provider
        reservation.
    """
    class Meta:
        name = "ProviderARNKSegment"
        namespace = "http://www.travelport.com/schema/common_v48_0"

    previous_segment: Optional["ProviderArnksegment.PreviousSegment"] = field(
        default=None,
        metadata={
            "name": "PreviousSegment",
            "type": "Element",
        }
    )
    next_segment: Optional["ProviderArnksegment.NextSegment"] = field(
        default=None,
        metadata={
            "name": "NextSegment",
            "type": "Element",
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    provider_reservation_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        }
    )
    provider_segment_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "ProviderSegmentOrder",
            "type": "Attribute",
            "max_inclusive": 999,
        }
    )

    @dataclass
    class PreviousSegment:
        """
        Parameters
        ----------
        air_segment_ref: Reference to AirSegment from an Air
            Reservation.
        hotel_reservation_ref: Specify the locator code of Hotel
            reservation.
        vehicle_reservation_ref: Specify the locator code of Vehicle
            reservation.
        passive_segment_ref: Reference to PassiveSegment from a Passive
            Reservation.
        """
        air_segment_ref: Optional[TypeSegmentRef] = field(
            default=None,
            metadata={
                "name": "AirSegmentRef",
                "type": "Element",
            }
        )
        hotel_reservation_ref: Optional[TypeNonAirReservationRef] = field(
            default=None,
            metadata={
                "name": "HotelReservationRef",
                "type": "Element",
            }
        )
        vehicle_reservation_ref: Optional[TypeNonAirReservationRef] = field(
            default=None,
            metadata={
                "name": "VehicleReservationRef",
                "type": "Element",
            }
        )
        passive_segment_ref: Optional[TypeSegmentRef] = field(
            default=None,
            metadata={
                "name": "PassiveSegmentRef",
                "type": "Element",
            }
        )

    @dataclass
    class NextSegment:
        """
        Parameters
        ----------
        air_segment_ref: Reference to AirSegment from an Air
            Reservation.
        hotel_reservation_ref: Specify the locator code of Hotel
            reservation.
        vehicle_reservation_ref: Specify the locator code of Vehicle
            reservation.
        passive_segment_ref: Reference to PassiveSegment from a Passive
            Reservation.
        """
        air_segment_ref: Optional[TypeSegmentRef] = field(
            default=None,
            metadata={
                "name": "AirSegmentRef",
                "type": "Element",
            }
        )
        hotel_reservation_ref: Optional[TypeNonAirReservationRef] = field(
            default=None,
            metadata={
                "name": "HotelReservationRef",
                "type": "Element",
            }
        )
        vehicle_reservation_ref: Optional[TypeNonAirReservationRef] = field(
            default=None,
            metadata={
                "name": "VehicleReservationRef",
                "type": "Element",
            }
        )
        passive_segment_ref: Optional[TypeSegmentRef] = field(
            default=None,
            metadata={
                "name": "PassiveSegmentRef",
                "type": "Element",
            }
        )


@dataclass
class ProviderReservationDetail(TypeProviderReservationDetail):
    """
    common element for mentioning provider reservation locator (PNR) details in
    request.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"


@dataclass
class QueuePlace:
    """
    Allow queue placement of a PNR at the time of booking to be used for
    Providers 1G,1V,1P and 1J.

    Parameters
    ----------
    pseudo_city_code: Pseudo City Code
    queue_selector: Identifies the Queue Information to be selected for
        placing the UR
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Element",
            "min_length": 2,
            "max_length": 10,
        }
    )
    queue_selector: List[QueueSelector] = field(
        default_factory=list,
        metadata={
            "name": "QueueSelector",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class RailLocation(Location):
    """
    RCH specific location code (a.k.a UCodes) which uniquely identifies a train
    station.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
        }
    )


@dataclass
class RailSeatAssignment:
    """
    Identifies the seat assignment for a passenger on RailSegment.

    Parameters
    ----------
    characteristic:
    key:
    status:
    seat:
    rail_segment_ref:
    coach_number:
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    characteristic: List[Characteristic] = field(
        default_factory=list,
        metadata={
            "name": "Characteristic",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
            "length": 2,
            "white_space": "collapse",
        }
    )
    seat: Optional[str] = field(
        default=None,
        metadata={
            "name": "Seat",
            "type": "Attribute",
            "required": True,
        }
    )
    rail_segment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "RailSegmentRef",
            "type": "Attribute",
        }
    )
    coach_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "CoachNumber",
            "type": "Attribute",
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class RequestKeyMappings:
    """
    All the elements for which mapping key sent in the request is different
    from the mapping key comes in the response.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    key_mapping: List[KeyMapping] = field(
        default_factory=list,
        metadata={
            "name": "KeyMapping",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class RequiredField:
    """
    Parameters
    ----------
    name: The name of the required field
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    name: Optional[RequiredFieldName] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Requisition:
    """
    Requisition Form of Payment.

    Parameters
    ----------
    number: Requisition number used for accounting
    category: Classification Category for the requisition payment
    type: Type can be Cash or Credit for category as Government
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
        }
    )
    category: Optional[RequisitionCategory] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
        }
    )
    type: Optional[RequisitionType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )


@dataclass
class ResponseMessage:
    """A simple textual fare note.

    Used within several other objects.

    Parameters
    ----------
    value:
    code:
    type: Indicates the type of message (Warning, Error, Info)
    provider_code:
    supplier_code:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    value: Optional[str] = field(
        default=None
    )
    code: Optional[int] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        }
    )
    type: Optional[ResponseMessageType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        }
    )


@dataclass
class ReviewBooking:
    """Review Booking or Queue Minders is to add the reminders in the Provider
    Reservation along with the date time and Queue details.

    On the date time defined in reminders, the message along with the
    PNR goes to the desired Queue.

    Parameters
    ----------
    key: Returned in response. Use it for update of saved review
        booking.
    queue: Queue number, Must be numeric and less than 100.
    queue_category: Queue Category, 2 Character Alpha or Numeric.
    date_time: Date and Time to place message on designated Queue,
        Should be prior to the last segment date in the PNR.
    pseudo_city_code: Input PCC optional value for placing the PNR into
        Queue. If not passed, will add as default PNR's Pseudo.
    provider_code: The code of the Provider (e.g 1G,1V).
    provider_reservation_info_ref: Provider Reservation reference.
        Returned in the response. Use it for update of saved Review
        Booking.
    remarks: Remark or reminder message. It can be truncated depending
        on the provider.
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    queue: Optional[int] = field(
        default=None,
        metadata={
            "name": "Queue",
            "type": "Attribute",
            "required": True,
            "max_inclusive": 99,
        }
    )
    queue_category: Optional[str] = field(
        default=None,
        metadata={
            "name": "QueueCategory",
            "type": "Attribute",
            "max_length": 2,
        }
    )
    date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DateTime",
            "type": "Attribute",
            "required": True,
        }
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    provider_reservation_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        }
    )
    remarks: Optional[str] = field(
        default=None,
        metadata={
            "name": "Remarks",
            "type": "Attribute",
            "required": True,
            "max_length": 300,
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class Ssr:
    """
    Special serivces like wheel chair, or pet carrier.

    Parameters
    ----------
    key:
    segment_ref: Reference to the air segment. May be required for some
        Types.
    passive_segment_ref: Reference to the passive segment.
    provider_reservation_info_ref: Provider reservation reference key.
    type: Programmatic SSRs use codes recognized by the
        provider/supplier (example, VGML=vegetarian meal code). Manual
        SSRs do not have an associated programmatic code.
    status:
    free_text: Certain SSR types will require a free text message. For
        example MAAS (Meet and assist).
    carrier:
    carrier_specific_text: Carrier specific information which are not
        captured in the FreeText field(not present in IATA's standard
        SSR DOCO format). An example is VISA Expiration Date.
    description:
    provider_defined_type: Original Type as sent by the provider
    ssrrule_ref: UniqueID to associate a rule to the SSR
    url:
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    profile_id: Key assigned for Secure Flight Document value from the
        specified profile
    profile_secure_flight_doc_key: Unique ID of Booking Traveler's
        Profile that contains the Secure flight Detail
    """
    class Meta:
        name = "SSR"
        namespace = "http://www.travelport.com/schema/common_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    segment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SegmentRef",
            "type": "Attribute",
        }
    )
    passive_segment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PassiveSegmentRef",
            "type": "Attribute",
        }
    )
    provider_reservation_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 4,
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
        }
    )
    free_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "FreeText",
            "type": "Attribute",
        }
    )
    carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    carrier_specific_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "CarrierSpecificText",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 64,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
        }
    )
    provider_defined_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderDefinedType",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        }
    )
    ssrrule_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SSRRuleRef",
            "type": "Attribute",
        }
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Attribute",
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )
    profile_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
        }
    )
    profile_secure_flight_doc_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProfileSecureFlightDocKey",
            "type": "Attribute",
        }
    )


@dataclass
class SearchEvent(TypeTimeRange):
    """
    Search for various reservation events.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    type: Optional[TypeEventType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )


@dataclass
class SearchTicketing:
    """
    Search restriction by Agent.

    Parameters
    ----------
    ticket_status: Return only PNRs with ticketed, non-ticketed or both
    reservation_status: Used only if "TicketStatus" set to "No" or
        "Both". Return only PNRs with specific reservation status or
        both statuses.
    ticket_date: Identifies when this reservation was ticketed, or when
        it should be ticketed by (in the event of a TTL)
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    ticket_status: SearchTicketingTicketStatus = field(
        default=SearchTicketingTicketStatus.BOTH,
        metadata={
            "name": "TicketStatus",
            "type": "Attribute",
        }
    )
    reservation_status: SearchTicketingReservationStatus = field(
        default=SearchTicketingReservationStatus.BOTH,
        metadata={
            "name": "ReservationStatus",
            "type": "Attribute",
        }
    )
    ticket_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TicketDate",
            "type": "Attribute",
        }
    )


@dataclass
class SeatAssignment:
    """
    Parameters
    ----------
    key:
    status:
    seat:
    seat_type_code: The 4 letter SSR code like SMSW,NSSW,SMST etc.
    segment_ref:
    flight_details_ref:
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    rail_coach_number: Coach number for which rail seatmap/coachmap is
        returned.
    """
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
            "length": 2,
            "white_space": "collapse",
        }
    )
    seat: Optional[str] = field(
        default=None,
        metadata={
            "name": "Seat",
            "type": "Attribute",
            "required": True,
        }
    )
    seat_type_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeatTypeCode",
            "type": "Attribute",
            "length": 4,
            "white_space": "collapse",
        }
    )
    segment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SegmentRef",
            "type": "Attribute",
        }
    )
    flight_details_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FlightDetailsRef",
            "type": "Attribute",
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )
    rail_coach_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "RailCoachNumber",
            "type": "Attribute",
        }
    )


@dataclass
class SeatAttributes:
    """
    Identifies the seat attribute of the service.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    seat_attribute: List[SeatAttribute] = field(
        default_factory=list,
        metadata={
            "name": "SeatAttribute",
            "type": "Element",
            "max_occurs": 10,
        }
    )


@dataclass
class Segment:
    """
    The base segment type.

    Parameters
    ----------
    segment_remark:
    key:
    status: Status of this segment.
    passive:
    travel_order: To identify the appropriate travel sequence for
        Air/Car/Hotel segments/reservations based on travel dates. This
        ordering is applicable across the UR not provider or traveler
        specific
    provider_segment_order: To identify the appropriate travel sequence
        for Air/Car/Hotel/Rail segments/reservations in the provider
        reservation.
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    segment_remark: List[SegmentRemark] = field(
        default_factory=list,
        metadata={
            "name": "SegmentRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
        }
    )
    passive: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Passive",
            "type": "Attribute",
        }
    )
    travel_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "TravelOrder",
            "type": "Attribute",
        }
    )
    provider_segment_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "ProviderSegmentOrder",
            "type": "Attribute",
            "max_inclusive": 999,
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class SpecialEquipment:
    """
    Parameters
    ----------
    key:
    type: Special equipment associated with a specific vehicle
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class SupplierLocator:
    """
    Locator code on the host carrier system.

    Parameters
    ----------
    segment_ref: Air/Passive Segment Reference
    supplier_code: Carrier Code
    supplier_locator_code: Carrier reservation locator code
    provider_reservation_info_ref: Provider Reservation  reference
    create_date_time: The Date and Time which the reservation is
        received from the Vendor as a SupplierLocator creation Date.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    segment_ref: List[TypeGeneralReference] = field(
        default_factory=list,
        metadata={
            "name": "SegmentRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )
    supplier_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierLocatorCode",
            "type": "Attribute",
            "required": True,
        }
    )
    provider_reservation_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        }
    )
    create_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreateDateTime",
            "type": "Attribute",
        }
    )


@dataclass
class ThirdPartyInformation:
    """Third party supplier locator information.

    Specifically applicable for SDK booking.

    Parameters
    ----------
    segment_ref: Air/Passive Segment Reference
    third_party_code: Third party supplier code.
    third_party_locator_code: Confirmation number for third party
        supplier.
    third_party_name: Third party supplier name.
    provider_reservation_info_ref: Provider Reservation  reference
    key: Unique identifier of the third party supplier. Key can be used
        to modify or delete saved third party information.
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    segment_ref: List[TypeGeneralReference] = field(
        default_factory=list,
        metadata={
            "name": "SegmentRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    third_party_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ThirdPartyCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    third_party_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ThirdPartyLocatorCode",
            "type": "Attribute",
            "max_length": 36,
        }
    )
    third_party_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ThirdPartyName",
            "type": "Attribute",
            "max_length": 64,
        }
    )
    provider_reservation_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class TravelComplianceData:
    """
    Travel Compliance and Preferred Supplier information of the traveler
    specific to a segment.

    Parameters
    ----------
    policy_compliance:
    contract_compliance:
    preferred_supplier:
    key: System generated key, returned back in the response. This can
        be used to modify or delete a saved TravelComplianceData.
    air_segment_ref: Refers to Air Segment. Applicable only for Air.
        Ignored for others.
    passive_segment_ref: Refers to Passive Segment. Applicable only for
        Passive. Ignored for others.
    rail_segment_ref: Refers to Rail Segment. Applicable only for Rail.
        Ignored for others.
    reservation_locator_ref: This is returned in the response. Any input
        will be ignored for this attribute. This represents the
        association of Travel Compliance Data with the uAPI reservation
        locator code, mainly relevant to Hotel and Vehicle.
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    policy_compliance: List["TravelComplianceData.PolicyCompliance"] = field(
        default_factory=list,
        metadata={
            "name": "PolicyCompliance",
            "type": "Element",
            "max_occurs": 2,
        }
    )
    contract_compliance: List["TravelComplianceData.ContractCompliance"] = field(
        default_factory=list,
        metadata={
            "name": "ContractCompliance",
            "type": "Element",
            "max_occurs": 2,
        }
    )
    preferred_supplier: List["TravelComplianceData.PreferredSupplier"] = field(
        default_factory=list,
        metadata={
            "name": "PreferredSupplier",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    air_segment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirSegmentRef",
            "type": "Attribute",
        }
    )
    passive_segment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PassiveSegmentRef",
            "type": "Attribute",
        }
    )
    rail_segment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "RailSegmentRef",
            "type": "Attribute",
        }
    )
    reservation_locator_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReservationLocatorRef",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )

    @dataclass
    class PolicyCompliance:
        """
        Parameters
        ----------
        in_policy: Policy Compliance Indicator. For In-Policy set to
            'true', For Out-Of-Policy set to 'false''.
        policy_token: Optional text message to set the rule or token for
            which it's In Policy or Out Of Policy.
        """
        in_policy: Optional[bool] = field(
            default=None,
            metadata={
                "name": "InPolicy",
                "type": "Attribute",
                "required": True,
            }
        )
        policy_token: Optional[str] = field(
            default=None,
            metadata={
                "name": "PolicyToken",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 128,
            }
        )

    @dataclass
    class ContractCompliance:
        """
        Parameters
        ----------
        in_contract: Contract Compliance Indicator. For In-Contract set
            to 'true', For Out-Of-Contract set to 'false'.
        contract_token: Optional text message to set the rule or token
            for which it's In Contract or Out Of Contract.
        """
        in_contract: Optional[bool] = field(
            default=None,
            metadata={
                "name": "InContract",
                "type": "Attribute",
                "required": True,
            }
        )
        contract_token: Optional[str] = field(
            default=None,
            metadata={
                "name": "ContractToken",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 128,
            }
        )

    @dataclass
    class PreferredSupplier:
        """
        Parameters
        ----------
        preferred: Preferred Supplier - 'true', 'false'.
        profile_type: Indicate profile type. e.g. if Agency Preferred
            then pass Agency, if Traveler Preferred then pass Traveler.
        """
        preferred: Optional[bool] = field(
            default=None,
            metadata={
                "name": "Preferred",
                "type": "Attribute",
                "required": True,
            }
        )
        profile_type: Optional[TypeProfileType] = field(
            default=None,
            metadata={
                "name": "ProfileType",
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass
class UnassociatedRemark(TypeRemarkWithTravelerRef):
    """
    A textual remark container to hold non-associated itinerary remarks.

    Parameters
    ----------
    key:
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class VendorLocation(TypeVendorLocation):
    """
    Location definition specific to a Vendor in a specific provider (e.g. 1G)
    system.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"


@dataclass
class Xmlremark:
    """A remark container to hold an XML document.

    (max 1024 chars) This will be encoded with xml encoding.

    Parameters
    ----------
    value:
    key:
    category: A category to group and organize the various remarks. This
        is not required, but it is recommended.
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        name = "XMLRemark"
        namespace = "http://www.travelport.com/schema/common_v48_0"

    value: Optional[str] = field(
        default=None
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    category: Optional[str] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
            "max_length": 10,
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class TypeAgencyHierarchyReference:
    class Meta:
        name = "typeAgencyHierarchyReference"

    profile_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_type: Optional[TypeAgencyProfileLevel] = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TypeAssociatedRemark(TypeRemarkWithTravelerRef):
    """
    A textual remark container to hold Associated itinerary remarks.

    Parameters
    ----------
    key:
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        name = "typeAssociatedRemark"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class TypeErrorInfo:
    """
    Container for error data when there is an application error.
    """
    class Meta:
        name = "typeErrorInfo"

    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "required": True,
        }
    )
    service: Optional[str] = field(
        default=None,
        metadata={
            "name": "Service",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "required": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "required": True,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "required": True,
        }
    )
    transaction_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransactionId",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "required": True,
        }
    )
    trace_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TraceId",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    command_history: Optional[str] = field(
        default=None,
        metadata={
            "name": "CommandHistory",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    auxdata: Optional[Auxdata] = field(
        default=None,
        metadata={
            "name": "Auxdata",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    stack_trace: Optional[str] = field(
        default=None,
        metadata={
            "name": "StackTrace",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )


@dataclass
class TypeFeeInfo:
    """
    A generic type of fee for those charges which are incurred by the
    passenger, but not necessarily shown on tickets.

    Parameters
    ----------
    tax_info_ref: This reference elements will associate relevant taxes
        to this fee
    included_in_base:
    base_amount:
    description:
    sub_code:
    key:
    amount:
    code:
    fee_token:
    payment_ref: The reference to the one of the air reservation
        payments if fee included in charge
    booking_traveler_ref: Reference to booking traveler
    passenger_type_code:
    text: Additional Information returned from Supplier.(ACH  only)
    provider_code:
    supplier_code:
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        name = "typeFeeInfo"

    tax_info_ref: List["TypeFeeInfo.TaxInfoRef"] = field(
        default_factory=list,
        metadata={
            "name": "TaxInfoRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    included_in_base: Optional[IncludedInBase] = field(
        default=None,
        metadata={
            "name": "IncludedInBase",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    base_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseAmount",
            "type": "Attribute",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
        }
    )
    sub_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubCode",
            "type": "Attribute",
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        }
    )
    fee_token: Optional[str] = field(
        default=None,
        metadata={
            "name": "FeeToken",
            "type": "Attribute",
        }
    )
    payment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentRef",
            "type": "Attribute",
        }
    )
    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        }
    )
    passenger_type_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PassengerTypeCode",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 5,
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 64,
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )

    @dataclass
    class TaxInfoRef:
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass
class TypeGuaranteeInformation:
    """
    Information pertaining to the payment of type Guarantee.

    Parameters
    ----------
    type: Guarantee only or Deposit
    agency_type: Guarantee to Agency IATA or Guarantee to Another Agency
        IATA
    iatanumber: Payment IATA number. (ie. IATA of Agency or Other
        Agency)
    """
    class Meta:
        name = "typeGuaranteeInformation"

    type: Optional[TypeGuaranteeInformationType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    agency_type: Optional[TypeGuaranteeInformationAgencyType] = field(
        default=None,
        metadata={
            "name": "AgencyType",
            "type": "Attribute",
            "required": True,
        }
    )
    iatanumber: Optional[str] = field(
        default=None,
        metadata={
            "name": "IATANumber",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )


@dataclass
class TypeKeyword:
    """
    A complexType for keyword information.

    Parameters
    ----------
    sub_key: A further breakdown of a keyword.
    text: Information for a keyword.
    name: The keyword name.
    number: The number for this keyword.
    description: A brief description of the keyword
    language_code: ISO 639 two-character language codes are used to
        retrieve specific information in the requested language. For
        Rich Content and Branding, language codes ZH-HANT (Chinese
        Traditional), ZH-HANS (Chinese Simplified), FR-CA (French
        Canadian) and PT-BR (Portuguese Brazil) can also be used. For
        RCH, language codes ENGB, ENUS, DEDE, DECH can also be used.
        Only certain services support this attribute. Providers: ACH,
        RCH, 1G, 1V, 1P, 1J.
    """
    class Meta:
        name = "typeKeyword"

    sub_key: List[TypeSubKey] = field(
        default_factory=list,
        metadata={
            "name": "SubKey",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 99,
        }
    )
    text: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "max_length": 12,
        }
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
        }
    )
    language_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LanguageCode",
            "type": "Attribute",
        }
    )


@dataclass
class TypeOtakeyword:
    """
    A complexType for keyword information.

    Parameters
    ----------
    sub_key: A further breakdown of a keyword.
    text: Information for a keyword.
    name: The keyword name.
    number: The number for this keyword.
    description: A brief description of the keyword
    """
    class Meta:
        name = "typeOTAKeyword"

    sub_key: List[TypeOtasubKey] = field(
        default_factory=list,
        metadata={
            "name": "SubKey",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 99,
        }
    )
    text: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "max_length": 6,
        }
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
        }
    )


@dataclass
class TypeProfileRef:
    """
    ProfileEntityID and ProfileLevel together identity a profile entity.
    """
    class Meta:
        name = "typeProfileRef"

    profile_entity_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProfileEntityID",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_level: Optional[TypeProfileLevel] = field(
        default=None,
        metadata={
            "name": "ProfileLevel",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TypeProviderReservationSpecificInfo:
    """
    Parameters
    ----------
    operated_by: Cross accrual carrier info
    provider_reservation_info_ref: Tagging provider reservation info
        with LoyaltyCard.
    provider_reservation_level: If true means Loyalty card is applied at
        ProviderReservation level.
    reservation_level: If true means Loyalty card is applied at
        Universal Record Reservation level e.g. Hotel Reservation,
        Vehicle Reservation etc.
    """
    class Meta:
        name = "typeProviderReservationSpecificInfo"

    operated_by: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OperatedBy",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
            "min_length": 1,
            "white_space": "collapse",
        }
    )
    provider_reservation_info_ref: Optional[ProviderReservationInfoRef] = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    provider_reservation_level: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ProviderReservationLevel",
            "type": "Attribute",
        }
    )
    reservation_level: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReservationLevel",
            "type": "Attribute",
        }
    )


@dataclass
class TypeResultMessage:
    """
    Used to identify the results of a requests.

    Parameters
    ----------
    value:
    code:
    type: Indicates the type of message (Warning, Error, Info)
    """
    class Meta:
        name = "typeResultMessage"

    value: Optional[str] = field(
        default=None
    )
    code: Optional[int] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        }
    )
    type: Optional[TypeResultMessageType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )


@dataclass
class TypeStructuredAddress:
    """
    A fully structured address.

    Parameters
    ----------
    address_name:
    street: The Address street and number, e.g. 105 Main St.
    city: The city name for the requested address, e.g. Atlanta.
    state: The State or Province of address requested, e.g. CA, Ontario.
    postal_code: The 5-15 alphanumeric postal Code for the requested
        address, e.g. 90210.
    country: The Full country name or two letter ISO country code e.g.
        US, France. A two letter country code is required for a Postal
        Code Searches.
    provider_reservation_info_ref: Tagging provider reservation info
        with Address.
    key: Key for update/delete of the element
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        name = "typeStructuredAddress"

    address_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddressName",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_length": 128,
        }
    )
    street: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Street",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 255,
        }
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "min_length": 2,
            "max_length": 50,
        }
    )
    state: Optional[str] = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    postal_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PostalCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "min_length": 1,
            "max_length": 15,
        }
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "length": 2,
        }
    )
    provider_reservation_info_ref: List[ProviderReservationInfoRef] = field(
        default_factory=list,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 99,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class TypeTaxInfo:
    """
    Parameters
    ----------
    tax_detail:
    included_in_base:
    key: The tax key represents a valid key of tax
    category: The tax category represents a valid IATA tax code.
    carrier_defined_category: Optional category, where a carrier has
        used a non-standard IATA tax category. The tax category will be
        set to "DU"
    segment_ref: The segment to which that tax is relative (if
        applicable)
    flight_details_ref: The flight details that this tax is relative to
        (if applicable)
    coupon_ref: The coupon to which that tax is relative (if applicable)
    amount:
    origin_airport:
    destination_airport:
    country_code:
    fare_info_ref:
    tax_exempted: This indicates whether the tax specified by tax
        category is exempted.
    provider_code: Code of the provider returning this TaxInfo.
    supplier_code: Code of the supplier returning this TaxInfo.
    text: Additional Information returned from Supplier.(ACH  only)
    """
    class Meta:
        name = "typeTaxInfo"

    tax_detail: List[TaxDetail] = field(
        default_factory=list,
        metadata={
            "name": "TaxDetail",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    included_in_base: Optional[IncludedInBase] = field(
        default=None,
        metadata={
            "name": "IncludedInBase",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    category: Optional[str] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
            "required": True,
        }
    )
    carrier_defined_category: Optional[str] = field(
        default=None,
        metadata={
            "name": "CarrierDefinedCategory",
            "type": "Attribute",
        }
    )
    segment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SegmentRef",
            "type": "Attribute",
        }
    )
    flight_details_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FlightDetailsRef",
            "type": "Attribute",
        }
    )
    coupon_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "CouponRef",
            "type": "Attribute",
        }
    )
    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
        }
    )
    origin_airport: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginAirport",
            "type": "Attribute",
            "length": 3,
        }
    )
    destination_airport: Optional[str] = field(
        default=None,
        metadata={
            "name": "DestinationAirport",
            "type": "Attribute",
            "length": 3,
        }
    )
    country_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CountryCode",
            "type": "Attribute",
        }
    )
    fare_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareInfoRef",
            "type": "Attribute",
        }
    )
    tax_exempted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TaxExempted",
            "type": "Attribute",
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )


@dataclass
class TypeTimeSpec:
    """
    Specifies times as either specific times, or a time range.

    Parameters
    ----------
    time_range:
    specific_time:
    preferred_time: Specifies a time that would be preferred within the
        time range specified.
    """
    class Meta:
        name = "typeTimeSpec"

    time_range: Optional[TypeTimeRange] = field(
        default=None,
        metadata={
            "name": "TimeRange",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    specific_time: Optional[TypeSpecificTime] = field(
        default=None,
        metadata={
            "name": "SpecificTime",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    preferred_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "PreferredTime",
            "type": "Attribute",
        }
    )


@dataclass
class TypeTransactionsAllowed(TypeBookingTransactionsAllowed):
    """
    Parameters
    ----------
    shopping_enabled: Allow or prohibit shopping transaction for the
        given product type on this Provider/Supplier. Inheritable.
    pricing_enabled: Allow or prohibit pricing transaction for the given
        product type on this Provider/Supplier. Inheritable.
    """
    class Meta:
        name = "typeTransactionsAllowed"

    shopping_enabled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ShoppingEnabled",
            "type": "Attribute",
        }
    )
    pricing_enabled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PricingEnabled",
            "type": "Attribute",
        }
    )


@dataclass
class TypeVoucherInformation:
    """
    Information pertaining to the payment of a Vehicle Rental.

    Parameters
    ----------
    voucher_type: Specifies if the Voucher is for Full Credit or a
        Group/Day or a Monetary Amount or RegularVoucher.
    amount: Amount associated with the Voucher.
    confirmation_number: Confirmation from the vendor for the voucher
    account_name: Associated account name for the voucher
    number: To advise car associates of the voucher number and store in
        the car segment. It is required when VoucherType selected as
        "RegularVoucher" for 1P, 1J only.
    """
    class Meta:
        name = "typeVoucherInformation"

    voucher_type: Optional[TypeVoucherType] = field(
        default=None,
        metadata={
            "name": "VoucherType",
            "type": "Attribute",
            "required": True,
        }
    )
    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        }
    )
    confirmation_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConfirmationNumber",
            "type": "Attribute",
        }
    )
    account_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountName",
            "type": "Attribute",
        }
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        }
    )


@dataclass
class AccountInformation:
    """
    Account Information required for File Finishing.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    address: Optional[TypeStructuredAddress] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
        }
    )
    phone_number: List[PhoneNumber] = field(
        default_factory=list,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    account_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountName",
            "type": "Attribute",
        }
    )


@dataclass
class AddressRestriction:
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    required_field: List[RequiredField] = field(
        default_factory=list,
        metadata={
            "name": "RequiredField",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class AgencyContactInfo:
    """Generic agency contact information container.

    It must contain  at least one phone number to be used by an agency
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    phone_number: List[PhoneNumber] = field(
        default_factory=list,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )


@dataclass
class AgencyInfo:
    """
    Tracks the various agent/agency information.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    agent_action: List[AgentAction] = field(
        default_factory=list,
        metadata={
            "name": "AgentAction",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class AgencyInformation:
    """
    Agency Information required for File Finishing.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    address: Optional[TypeStructuredAddress] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
        }
    )
    email: List[Email] = field(
        default_factory=list,
        metadata={
            "name": "Email",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    phone_number: List[PhoneNumber] = field(
        default_factory=list,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class AirExchangeInfo:
    """
    Provides results of a exchange quote.

    Parameters
    ----------
    total_penalty_tax_info:
    paid_tax:
    ticket_fee_info: Used for rapid reprice. Providers: 1G/1V/1P/1S/1A
    reason: Used for rapid reprice. The reason code or text is returned
        if the PricingTag is not equal to A, and explains why A was not
        returned. Providers: 1G/1V/1P/1S/1A
    fee_info:
    tax_info: Itinerary level taxes
    exchange_amount:
    base_fare:
    equivalent_base_fare:
    taxes:
    change_fee:
    forfeit_amount:
    refundable:
    exchangeable:
    first_class_upgrade:
    ticket_by_date:
    pricing_tag:
    equivalent_change_fee:
    equivalent_exchange_amount:
    add_collection:
    residual_value:
    total_residual_value:
    original_flight_value:
    flown_segment_value:
    bulk_ticket_advisory:
    fare_pull:
    passenger_type_code:
    passenger_count:
    form_of_refund: How the refund will be issued. Values will be MCO or
        FormOfPayment
    refund: Total refund amount.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    total_penalty_tax_info: Optional["AirExchangeInfo.TotalPenaltyTaxInfo"] = field(
        default=None,
        metadata={
            "name": "TotalPenaltyTaxInfo",
            "type": "Element",
        }
    )
    paid_tax: List[TypeTax] = field(
        default_factory=list,
        metadata={
            "name": "PaidTax",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    ticket_fee_info: List["AirExchangeInfo.TicketFeeInfo"] = field(
        default_factory=list,
        metadata={
            "name": "TicketFeeInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    reason: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    fee_info: List[TypeFeeInfo] = field(
        default_factory=list,
        metadata={
            "name": "FeeInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    tax_info: List[TypeTaxInfo] = field(
        default_factory=list,
        metadata={
            "name": "TaxInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    exchange_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExchangeAmount",
            "type": "Attribute",
            "required": True,
        }
    )
    base_fare: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseFare",
            "type": "Attribute",
        }
    )
    equivalent_base_fare: Optional[str] = field(
        default=None,
        metadata={
            "name": "EquivalentBaseFare",
            "type": "Attribute",
        }
    )
    taxes: Optional[str] = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Attribute",
        }
    )
    change_fee: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChangeFee",
            "type": "Attribute",
        }
    )
    forfeit_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "ForfeitAmount",
            "type": "Attribute",
        }
    )
    refundable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Refundable",
            "type": "Attribute",
        }
    )
    exchangeable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Exchangeable",
            "type": "Attribute",
        }
    )
    first_class_upgrade: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FirstClassUpgrade",
            "type": "Attribute",
        }
    )
    ticket_by_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketByDate",
            "type": "Attribute",
        }
    )
    pricing_tag: Optional[str] = field(
        default=None,
        metadata={
            "name": "PricingTag",
            "type": "Attribute",
        }
    )
    equivalent_change_fee: Optional[str] = field(
        default=None,
        metadata={
            "name": "EquivalentChangeFee",
            "type": "Attribute",
        }
    )
    equivalent_exchange_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "EquivalentExchangeAmount",
            "type": "Attribute",
        }
    )
    add_collection: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddCollection",
            "type": "Attribute",
        }
    )
    residual_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResidualValue",
            "type": "Attribute",
        }
    )
    total_residual_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalResidualValue",
            "type": "Attribute",
        }
    )
    original_flight_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginalFlightValue",
            "type": "Attribute",
        }
    )
    flown_segment_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "FlownSegmentValue",
            "type": "Attribute",
        }
    )
    bulk_ticket_advisory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BulkTicketAdvisory",
            "type": "Attribute",
        }
    )
    fare_pull: Optional[TypeFarePull] = field(
        default=None,
        metadata={
            "name": "FarePull",
            "type": "Attribute",
        }
    )
    passenger_type_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PassengerTypeCode",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 5,
        }
    )
    passenger_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "PassengerCount",
            "type": "Attribute",
        }
    )
    form_of_refund: Optional[TypeFormOfRefund] = field(
        default=None,
        metadata={
            "name": "FormOfRefund",
            "type": "Attribute",
        }
    )
    refund: Optional[str] = field(
        default=None,
        metadata={
            "name": "Refund",
            "type": "Attribute",
        }
    )

    @dataclass
    class TotalPenaltyTaxInfo:
        penalty_tax_info: List[TypeTax] = field(
            default_factory=list,
            metadata={
                "name": "PenaltyTaxInfo",
                "type": "Element",
                "max_occurs": 999,
            }
        )
        total_penalty_tax: Optional[str] = field(
            default=None,
            metadata={
                "name": "TotalPenaltyTax",
                "type": "Attribute",
            }
        )

    @dataclass
    class TicketFeeInfo:
        base: Optional[str] = field(
            default=None,
            metadata={
                "name": "Base",
                "type": "Attribute",
            }
        )
        tax: Optional[str] = field(
            default=None,
            metadata={
                "name": "Tax",
                "type": "Attribute",
            }
        )
        total: Optional[str] = field(
            default=None,
            metadata={
                "name": "Total",
                "type": "Attribute",
            }
        )


@dataclass
class AirSeatAssignment(SeatAssignment):
    """
    Identifies the seat assignment for a passenger.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"


@dataclass
class BaseCoreSearchReq(BaseCoreReq):
    """
    Base Request for Air Search.
    """
    next_result_reference: List[NextResultReference] = field(
        default_factory=list,
        metadata={
            "name": "NextResultReference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )


@dataclass
class BaseReq(BaseCoreReq):
    override_pcc: Optional[OverridePcc] = field(
        default=None,
        metadata={
            "name": "OverridePCC",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    retrieve_provider_reservation_details: bool = field(
        default=False,
        metadata={
            "name": "RetrieveProviderReservationDetails",
            "type": "Attribute",
        }
    )


@dataclass
class BaseRsp:
    """
    The base type for all responses.

    Parameters
    ----------
    response_message:
    trace_id: Unique identifier for this atomic transaction traced by
        the user. Use is optional.
    transaction_id: System generated unique identifier for this atomic
        transaction.
    response_time: The time (in ms) the system spent processing this
        request, not including transmission times.
    command_history: HTTP link to download command history and debugging
        information of the request that generated this response. Must be
        enabled on the system.
    """
    response_message: List[ResponseMessage] = field(
        default_factory=list,
        metadata={
            "name": "ResponseMessage",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    trace_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TraceId",
            "type": "Attribute",
        }
    )
    transaction_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransactionId",
            "type": "Attribute",
        }
    )
    response_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "ResponseTime",
            "type": "Attribute",
        }
    )
    command_history: Optional[str] = field(
        default=None,
        metadata={
            "name": "CommandHistory",
            "type": "Attribute",
        }
    )


@dataclass
class CardRestriction:
    """
    Parameters
    ----------
    required_field:
    code: 2 letter Credit/Debit Card merchant type
    name: Card merchant description
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    required_field: List[RequiredField] = field(
        default_factory=list,
        metadata={
            "name": "RequiredField",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 2,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class DeliveryInfo:
    """
    Container to encapsulate all delivery related information.

    Parameters
    ----------
    shipping_address:
    phone_number:
    email:
    general_remark:
    provider_reservation_info_ref: Tagging provider reservation info
        with Delivery Info.
    type: An arbitrary identifier to categorize this delivery info
    signature_required: Indicates whether a signature shoud be required
        in order to make the delivery.
    tracking_number: The tracking number of the shipping company making
        the delivery.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    shipping_address: Optional[TypeStructuredAddress] = field(
        default=None,
        metadata={
            "name": "ShippingAddress",
            "type": "Element",
        }
    )
    phone_number: Optional[PhoneNumber] = field(
        default=None,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
        }
    )
    email: Optional[Email] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
        }
    )
    general_remark: List[GeneralRemark] = field(
        default_factory=list,
        metadata={
            "name": "GeneralRemark",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    provider_reservation_info_ref: List[ProviderReservationInfoRef] = field(
        default_factory=list,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    signature_required: Optional[str] = field(
        default=None,
        metadata={
            "name": "SignatureRequired",
            "type": "Attribute",
            "max_length": 10,
        }
    )
    tracking_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrackingNumber",
            "type": "Attribute",
        }
    )


@dataclass
class ErrorInfo(TypeErrorInfo):
    """
    Container for error data when there is an application error.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"


@dataclass
class HostTokenList:
    """
    The shared object list of Host Tokens.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    host_token: List[HostToken] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class InvoiceData:
    """
    List of invoices only for 1G/1V.

    Parameters
    ----------
    booking_traveler_information:
    key:
    invoice_number: Invoice number
    issue_date: Invoice issue date
    provider_reservation_info_ref: Provider reservation reference key.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    booking_traveler_information: List[BookingTravelerInformation] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerInformation",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 9,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    invoice_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "InvoiceNumber",
            "type": "Attribute",
            "required": True,
        }
    )
    issue_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Attribute",
        }
    )
    provider_reservation_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class InvoiceRemark(TypeAssociatedRemark):
    """
    Parameters
    ----------
    air_segment_ref: Reference to AirSegment from an Air Reservation.
    hotel_reservation_ref: Specify the locator code of Hotel
        reservation.
    vehicle_reservation_ref: Specify the locator code of Vehicle
        reservation.
    passive_segment_ref: Reference to PassiveSegment from a Passive
        Reservation.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    air_segment_ref: Optional[TypeSegmentRef] = field(
        default=None,
        metadata={
            "name": "AirSegmentRef",
            "type": "Element",
        }
    )
    hotel_reservation_ref: Optional[TypeNonAirReservationRef] = field(
        default=None,
        metadata={
            "name": "HotelReservationRef",
            "type": "Element",
        }
    )
    vehicle_reservation_ref: Optional[TypeNonAirReservationRef] = field(
        default=None,
        metadata={
            "name": "VehicleReservationRef",
            "type": "Element",
        }
    )
    passive_segment_ref: Optional[TypeSegmentRef] = field(
        default=None,
        metadata={
            "name": "PassiveSegmentRef",
            "type": "Element",
        }
    )


@dataclass
class Keyword(TypeKeyword):
    """
    Detail information of keywords.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"


@dataclass
class LocationAddress(TypeStructuredAddress):
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"


@dataclass
class LoyaltyCard:
    """
    Provider loyalty card information.

    Parameters
    ----------
    provider_reservation_specific_info:
    key:
    supplier_code: The code used to identify the Loyalty supplier, e.g.
        AA, ZE, MC
    alliance_level:
    membership_program: Loyalty Program membership Id of the traveler
        specific to Amtrak(2V) Guest Rewards
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    card_number:
    status:
    membership_status:
    free_text:
    supplier_type:
    level:
    priority_code:
    vendor_location_ref:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    provider_reservation_specific_info: List[TypeProviderReservationSpecificInfo] = field(
        default_factory=list,
        metadata={
            "name": "ProviderReservationSpecificInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )
    alliance_level: Optional[str] = field(
        default=None,
        metadata={
            "name": "AllianceLevel",
            "type": "Attribute",
        }
    )
    membership_program: Optional[str] = field(
        default=None,
        metadata={
            "name": "MembershipProgram",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )
    card_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardNumber",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 36,
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
        }
    )
    membership_status: Optional[str] = field(
        default=None,
        metadata={
            "name": "MembershipStatus",
            "type": "Attribute",
        }
    )
    free_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "FreeText",
            "type": "Attribute",
        }
    )
    supplier_type: Optional[TypeProduct] = field(
        default=None,
        metadata={
            "name": "SupplierType",
            "type": "Attribute",
        }
    )
    level: Optional[str] = field(
        default=None,
        metadata={
            "name": "Level",
            "type": "Attribute",
            "pattern": r"[a-zA-Z0-9]{1,1}",
        }
    )
    priority_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PriorityCode",
            "type": "Attribute",
            "pattern": r"[a-zA-Z0-9]{1,1}",
        }
    )
    vendor_location_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "VendorLocationRef",
            "type": "Attribute",
        }
    )


@dataclass
class Mcoinformation:
    """
    Parameters
    ----------
    passenger_info:
    mconumber: The unique MCO number
    status: Current status of the MCO
    mcotype: The Type of MCO. Once of Agency Fee, Airline Service Fee,
        or Residual value from an Exchange.
    """
    class Meta:
        name = "MCOInformation"

    passenger_info: List[PassengerInfo] = field(
        default_factory=list,
        metadata={
            "name": "PassengerInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    mconumber: Optional[str] = field(
        default=None,
        metadata={
            "name": "MCONumber",
            "type": "Attribute",
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
        }
    )
    mcotype: Optional[str] = field(
        default=None,
        metadata={
            "name": "MCOType",
            "type": "Attribute",
        }
    )


@dataclass
class McopriceData:
    """
    Parameters
    ----------
    tax_info:
    commission:
    mcoamount: The total value of the MCO including any processing fees.
    mcoequivalent_fare: Exchange value of the currency actually
        collected.
    mcototal_amount: The Total amount for the MCO.
    """
    class Meta:
        name = "MCOPriceData"
        namespace = "http://www.travelport.com/schema/common_v48_0"

    tax_info: List[TypeTaxInfo] = field(
        default_factory=list,
        metadata={
            "name": "TaxInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    commission: Optional["McopriceData.Commission"] = field(
        default=None,
        metadata={
            "name": "Commission",
            "type": "Element",
        }
    )
    mcoamount: Optional[str] = field(
        default=None,
        metadata={
            "name": "MCOAmount",
            "type": "Attribute",
            "required": True,
        }
    )
    mcoequivalent_fare: Optional[str] = field(
        default=None,
        metadata={
            "name": "MCOEquivalentFare",
            "type": "Attribute",
        }
    )
    mcototal_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "MCOTotalAmount",
            "type": "Attribute",
        }
    )

    @dataclass
    class Commission:
        """
        Parameters
        ----------
        amount: The monetary amount.
        percentage: The percentage.
        """
        amount: Optional[str] = field(
            default=None,
            metadata={
                "name": "Amount",
                "type": "Attribute",
            }
        )
        percentage: Optional[str] = field(
            default=None,
            metadata={
                "name": "Percentage",
                "type": "Attribute",
                "pattern": r"([0-9]{1,2}|100)\.[0-9]{1,2}",
            }
        )


@dataclass
class PassiveInfo:
    """
    Used by CreateReservationReq for passing in elements normally found post-
    booking.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    ticket_number: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    confirmation_number: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ConfirmationNumber",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    commission: Optional[Commission] = field(
        default=None,
        metadata={
            "name": "Commission",
            "type": "Element",
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
        }
    )
    provider_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
        }
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
        }
    )
    supplier_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierLocatorCode",
            "type": "Attribute",
        }
    )


@dataclass
class ReservationName:
    """
    Container to represent reservation name as appears in GDS booking.

    Parameters
    ----------
    booking_traveler_ref:
    name_override: To be used if the reservation name is other than
        booking travelers in the PNR
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    booking_traveler_ref: Optional[BookingTravelerRef] = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
        }
    )
    name_override: Optional[NameOverride] = field(
        default=None,
        metadata={
            "name": "NameOverride",
            "type": "Element",
        }
    )


@dataclass
class Ssrinfo:
    """
    Bundle SSR with BookingTraveler reference in order to add SSR post booking.

    Parameters
    ----------
    ssr:
    booking_traveler_ref: Reference to Booking Traveler.
    """
    class Meta:
        name = "SSRInfo"
        namespace = "http://www.travelport.com/schema/common_v48_0"

    ssr: Optional[Ssr] = field(
        default=None,
        metadata={
            "name": "SSR",
            "type": "Element",
            "required": True,
        }
    )
    booking_traveler_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class ServiceData:
    """
    Parameters
    ----------
    seat_attributes:
    cabin_class:
    ssrref: References to the related SSRs. At present, only reference
        to ASVC SSR is supported. Supported providers are 1G/1V/1P/1J
    data: Data that specifies the details of the merchandising offering
        (e.g. seat number for seat service)
    air_segment_ref: Reference to a segment if the merchandising
        offering only pertains to that segment. If no segment reference
        is present this means this offering is for the whole itinerary.
    booking_traveler_ref: Reference to a passenger if the merchandising
        offering only pertains to that passenger. If no passenger
        reference is present this means this offering is for all
        passengers.
    stop_over: Indicates that there is a significant delay between
        flights (usually 12 hours or more)
    traveler_type: Passenger Type Code.
    emdsummary_ref: Reference to the corresponding EMD issued. Supported
        providers are 1G/1V/1P/1J
    emdcoupon_ref: Reference to the corresponding EMD coupon issued.
        Supported providers are 1G/1V/1P/1J
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    seat_attributes: Optional[SeatAttributes] = field(
        default=None,
        metadata={
            "name": "SeatAttributes",
            "type": "Element",
        }
    )
    cabin_class: Optional[CabinClass] = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Element",
        }
    )
    ssrref: List[TypeKeyBasedReference] = field(
        default_factory=list,
        metadata={
            "name": "SSRRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    data: Optional[str] = field(
        default=None,
        metadata={
            "name": "Data",
            "type": "Attribute",
        }
    )
    air_segment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirSegmentRef",
            "type": "Attribute",
        }
    )
    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        }
    )
    stop_over: bool = field(
        default=False,
        metadata={
            "name": "StopOver",
            "type": "Attribute",
        }
    )
    traveler_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "TravelerType",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 5,
        }
    )
    emdsummary_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "EMDSummaryRef",
            "type": "Attribute",
        }
    )
    emdcoupon_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "EMDCouponRef",
            "type": "Attribute",
        }
    )


@dataclass
class ServiceInfo:
    """
    Parameters
    ----------
    description: Description of the Service.  Usually used in tandem
        with  one or more media items.
    media_item:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    description: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    media_item: List[MediaItem] = field(
        default_factory=list,
        metadata={
            "name": "MediaItem",
            "type": "Element",
            "max_occurs": 3,
        }
    )


@dataclass
class TransactionType:
    """Configuration for products by type.

    Inheritable.

    Parameters
    ----------
    air:
    hotel:
    rail:
    vehicle:
    passive: For true passive segments such as ground, cruise etc
    background_passive: For behind the scenes or background passives
        Only
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    air: Optional["TransactionType.Air"] = field(
        default=None,
        metadata={
            "name": "Air",
            "type": "Element",
        }
    )
    hotel: Optional[TypeTransactionsAllowed] = field(
        default=None,
        metadata={
            "name": "Hotel",
            "type": "Element",
        }
    )
    rail: Optional[TypeTransactionsAllowed] = field(
        default=None,
        metadata={
            "name": "Rail",
            "type": "Element",
        }
    )
    vehicle: Optional[TypeTransactionsAllowed] = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
        }
    )
    passive: Optional[TypeBookingTransactionsAllowed] = field(
        default=None,
        metadata={
            "name": "Passive",
            "type": "Element",
        }
    )
    background_passive: Optional[TypeBookingTransactionsAllowed] = field(
        default=None,
        metadata={
            "name": "BackgroundPassive",
            "type": "Element",
        }
    )

    @dataclass
    class Air(TypeTransactionsAllowed):
        """
        Parameters
        ----------
        tier: Indicate the Tier Level
        days_enabled: Allow or prohibit Flexible Days (within a date
            range) shopping option
        weekends_enabled: Allow or prohibit Flexible Weekends shopping
            option
        airports_enabled: Allow or prohibit Flexible Airport (choice of
            Origin and Destination airports) shopping option
        odenabled: Allow or prohibit Flexible Origin and Destination
            (choice of airports within a radius) shopping option
        one_way_shop: Allows or prohibits one way shopping functionality
            for the associated provisioning provider configuration
        flex_explore: Allows or prohibits flex explore functionality for
            the associated provisioning provider configuration
        rapid_reprice_enabled: Allows or prohibits rapid reprice
            functionality for the associated provisioning provider
            configuration. Providers: 1G/1V
        return_upsell_fare: When set to “true”, Upsell information will
            be returned in the shop response.  Provider: 1G, 1V, 1P, 1J,
            ACH
        """
        tier: Optional[AttrFlexShoppingTier] = field(
            default=None,
            metadata={
                "name": "Tier",
                "type": "Attribute",
            }
        )
        days_enabled: Optional[bool] = field(
            default=None,
            metadata={
                "name": "DaysEnabled",
                "type": "Attribute",
            }
        )
        weekends_enabled: Optional[bool] = field(
            default=None,
            metadata={
                "name": "WeekendsEnabled",
                "type": "Attribute",
            }
        )
        airports_enabled: Optional[bool] = field(
            default=None,
            metadata={
                "name": "AirportsEnabled",
                "type": "Attribute",
            }
        )
        odenabled: Optional[bool] = field(
            default=None,
            metadata={
                "name": "ODEnabled",
                "type": "Attribute",
            }
        )
        one_way_shop: Optional[bool] = field(
            default=None,
            metadata={
                "name": "OneWayShop",
                "type": "Attribute",
            }
        )
        flex_explore: Optional[bool] = field(
            default=None,
            metadata={
                "name": "FlexExplore",
                "type": "Attribute",
            }
        )
        rapid_reprice_enabled: Optional[bool] = field(
            default=None,
            metadata={
                "name": "RapidRepriceEnabled",
                "type": "Attribute",
            }
        )
        return_upsell_fare: Optional[bool] = field(
            default=None,
            metadata={
                "name": "ReturnUpsellFare",
                "type": "Attribute",
            }
        )


@dataclass
class TravelSegment(Segment):
    """
    Generic segment used to provide travel information that was not processed
    by the system.

    Parameters
    ----------
    origin: The IATA location code for this origination of this entity.
    destination: The IATA location code for this destination of this
        entity.
    departure_time: The date and time at which this entity departs. This
        does not include time zone information since it can be derived
        from the origin location.
    arrival_time: The date and time at which this entity arrives at the
        destination. This does not include time zone information since
        it can be derived from the origin location.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    departure_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Attribute",
        }
    )
    arrival_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "ArrivalTime",
            "type": "Attribute",
        }
    )


@dataclass
class TravelerInformation:
    """
    Traveler Information required for File Finishing.

    Parameters
    ----------
    emergency_contact:
    home_airport:
    visa_expiration_date:
    booking_traveler_ref: A reference to a passenger.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    emergency_contact: Optional["TravelerInformation.EmergencyContact"] = field(
        default=None,
        metadata={
            "name": "EmergencyContact",
            "type": "Element",
        }
    )
    home_airport: Optional[str] = field(
        default=None,
        metadata={
            "name": "HomeAirport",
            "type": "Attribute",
            "length": 3,
        }
    )
    visa_expiration_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "VisaExpirationDate",
            "type": "Attribute",
        }
    )
    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class EmergencyContact:
        """
        Parameters
        ----------
        phone_number:
        name: Name of Emergency Contact Person
        relationship: Relationship between Traveler and Emergency
            Contact Person
        """
        phone_number: Optional[PhoneNumber] = field(
            default=None,
            metadata={
                "name": "PhoneNumber",
                "type": "Element",
            }
        )
        name: Optional[str] = field(
            default=None,
            metadata={
                "name": "Name",
                "type": "Attribute",
            }
        )
        relationship: Optional[str] = field(
            default=None,
            metadata={
                "name": "Relationship",
                "type": "Attribute",
            }
        )


@dataclass
class TypeAgencyHierarchyLongReference(TypeAgencyHierarchyReference):
    """
    Parameters
    ----------
    profile_version:
    profile_name: Initially: Agent: Last, First, Branch: BranchCode,
        Agency: Name. After new profile  implementation: Agent:
        UserName, others levels: Name.
    """
    class Meta:
        name = "typeAgencyHierarchyLongReference"

    profile_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "ProfileVersion",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProfileName",
            "type": "Attribute",
            "required": True,
            "max_length": 102,
        }
    )


@dataclass
class TypeAssociatedRemarkWithSegmentRef(TypeAssociatedRemark):
    """
    A textual remark container to hold Associated itinerary remarks with
    segment association.

    Parameters
    ----------
    segment_ref: Reference to an Air/Passive Segment
    """
    class Meta:
        name = "typeAssociatedRemarkWithSegmentRef"

    segment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SegmentRef",
            "type": "Attribute",
        }
    )


@dataclass
class TypeFlexibleTimeSpec(TypeTimeSpec):
    """
    A type which can be used for flexible date/time specification -extends the
    generic type typeTimeSpec to provide extra options for search.

    Parameters
    ----------
    search_extra_days: Options to search for extra days on top of the
        specified date
    """
    class Meta:
        name = "typeFlexibleTimeSpec"

    search_extra_days: Optional["TypeFlexibleTimeSpec.SearchExtraDays"] = field(
        default=None,
        metadata={
            "name": "SearchExtraDays",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )

    @dataclass
    class SearchExtraDays:
        """
        Parameters
        ----------
        days_before: Number of days to search before the specified date
        days_after: Number of days to search after the specified date
        """
        days_before: Optional[int] = field(
            default=None,
            metadata={
                "name": "DaysBefore",
                "type": "Attribute",
            }
        )
        days_after: Optional[int] = field(
            default=None,
            metadata={
                "name": "DaysAfter",
                "type": "Attribute",
            }
        )


@dataclass
class TypeLocation:
    class Meta:
        name = "typeLocation"

    airport: Optional[Airport] = field(
        default=None,
        metadata={
            "name": "Airport",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    city: Optional[City] = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    city_or_airport: Optional[CityOrAirport] = field(
        default=None,
        metadata={
            "name": "CityOrAirport",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )


@dataclass
class TypePaymentCard:
    """
    Container for all credit and debit card information.

    Parameters
    ----------
    phone_number:
    billing_address: The address to where the billing statements for
        this card are sent. Used for address verification purposes.
    type: The 2 letter credit/ debit card type.
    number:
    exp_date: The Expiration date of this card in YYYY-MM format.
    name: The name as it appears on the card.
    cvv: Card Verification Code
    approval_code: This code is required for an authorization process
        from the Credit Card company directly,required for some of the
        CCH carriers.This attribute is also used for EMD retrieve and
        issuance transactions.
    """
    class Meta:
        name = "typePaymentCard"

    phone_number: Optional[PhoneNumber] = field(
        default=None,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    billing_address: Optional[TypeStructuredAddress] = field(
        default=None,
        metadata={
            "name": "BillingAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 2,
        }
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "min_length": 13,
            "max_length": 128,
        }
    )
    exp_date: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "ExpDate",
            "type": "Attribute",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "max_length": 128,
        }
    )
    cvv: Optional[str] = field(
        default=None,
        metadata={
            "name": "CVV",
            "type": "Attribute",
            "max_length": 4,
        }
    )
    approval_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApprovalCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        }
    )


@dataclass
class TypeSearchLocation:
    class Meta:
        name = "typeSearchLocation"

    airport: Optional[Airport] = field(
        default=None,
        metadata={
            "name": "Airport",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    city: Optional[City] = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    city_or_airport: Optional[CityOrAirport] = field(
        default=None,
        metadata={
            "name": "CityOrAirport",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    coordinate_location: Optional[CoordinateLocation] = field(
        default=None,
        metadata={
            "name": "CoordinateLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    rail_location: Optional[RailLocation] = field(
        default=None,
        metadata={
            "name": "RailLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    distance: Optional[Distance] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )


@dataclass
class Apiprovider:
    """
    Parameters
    ----------
    transaction_type:
    available_pseudo_city_code:
    provider_code: The Provider Code of the host
    supplier_code: The Supplier Code of the host
    iatacode: Agency IATA or ARC code, used as an ID with airlines.
    """
    class Meta:
        name = "APIProvider"
        namespace = "http://www.travelport.com/schema/common_v48_0"

    transaction_type: Optional[TransactionType] = field(
        default=None,
        metadata={
            "name": "TransactionType",
            "type": "Element",
        }
    )
    available_pseudo_city_code: List["Apiprovider.AvailablePseudoCityCode"] = field(
        default_factory=list,
        metadata={
            "name": "AvailablePseudoCityCode",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        }
    )
    iatacode: Optional[str] = field(
        default=None,
        metadata={
            "name": "IATACode",
            "type": "Attribute",
            "max_length": 8,
        }
    )

    @dataclass
    class AvailablePseudoCityCode:
        """
        Parameters
        ----------
        pseudo_city_code: The PseudoCityCode used to connect to the
            host.
        """
        pseudo_city_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "PseudoCityCode",
                "type": "Attribute",
                "min_length": 2,
                "max_length": 10,
            }
        )


@dataclass
class BaseReservation:
    """
    Parameters
    ----------
    accounting_remark:
    general_remark:
    restriction:
    passive_info:
    locator_code: The unique identifier for this reservation. If this is
        this View Only UR LocatorCode is '999999'.
    create_date: The date and time that this reservation was created.
    modified_date: The date and time that this reservation was last
        modified for any reason.
    customer_number:
    """
    accounting_remark: List[AccountingRemark] = field(
        default_factory=list,
        metadata={
            "name": "AccountingRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    general_remark: List[GeneralRemark] = field(
        default_factory=list,
        metadata={
            "name": "GeneralRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    restriction: List[Restriction] = field(
        default_factory=list,
        metadata={
            "name": "Restriction",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    passive_info: Optional[PassiveInfo] = field(
        default=None,
        metadata={
            "name": "PassiveInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    create_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "CreateDate",
            "type": "Attribute",
            "required": True,
        }
    )
    modified_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "ModifiedDate",
            "type": "Attribute",
            "required": True,
        }
    )
    customer_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomerNumber",
            "type": "Attribute",
        }
    )


@dataclass
class BaseSearchReq(BaseReq):
    next_result_reference: List[NextResultReference] = field(
        default_factory=list,
        metadata={
            "name": "NextResultReference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )


@dataclass
class BaseSearchRsp(BaseRsp):
    next_result_reference: List[NextResultReference] = field(
        default_factory=list,
        metadata={
            "name": "NextResultReference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )


@dataclass
class BookingTraveler:
    """
    A traveler and all their accompanying data.

    Parameters
    ----------
    booking_traveler_name:
    delivery_info:
    phone_number:
    email:
    loyalty_card:
    discount_card:
    ssr:
    name_remark:
    air_seat_assignment:
    rail_seat_assignment:
    emergency_info:
    address:
    drivers_license:
    applied_profile:
    customized_name_data:
    travel_compliance_data: Travel Compliance and Preferred Supplier
        information of the booking traveler specific to a segment. Not
        applicable to Saved Trip.
    travel_info:
    key:
    traveler_type: Defines the type of traveler used for booking which
        could be a non-defining type (Companion, Web-fare, etc), or a
        standard type (Adult, Child, etc).
    age: BookingTraveler age
    vip: When set to True indicates that the Booking Traveler is a VIP
        based on agency/customer criteria
    dob: Traveler Date of Birth
    gender: The BookingTraveler gender type
    nationality: Specify ISO country code for nationality of the Booking
        Traveler
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    name_number: Host Name Number
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    booking_traveler_name: Optional[BookingTravelerName] = field(
        default=None,
        metadata={
            "name": "BookingTravelerName",
            "type": "Element",
            "required": True,
        }
    )
    delivery_info: List[DeliveryInfo] = field(
        default_factory=list,
        metadata={
            "name": "DeliveryInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    phone_number: List[PhoneNumber] = field(
        default_factory=list,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    email: List[Email] = field(
        default_factory=list,
        metadata={
            "name": "Email",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    loyalty_card: List[LoyaltyCard] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCard",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    discount_card: List[DiscountCard] = field(
        default_factory=list,
        metadata={
            "name": "DiscountCard",
            "type": "Element",
            "max_occurs": 9,
        }
    )
    ssr: List[Ssr] = field(
        default_factory=list,
        metadata={
            "name": "SSR",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    name_remark: List[NameRemark] = field(
        default_factory=list,
        metadata={
            "name": "NameRemark",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_seat_assignment: List[AirSeatAssignment] = field(
        default_factory=list,
        metadata={
            "name": "AirSeatAssignment",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    rail_seat_assignment: List[RailSeatAssignment] = field(
        default_factory=list,
        metadata={
            "name": "RailSeatAssignment",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    emergency_info: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmergencyInfo",
            "type": "Element",
        }
    )
    address: List[TypeStructuredAddress] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    drivers_license: List[DriversLicense] = field(
        default_factory=list,
        metadata={
            "name": "DriversLicense",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    applied_profile: List[AppliedProfile] = field(
        default_factory=list,
        metadata={
            "name": "AppliedProfile",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    customized_name_data: List[CustomizedNameData] = field(
        default_factory=list,
        metadata={
            "name": "CustomizedNameData",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    travel_compliance_data: List[TravelComplianceData] = field(
        default_factory=list,
        metadata={
            "name": "TravelComplianceData",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    travel_info: Optional[TravelInfo] = field(
        default=None,
        metadata={
            "name": "TravelInfo",
            "type": "Element",
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    traveler_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "TravelerType",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 5,
        }
    )
    age: Optional[int] = field(
        default=None,
        metadata={
            "name": "Age",
            "type": "Attribute",
        }
    )
    vip: bool = field(
        default=False,
        metadata={
            "name": "VIP",
            "type": "Attribute",
        }
    )
    dob: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DOB",
            "type": "Attribute",
        }
    )
    gender: Optional[str] = field(
        default=None,
        metadata={
            "name": "Gender",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 2,
        }
    )
    nationality: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nationality",
            "type": "Attribute",
            "length": 2,
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )
    name_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "NameNumber",
            "type": "Attribute",
        }
    )


@dataclass
class BookingTravelerInfo:
    """
    Container that will allow modifying Universal record data that is not
    product specific.

    Parameters
    ----------
    booking_traveler_name:
    name_remark:
    dob: Traveler Date of Birth
    travel_info:
    email:
    phone_number:
    address:
    emergency_info:
    delivery_info:
    age:
    customized_name_data:
    applied_profile:
    key:
    traveler_type:
    gender:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    booking_traveler_name: Optional[BookingTravelerName] = field(
        default=None,
        metadata={
            "name": "BookingTravelerName",
            "type": "Element",
        }
    )
    name_remark: Optional[NameRemark] = field(
        default=None,
        metadata={
            "name": "NameRemark",
            "type": "Element",
        }
    )
    dob: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DOB",
            "type": "Element",
        }
    )
    travel_info: Optional[TravelInfo] = field(
        default=None,
        metadata={
            "name": "TravelInfo",
            "type": "Element",
        }
    )
    email: Optional[Email] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
        }
    )
    phone_number: Optional[PhoneNumber] = field(
        default=None,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
        }
    )
    address: Optional[TypeStructuredAddress] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
        }
    )
    emergency_info: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmergencyInfo",
            "type": "Element",
        }
    )
    delivery_info: Optional[DeliveryInfo] = field(
        default=None,
        metadata={
            "name": "DeliveryInfo",
            "type": "Element",
        }
    )
    age: Optional[int] = field(
        default=None,
        metadata={
            "name": "Age",
            "type": "Element",
        }
    )
    customized_name_data: Optional[CustomizedNameData] = field(
        default=None,
        metadata={
            "name": "CustomizedNameData",
            "type": "Element",
        }
    )
    applied_profile: Optional[AppliedProfile] = field(
        default=None,
        metadata={
            "name": "AppliedProfile",
            "type": "Element",
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    traveler_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "TravelerType",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 5,
        }
    )
    gender: Optional[str] = field(
        default=None,
        metadata={
            "name": "Gender",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 2,
        }
    )


@dataclass
class ConnectionPoint(TypeLocation):
    """
    A connection point can be eith an IATA airport or cir city code.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"


@dataclass
class DebitCard(TypePaymentCard):
    """
    Container for all debit card information.

    Parameters
    ----------
    issue_number: Verification number for Debit Cards
    profile_id: The unique ID of the profile that contains the payment
        details to use.
    key: The Key assigned to the payment details value from the
        specified profile.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    issue_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssueNumber",
            "type": "Attribute",
            "max_length": 8,
        }
    )
    profile_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )


@dataclass
class FileFinishingInfo:
    """Misc Data required for File Finishing.

    This data is transient and not saved in database.

    Parameters
    ----------
    shop_information:
    policy_information: Policy Information required for File Finishing.
        Would repeat per Policy Type
    account_information:
    agency_information:
    traveler_information:
    custom_profile_information:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    shop_information: Optional[ShopInformation] = field(
        default=None,
        metadata={
            "name": "ShopInformation",
            "type": "Element",
        }
    )
    policy_information: List[PolicyInformation] = field(
        default_factory=list,
        metadata={
            "name": "PolicyInformation",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    account_information: Optional[AccountInformation] = field(
        default=None,
        metadata={
            "name": "AccountInformation",
            "type": "Element",
        }
    )
    agency_information: Optional[AgencyInformation] = field(
        default=None,
        metadata={
            "name": "AgencyInformation",
            "type": "Element",
        }
    )
    traveler_information: List[TravelerInformation] = field(
        default_factory=list,
        metadata={
            "name": "TravelerInformation",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    custom_profile_information: Optional[CustomProfileInformation] = field(
        default=None,
        metadata={
            "name": "CustomProfileInformation",
            "type": "Element",
        }
    )


@dataclass
class Group:
    """Represents a traveler group for Group booking and all their accompanying
    data.

    SUPPORTED PROVIDER: Worldspan and JAL.

    Parameters
    ----------
    name: Name of the group in group booking.
    delivery_info:
    phone_number:
    ssrref: Reference Element for SSR.
    address:
    booking_traveler_ref: Reference Element for Booking Traveler.
    key:
    traveler_type: Defines the type of traveler used for booking which
        could be a non-defining type (Companion, Web-fare, etc), or a
        standard type (Adult, Child, etc).
    group_size: Represents size of the group
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "min_length": 1,
            "white_space": "collapse",
        }
    )
    delivery_info: Optional[DeliveryInfo] = field(
        default=None,
        metadata={
            "name": "DeliveryInfo",
            "type": "Element",
        }
    )
    phone_number: List[PhoneNumber] = field(
        default_factory=list,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    ssrref: List["Group.Ssrref"] = field(
        default_factory=list,
        metadata={
            "name": "SSRRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    address: Optional[TypeStructuredAddress] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
        }
    )
    booking_traveler_ref: List["Group.BookingTravelerRef"] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    traveler_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "TravelerType",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 5,
        }
    )
    group_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "GroupSize",
            "type": "Attribute",
            "required": True,
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )

    @dataclass
    class Ssrref:
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class BookingTravelerRef:
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass
class PaymentRestriction:
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    card_restriction: List[CardRestriction] = field(
        default_factory=list,
        metadata={
            "name": "CardRestriction",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    address_restriction: Optional[AddressRestriction] = field(
        default=None,
        metadata={
            "name": "AddressRestriction",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ServiceRuleType:
    """
    Contains the rules for applying service rules.

    Parameters
    ----------
    application_rules: The rules to apply the rule to the itinerary
    application_level: Lists the levels where the option is applied in
        the itinerary. Some options are applied for the entire
        itinerary, some for entire segments, etc.
    modify_rules: Groups the modification rules for the Option
    secondary_type_rules: Lists the supported Secondary Codes for the
        optional / additional service.
    remarks: Adds text remarks / rules for the optional / additional
        service
    key: Unique ID to identify an optional service rule
    """
    application_rules: Optional["ServiceRuleType.ApplicationRules"] = field(
        default=None,
        metadata={
            "name": "ApplicationRules",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    application_level: Optional["ServiceRuleType.ApplicationLevel"] = field(
        default=None,
        metadata={
            "name": "ApplicationLevel",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    modify_rules: Optional["ServiceRuleType.ModifyRules"] = field(
        default=None,
        metadata={
            "name": "ModifyRules",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    secondary_type_rules: Optional["ServiceRuleType.SecondaryTypeRules"] = field(
        default=None,
        metadata={
            "name": "SecondaryTypeRules",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    remarks: List[FormattedTextTextType] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 99,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class ApplicationRules:
        """
        Parameters
        ----------
        required_for_all_travelers: Indicates if the option needs to be
            applied to all travelers in the itinerary if selected
        required_for_all_segments: Indicates if the option needs to be
            applied to all segments in the itinerary if selected
        required_for_all_segments_in_od: Indicates if the option needs
            to be applied to all segments in a origin / destination
            (connection flights) if selected for one segment in the OD
        unselected_option_required: If an UnselectedOption is present in
            the option, then the Unselected option  needs to be selected
            even if the option is not selected when this flag is set to
            true
        secondary_option_code_required: If set to true, the secondary
            option code is required for this option
        """
        required_for_all_travelers: Optional[bool] = field(
            default=None,
            metadata={
                "name": "RequiredForAllTravelers",
                "type": "Attribute",
            }
        )
        required_for_all_segments: Optional[bool] = field(
            default=None,
            metadata={
                "name": "RequiredForAllSegments",
                "type": "Attribute",
            }
        )
        required_for_all_segments_in_od: Optional[bool] = field(
            default=None,
            metadata={
                "name": "RequiredForAllSegmentsInOD",
                "type": "Attribute",
            }
        )
        unselected_option_required: Optional[bool] = field(
            default=None,
            metadata={
                "name": "UnselectedOptionRequired",
                "type": "Attribute",
            }
        )
        secondary_option_code_required: Optional[bool] = field(
            default=None,
            metadata={
                "name": "SecondaryOptionCodeRequired",
                "type": "Attribute",
            }
        )

    @dataclass
    class ApplicationLevel:
        """
        Parameters
        ----------
        application_limits: Adds the limits on the number of options
            that can be selected for a particular type
        service_data:
        applicable_levels: Indicates the level in the itinerary when the
            option is applied.
        provider_defined_applicable_levels: Indicates the actual
            provider defined ApplicableLevels which is mapped to Other
        """
        application_limits: Optional["ServiceRuleType.ApplicationLevel.ApplicationLimits"] = field(
            default=None,
            metadata={
                "name": "ApplicationLimits",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v48_0",
            }
        )
        service_data: List[ServiceData] = field(
            default_factory=list,
            metadata={
                "name": "ServiceData",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v48_0",
                "max_occurs": 999,
            }
        )
        applicable_levels: List[OptionalServiceApplicabilityType] = field(
            default_factory=list,
            metadata={
                "name": "ApplicableLevels",
                "type": "Attribute",
                "tokens": True,
            }
        )
        provider_defined_applicable_levels: Optional[str] = field(
            default=None,
            metadata={
                "name": "ProviderDefinedApplicableLevels",
                "type": "Attribute",
            }
        )

        @dataclass
        class ApplicationLimits:
            """
            Parameters
            ----------
            application_limit: The application limits for a particular
                level
            """
            application_limit: List[OptionalServiceApplicationLimitType] = field(
                default_factory=list,
                metadata={
                    "name": "ApplicationLimit",
                    "type": "Element",
                    "namespace": "http://www.travelport.com/schema/common_v48_0",
                    "min_occurs": 1,
                    "max_occurs": 10,
                }
            )

    @dataclass
    class ModifyRules:
        """
        Parameters
        ----------
        modify_rule: Indicates modification rules for the particular
            modification type.
        supported_modifications: Lists the supported modifications for
            the itinerary.
        provider_defined_modification_type: Indicates the actual
            provider defined modification type which is mapped to Other
        """
        modify_rule: List["ServiceRuleType.ModifyRules.ModifyRule"] = field(
            default_factory=list,
            metadata={
                "name": "ModifyRule",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v48_0",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )
        supported_modifications: List[ModificationType] = field(
            default_factory=list,
            metadata={
                "name": "SupportedModifications",
                "type": "Attribute",
                "tokens": True,
            }
        )
        provider_defined_modification_type: Optional[str] = field(
            default=None,
            metadata={
                "name": "ProviderDefinedModificationType",
                "type": "Attribute",
            }
        )

        @dataclass
        class ModifyRule:
            """
            Parameters
            ----------
            modification: The modificaiton for which this rule group
                applies.
            automatically_applied_on_add: Indicates if the option will
                be automatically added to new segments / passengers in
                the itinerary.
            can_delete: Indicates if the option can be deleted from the
                itinerary without segment or passenger modifications
            can_add: Indicates if the option can be added to the
                itinerary without segment or passenger modification
            refundable: Indicates if the price of the option is
                refundable.
            provider_defined_modification_type: Indicates the actual
                provider defined modification type which is mapped to
                Other
            """
            modification: Optional[ModificationType] = field(
                default=None,
                metadata={
                    "name": "Modification",
                    "type": "Attribute",
                    "required": True,
                }
            )
            automatically_applied_on_add: bool = field(
                default=False,
                metadata={
                    "name": "AutomaticallyAppliedOnAdd",
                    "type": "Attribute",
                }
            )
            can_delete: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "CanDelete",
                    "type": "Attribute",
                }
            )
            can_add: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "CanAdd",
                    "type": "Attribute",
                }
            )
            refundable: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "Refundable",
                    "type": "Attribute",
                }
            )
            provider_defined_modification_type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "ProviderDefinedModificationType",
                    "type": "Attribute",
                }
            )

    @dataclass
    class SecondaryTypeRules:
        """
        Parameters
        ----------
        secondary_type_rule: Lists a single secondary code for the
            optional / additional service.
        """
        secondary_type_rule: List["ServiceRuleType.SecondaryTypeRules.SecondaryTypeRule"] = field(
            default_factory=list,
            metadata={
                "name": "SecondaryTypeRule",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v48_0",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )

        @dataclass
        class SecondaryTypeRule:
            """
            Parameters
            ----------
            application_limit:
            secondary_type: The unique type to associate a secondary
                type in an optional service
            """
            application_limit: List[OptionalServiceApplicationLimitType] = field(
                default_factory=list,
                metadata={
                    "name": "ApplicationLimit",
                    "type": "Element",
                    "namespace": "http://www.travelport.com/schema/common_v48_0",
                    "max_occurs": 10,
                }
            )
            secondary_type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "SecondaryType",
                    "type": "Attribute",
                    "required": True,
                }
            )


@dataclass
class TypeCreditCardType(TypePaymentCard):
    """
    Parameters
    ----------
    extended_payment: Used for American Express cards.
    customer_reference: Agencies use this to pass the traveler
        information to the credit card company.
    acceptance_override: Override airline restriction on the credit
        card.
    third_party_payment: If true, this indicates that the credit card
        holder is not one of the passengers.
    bank_name: Issuing bank name for this credit card
    bank_country_code: ISO Country code associated with the issuing bank
    bank_state_code: State code associated with the issuing bank.
    enett: Acceptable values are true or false. If set to true it will
        denote that the credit card used has been issued through Enett.
        For all other credit card payments this value will be set to
        false.
    """
    class Meta:
        name = "typeCreditCardType"

    extended_payment: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExtendedPayment",
            "type": "Attribute",
        }
    )
    customer_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomerReference",
            "type": "Attribute",
        }
    )
    acceptance_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AcceptanceOverride",
            "type": "Attribute",
        }
    )
    third_party_payment: bool = field(
        default=False,
        metadata={
            "name": "ThirdPartyPayment",
            "type": "Attribute",
        }
    )
    bank_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "BankName",
            "type": "Attribute",
        }
    )
    bank_country_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "BankCountryCode",
            "type": "Attribute",
            "length": 2,
        }
    )
    bank_state_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "BankStateCode",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    enett: bool = field(
        default=False,
        metadata={
            "name": "Enett",
            "type": "Attribute",
        }
    )


@dataclass
class TypePassengerType:
    """
    Passenger type code with optional age information.

    Parameters
    ----------
    name: Optional passenger Name with associated LoyaltyCard may
        provide benefit when pricing itineraries using Low Cost
        Carriers. In general, most carriers do not consider passenger
        LoyalyCard information when initially pricing itineraries.
    loyalty_card:
    discount_card:
    personal_geography: Passenger personal geography detail to be sent
        to Host for accessing location specific fares
    code: The 3-char IATA passenger type code
    age:
    dob: Passenger Date of Birth
    gender: The passenger gender type
    price_ptconly:
    booking_traveler_ref: This value should be set for Multiple
        Passengers in the request.
    accompanied_passenger: Container to identify accompanied passenger.
        Set true means this passenger is accompanied
    residency_type: The passenger residence type.
    """
    class Meta:
        name = "typePassengerType"

    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    loyalty_card: List[LoyaltyCard] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    discount_card: List[DiscountCard] = field(
        default_factory=list,
        metadata={
            "name": "DiscountCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 9,
        }
    )
    personal_geography: Optional[PersonalGeography] = field(
        default=None,
        metadata={
            "name": "PersonalGeography",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 3,
            "max_length": 5,
        }
    )
    age: Optional[int] = field(
        default=None,
        metadata={
            "name": "Age",
            "type": "Attribute",
        }
    )
    dob: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DOB",
            "type": "Attribute",
        }
    )
    gender: Optional[str] = field(
        default=None,
        metadata={
            "name": "Gender",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 2,
        }
    )
    price_ptconly: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PricePTCOnly",
            "type": "Attribute",
        }
    )
    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        }
    )
    accompanied_passenger: bool = field(
        default=False,
        metadata={
            "name": "AccompaniedPassenger",
            "type": "Attribute",
        }
    )
    residency_type: Optional[TypeResidency] = field(
        default=None,
        metadata={
            "name": "ResidencyType",
            "type": "Attribute",
        }
    )


@dataclass
class BaseCreateReservationReq(BaseReq):
    """
    Parameters
    ----------
    linked_universal_record:
    booking_traveler:
    osi:
    accounting_remark:
    general_remark:
    xmlremark:
    unassociated_remark:
    postscript:
    passive_info:
    continuity_check_override: This element will be used if user wants
        to override segment continuity check.
    agency_contact_info:
    customer_id:
    file_finishing_info:
    commission_remark:
    consolidator_remark:
    invoice_remark:
    ssr: SSR element outside Booking Traveler without any Segment Ref or
        Booking Traveler Ref.
    email_notification:
    queue_place: Allow queue placement of a PNR at the time of booking
        in
        AirCreateReservationReq,HotelCreateReservationReq,PassiveCreateReservationReq
        and VehicleCreateReservationReq for providers 1G,1V,1P and 1J.
    rule_name: This attribute is meant to attach a mandatory custom
        check rule name to a PNR. A non-mandatory custom check rule too
        can be attached to a PNR.
    universal_record_locator_code: Which UniversalRecord should this new
        reservation be applied to.  If blank, then a new one is created.
    provider_locator_code: Which Provider reservation does this
        reservation get added to.
    provider_code: To be used with ProviderLocatorCode, which host the
        reservation being added to belongs to.
    customer_number: Optional client centric customer identifier
    version:
    """
    linked_universal_record: List[LinkedUniversalRecord] = field(
        default_factory=list,
        metadata={
            "name": "LinkedUniversalRecord",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    booking_traveler: List[BookingTraveler] = field(
        default_factory=list,
        metadata={
            "name": "BookingTraveler",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    osi: List[Osi] = field(
        default_factory=list,
        metadata={
            "name": "OSI",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    accounting_remark: List[AccountingRemark] = field(
        default_factory=list,
        metadata={
            "name": "AccountingRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    general_remark: List[GeneralRemark] = field(
        default_factory=list,
        metadata={
            "name": "GeneralRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    xmlremark: List[Xmlremark] = field(
        default_factory=list,
        metadata={
            "name": "XMLRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    unassociated_remark: List[UnassociatedRemark] = field(
        default_factory=list,
        metadata={
            "name": "UnassociatedRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    postscript: Optional[Postscript] = field(
        default=None,
        metadata={
            "name": "Postscript",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    passive_info: Optional[PassiveInfo] = field(
        default=None,
        metadata={
            "name": "PassiveInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    continuity_check_override: Optional[ContinuityCheckOverride] = field(
        default=None,
        metadata={
            "name": "ContinuityCheckOverride",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    agency_contact_info: Optional[AgencyContactInfo] = field(
        default=None,
        metadata={
            "name": "AgencyContactInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    customer_id: Optional[CustomerId] = field(
        default=None,
        metadata={
            "name": "CustomerID",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    file_finishing_info: Optional[FileFinishingInfo] = field(
        default=None,
        metadata={
            "name": "FileFinishingInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    commission_remark: Optional[CommissionRemark] = field(
        default=None,
        metadata={
            "name": "CommissionRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    consolidator_remark: Optional[ConsolidatorRemark] = field(
        default=None,
        metadata={
            "name": "ConsolidatorRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    invoice_remark: List[InvoiceRemark] = field(
        default_factory=list,
        metadata={
            "name": "InvoiceRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    ssr: List[Ssr] = field(
        default_factory=list,
        metadata={
            "name": "SSR",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )
    email_notification: Optional[EmailNotification] = field(
        default=None,
        metadata={
            "name": "EmailNotification",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    queue_place: Optional[QueuePlace] = field(
        default=None,
        metadata={
            "name": "QueuePlace",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
        }
    )
    rule_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "RuleName",
            "type": "Attribute",
            "max_length": 10,
        }
    )
    universal_record_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        }
    )
    provider_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
        }
    )
    customer_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomerNumber",
            "type": "Attribute",
        }
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
        }
    )


@dataclass
class CreditCard(TypeCreditCardType):
    """
    Container for all credit card information.

    Parameters
    ----------
    profile_id: The unique ID of the profile that contains the payment
        details to use.
    key: The Key assigned to the payment details value from the
        specified profile.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    profile_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )


@dataclass
class SearchPassenger(TypePassengerType):
    """
    Passenger type with code and optional age information.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )


@dataclass
class FormOfPayment:
    """
    A Form of Payment used to purchase all or part of a booking.

    Parameters
    ----------
    credit_card:
    debit_card:
    enett_van:
    certificate:
    ticket_number:
    check:
    requisition:
    misc_form_of_payment:
    agency_payment:
    united_nations:
    direct_payment:
    agent_voucher:
    payment_advice:
    provider_reservation_info_ref:
    segment_ref:
    bsppayment:
    arcpayment:
    key:
    type:
    fulfillment_type: Defines how the client wishes to receive travel
        documents. Type does not define where or how payment is made.
        The supported values are  "Ticket on Departure", "Travel
        Agency", "Courier", "Standard Mail", "Ticketless", "Ticket
        Office", "Express Mail", "Corporate Kiosk", "Train Station
        Service Desk", "Direct Printing of Ticket", "Ticket by Email",
        "Digital Printing of Ticket at Home", "Retrieve Ticket at
        Eurostar in London" Collect booking ticket at a Kiosk, print in
        agency.
    fulfillment_location: Information about the location of the printer.
    fulfillment_idtype: Identification type, e.g. credit card, to define
        how the customer will identify himself when collecting the
        ticket
    fulfillment_idnumber: Identification number, e.g. card number, to
        define how the customer will identify himself when collecting
        the ticket
    is_agent_type: If this is true then FormOfPayment mention in Type is
        anAgent type FormOfPayment.
    agent_text: This is only relevent when IsAgentType is specified as
        true. Otherwise this will be ignored.
    reuse_fop: Key of the FOP Key to be reused as this Form of
        Payment.Only Credit and Debit Card will be supported for FOP
        Reuse.
    external_reference:
    reusable: Indicates whether the form of payment can be reused or
        not. Currently applicable for Credit and Debit form of payment
    profile_id: The unique ID of the profile that contains the payment
        details to use.
    profile_key: The Key assigned to the payment details value from the
        specified profile.
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    credit_card: Optional[CreditCard] = field(
        default=None,
        metadata={
            "name": "CreditCard",
            "type": "Element",
        }
    )
    debit_card: Optional[DebitCard] = field(
        default=None,
        metadata={
            "name": "DebitCard",
            "type": "Element",
        }
    )
    enett_van: Optional[EnettVan] = field(
        default=None,
        metadata={
            "name": "EnettVan",
            "type": "Element",
        }
    )
    certificate: Optional[Certificate] = field(
        default=None,
        metadata={
            "name": "Certificate",
            "type": "Element",
        }
    )
    ticket_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "min_length": 1,
            "max_length": 13,
        }
    )
    check: Optional[Check] = field(
        default=None,
        metadata={
            "name": "Check",
            "type": "Element",
        }
    )
    requisition: Optional[Requisition] = field(
        default=None,
        metadata={
            "name": "Requisition",
            "type": "Element",
        }
    )
    misc_form_of_payment: Optional[MiscFormOfPayment] = field(
        default=None,
        metadata={
            "name": "MiscFormOfPayment",
            "type": "Element",
        }
    )
    agency_payment: Optional[AgencyPayment] = field(
        default=None,
        metadata={
            "name": "AgencyPayment",
            "type": "Element",
        }
    )
    united_nations: Optional[UnitedNations] = field(
        default=None,
        metadata={
            "name": "UnitedNations",
            "type": "Element",
        }
    )
    direct_payment: Optional[DirectPayment] = field(
        default=None,
        metadata={
            "name": "DirectPayment",
            "type": "Element",
        }
    )
    agent_voucher: Optional[AgentVoucher] = field(
        default=None,
        metadata={
            "name": "AgentVoucher",
            "type": "Element",
        }
    )
    payment_advice: Optional[PaymentAdvice] = field(
        default=None,
        metadata={
            "name": "PaymentAdvice",
            "type": "Element",
        }
    )
    provider_reservation_info_ref: List[TypeFormOfPaymentPnrreference] = field(
        default_factory=list,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    segment_ref: List[TypeGeneralReference] = field(
        default_factory=list,
        metadata={
            "name": "SegmentRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    bsppayment: Optional[Bsppayment] = field(
        default=None,
        metadata={
            "name": "BSPPayment",
            "type": "Element",
        }
    )
    arcpayment: Optional[Arcpayment] = field(
        default=None,
        metadata={
            "name": "ARCPayment",
            "type": "Element",
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
            "max_length": 25,
        }
    )
    fulfillment_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "FulfillmentType",
            "type": "Attribute",
        }
    )
    fulfillment_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "FulfillmentLocation",
            "type": "Attribute",
        }
    )
    fulfillment_idtype: Optional[TypeFulfillmentIdtype] = field(
        default=None,
        metadata={
            "name": "FulfillmentIDType",
            "type": "Attribute",
        }
    )
    fulfillment_idnumber: Optional[str] = field(
        default=None,
        metadata={
            "name": "FulfillmentIDNumber",
            "type": "Attribute",
        }
    )
    is_agent_type: bool = field(
        default=False,
        metadata={
            "name": "IsAgentType",
            "type": "Attribute",
        }
    )
    agent_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgentText",
            "type": "Attribute",
        }
    )
    reuse_fop: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReuseFOP",
            "type": "Attribute",
        }
    )
    external_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExternalReference",
            "type": "Attribute",
            "max_length": 32,
        }
    )
    reusable: bool = field(
        default=False,
        metadata={
            "name": "Reusable",
            "type": "Attribute",
        }
    )
    profile_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
        }
    )
    profile_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProfileKey",
            "type": "Attribute",
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class Guarantee:
    """
    Payment Guarantee Guarantee, Deposit or PrePayment.

    Parameters
    ----------
    credit_card:
    other_guarantee_info:
    type: Guarantee, Deposit for 1G/1V/1P/1J and PrePayment for 1P/1J
        only
    key: Key for update/delete of the element
    reuse_fop: Key of the FOP Key to be reused as this Form of
        Payment.Only Credit and Debit Card will be supported for FOP
        Reuse.
    external_reference:
    reusable: Indicates whether the form of payment can be reused or
        not. Currently applicable for Credit and Debit form of payment
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    credit_card: Optional[CreditCard] = field(
        default=None,
        metadata={
            "name": "CreditCard",
            "type": "Element",
        }
    )
    other_guarantee_info: Optional[OtherGuaranteeInfo] = field(
        default=None,
        metadata={
            "name": "OtherGuaranteeInfo",
            "type": "Element",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    reuse_fop: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReuseFOP",
            "type": "Attribute",
        }
    )
    external_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExternalReference",
            "type": "Attribute",
            "max_length": 32,
        }
    )
    reusable: bool = field(
        default=False,
        metadata={
            "name": "Reusable",
            "type": "Attribute",
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )


@dataclass
class BaseCreateWithFormOfPaymentReq(BaseCreateReservationReq):
    """
    Container for BaseCreateReservation along with Form Of Payment.

    Parameters
    ----------
    form_of_payment: Provider:1G,1V,1P,1J,ACH,SDK.
    """
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v48_0",
            "max_occurs": 999,
        }
    )


@dataclass
class McoexchangeInfo:
    """
    Information related to the exchange tickets available for the MCO.

    Parameters
    ----------
    form_of_payment:
    exchanged_coupon:
    original_ticket_number: Airline form and serial number of the
        original ticket issued.
    original_city_code: Location of honoring carrier or operator.
    original_ticket_date: Date that the Original ticket was issued.
    iatacode: IATA code of the issuing agency.
    """
    class Meta:
        name = "MCOExchangeInfo"
        namespace = "http://www.travelport.com/schema/common_v48_0"

    form_of_payment: Optional[FormOfPayment] = field(
        default=None,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
        }
    )
    exchanged_coupon: List[ExchangedCoupon] = field(
        default_factory=list,
        metadata={
            "name": "ExchangedCoupon",
            "type": "Element",
            "max_occurs": 4,
        }
    )
    original_ticket_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginalTicketNumber",
            "type": "Attribute",
            "length": 13,
        }
    )
    original_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginalCityCode",
            "type": "Attribute",
            "length": 3,
        }
    )
    original_ticket_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginalTicketDate",
            "type": "Attribute",
            "pattern": r"[^:Z].*",
        }
    )
    iatacode: Optional[str] = field(
        default=None,
        metadata={
            "name": "IATACode",
            "type": "Attribute",
            "max_length": 8,
        }
    )


@dataclass
class ServiceFeeInfo:
    """
    Travel Agency Service Fees (TASF) are charged by the agency through BSP or
    Airline Reporting Corporation (ARC).

    Parameters
    ----------
    form_of_payment:
    service_fee_tax_info:
    credit_card_auth:
    payment:
    status: Status of the service fee. Possible Values – Issued,
        ReadyToIssue, IssueLater.
    description: The description of the service fee.
    key:
    confirmation: The confirmation number of the service fee in the
        merchant host system.
    ticket_number: The ticket that this fee was issued in connection
        with.
    booking_traveler_ref: A reference to a passenger.
    provider_reservation_info_ref: A reference to the provider
        reservation info to which the service is tied.
    passive_provider_reservation_info_ref: A reference to the passive
        provider reservation info to which the service is tied.
    total_amount: The total amount for this Service Fee including base
        amount and all taxes.
    base_amount: Represents the base price for this entity. This does
        not include any taxes.
    taxes: The aggregated amount of all the taxes that are associated
        with this entity. See the associated Service Fee TaxInfo array
        for a breakdown of the individual taxes.
    el_stat: This attribute is used to show the action results of an
        element. Possible values are "A" (when elements have been added
        to the UR) and "M" (when existing elements have been modified).
        Response only.
    key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    booking_traveler_name: The name of the passenger.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v48_0"

    form_of_payment: Optional[FormOfPayment] = field(
        default=None,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
        }
    )
    service_fee_tax_info: List[ServiceFeeTaxInfo] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFeeTaxInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    credit_card_auth: Optional[CreditCardAuth] = field(
        default=None,
        metadata={
            "name": "CreditCardAuth",
            "type": "Element",
        }
    )
    payment: Optional[Payment] = field(
        default=None,
        metadata={
            "name": "Payment",
            "type": "Element",
        }
    )
    status: Optional[TypeStatus] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    confirmation: Optional[str] = field(
        default=None,
        metadata={
            "name": "Confirmation",
            "type": "Attribute",
        }
    )
    ticket_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Attribute",
        }
    )
    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        }
    )
    provider_reservation_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        }
    )
    passive_provider_reservation_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PassiveProviderReservationInfoRef",
            "type": "Attribute",
        }
    )
    total_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalAmount",
            "type": "Attribute",
        }
    )
    base_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseAmount",
            "type": "Attribute",
        }
    )
    taxes: Optional[str] = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Attribute",
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )
    booking_traveler_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingTravelerName",
            "type": "Attribute",
        }
    )


@dataclass
class Mco(Mcoinformation):
    """
    Parameters
    ----------
    form_of_payment:
    endorsement:
    mcoexchange_info:
    mcofee_info:
    mcoremark:
    mcoprice_data:
    stock_control:
    mcotext:
    ticket_type: Ticket issue indicator. Possible values "Pre-paid
        ticket advice", "Ticket on departure" and "Other" .
    ticket_number: The ticket that this MCO was issued in connection
        with. Could be the ticket that caused the fee, a residual from
        an exchange, or an airline service fee.
    mcoissued: Set to true when the MCO is to be issued and set to false
        if it is stored for issue at a later time.
    mcoissue_date: Date and time in which the MCO was issued.
    mcodoc_num: MCO document number.
    issue_reason_code: MCO issuing reason code. Possible Values (List):
        A - Air transportation, B - Surface transportation C - Bag
        shipped as cargo, D - Land arrgs for it, E - Car hire, F -
        Sleeper / berth G - Up-grading, H - Under collections, I -
        Taxes/fees/charges, J - Deposits down payments K - Refundable
        Balances, L - Hotel accommodations, M - Sundry charges, N -
        Cancellation fee O - Other, P thru Z - airline specific, 1 thru
        9 - market specific
    plating_carrier: The Plating Carrier for this MCO
    tour_operator: Tour Operator - name of honoring carrier or operator.
    location: Location of honoring carrier or operator.
    tour_code: The Tour Code of the MCO.
    provider_code: Contains the Provider Code of the provider that
        houses this MCO.
    provider_locator_code: Contains the Provider Locator Code of the
        Provider Reservation that houses this MCO.
    pseudo_city_code: The PCC in the host system.
    expiry_date: E-Voucher’s Expiry Date. This expiry date is specific
        to Rail product
    """
    class Meta:
        name = "MCO"
        namespace = "http://www.travelport.com/schema/common_v48_0"

    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    endorsement: Optional[Endorsement] = field(
        default=None,
        metadata={
            "name": "Endorsement",
            "type": "Element",
        }
    )
    mcoexchange_info: Optional[McoexchangeInfo] = field(
        default=None,
        metadata={
            "name": "MCOExchangeInfo",
            "type": "Element",
        }
    )
    mcofee_info: Optional[McofeeInfo] = field(
        default=None,
        metadata={
            "name": "MCOFeeInfo",
            "type": "Element",
        }
    )
    mcoremark: List[Mcoremark] = field(
        default_factory=list,
        metadata={
            "name": "MCORemark",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    mcoprice_data: Optional[McopriceData] = field(
        default=None,
        metadata={
            "name": "MCOPriceData",
            "type": "Element",
        }
    )
    stock_control: List[StockControl] = field(
        default_factory=list,
        metadata={
            "name": "StockControl",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    mcotext: List[Mcotext] = field(
        default_factory=list,
        metadata={
            "name": "MCOText",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    ticket_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketType",
            "type": "Attribute",
        }
    )
    ticket_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Attribute",
        }
    )
    mcoissued: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MCOIssued",
            "type": "Attribute",
            "required": True,
        }
    )
    mcoissue_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "MCOIssueDate",
            "type": "Attribute",
        }
    )
    mcodoc_num: Optional[str] = field(
        default=None,
        metadata={
            "name": "MCODocNum",
            "type": "Attribute",
        }
    )
    issue_reason_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssueReasonCode",
            "type": "Attribute",
        }
    )
    plating_carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlatingCarrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    tour_operator: Optional[str] = field(
        default=None,
        metadata={
            "name": "TourOperator",
            "type": "Attribute",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Attribute",
        }
    )
    tour_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "TourCode",
            "type": "Attribute",
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    provider_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "max_length": 15,
        }
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        }
    )
    expiry_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ExpiryDate",
            "type": "Attribute",
        }
    )
