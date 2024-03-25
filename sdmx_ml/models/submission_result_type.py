from dataclasses import dataclass, field
from typing import Optional

from sdmx_ml.models.status_message_type_2 import StatusMessageType2
from sdmx_ml.models.submitted_structure_type import SubmittedStructureType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


@dataclass(frozen=True)
class SubmissionResultType:
    """SubmissionResultType provides the status of the structural object submission
    request.

    It will identify the object submitted, report back the action
    requested, and convey the status and any error messages which are
    relevant to the submission.

    :ivar submitted_structure: SubmittedStructure provides a reference
        to the submitted structural object and echoes back the action
        requested for it.
    :ivar status_message: StatusMessage provides that status for the
        submission of the structural object, and if necessary, any error
        or warning information.
    """

    submitted_structure: Optional[SubmittedStructureType] = field(
        default=None,
        metadata={
            "name": "SubmittedStructure",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
            "required": True,
        },
    )
    status_message: Optional[StatusMessageType2] = field(
        default=None,
        metadata={
            "name": "StatusMessage",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
            "required": True,
        },
    )
