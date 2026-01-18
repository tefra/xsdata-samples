from __future__ import annotations

from dataclasses import dataclass

from .t_participant import TParticipant

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class Participant(TParticipant):
    class Meta:
        name = "participant"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
