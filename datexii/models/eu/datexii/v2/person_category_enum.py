from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class PersonCategoryEnum(Enum):
    """
    Categories of person.

    :cvar ADULT: Adult.
    :cvar CHILD: Child (age 4 to 17).
    :cvar EMERGENCY_SERVICES_PERSON: A member of the emergency services,
        other than the police.
    :cvar FIREMAN: A member of the fire service.
    :cvar INFANT: Infant (age 0 to 3).
    :cvar MEDICAL_STAFF: A member of the medical service.
    :cvar MEMBER_OF_THE_PUBLIC: A member of the general public.
    :cvar POLICEMAN: A member of the police force.
    :cvar POLITICIAN: A politician.
    :cvar PUBLIC_TRANSPORT_PASSENGER: A passenger on or from a public
        transport vehicle.
    :cvar SICK_PERSON: A sick person.
    :cvar TRAFFIC_OFFICER: A traffic patrol officer of the road
        authority.
    :cvar TRAFFIC_WARDEN: A member of the local traffic warden service.
    :cvar VERY_IMPORTANT_PERSON: A very important person.
    """
    ADULT = "adult"
    CHILD = "child"
    EMERGENCY_SERVICES_PERSON = "emergencyServicesPerson"
    FIREMAN = "fireman"
    INFANT = "infant"
    MEDICAL_STAFF = "medicalStaff"
    MEMBER_OF_THE_PUBLIC = "memberOfThePublic"
    POLICEMAN = "policeman"
    POLITICIAN = "politician"
    PUBLIC_TRANSPORT_PASSENGER = "publicTransportPassenger"
    SICK_PERSON = "sickPerson"
    TRAFFIC_OFFICER = "trafficOfficer"
    TRAFFIC_WARDEN = "trafficWarden"
    VERY_IMPORTANT_PERSON = "veryImportantPerson"
