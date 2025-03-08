from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from sabre.models.document_type_gender import DocumentTypeGender
from sabre.models.document_type_share_market_ind import (
    DocumentTypeShareMarketInd,
)
from sabre.models.document_type_share_synch_ind import (
    DocumentTypeShareSynchInd,
)

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class DocumentType:
    """
    Provides information on a specific documents.

    Attributes:
        doc_holder_name: Specify document holder name.
        doc_limitations: Used to indicate any limitations on the
            document (e.g. as a person may only be allowed to spend a
            max of 30 days in country on a visitor's visa).
        share_synch_ind:
        share_market_ind:
        doc_issue_authority: Indicates the group or association that
            granted the document.
        doc_issue_location: Indicates the location where the document
            was issued.
        doc_id: Unique number assigned by authorities to document.
        doc_type: Indicates the type of document (e.g. Passport,
            Military ID, Drivers License, national ID, Vaccination
            Certificate). Refer to OTA Code List Document Type (DOC).
        gender:
        birth_date: Indicates the date of birth as indicated in the
            document, in ISO 8601 prescribed format.
        effective_date: Indicates the starting date.
        expire_date: Indicates the ending date.
    """

    doc_holder_name: None | str = field(
        default=None,
        metadata={
            "name": "DocHolderName",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_length": 1,
            "max_length": 64,
        },
    )
    doc_limitations: list[str] = field(
        default_factory=list,
        metadata={
            "name": "DocLimitations",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 9,
            "min_length": 1,
            "max_length": 64,
        },
    )
    share_synch_ind: None | DocumentTypeShareSynchInd = field(
        default=None,
        metadata={
            "name": "ShareSynchInd",
            "type": "Attribute",
        },
    )
    share_market_ind: None | DocumentTypeShareMarketInd = field(
        default=None,
        metadata={
            "name": "ShareMarketInd",
            "type": "Attribute",
        },
    )
    doc_issue_authority: None | str = field(
        default=None,
        metadata={
            "name": "DocIssueAuthority",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 64,
        },
    )
    doc_issue_location: None | str = field(
        default=None,
        metadata={
            "name": "DocIssueLocation",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 64,
        },
    )
    doc_id: None | str = field(
        default=None,
        metadata={
            "name": "DocID",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        },
    )
    doc_type: None | str = field(
        default=None,
        metadata={
            "name": "DocType",
            "type": "Attribute",
        },
    )
    gender: None | DocumentTypeGender = field(
        default=None,
        metadata={
            "name": "Gender",
            "type": "Attribute",
        },
    )
    birth_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "BirthDate",
            "type": "Attribute",
        },
    )
    effective_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "EffectiveDate",
            "type": "Attribute",
        },
    )
    expire_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "ExpireDate",
            "type": "Attribute",
        },
    )
