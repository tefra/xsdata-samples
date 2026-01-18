from __future__ import annotations

from dataclasses import dataclass

from .t_import import TImport

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class Import(TImport):
    class Meta:
        name = "import"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
