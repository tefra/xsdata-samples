from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate
from travelport.models.type_itinerary_code import TypeItineraryCode

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class OriginalItineraryDetails:
    """Used for rapid reprice to provide additional information about the original
    itinerary.

    Providers: 1G/1V/1P/1S/1A

    Parameters
    ----------
    itinerary_type
        Values allowed are International or Domestic. This tells if the
        itinerary is international or domestic.
    bulk_ticket
        Set to true and the itinerary is/will be a bulk ticket. Set to false
        and the itinerary being repriced will not be a bulk ticket. Default
        is false.
    ticketing_pcc
        This is the PCC or SID where the ticket was issued
    ticketing_iata
        This is the IATA where the ticket was issued.
    ticketing_country
        This is the country where the ticket was issued.
    tour_code
    ticketing_date
        The date the repriced itinerary was ticketed
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    itinerary_type: None | TypeItineraryCode = field(
        default=None,
        metadata={
            "name": "ItineraryType",
            "type": "Attribute",
        }
    )
    bulk_ticket: bool = field(
        default=False,
        metadata={
            "name": "BulkTicket",
            "type": "Attribute",
        }
    )
    ticketing_pcc: None | str = field(
        default=None,
        metadata={
            "name": "TicketingPCC",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        }
    )
    ticketing_iata: None | str = field(
        default=None,
        metadata={
            "name": "TicketingIATA",
            "type": "Attribute",
            "max_length": 8,
        }
    )
    ticketing_country: None | str = field(
        default=None,
        metadata={
            "name": "TicketingCountry",
            "type": "Attribute",
            "length": 2,
        }
    )
    tour_code: None | str = field(
        default=None,
        metadata={
            "name": "TourCode",
            "type": "Attribute",
            "max_length": 15,
        }
    )
    ticketing_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "TicketingDate",
            "type": "Attribute",
        }
    )
