from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.characteristic_3 import Characteristic3
from travelport.models.emd import Emd
from travelport.models.passenger_seat_price import PassengerSeatPrice
from travelport.models.remark_1 import Remark1
from travelport.models.service_data_1 import ServiceData1
from travelport.models.tax_info import TaxInfo
from travelport.models.tour_code import TourCode
from travelport.models.type_facility import TypeFacility
from travelport.models.type_seat_availability import TypeSeatAvailability

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class Facility:
    """
    The facility definition for a part of a row or a seat map.

    Parameters
    ----------
    characteristic
    remark
    passenger_seat_price
    tax_info
        Tax information related to seat price. This is presently populated
        for MCH and ACH content. Applicable providers are MCH/ACH
    emd
    service_data
    tour_code
    type_value
        The type of facility
    seat_code
        If a seat type, the seat identifier
    availability
        If a seat type, the availability of the seat
    seat_price
        The price of the seat, if applicable.
    paid
        Set to True if either SeatPrice or GroupSeatPrice are returned.
    service_sub_code
        The service subcode associated with the Facility
    ssrcode
        The SSR Code associated with the Facility
    issuance_reason
        A one-letter RFIC value filed by the airline in each Optional
        Service will be mapped to this attribute. RFIC is IATA Reason for
        Issuance Code. Possible codes are A (Air transportation),B (Surface
        Transportation),C(Bagage), D(Financial Impact),E(Airport
        Services),F(Merchandise),G(Inflight Services),I (Individual Airline
        use).
    base_seat_price
        Price of the seats excluding Taxes.
    taxes
        Tax amount for the seat price.
    quantity
        The number of units availed for each optional service (e.g. 2
        baggage availed will be specified as 2 in quantity for optional
        service BAGGAGE)
    sequence_number
        The sequence number associated with the OptionalService
    inclusive_of_tax
        Identifies if the service was filed with a fee that is inclusive of
        tax.
    interline_settlement_allowed
        Identifies if the interline settlement is allowed in service .
    geography_specification
        Sector, Portion, Journey.
    source
        The Source of the optional service. The source can be ACH, MCE, or
        MCH.
    optional_service_ref
        References the OptionalService for the Row/Facility. Providers: ACH,
        1G, 1V, 1P
    seat_information_ref
        Specifies the seat information for the seat. Providers: ACH, 1G, 1V,
        1P
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    characteristic: list[Characteristic3] = field(
        default_factory=list,
        metadata={
            "name": "Characteristic",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    remark: list[Remark1] = field(
        default_factory=list,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    passenger_seat_price: list[PassengerSeatPrice] = field(
        default_factory=list,
        metadata={
            "name": "PassengerSeatPrice",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    tax_info: list[TaxInfo] = field(
        default_factory=list,
        metadata={
            "name": "TaxInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    emd: None | Emd = field(
        default=None,
        metadata={
            "name": "EMD",
            "type": "Element",
        },
    )
    service_data: list[ServiceData1] = field(
        default_factory=list,
        metadata={
            "name": "ServiceData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    tour_code: None | TourCode = field(
        default=None,
        metadata={
            "name": "TourCode",
            "type": "Element",
        },
    )
    type_value: TypeFacility = field(
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    seat_code: None | str = field(
        default=None,
        metadata={
            "name": "SeatCode",
            "type": "Attribute",
        },
    )
    availability: None | TypeSeatAvailability = field(
        default=None,
        metadata={
            "name": "Availability",
            "type": "Attribute",
        },
    )
    seat_price: None | str = field(
        default=None,
        metadata={
            "name": "SeatPrice",
            "type": "Attribute",
        },
    )
    paid: None | bool = field(
        default=None,
        metadata={
            "name": "Paid",
            "type": "Attribute",
        },
    )
    service_sub_code: None | str = field(
        default=None,
        metadata={
            "name": "ServiceSubCode",
            "type": "Attribute",
            "max_length": 3,
        },
    )
    ssrcode: None | str = field(
        default=None,
        metadata={
            "name": "SSRCode",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 4,
        },
    )
    issuance_reason: None | str = field(
        default=None,
        metadata={
            "name": "IssuanceReason",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 1,
        },
    )
    base_seat_price: None | str = field(
        default=None,
        metadata={
            "name": "BaseSeatPrice",
            "type": "Attribute",
        },
    )
    taxes: None | str = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Attribute",
        },
    )
    quantity: None | int = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Attribute",
        },
    )
    sequence_number: None | int = field(
        default=None,
        metadata={
            "name": "SequenceNumber",
            "type": "Attribute",
        },
    )
    inclusive_of_tax: None | bool = field(
        default=None,
        metadata={
            "name": "InclusiveOfTax",
            "type": "Attribute",
        },
    )
    interline_settlement_allowed: None | bool = field(
        default=None,
        metadata={
            "name": "InterlineSettlementAllowed",
            "type": "Attribute",
        },
    )
    geography_specification: None | str = field(
        default=None,
        metadata={
            "name": "GeographySpecification",
            "type": "Attribute",
        },
    )
    source: None | str = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Attribute",
        },
    )
    optional_service_ref: None | str = field(
        default=None,
        metadata={
            "name": "OptionalServiceRef",
            "type": "Attribute",
        },
    )
    seat_information_ref: None | str = field(
        default=None,
        metadata={
            "name": "SeatInformationRef",
            "type": "Attribute",
        },
    )
