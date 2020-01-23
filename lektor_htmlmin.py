# -*- coding: utf-8 -*-
import os
import codecs
import chardet
import sys


import htmlmin
from lektor.pluginsystem import Plugin
from lektor.reporter import reporter


class HTMLMinPlugin(Plugin):
    name = u'Lektor HTMLmin'
    description = u'HTML minifier for Lektor. Based on htmlmin.'

    def __init__(self, *args, **kwargs):
        Plugin.__init__(self, *args, **kwargs)
        self.options = {
            'remove_empty_space': True,
            'remove_all_empty_space': True,
            'reduce_empty_attributes': True,
            'reduce_boolean_attributes': False,
            'remove_optional_attribute_quotes': False,
            'keep_pre': False,
            'pre_attr': 'pre',
            'remove_comments': True
        }

    def is_enabled(self, build_flags):
        return bool(build_flags.get('htmlmin'))

    def find_html_files(self, destination):
        """
        Finds all html files in the given destination.
        """
        for root, dirs, files in os.walk(destination):
            for f in files:
                if f.endswith('.html'):
                    yield os.path.join(root, f)

    def minify_file(self, target):
        """
        Minifies the target html file.
        """
        html = open(target, 'rb')
        enc = chardet.detect(html.read())['encoding']
        html.close()
        with codecs.open(target, 'r+', enc) as f:
            result = htmlmin.minify(f.read(), **self.options)
            f.seek(0)
            f.write(result)
            f.truncate()

    def on_after_build_all(self, builder, **extra):
        """
        after-build-all lektor event
        """
        # NOTE(vesuvium): compatibility for lektor 2.X and 3.X
        try:
            is_enabled = self.is_enabled(builder.build_flags)
        except AttributeError:
            is_enabled = self.is_enabled(builder.extra_flags)

        if not is_enabled:
            return

        reporter.report_generic('HTML minification started')
        for htmlfile in self.find_html_files(builder.destination_path):
            self.minify_file(htmlfile)
        reporter.report_generic('HTML minification finished')
