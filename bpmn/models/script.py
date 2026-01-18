from __future__ import annotations

from dataclasses import dataclass

from .t_script import TScript

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class Script(TScript):
    class Meta:
        name = "script"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
