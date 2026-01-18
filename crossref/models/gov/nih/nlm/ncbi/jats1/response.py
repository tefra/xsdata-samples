from __future__ import annotations

from dataclasses import dataclass, field

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

    processing_meta: None | ProcessingMeta = field(
        default=None,
        metadata={
            "name": "processing-meta",
            "type": "Element",
        },
    )
    front: None | Front = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    front_stub: None | FrontStub = field(
        default=None,
        metadata={
            "name": "front-stub",
            "type": "Element",
        },
    )
    body: None | Body = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    back: None | Back = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    floats_group: None | FloatsGroup = field(
        default=None,
        metadata={
            "name": "floats-group",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    response_type: None | str = field(
        default=None,
        metadata={
            "name": "response-type",
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
