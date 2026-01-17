from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.area_of_interest_enum import (
    AreaOfInterestEnum,
)
from datexii.models.eu.datexii.v2.confidentiality_value_enum import (
    ConfidentialityValueEnum,
)
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.information_status_enum import (
    InformationStatusEnum,
)
from datexii.models.eu.datexii.v2.urgency_enum import UrgencyEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class HeaderInformation:
    """
    Management information relating to the data contained within a
    publication.

    :ivar area_of_interest: The extent of the geographic area to which
        the related information should be distributed.
    :ivar confidentiality: The extent to which the related information
        may be circulated, according to the recipient type. Recipients
        must comply with this confidentiality statement.
    :ivar information_status: The status of the related information
        (real, test, exercise ....).
    :ivar urgency: This indicates the urgency with which a message
        recipient or Client should distribute the enclosed information.
        Urgency particularly relates to functions within RDS-TMC
        applications.
    :ivar header_information_extension:
    """

    area_of_interest: Optional[AreaOfInterestEnum] = field(
        default=None,
        metadata={
            "name": "areaOfInterest",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    confidentiality: Optional[ConfidentialityValueEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    information_status: Optional[InformationStatusEnum] = field(
        default=None,
        metadata={
            "name": "informationStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    urgency: Optional[UrgencyEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    header_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "headerInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
