from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Advtype:
    """
    Parameters
    ----------
    adv_rsvn_only_if_tk
        Reservation only if ticketed. True is advanced reservations only if
        tickets. False is no advanced reservations
    adv_rsvn_any_tm
        Reservation anytime. True if advanced reservatiosn anytime. False if
        advanced reservations for a limited time.
    adv_rsvn_hrs
        Reservation hours. True if advanced reservation time in hours. False
        if advanced reservation time not in hours.
    adv_rsvn_days
        Reservation days. True if advanced reservation time in days. False
        if advanced reservation time not in days.
    adv_rsvn_months
        Reservation months. True if advanced reservation time in months.
        False if advanced reservation time not in months.
    adv_rsvn_earliest_tm
        Earliest reservation time. True if advanced reservations time is
        earliest permitted. False is advanced reservation time not earliest
        permitted time.
    adv_rsvn_latest_tm
        Latest reservation time. True if advanced reservations time is
        latest permitted. False is advanced reservation time not latest
        permitted time.
    adv_rsvn_waived
        Reservation Waived. True if advanced reservation waived. False if
        advanced reservation not waived.
    adv_rsvn_data_exists
        Reservation data exists. True if advanced reservation data exists.
        False if advanced reservation data does not exist.
    adv_rsvn_end_item
        Reservation end item. True if advanced reservation end item and more
        values. False if it does not exist.
    adv_tk_earliest_tm
        Earliest ticketing time. True if earliest permitted. False if not
        earliest permitted.
    adv_tk_latest_tm
        Latest ticketing time. True if time is latest permitted. False if
        time is not latest permitted.
    adv_tk_rsvn_hrs
        Ticketing reservation hours. True if in hours. False if not in
        hours.
    adv_tk_rsvn_days
        Ticketing reservation days. True if in days. False if not in days.
    adv_tk_rsvn_months
        Ticketing reservation months. True if in months. False if not in
        months.
    adv_tk_start_hrs
        Latest ticketing departure. True if time is latest permitted. False
        if time is not latest permitted.
    adv_tk_start_days
        Ticketing departure days. True if in days. False if not in days.
    adv_tk_start_months
        Ticketing reservation months. True if in months. False if not in
        months.
    adv_tk_waived
        Ticketing waived. True if waived. False if not waived.
    adv_tk_any_tm
        Ticketing anytime. True if anytime. False if limited time.
    adv_tk_end_item
        Ticketing end item. True if advanced ticketing item and more values.
        False if end item does not exist.
    adv_rsvn_tm
        Advanced reservation time.
    adv_tk_rsvn_tm
        Advanced ticketing reservation time.
    adv_tk_start_tm
        Advanced ticketing departure time.
    earliest_rsvn_dt_present
        Earliest reservation date. True if date is present. False if date is
        not present.
    earliest_tk_dt_present
        Earliest ticketing date. True if date is present. False if date is
        not present.
    latest_rsvn_dt_present
        Latest reservation date. True if date is present. False if date is
        not present.
    latest_tk_dt_present
        Latest ticketing date.  True if date is present. False if date is
        not present.
    earliest_rsvn_dt
        Earliest reservation date.
    earliest_tk_dt
        Earliest ticketing date.
    latest_rsvn_dt
        Latest reservation date.
    latest_tk_dt
        Latest ticketing date.
    """
    class Meta:
        name = "ADVType"

    adv_rsvn_only_if_tk: None | bool = field(
        default=None,
        metadata={
            "name": "AdvRsvnOnlyIfTk",
            "type": "Attribute",
        }
    )
    adv_rsvn_any_tm: None | bool = field(
        default=None,
        metadata={
            "name": "AdvRsvnAnyTm",
            "type": "Attribute",
        }
    )
    adv_rsvn_hrs: None | bool = field(
        default=None,
        metadata={
            "name": "AdvRsvnHrs",
            "type": "Attribute",
        }
    )
    adv_rsvn_days: None | bool = field(
        default=None,
        metadata={
            "name": "AdvRsvnDays",
            "type": "Attribute",
        }
    )
    adv_rsvn_months: None | bool = field(
        default=None,
        metadata={
            "name": "AdvRsvnMonths",
            "type": "Attribute",
        }
    )
    adv_rsvn_earliest_tm: None | bool = field(
        default=None,
        metadata={
            "name": "AdvRsvnEarliestTm",
            "type": "Attribute",
        }
    )
    adv_rsvn_latest_tm: None | bool = field(
        default=None,
        metadata={
            "name": "AdvRsvnLatestTm",
            "type": "Attribute",
        }
    )
    adv_rsvn_waived: None | bool = field(
        default=None,
        metadata={
            "name": "AdvRsvnWaived",
            "type": "Attribute",
        }
    )
    adv_rsvn_data_exists: None | bool = field(
        default=None,
        metadata={
            "name": "AdvRsvnDataExists",
            "type": "Attribute",
        }
    )
    adv_rsvn_end_item: None | bool = field(
        default=None,
        metadata={
            "name": "AdvRsvnEndItem",
            "type": "Attribute",
        }
    )
    adv_tk_earliest_tm: None | bool = field(
        default=None,
        metadata={
            "name": "AdvTkEarliestTm",
            "type": "Attribute",
        }
    )
    adv_tk_latest_tm: None | bool = field(
        default=None,
        metadata={
            "name": "AdvTkLatestTm",
            "type": "Attribute",
        }
    )
    adv_tk_rsvn_hrs: None | bool = field(
        default=None,
        metadata={
            "name": "AdvTkRsvnHrs",
            "type": "Attribute",
        }
    )
    adv_tk_rsvn_days: None | bool = field(
        default=None,
        metadata={
            "name": "AdvTkRsvnDays",
            "type": "Attribute",
        }
    )
    adv_tk_rsvn_months: None | bool = field(
        default=None,
        metadata={
            "name": "AdvTkRsvnMonths",
            "type": "Attribute",
        }
    )
    adv_tk_start_hrs: None | bool = field(
        default=None,
        metadata={
            "name": "AdvTkStartHrs",
            "type": "Attribute",
        }
    )
    adv_tk_start_days: None | bool = field(
        default=None,
        metadata={
            "name": "AdvTkStartDays",
            "type": "Attribute",
        }
    )
    adv_tk_start_months: None | bool = field(
        default=None,
        metadata={
            "name": "AdvTkStartMonths",
            "type": "Attribute",
        }
    )
    adv_tk_waived: None | bool = field(
        default=None,
        metadata={
            "name": "AdvTkWaived",
            "type": "Attribute",
        }
    )
    adv_tk_any_tm: None | bool = field(
        default=None,
        metadata={
            "name": "AdvTkAnyTm",
            "type": "Attribute",
        }
    )
    adv_tk_end_item: None | bool = field(
        default=None,
        metadata={
            "name": "AdvTkEndItem",
            "type": "Attribute",
        }
    )
    adv_rsvn_tm: None | int = field(
        default=None,
        metadata={
            "name": "AdvRsvnTm",
            "type": "Attribute",
        }
    )
    adv_tk_rsvn_tm: None | int = field(
        default=None,
        metadata={
            "name": "AdvTkRsvnTm",
            "type": "Attribute",
        }
    )
    adv_tk_start_tm: None | int = field(
        default=None,
        metadata={
            "name": "AdvTkStartTm",
            "type": "Attribute",
        }
    )
    earliest_rsvn_dt_present: None | bool = field(
        default=None,
        metadata={
            "name": "EarliestRsvnDtPresent",
            "type": "Attribute",
        }
    )
    earliest_tk_dt_present: None | bool = field(
        default=None,
        metadata={
            "name": "EarliestTkDtPresent",
            "type": "Attribute",
        }
    )
    latest_rsvn_dt_present: None | bool = field(
        default=None,
        metadata={
            "name": "LatestRsvnDtPresent",
            "type": "Attribute",
        }
    )
    latest_tk_dt_present: None | bool = field(
        default=None,
        metadata={
            "name": "LatestTkDtPresent",
            "type": "Attribute",
        }
    )
    earliest_rsvn_dt: None | XmlDate = field(
        default=None,
        metadata={
            "name": "EarliestRsvnDt",
            "type": "Attribute",
        }
    )
    earliest_tk_dt: None | XmlDate = field(
        default=None,
        metadata={
            "name": "EarliestTkDt",
            "type": "Attribute",
        }
    )
    latest_rsvn_dt: None | XmlDate = field(
        default=None,
        metadata={
            "name": "LatestRsvnDt",
            "type": "Attribute",
        }
    )
    latest_tk_dt: None | XmlDate = field(
        default=None,
        metadata={
            "name": "LatestTkDt",
            "type": "Attribute",
        }
    )
