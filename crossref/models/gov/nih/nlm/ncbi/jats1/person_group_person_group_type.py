from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


class PersonGroupPersonGroupType(StrEnum):
    ALLAUTHORS = "allauthors"
    ASSIGNEE = "assignee"
    AUTHOR = "author"
    COMPILER = "compiler"
    CURATOR = "curator"
    CUSTOM = "custom"
    DIRECTOR = "director"
    EDITOR = "editor"
    GUEST_EDITOR = "guest-editor"
    ILLUSTRATOR = "illustrator"
    INVENTOR = "inventor"
    RESEARCH_ASSISTANT = "research-assistant"
    TRANSED = "transed"
    TRANSLATOR = "translator"
