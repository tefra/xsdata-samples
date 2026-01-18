from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.org.w3.pkg_1998.math.math_ml.malignmark import Malignmark
from crossref.models.org.w3.pkg_1998.math.math_ml.mglyph import Mglyph
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_accent import MoAccent
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_dir import MoDir
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_fence import MoFence
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_fontstyle import (
    MoFontstyle,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_fontweight import (
    MoFontweight,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_form import MoForm
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_indentalign import (
    MoIndentalign,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_indentalignfirst import (
    MoIndentalignfirst,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_indentalignlast import (
    MoIndentalignlast,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_largeop import MoLargeop
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_linebreak import (
    MoLinebreak,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_linebreakstyle import (
    MoLinebreakstyle,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_mathvariant import (
    MoMathvariant,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_movablelimits import (
    MoMovablelimits,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_separator import (
    MoSeparator,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_stretchy import MoStretchy
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_symmetric import (
    MoSymmetric,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_value import MoValue

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


@dataclass
class Mo:
    class Meta:
        name = "mo"
        namespace = "http://www.w3.org/1998/Math/MathML"

    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    xref: object | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: list[str] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Attribute",
            "tokens": True,
        },
    )
    style: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    href: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other: object | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
    mathcolor: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        },
    )
    mathbackground: str | MoValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        },
    )
    mathvariant: MoMathvariant | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    mathsize: str | MoValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    dir: MoDir | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    fontfamily: object | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    fontweight: MoFontweight | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    fontstyle: MoFontstyle | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    fontsize: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    color: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        },
    )
    background: str | MoValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        },
    )
    form: MoForm | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    fence: MoFence | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    separator: MoSeparator | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lspace: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    rspace: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    stretchy: MoStretchy | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    symmetric: MoSymmetric | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    maxsize: str | MoValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    minsize: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    largeop: MoLargeop | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    movablelimits: MoMovablelimits | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    accent: MoAccent | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    linebreak: MoLinebreak | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lineleading: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    linebreakstyle: MoLinebreakstyle | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    linebreakmultchar: object | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    indentalign: MoIndentalign | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    indentshift: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    indenttarget: object | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    indentalignfirst: MoIndentalignfirst | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    indentshiftfirst: str | MoValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    indentalignlast: MoIndentalignlast | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    indentshiftlast: str | MoValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "mglyph",
                    "type": Mglyph,
                },
                {
                    "name": "malignmark",
                    "type": Malignmark,
                },
            ),
        },
    )
