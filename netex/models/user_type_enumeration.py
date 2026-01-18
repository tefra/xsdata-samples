from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class UserTypeEnumeration(Enum):
    ADULT = "adult"
    CHILD = "child"
    INFANT = "infant"
    SENIOR = "senior"
    STUDENT = "student"
    YOUNG_PERSON = "youngPerson"
    SCHOOL_PUPIL = "schoolPupil"
    MILITARY = "military"
    DISABLED = "disabled"
    DISABLED_COMPANION = "disabledCompanion"
    JOB_SEEKER = "jobSeeker"
    EMPLOYEE = "employee"
    ANIMAL = "animal"
    GUIDE_DOG = "guideDog"
    MEMBER = "member"
    OTHER = "other"
    ANYONE = "anyone"
