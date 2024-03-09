from __future__ import annotations

from dataclasses import dataclass

from npo.models.subtitles_form_type import SubtitlesFormType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class SubtitlesForm(SubtitlesFormType):
    class Meta:
        name = "subtitlesForm"
        namespace = "urn:vpro:api:2013"
