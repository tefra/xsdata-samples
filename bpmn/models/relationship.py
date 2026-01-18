from __future__ import annotations

from dataclasses import dataclass

from .t_relationship import TRelationship

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class Relationship(TRelationship):
    class Meta:
        name = "relationship"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
