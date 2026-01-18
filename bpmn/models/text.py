from __future__ import annotations

from dataclasses import dataclass

from .t_text import TText

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class Text(TText):
    class Meta:
        name = "text"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
