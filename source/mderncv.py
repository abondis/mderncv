"""
Pandoc filter using panflute to create a cv using moderncv LaTeX package
from markdown.

Usage: pandoc  cv_panflute.md -s -o cv_panflute.tex --filter mderncv/source/mderncv.py
"""

import sys
import panflute as pf


class CV:
    nb_par = 0
    _type = None

    def __init__(self, content):
        self.content = content

    def to_tex(self):
        # generate cventry arguments based on  number of elements
        nb_elt = len(self.content)
        skip = 0
        start = ""
        if not isinstance(self.content[0], pf.Emph):
            start = "{{}}"
            skip = 1
        start = start + "{{{}}}" * (nb_elt - skip)
        end = "{{}}" * (self.nb_par - nb_elt - skip)
        entry = f"\\{self._type}{start}{end}"
        result = entry.format(*map(pf.stringify, self.content))
        if "&" in result:
            result = result.replace("&", "\\&")
        return result


class CVEntry(CV):
    def __init__(self, content):
        self._type = "cventry"
        self.nb_par = 6
        super().__init__(content)
        self.content = [x for x in content.list if not isinstance(x, pf.Space)]


class CVItem(CV):
    def __init__(self, content):
        self._type = "cvitem"
        self.nb_par = 3
        plain = content.list[0]


def personal_data_to_tex(doc: pf.Doc):
    c = []
    c.append(
        pf.RawBlock(
            "\\lastname {{{}}}".format(doc.get_metadata("lastname")),
            format="latex",
        )
    )
    c.append(
        pf.RawBlock(
            "\\firstname {{{}}}".format(doc.get_metadata("firstname")),
            format="latex",
        )
    )
    c.append(
        pf.RawBlock(
            "\\name {{{}}}{{{}}}".format(
                doc.get_metadata("firstname"), doc.get_metadata("lastname")
            ),
            format="latex",
        )
    )
    c.append(
        pf.RawBlock(
            "\\name {{{}}}{{{}}}".format(
                doc.get_metadata("firstname"), doc.get_metadata("lastname")
            ),
            format="latex",
        )
    )
    if doc.get_metadata("title") is not None:
        c.append(
            pf.RawBlock("\\title{{{}}}".format(doc.get_metadata("title")), "latex")
        )
    if doc.get_metadata("photo") is not None:
        c.append(
            pf.RawBlock(
                "\\photo[80pt][0pt]{{{}}}".format(doc.get_metadata("photo")), "latex"
            )
        )
    if doc.get_metadata("email") is not None:
        c.append(
            pf.RawBlock("\\email{{{}}}".format(doc.get_metadata("email")), "latex")
        )
    if doc.get_metadata("homepage") is not None:
        c.append(
            pf.RawBlock(
                "\\homepage{{{}}}".format(doc.get_metadata("homepage")), "latex"
            )
        )
    if doc.get_metadata("linkedin") is not None:
        c.append(
            pf.RawBlock(
                "\\social[linkedin]{{{}}}".format(doc.get_metadata("linkedin")), "latex"
            )
        )
    if doc.get_metadata("github") is not None:
        c.append(
            pf.RawBlock(
                "\\social[github]{{{}}}".format(doc.get_metadata("github")), "latex"
            )
        )
    if doc.get_metadata("gitlab") is not None:
        c.append(
            pf.RawBlock(
                "\\social[gitlab]{{{}}}".format(doc.get_metadata("gitlab")), "latex"
            )
        )
    return c


def prepare(doc):
    pass


def action(elem: pf.Element, doc: pf.Doc):
    if isinstance(elem, pf.MetaInlines) and hasattr( elem.content[0], 'text') and elem.content[0].text == "$perso":
        pf.debug(elem.parent)
        c = personal_data_to_tex(elem.doc)
        return pf.MetaBlocks(*c)
    if isinstance(elem, pf.Math) and doc.format == "latex":
        return pf.RawInline(f"\\({elem.text}\\)", "markdown")
    if isinstance(elem, pf.Header) and doc.format == "latex":
        if elem.level >= 2:
            demo = CVEntry(elem.content).to_tex()
            block = pf.RawBlock(demo, format="latex")
            return block
    elif isinstance(elem, pf.BulletList) and doc.format == "latex":
        div = pf.Div()
        pf.debug(elem)
        for item in elem.content.list:
            plain = item.content.list[0]
            key = ""
            if isinstance(plain.content[0], pf.Emph):
                key = pf.stringify(plain.content.pop(0))
            cv_line_tex = "\cvitem{%s}{$\circ$ %s}{}" % (
                key,
                pf.stringify(plain),
            )
            if "&" in cv_line_tex:
                cv_line_tex = cv_line_tex.replace("&", "\&")
            raw_inline = pf.RawInline(cv_line_tex, format="latex")
            all_list = [pf.Plain(raw_inline)]
            # for sub in elem.content.list[1:]:
            #     cv_line_tex = "\cvitem{}{\hspace{\parindent} - %s}{}" % (
            #         pf.stringify(sub.content.list[0]),
            #     )
            #     all_list.append(pf.RawBlock(cv_line_tex, "latex"))
            #     # pf.debug(all_list)
                
            div.content.extend(all_list)
        return div


def finalize(doc):
    pass


def main(doc=None):
    return pf.run_filter(action, prepare=prepare, finalize=finalize, doc=doc)


if __name__ == "__main__":
    pf.toJSONFilter(action, prepare=prepare, finalize=finalize)
