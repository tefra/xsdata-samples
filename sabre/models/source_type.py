from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.position_type import PositionType
from sabre.models.source_booking_channel_type import SourceBookingChannelType
from sabre.models.unique_id_type import UniqueIdType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class SourceType:
    """
    Attributes:
        requestor_id: An identifier of the entity making the request
            (e.g. ATA/IATA/ID number, Electronic Reservation Service
            Provider (ERSP), Association of British Travel Agents
            (ABTA)).
        position:
        booking_channel:
        agent_sine: Identifies the party within the requesting entity.
        pseudo_city_code: An identification code assigned to an
            office/agency by a reservation system.
        isocountry: The country code of the requesting party.
        isocurrency: The currency code in which the reservation will be
            ticketed.
        agent_duty_code: An authority code assigned to a requestor.
        airline_vendor_id: The IATA assigned airline code.
        airport_code: The IATA assigned airport code.
        first_depart_point: The point of first departure in a trip.
        ersp_user_id: Electronic Reservation Service Provider (ERSP)
            assigned identifier used to identify the individual using
            the ERSP system.
        personal_city_code: City code part of Office Accounting Code
        accounting_code: Accounting Code part of Office Accounting Code
        office_code: Office Code part of Office Accounting Code
        default_ticketing_carrier: Default Ticketing Carrier for Office
            Accounting Code
        airline_channel_code: Airline Channel Code
        agent_department_code: Agent department code
        agent_function: Agent function
        travel_agency_iata: Travel agency IATA
        home_agency_iata: Home agency IATA
        agent_iata: Agent IATA
        vendor_crscode: Vendor CRS code
        agent_duty: Agent duty
        abacus_user: Abacus user
        agent_city: Agent city
        carrier: Carrier
        main_travel_agency_pcc: Main travel agency PCC
        home_pcc: Home PCC
    """

    requestor_id: UniqueIdType = field(
        metadata={
            "name": "RequestorID",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    position: None | PositionType = field(
        default=None,
        metadata={
            "name": "Position",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    booking_channel: None | SourceBookingChannelType = field(
        default=None,
        metadata={
            "name": "BookingChannel",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    agent_sine: None | str = field(
        default=None,
        metadata={
            "name": "AgentSine",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pseudo_city_code: None | str = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        },
    )
    isocountry: None | str = field(
        default=None,
        metadata={
            "name": "ISOCountry",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{2}",
        },
    )
    isocurrency: None | str = field(
        default=None,
        metadata={
            "name": "ISOCurrency",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{3}",
        },
    )
    agent_duty_code: None | str = field(
        default=None,
        metadata={
            "name": "AgentDutyCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        },
    )
    airline_vendor_id: None | str = field(
        default=None,
        metadata={
            "name": "AirlineVendorID",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{2,3}",
        },
    )
    airport_code: None | str = field(
        default=None,
        metadata={
            "name": "AirportCode",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{3,5}",
        },
    )
    first_depart_point: None | str = field(
        default=None,
        metadata={
            "name": "FirstDepartPoint",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 3,
        },
    )
    ersp_user_id: None | str = field(
        default=None,
        metadata={
            "name": "ERSP_UserID",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        },
    )
    personal_city_code: None | str = field(
        default=None,
        metadata={
            "name": "PersonalCityCode",
            "type": "Attribute",
            "pattern": r"[0-9A-Z]{3,4}",
        },
    )
    accounting_code: None | str = field(
        default=None,
        metadata={
            "name": "AccountingCode",
            "type": "Attribute",
            "pattern": r"[0-9a-zA-Z]{2,3}",
        },
    )
    office_code: None | str = field(
        default=None,
        metadata={
            "name": "OfficeCode",
            "type": "Attribute",
            "pattern": r"[0-9]{7}",
        },
    )
    default_ticketing_carrier: None | str = field(
        default=None,
        metadata={
            "name": "DefaultTicketingCarrier",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{2}[A-Z]?",
        },
    )
    airline_channel_code: None | str = field(
        default=None,
        metadata={
            "name": "AirlineChannelCode",
            "type": "Attribute",
            "pattern": r"[A-Z]{3}",
        },
    )
    agent_department_code: None | str = field(
        default=None,
        metadata={
            "name": "AgentDepartmentCode",
            "type": "Attribute",
            "max_length": 6,
        },
    )
    agent_function: None | str = field(
        default=None,
        metadata={
            "name": "AgentFunction",
            "type": "Attribute",
            "max_length": 3,
        },
    )
    travel_agency_iata: None | str = field(
        default=None,
        metadata={
            "name": "TravelAgencyIATA",
            "type": "Attribute",
            "pattern": r"[0-9]{1,14}",
        },
    )
    home_agency_iata: None | str = field(
        default=None,
        metadata={
            "name": "HomeAgencyIATA",
            "type": "Attribute",
            "pattern": r"[0-9]{1,14}",
        },
    )
    agent_iata: None | str = field(
        default=None,
        metadata={
            "name": "AgentIATA",
            "type": "Attribute",
            "pattern": r"[0-9]{1,14}",
        },
    )
    vendor_crscode: None | str = field(
        default=None,
        metadata={
            "name": "VendorCRSCode",
            "type": "Attribute",
        },
    )
    agent_duty: None | str = field(
        default=None,
        metadata={
            "name": "AgentDuty",
            "type": "Attribute",
            "length": 1,
        },
    )
    abacus_user: bool = field(
        default=False,
        metadata={
            "name": "AbacusUser",
            "type": "Attribute",
        },
    )
    agent_city: None | str = field(
        default=None,
        metadata={
            "name": "AgentCity",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{3}",
        },
    )
    carrier: None | str = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "pattern": r"[0-9A-Z]{2,3}",
        },
    )
    main_travel_agency_pcc: None | str = field(
        default=None,
        metadata={
            "name": "MainTravelAgencyPCC",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        },
    )
    home_pcc: None | str = field(
        default=None,
        metadata={
            "name": "HomePCC",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        },
    )
