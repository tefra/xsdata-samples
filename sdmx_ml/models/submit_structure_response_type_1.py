from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.submission_result_type import SubmissionResultType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


@dataclass(frozen=True, kw_only=True)
class SubmitStructureResponseType1:
    """
    SubmitStructureResponseType describes the structure of a response to a
    structure submission.

    For each submitted structure, a Result will be returned.

    :ivar submission_result: SubmissionResult provides a status for each
        submitted structural object.
    """

    class Meta:
        name = "SubmitStructureResponseType"

    submission_result: tuple[SubmissionResultType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SubmissionResult",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
            "min_occurs": 1,
        },
    )
