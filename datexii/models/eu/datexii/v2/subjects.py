from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.subject_type_of_works_enum import SubjectTypeOfWorksEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Subjects:
    """
    The subjects with which the roadworks are associated.

    :ivar subject_type_of_works: The subject type of the roadworks (i.e.
        on what the construction or maintenance work is being
        performed).
    :ivar number_of_subjects: The number of subjects on which the
        roadworks (construction or maintenance) are being performed.
    :ivar subjects_extension:
    """
    subject_type_of_works: Optional[SubjectTypeOfWorksEnum] = field(
        default=None,
        metadata={
            "name": "subjectTypeOfWorks",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    number_of_subjects: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfSubjects",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    subjects_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "subjectsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
