from __future__ import annotations

from dataclasses import dataclass

from npo.models.program_type import ProgramType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class Program(ProgramType):
    """
    This is the most used entity in POMS.

    It represents e.g. one broadcast program or one web-only clip. It
    represent a standalone entity which a consumer can view or listen to.
    """

    class Meta:
        name = "program"
        namespace = "urn:vpro:media:2009"
