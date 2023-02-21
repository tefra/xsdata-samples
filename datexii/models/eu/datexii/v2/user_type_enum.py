from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class UserTypeEnum(Enum):
    """
    Types of users; used for parking but also for usage of equipment and services.

    :cvar ALL_USERS: All users.
    :cvar SHOPPERS: Shoppers.
    :cvar HOTEL_GUESTS: Hotel guests.
    :cvar SUBSCRIBERS: Subscribers.
    :cvar RESERVATION_HOLDERS: Those who have a valid reservation for
        the duration of parking.
    :cvar SEASON_TICKET_HOLDERS: Season ticket holders.
    :cvar REGISTERED_DISABLED_USERS: Registered disabled persons.
    :cvar DISABLED: Physically impaired people.
    :cvar HANDICAPPED: Persons with deficiencies in their daily life.
    :cvar HEARING_IMPAIRED: People with difficulties to hear.
    :cvar VISUALLY_IMPAIRED: People with difficulties to see.
    :cvar WHEELCHAIR_USERS: Wheelchair users.
    :cvar ELDERLY_USERS: Elderly users.
    :cvar FAMILIES: Families.
    :cvar MEN: Men.
    :cvar WOMEN: Women.
    :cvar PREGNANT_WOMEN: Pregnant women.
    :cvar PENSIONERS: Pensioners.
    :cvar STUDENTS: Students.
    :cvar STAFF: Staff.
    :cvar EMPLOYEES: Employees.
    :cvar CUSTOMERS: Customers.
    :cvar VISITORS: Visitors.
    :cvar MEMBERS: Members.
    :cvar SHORT_TERM_PARKER: Short-term parker.
    :cvar LONG_TERM_PARKER: Long-term parker.
    :cvar OVERNIGHT_PARKER: Overnight parker.
    :cvar SPORT_EVENT_AWAY_SUPPORTERS: Sport event away supporters.
    :cvar SPORT_EVENT_HOME_SUPPORTERS: Sport event home supporters.
    :cvar RESIDENTS: Local residents.
    :cvar COMMUTERS: Commuters.
    :cvar PARK_AND_RIDE_USERS: Users that are changing into public
        transport at this parking.
    :cvar PARK_AND_WALK_USER: Park and walk user.
    :cvar PARK_AND_CYCLE_USER: Park and cycle user.
    :cvar OTHER: Other.
    :cvar UNKNOWN: Unknown.
    """
    ALL_USERS = "allUsers"
    SHOPPERS = "shoppers"
    HOTEL_GUESTS = "hotelGuests"
    SUBSCRIBERS = "subscribers"
    RESERVATION_HOLDERS = "reservationHolders"
    SEASON_TICKET_HOLDERS = "seasonTicketHolders"
    REGISTERED_DISABLED_USERS = "registeredDisabledUsers"
    DISABLED = "disabled"
    HANDICAPPED = "handicapped"
    HEARING_IMPAIRED = "hearingImpaired"
    VISUALLY_IMPAIRED = "visuallyImpaired"
    WHEELCHAIR_USERS = "wheelchairUsers"
    ELDERLY_USERS = "elderlyUsers"
    FAMILIES = "families"
    MEN = "men"
    WOMEN = "women"
    PREGNANT_WOMEN = "pregnantWomen"
    PENSIONERS = "pensioners"
    STUDENTS = "students"
    STAFF = "staff"
    EMPLOYEES = "employees"
    CUSTOMERS = "customers"
    VISITORS = "visitors"
    MEMBERS = "members"
    SHORT_TERM_PARKER = "shortTermParker"
    LONG_TERM_PARKER = "longTermParker"
    OVERNIGHT_PARKER = "overnightParker"
    SPORT_EVENT_AWAY_SUPPORTERS = "sportEventAwaySupporters"
    SPORT_EVENT_HOME_SUPPORTERS = "sportEventHomeSupporters"
    RESIDENTS = "residents"
    COMMUTERS = "commuters"
    PARK_AND_RIDE_USERS = "parkAndRideUsers"
    PARK_AND_WALK_USER = "parkAndWalkUser"
    PARK_AND_CYCLE_USER = "parkAndCycleUser"
    OTHER = "other"
    UNKNOWN = "unknown"
