from dataclasses import dataclass, field
from typing import List, Optional
from models.coreschemas.datatypes_base import (
    Ii,
)

__NAMESPACE__ = "urn:ihe:iti:xcpd:2009"


@dataclass
class CorrelationTimeToLive:
    """
    :ivar value:
    """
    class Meta:
        namespace = "urn:ihe:iti:xcpd:2009"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class PatientLocationQueryRequestType:
    """
    :ivar requested_patient_id: The Patient Identifier known by the responder
    """
    requested_patient_id: Optional[Ii] = field(
        default=None,
        metadata=dict(
            name="RequestedPatientId",
            type="Element",
            namespace="urn:ihe:iti:xcpd:2009",
            required=True
        )
    )


@dataclass
class PatientLocationQueryResponseType:
    """
    :ivar patient_location_response:
    """
    patient_location_response: List["PatientLocationQueryResponseType.PatientLocationResponse"] = field(
        default_factory=list,
        metadata=dict(
            name="PatientLocationResponse",
            type="Element",
            namespace="urn:ihe:iti:xcpd:2009",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )

    @dataclass
    class PatientLocationResponse:
        """
        :ivar home_community_id: This is the unique identifier of the community
        									that knows of the patient
        :ivar corresponding_patient_id: This is the patient identifier as known in the
        									community identified by homeCommunityId
        :ivar requested_patient_id: This is the patient identifier from the pation
        									location request
        """
        home_community_id: Optional[str] = field(
            default=None,
            metadata=dict(
                name="HomeCommunityId",
                type="Element",
                namespace="urn:ihe:iti:xcpd:2009",
                required=True
            )
        )
        corresponding_patient_id: Optional[Ii] = field(
            default=None,
            metadata=dict(
                name="CorrespondingPatientId",
                type="Element",
                namespace="urn:ihe:iti:xcpd:2009",
                required=True
            )
        )
        requested_patient_id: Optional[Ii] = field(
            default=None,
            metadata=dict(
                name="RequestedPatientId",
                type="Element",
                namespace="urn:ihe:iti:xcpd:2009",
                required=True
            )
        )


@dataclass
class PatientLocationQueryRequest(PatientLocationQueryRequestType):
    class Meta:
        namespace = "urn:ihe:iti:xcpd:2009"


@dataclass
class PatientLocationQueryResponse(PatientLocationQueryResponseType):
    class Meta:
        namespace = "urn:ihe:iti:xcpd:2009"
