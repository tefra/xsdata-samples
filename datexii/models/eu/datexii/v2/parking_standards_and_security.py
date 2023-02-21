from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.labelsecurity_level_enum import LABELSecurityLevelEnum
from datexii.models.eu.datexii.v2.labelservice_level_enum import LABELServiceLevelEnum
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.parking_security_enum import ParkingSecurityEnum
from datexii.models.eu.datexii.v2.parking_supervision_enum import ParkingSupervisionEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingStandardsAndSecurity:
    """
    Security measures and standards or standard-like categorization for a parking
    site.

    :ivar label_security_level: Formal assessment for the security level
        defined by the LABEL project  http://truckparkinglabel.eu.
    :ivar label_service_level: Formal assessment for the service level
        defined by the LABEL project  http://truckparkinglabel.eu.
    :ivar label_security_level_self_assessment: Self-assessment for the
        security level defined by the LABEL project
        http://truckparkinglabel.eu.
    :ivar label_service_level_self_assessment: Self-assessment for the
        service level defined by the LABEL project
        http://truckparkinglabel.eu.
    :ivar parking_security: Specifies security measures related to the
        parking site or particular spaces.
    :ivar parking_additional_security: Security equipment of the parking
        site that is not covered by the enumeration
        'ParkingSecurityEnum'.
    :ivar parking_supervision: Defines the kind of supervision of the
        parking site.
    :ivar parking_security_national_classification: A national
        classification of the parking security.
    :ivar certified_secure_parking: Presence of a certification for
        secure parking.
    :ivar date_of_certification: Date of certification.
    :ivar parking_standards_and_security_extension:
    """
    label_security_level: Optional[LABELSecurityLevelEnum] = field(
        default=None,
        metadata={
            "name": "labelSecurityLevel",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    label_service_level: Optional[LABELServiceLevelEnum] = field(
        default=None,
        metadata={
            "name": "labelServiceLevel",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    label_security_level_self_assessment: Optional[LABELSecurityLevelEnum] = field(
        default=None,
        metadata={
            "name": "labelSecurityLevelSelfAssessment",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    label_service_level_self_assessment: Optional[LABELServiceLevelEnum] = field(
        default=None,
        metadata={
            "name": "labelServiceLevelSelfAssessment",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_security: List[ParkingSecurityEnum] = field(
        default_factory=list,
        metadata={
            "name": "parkingSecurity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_additional_security: List[MultilingualString] = field(
        default_factory=list,
        metadata={
            "name": "parkingAdditionalSecurity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_supervision: List[ParkingSupervisionEnum] = field(
        default_factory=list,
        metadata={
            "name": "parkingSupervision",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_security_national_classification: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "parkingSecurityNationalClassification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    certified_secure_parking: Optional[bool] = field(
        default=None,
        metadata={
            "name": "certifiedSecureParking",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    date_of_certification: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dateOfCertification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_standards_and_security_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingStandardsAndSecurityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
