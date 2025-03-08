from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.free_text_type import FreeTextType
from sabre.models.message_class_type import MessageClassType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class ErrorType(FreeTextType):
    """
    Standard way to indicate that an error occurred during the processing of an OTA
    message.

    Attributes:
        type_value: The Error element MUST contain the Type attribute
            that uses a recommended set of values to indicate the error
            type. The validating XSD can expect to accept values that it
            has NOT been explicitly coded for and process them by using
            Type ="Unknown".  Refer to OTA Code List Error Warning Type
            (EWT).
        short_text:
        code: If present, this refers to a table of coded values
            exchanged between applications to identify errors or
            warnings. Refer to OTA Code List Error Codes (ERR).
        doc_url: If present, this URL refers to an online description of
            the error that occurred.
        status: If present, recommended values are those enumerated in
            the OTA_ErrorRS, (NotProcessed | Incomplete | Complete |
            Unknown) however, the data type is designated as string
            data, recognizing that trading partners may identify
            additional status conditions not included in the
            enumeration.
        tag: If present, this attribute may identify an unknown or
            misspelled tag that caused an error in processing. It is
            recommended that the Tag attribute use XPath notation to
            identify the location of a tag in the event that more than
            one tag of the same name is present in the document.
            Alternatively, the tag name alone can be used to identify
            missing data [Type=ReqFieldMissing].
        record_id: If present, this attribute allows for batch
            processing and the identification of the record that failed
            amongst a group of records.
        message_class: If present specify the message class.
        node_list: An XPath expression that selects all the nodes whose
            data caused this error.  Further, this expression should
            have an   additional contraint which contains the data of
            the node.  This will provide the offending data back to
            systems that cannot maintain the original message.
    """

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
    short_text: None | str = field(
        default=None,
        metadata={
            "name": "ShortText",
            "type": "Attribute",
        },
    )
    code: None | str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        },
    )
    doc_url: None | str = field(
        default=None,
        metadata={
            "name": "DocURL",
            "type": "Attribute",
        },
    )
    status: None | str = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 64,
        },
    )
    tag: None | str = field(
        default=None,
        metadata={
            "name": "Tag",
            "type": "Attribute",
        },
    )
    record_id: None | str = field(
        default=None,
        metadata={
            "name": "RecordID",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        },
    )
    message_class: None | MessageClassType = field(
        default=None,
        metadata={
            "name": "MessageClass",
            "type": "Attribute",
        },
    )
    node_list: None | str = field(
        default=None,
        metadata={
            "name": "NodeList",
            "type": "Attribute",
        },
    )
