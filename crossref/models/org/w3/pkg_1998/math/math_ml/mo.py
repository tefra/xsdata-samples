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


@dataclass(kw_only=True)
class Mo:
    class Meta:
        name = "mo"
        namespace = "http://www.w3.org/1998/Math/MathML"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    xref: None | object = field(
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
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other: None | object = field(
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
    mathcolor: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        },
    )
    mathbackground: None | str | MoValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        },
    )
    mathvariant: None | MoMathvariant = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    mathsize: None | str | MoValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    dir: None | MoDir = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    fontfamily: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    fontweight: None | MoFontweight = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    fontstyle: None | MoFontstyle = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    fontsize: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    color: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        },
    )
    background: None | str | MoValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        },
    )
    form: None | MoForm = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    fence: None | MoFence = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    separator: None | MoSeparator = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lspace: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    rspace: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    stretchy: None | MoStretchy = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    symmetric: None | MoSymmetric = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    maxsize: None | str | MoValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    minsize: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    largeop: None | MoLargeop = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    movablelimits: None | MoMovablelimits = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    accent: None | MoAccent = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    linebreak: None | MoLinebreak = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lineleading: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    linebreakstyle: None | MoLinebreakstyle = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    linebreakmultchar: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    indentalign: None | MoIndentalign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    indentshift: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    indenttarget: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    indentalignfirst: None | MoIndentalignfirst = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    indentshiftfirst: None | str | MoValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    indentalignlast: None | MoIndentalignlast = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    indentshiftlast: None | str | MoValue = field(
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
