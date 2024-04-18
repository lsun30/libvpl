#!/usr/bin/env python3
############################################################################
# Copyright (C) Intel Corporation
#
# SPDX-License-Identifier: MIT
############################################################################
"""
Common configuration for building specification.
"""
# pylint: disable=invalid-name

# Derived from:
# github.com/oneapi-src/oneAPI-spec/blob/main/source/conf/common_conf.py

import string
import docutils

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.graphviz',
    'sphinxcontrib.spelling',
    'sphinxcontrib.inkscapeconverter',
    'sphinxmark',
    'sphinx-prompt',
    'sphinx_substitution_extensions',
    'sphinxcontrib.plantuml',
    'breathe',
]

env = {
    'vpl_spec_version': "2.11.0",
}

prolog_template = string.Template(r"""

.. |vpl_full_name| replace:: Intel\ :supsub:`reg` Video Processing Library
.. |vpl_short_name| replace:: Intel\ :supsub:`reg` VPL
.. |vpl_version| replace:: $vpl_spec_version
.. include:: <isonum.txt>
.. |regsup| replace:: :supsub:`reg`
.. |intel_r| replace:: Intel\ :supsub:`reg`
.. |msdk_full_name| replace:: Intel\ :supsub:`reg`""" +
                                  ' Media Software Development Kit')

rst_prolog = prolog_template.substitute(env)

# for substitutions in code blocks and sphinx-prompts:
substitutions = []

primary_domain = 'cpp'

latex_elements = {
    'preamble': r'''
\usepackage{makeidx}
\usepackage[columns=1]{idxlayout}
\makeindex
\DeclareUnicodeCharacter{2208}{$\in$}
\DeclareUnicodeCharacter{2212}{$-$}
\DeclareUnicodeCharacter{222A}{$\cup$}
\DeclareUnicodeCharacter{2236}{$\colon$}
\DeclareUnicodeCharacter{2260}{$\neq$}
\DeclareUnicodeCharacter{2264}{$\leq$}
\DeclareUnicodeCharacter{2265}{$\geq$}
\DeclareUnicodeCharacter{3B3}{$\gamma$}
\DeclareUnicodeCharacter{39B}{$\Lambda$}
\DeclareUnicodeCharacter{3A3}{$\Sigma$}
\DeclareUnicodeCharacter{3A6}{$\phi$}
\DeclareUnicodeCharacter{3B1}{$\alpha$}
\DeclareUnicodeCharacter{3B2}{$\beta$}
\DeclareUnicodeCharacter{3B4}{$\delta$}
\DeclareUnicodeCharacter{3BB}{$\lambda$}
\DeclareUnicodeCharacter{3BC}{$\mu$}
\DeclareUnicodeCharacter{3BD}{$\nu$}
\DeclareUnicodeCharacter{3C0}{$\pi$}
\DeclareUnicodeCharacter{3C3}{$\sigma$}
\DeclareUnicodeCharacter{FB01}{$fi$}
\DeclareUnicodeCharacter{FB02}{$fl$}
\newcommand{\src}{\operatorname{src}}
\newcommand{\srclayer}{\operatorname{src\_layer}}
\newcommand{\srciter}{\operatorname{src\_iter}}
\newcommand{\srciterc}{\operatorname{src\_iter\_c}}
\newcommand{\weights}{\operatorname{weights}}
\newcommand{\weightslayer}{\operatorname{weights\_layer}}
\newcommand{\weightsiter}{\operatorname{weights\_iter}}
\newcommand{\weightspeephole}{\operatorname{weights\_peephole}}
\newcommand{\weightsprojection}{\operatorname{weights\_projection}}
\newcommand{\bias}{\operatorname{bias}}
\newcommand{\dst}{\operatorname{dst}}
\newcommand{\dstlayer}{\operatorname{dst\_layer}}
\newcommand{\dstiter}{\operatorname{dst\_iter}}
\newcommand{\dstiterc}{\operatorname{dst\_iter\_c}}
\newcommand{\diffsrc}{\operatorname{diff\_src}}
\newcommand{\diffsrclayer}{\operatorname{diff\_src\_layer}}
\newcommand{\diffsrciter}{\operatorname{diff\_src\_iter}}
\newcommand{\diffsrciterc}{\operatorname{diff\_src\_iter\_c}}
\newcommand{\diffweights}{\operatorname{diff\_weights}}
\newcommand{\diffweightslayer}{\operatorname{diff\_weights\_layer}}
\newcommand{\diffweightsiter}{\operatorname{diff\_weights\_iter}}
\newcommand{\diffweightspeephole}{\operatorname{diff\_weights\_peephole}}
\newcommand{\diffweightsprojection}{\operatorname{diff\_weights\_projection}}
\newcommand{\diffbias}{\operatorname{diff\_bias}}
\newcommand{\diffdst}{\operatorname{diff\_dst}}
\newcommand{\diffdstlayer}{\operatorname{diff\_dst\_layer}}
\newcommand{\diffdstiter}{\operatorname{diff\_dst\_iter}}
\newcommand{\diffdstiterc}{\operatorname{diff\_dst\_iter\_c}}
\newcommand{\diffgamma}{\operatorname{diff\_\gamma}}
\newcommand{\diffbeta}{\operatorname{diff\_\beta}}
\newcommand{\workspace}{\operatorname{workspace}}
\newcommand{\srcshape}{\operatorname{src\_shape}}
''',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
    'extraclassoptions': 'openany,oneside',
}

imgmath_latex_preamble = r'''
\newcommand{\src}{\operatorname{src}}
\newcommand{\srclayer}{\operatorname{src\_layer}}
\newcommand{\srciter}{\operatorname{src\_iter}}
\newcommand{\srciterc}{\operatorname{src\_iter\_c}}
\newcommand{\weights}{\operatorname{weights}}
\newcommand{\weightslayer}{\operatorname{weights\_layer}}
\newcommand{\weightsiter}{\operatorname{weights\_iter}}
\newcommand{\weightspeephole}{\operatorname{weights\_peephole}}
\newcommand{\weightsprojection}{\operatorname{weights\_projection}}
\newcommand{\bias}{\operatorname{bias}}
\newcommand{\dst}{\operatorname{dst}}
\newcommand{\dstlayer}{\operatorname{dst\_layer}}
\newcommand{\dstiter}{\operatorname{dst\_iter}}
\newcommand{\dstiterc}{\operatorname{dst\_iter\_c}}
\newcommand{\diffsrc}{\operatorname{diff\_src}}
\newcommand{\diffsrclayer}{\operatorname{diff\_src\_layer}}
\newcommand{\diffsrciter}{\operatorname{diff\_src\_iter}}
\newcommand{\diffsrciterc}{\operatorname{diff\_src\_iter\_c}}
\newcommand{\diffweights}{\operatorname{diff\_weights}}
\newcommand{\diffweightslayer}{\operatorname{diff\_weights\_layer}}
\newcommand{\diffweightsiter}{\operatorname{diff\_weights\_iter}}
\newcommand{\diffweightspeephole}{\operatorname{diff\_weights\_peephole}}
\newcommand{\diffweightsprojection}{\operatorname{diff\_weights\_projection}}
\newcommand{\diffbias}{\operatorname{diff\_bias}}
\newcommand{\diffdst}{\operatorname{diff\_dst}}
\newcommand{\diffdstlayer}{\operatorname{diff\_dst\_layer}}
\newcommand{\diffdstiter}{\operatorname{diff\_dst\_iter}}
\newcommand{\diffdstiterc}{\operatorname{diff\_dst\_iter\_c}}
\newcommand{\diffgamma}{\operatorname{diff\_\gamma}}
\newcommand{\diffbeta}{\operatorname{diff\_\beta}}
\newcommand{\workspace}{\operatorname{workspace}}
\newcommand{\srcshape}{\operatorname{src\_shape}}
'''

mathjax3_config = {
    'tex': {
        'macros': {
            'src': '\\operatorname{src}',
            'srclayer': '\\operatorname{src\\_layer}',
            'srciter': '\\operatorname{src\\_iter}',
            'srciterc': '\\operatorname{src\\_iter\\_c}',
            'weights': '\\operatorname{weights}',
            'weightslayer': '\\operatorname{weights\\_layer}',
            'weightsiter': '\\operatorname{weights\\_iter}',
            'weightspeephole': '\\operatorname{weights\\_peephole}',
            'weightsprojection': '\\operatorname{weights\\_projection}',
            'bias': '\\operatorname{bias}',
            'dst': '\\operatorname{dst}',
            'dstlayer': '\\operatorname{dst\\_layer}',
            'dstiter': '\\operatorname{dst\\_iter}',
            'dstiterc': '\\operatorname{dst\\_iter\\_c}',
            'diffsrc': '\\operatorname{diff\\_src}',
            'diffsrclayer': '\\operatorname{diff\\_src\\_layer}',
            'diffsrciter': '\\operatorname{diff\\_src\\_iter}',
            'diffsrciterc': '\\operatorname{diff\\_src\\_iter\\_c}',
            'diffweights': '\\operatorname{diff\\_weights}',
            'diffweightslayer': '\\operatorname{diff\\_weights\\_layer}',
            'diffweightsiter': '\\operatorname{diff\\_weights\\_iter}',
            'diffweightspeephole': '\\operatorname{diff\\_weights\\_peephole}',
            'diffweightsprojection':
            '\\operatorname{diff\\_weights\\_projection}',  # noqa: E501
            'diffbias': '\\operatorname{diff\\_bias}',
            'diffdst': '\\operatorname{diff\\_dst}',
            'diffdstlayer': '\\operatorname{diff\\_dst\\_layer}',
            'diffdstiter': '\\operatorname{diff\\_dst\\_iter}',
            'diffdstiterc': '\\operatorname{diff\\_dst\\_iter\\_c}',
            'diffgamma': '\\operatorname{diff\\_\\gamma}',
            'diffbeta': '\\operatorname{diff\\_\\beta}',
            'workspace': '\\operatorname{workspace}',
            'srcshape': '\\operatorname{src\\_shape}',
        }
    }
}


def supsub_role(_name,
                _rawtext,
                text,
                _lineno,
                _inliner,
                _options=None,
                _content=None):
    """Superscript substitution"""
    node = docutils.nodes.superscript()
    node2 = docutils.nodes.substitution_reference(refname=text)
    node += [node2]
    return [node], []


def setup(app):
    """Setup"""
    app.add_role('supsub', supsub_role)
    app.add_css_file('custom.css')
