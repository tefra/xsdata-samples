from dataclasses import dataclass, field
from typing import Optional, Union

from crossref.models.gov.nih.nlm.ncbi.jats1.back import Back
from crossref.models.gov.nih.nlm.ncbi.jats1.body import Body
from crossref.models.gov.nih.nlm.ncbi.jats1.floats_group import FloatsGroup
from crossref.models.gov.nih.nlm.ncbi.jats1.front import Front
from crossref.models.gov.nih.nlm.ncbi.jats1.front_stub import FrontStub
from crossref.models.gov.nih.nlm.ncbi.jats1.processing_meta import (
    ProcessingMeta,
)
from crossref.models.xml.lang_value import LangValue

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class Response:
    """
    <div> <h3>Response</h3> </div>.
    """

    class Meta:
        name = "response"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    processing_meta: ProcessingMeta | None = field(
        default=None,
        metadata={
            "name": "processing-meta",
            "type": "Element",
        },
    )
    front: Front | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    front_stub: FrontStub | None = field(
        default=None,
        metadata={
            "name": "front-stub",
            "type": "Element",
        },
    )
    body: Body | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    back: Back | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    floats_group: FloatsGroup | None = field(
        default=None,
        metadata={
            "name": "floats-group",
            "type": "Element",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    response_type: str | None = field(
        default=None,
        metadata={
            "name": "response-type",
            "type": "Attribute",
        },
    )
    specific_use: str | None = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: str | LangValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
