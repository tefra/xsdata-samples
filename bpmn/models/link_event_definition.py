from dataclasses import dataclass
from .t_link_event_definition import TLinkEventDefinition

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class LinkEventDefinition(TLinkEventDefinition):
    class Meta:
        name = "linkEventDefinition"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
