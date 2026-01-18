from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ProofOfIdentityEnumeration(Enum):
    NONE_REQUIRED = "noneRequired"
    CREDIT_CARD = "creditCard"
    PASSPORT = "passport"
    DRIVING_LICENCE = "drivingLicence"
    BIRTH_CERTIFICATE = "birthCertificate"
    MEMBERSHIP_CARD = "membershipCard"
    IDENTITY_DOCUMENT = "identityDocument"
    MEDICAL_DOCUMENT = "medicalDocument"
    STUDENT_CARD = "studentCard"
    LETTER_WITH_ADDRESS = "letterWIthAddress"
    MOBILE_DEVICE = "mobileDevice"
    EMAIL_ACCOUNT = "emailAccount"
    MEASUREMENT = "measurement"
    OTHER = "other"
