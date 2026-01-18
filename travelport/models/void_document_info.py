from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.void_document_info_document_type import (
    VoidDocumentInfoDocumentType,
)

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class VoidDocumentInfo:
    """
    Container to represent document information.

    Parameters
    ----------
    document_number
        Identifies the document number to be voided.
    document_type
        Identifies the document type to be voided, Document Type can have
        four values like Service Fee, Paper Ticket , MCO and E-Ticket.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    document_number: None | str = field(
        default=None,
        metadata={
            "name": "DocumentNumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 13,
        },
    )
    document_type: None | VoidDocumentInfoDocumentType = field(
        default=None,
        metadata={
            "name": "DocumentType",
            "type": "Attribute",
        },
    )
