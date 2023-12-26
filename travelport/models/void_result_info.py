from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.void_result_info_document_type import (
    VoidResultInfoDocumentType,
)

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class VoidResultInfo:
    """
    List of Successful Or Failed void document results.

    Parameters
    ----------
    failure_remark
        Container to show all provider failure information.
    document_number
        Identifies the document number to be voided.
    document_type
        Identifies the document type to be voided, Document Type can have
        four values like Service Fee, Paper Ticket , MCO and E-Ticket.
    result_type
        Successful Or Failed result indicator.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    failure_remark: None | str = field(
        default=None,
        metadata={
            "name": "FailureRemark",
            "type": "Element",
        },
    )
    document_number: None | str = field(
        default=None,
        metadata={
            "name": "DocumentNumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 13,
        },
    )
    document_type: None | VoidResultInfoDocumentType = field(
        default=None,
        metadata={
            "name": "DocumentType",
            "type": "Attribute",
        },
    )
    result_type: None | str = field(
        default=None,
        metadata={
            "name": "ResultType",
            "type": "Attribute",
        },
    )
