from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


class TypeDisplayDetailName(Enum):
    """
    Properties
    ----------
    OWNING_AGENCY_PCC
        The pseudo city code of the agency owning the PNR
    CREATING_AGENT_SIGN_ON
        Sign on code of the agent created the PNR
    CREATING_AGENT_DUTY
        Duty code of the agent created the PNR
    CREATING_AGENCY_IATA
        IATA number of the agency  created the PNR
    PREPAID_TICKET_ADVICE_INDICATOR
        Indicates whether Prepaid Ticket Advice is attached to PNR
    BFBORROWED
        Indicates the current PNR as borrowed
    GLOBAL_PNR
        Indicates whether current PNR is Global PNR
    READ_ONLY_PNR
        Indicates PNR as read only
    PAST_DATE_QUICK_RETRIEVED_PNR
        Indicates PNR retrieved from offline archival process
    SUPER_PNR
        Indicates whether current PNR is Super PNR
    PNRPURGE_DATE
        Purge date of the PNR
    ORIGINAL_RECEIVED_FIELD_VALUE
        The original data in the received field
    DIV_PSGR_NAME
        Passenger Name in a divided PNR
    TRUNC_IND
        Indicator for Truncated names
    DIV_TYPE_IND
        Divide Type Indicator if it pertains to child or parent booking
    RLOC
        Record Locator of parent or child booking
    DIV_DT
        Date of divide action
    DIV_TM
        Time of day of divide action
    TRAVEL_ORDER
        Travel order of the segment
    SEGMENT_STATUS
        Status of associated segment
    START_DATE
        Date of departure of the rail segment
    DAY_CHANGE
        Indicates arrival date as number of days before or after departure
        date
    VENDOR
        Vendor code of the segment
    START_TIME
        Start Time of the segment
    END_TIME
        End Time of the segment
    BOOKING_CODE
        The booking code of the rail segment seating area
    TRAIN_NUMBER
        Denotes Train number
    NUMBER_OF_SEATS
        Number of seats sold for the trip
    SELL_TYPE
        The mode of selling the segment
    TARIFF_TYPE
        Type of Tariff for the segment
    CONFIRMATION_NUMBER
        The confirmation number of the segment
    BOARDING_INFORMATION
        Information related to boarding point of the segment
    ARRIVAL_INFORMATION
        Information related to arrival point of the segment
    TEXT
        Additional   information
    """

    OWNING_AGENCY_PCC = "OwningAgencyPCC"
    CREATING_AGENT_SIGN_ON = "CreatingAgentSignOn"
    CREATING_AGENT_DUTY = "CreatingAgentDuty"
    CREATING_AGENCY_IATA = "CreatingAgencyIATA"
    PREPAID_TICKET_ADVICE_INDICATOR = "PrepaidTicketAdviceIndicator"
    BFBORROWED = "BFBorrowed"
    GLOBAL_PNR = "GlobalPNR"
    READ_ONLY_PNR = "ReadOnlyPNR"
    PAST_DATE_QUICK_RETRIEVED_PNR = "PastDateQuickRetrievedPNR"
    SUPER_PNR = "SuperPNR"
    PNRPURGE_DATE = "PNRPurgeDate"
    ORIGINAL_RECEIVED_FIELD_VALUE = "OriginalReceivedFieldValue"
    DIV_PSGR_NAME = "DivPsgrName"
    TRUNC_IND = "TruncInd"
    DIV_TYPE_IND = "DivTypeInd"
    RLOC = "RLoc"
    DIV_DT = "DivDt"
    DIV_TM = "DivTm"
    TRAVEL_ORDER = "TravelOrder"
    SEGMENT_STATUS = "SegmentStatus"
    START_DATE = "StartDate"
    DAY_CHANGE = "DayChange"
    VENDOR = "Vendor"
    START_TIME = "StartTime"
    END_TIME = "EndTime"
    BOOKING_CODE = "BookingCode"
    TRAIN_NUMBER = "TrainNumber"
    NUMBER_OF_SEATS = "NumberOfSeats"
    SELL_TYPE = "SellType"
    TARIFF_TYPE = "TariffType"
    CONFIRMATION_NUMBER = "ConfirmationNumber"
    BOARDING_INFORMATION = "BoardingInformation"
    ARRIVAL_INFORMATION = "ArrivalInformation"
    TEXT = "Text"
