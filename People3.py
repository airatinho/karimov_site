#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Thu Jan 14 11:24:47 2021 by generateDS.py version 2.37.12.
# Python 3.8.5 (default, Sep  3 2020, 21:29:08) [MSC v.1916 64 bit (AMD64)]
#
# Command line options:
#   ('--subclass-suffix', '_Action')
#   ('--export', 'django')
#   ('-o', 'People3.py')
#
# Command line arguments:
#   People.xsd
#
# Command line:
#   generateDS.py --subclass-suffix="_Action" --export="django" -o "People3.py" People.xsd
#
# Current working directory (os.getcwd()):
#   pythonProject
#

import sys
try:
    ModulenotfoundExp_ = ModuleNotFoundError
except NameError:
    ModulenotfoundExp_ = ImportError
from six.moves import zip_longest
import os
import re as re_
import base64
# imports for django and/or sqlalchemy
import json as json_
try:
    import models as models_
except ModulenotfoundExp_ :
    models_ = None
import datetime as datetime_
import decimal as decimal_
try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


Validate_simpletypes_ = True
SaveElementTreeNode = True
if sys.version_info.major == 2:
    BaseStrType_ = basestring
else:
    BaseStrType_ = str


def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Namespace prefix definition table (and other attributes, too)
#
# The module generatedsnamespaces, if it is importable, must contain
# a dictionary named GeneratedsNamespaceDefs.  This Python dictionary
# should map element type names (strings) to XML schema namespace prefix
# definitions.  The export method for any class for which there is
# a namespace prefix definition, will export that definition in the
# XML representation of that element.  See the export method of
# any generated element type class for an example of the use of this
# table.
# A sample table is:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceDefs = {
#         "ElementtypeA": "http://www.xxx.com/namespaceA",
#         "ElementtypeB": "http://www.xxx.com/namespaceB",
#     }
#
# Additionally, the generatedsnamespaces module can contain a python
# dictionary named GenerateDSNamespaceTypePrefixes that associates element
# types with the namespace prefixes that are to be added to the
# "xsi:type" attribute value.  See the exportAttributes method of
# any generated element type and the generation of "xsi:type" for an
# example of the use of this table.
# An example table:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceTypePrefixes = {
#         "ElementtypeC": "aaa:",
#         "ElementtypeD": "bbb:",
#     }
#

try:
    from generatedsnamespaces import GenerateDSNamespaceDefs as GenerateDSNamespaceDefs_
except ModulenotfoundExp_ :
    GenerateDSNamespaceDefs_ = {}
try:
    from generatedsnamespaces import GenerateDSNamespaceTypePrefixes as GenerateDSNamespaceTypePrefixes_
except ModulenotfoundExp_ :
    GenerateDSNamespaceTypePrefixes_ = {}

#
# You can replace the following class definition by defining an
# importable module named "generatedscollector" containing a class
# named "GdsCollector".  See the default class definition below for
# clues about the possible content of that class.
#
try:
    from generatedscollector import GdsCollector as GdsCollector_
except ModulenotfoundExp_ :

    class GdsCollector_(object):

        def __init__(self, messages=None):
            if messages is None:
                self.messages = []
            else:
                self.messages = messages

        def add_message(self, msg):
            self.messages.append(msg)

        def get_messages(self):
            return self.messages

        def clear_messages(self):
            self.messages = []

        def print_messages(self):
            for msg in self.messages:
                print("Warning: {}".format(msg))

        def write_messages(self, outstream):
            for msg in self.messages:
                outstream.write("Warning: {}\n".format(msg))


#
# The super-class for enum types
#

try:
    from enum import Enum
except ModulenotfoundExp_ :
    Enum = object

#
# The root super-class for element type classes
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ModulenotfoundExp_ as exp:
    
    class GeneratedsSuper(object):
        __hash__ = object.__hash__
        tzoff_pattern = re_.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')
        class _FixedOffsetTZ(datetime_.tzinfo):
            def __init__(self, offset, name):
                self.__offset = datetime_.timedelta(minutes=offset)
                self.__name = name
            def utcoffset(self, dt):
                return self.__offset
            def tzname(self, dt):
                return self.__name
            def dst(self, dt):
                return None
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_parse_string(self, input_data, node=None, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node=None, input_name=''):
            if not input_data:
                return ''
            else:
                return input_data
        def gds_format_base64(self, input_data, input_name=''):
            return base64.b64encode(input_data)
        def gds_validate_base64(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % input_data
        def gds_parse_integer(self, input_data, node=None, input_name=''):
            try:
                ival = int(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires integer value: %s' % exp)
            return ival
        def gds_validate_integer(self, input_data, node=None, input_name=''):
            try:
                value = int(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires integer value')
            return value
        def gds_format_integer_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_integer_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    int(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of integer values')
            return values
        def gds_format_float(self, input_data, input_name=''):
            return ('%.15f' % input_data).rstrip('0')
        def gds_parse_float(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires float or double value: %s' % exp)
            return fval_
        def gds_validate_float(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires float value')
            return value
        def gds_format_float_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_float_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of float values')
            return values
        def gds_format_decimal(self, input_data, input_name=''):
            return_value = '%s' % input_data
            if '.' in return_value:
                return_value = return_value.rstrip('0')
                if return_value.endswith('.'):
                    return_value = return_value.rstrip('.')
            return return_value
        def gds_parse_decimal(self, input_data, node=None, input_name=''):
            try:
                decimal_value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return decimal_value
        def gds_validate_decimal(self, input_data, node=None, input_name=''):
            try:
                value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return value
        def gds_format_decimal_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return ' '.join([self.gds_format_decimal(item) for item in input_data])
        def gds_validate_decimal_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    decimal_.Decimal(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of decimal values')
            return values
        def gds_format_double(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_parse_double(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires double or float value: %s' % exp)
            return fval_
        def gds_validate_double(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires double or float value')
            return value
        def gds_format_double_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_double_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(
                        node, 'Requires sequence of double or float values')
            return values
        def gds_format_boolean(self, input_data, input_name=''):
            return ('%s' % input_data).lower()
        def gds_parse_boolean(self, input_data, node=None, input_name=''):
            if input_data in ('true', '1'):
                bval = True
            elif input_data in ('false', '0'):
                bval = False
            else:
                raise_parse_error(node, 'Requires boolean value')
            return bval
        def gds_validate_boolean(self, input_data, node=None, input_name=''):
            if input_data not in (True, 1, False, 0, ):
                raise_parse_error(
                    node,
                    'Requires boolean value '
                    '(one of True, 1, False, 0)')
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_boolean_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                if value not in (True, 1, False, 0, ):
                    raise_parse_error(
                        node,
                        'Requires sequence of boolean values '
                        '(one of True, 1, False, 0)')
            return values
        def gds_validate_datetime(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_datetime(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d.%s' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        @classmethod
        def gds_parse_datetime(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            time_parts = input_data.split('.')
            if len(time_parts) > 1:
                micro_seconds = int(float('0.' + time_parts[1]) * 1000000)
                input_data = '%s.%s' % (
                    time_parts[0], "{}".format(micro_seconds).rjust(6, "0"), )
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt
        def gds_validate_date(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_date(self, input_data, input_name=''):
            _svalue = '%04d-%02d-%02d' % (
                input_data.year,
                input_data.month,
                input_data.day,
            )
            try:
                if input_data.tzinfo is not None:
                    tzoff = input_data.tzinfo.utcoffset(input_data)
                    if tzoff is not None:
                        total_seconds = tzoff.seconds + (86400 * tzoff.days)
                        if total_seconds == 0:
                            _svalue += 'Z'
                        else:
                            if total_seconds < 0:
                                _svalue += '-'
                                total_seconds *= -1
                            else:
                                _svalue += '+'
                            hours = total_seconds // 3600
                            minutes = (total_seconds - (hours * 3600)) // 60
                            _svalue += '{0:02d}:{1:02d}'.format(
                                hours, minutes)
            except AttributeError:
                pass
            return _svalue
        @classmethod
        def gds_parse_date(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            dt = datetime_.datetime.strptime(input_data, '%Y-%m-%d')
            dt = dt.replace(tzinfo=tz)
            return dt.date()
        def gds_validate_time(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_time(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%02d:%02d:%02d' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%02d:%02d:%02d.%s' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        def gds_validate_simple_patterns(self, patterns, target):
            # pat is a list of lists of strings/patterns.
            # The target value must match at least one of the patterns
            # in order for the test to succeed.
            found1 = True
            for patterns1 in patterns:
                found2 = False
                for patterns2 in patterns1:
                    mo = re_.search(patterns2, target)
                    if mo is not None and len(mo.group(0)) == len(target):
                        found2 = True
                        break
                if not found2:
                    found1 = False
                    break
            return found1
        @classmethod
        def gds_parse_time(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            if len(input_data.split('.')) > 1:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt.time()
        def gds_check_cardinality_(
                self, value, input_name,
                min_occurs=0, max_occurs=1, required=None):
            if value is None:
                length = 0
            elif isinstance(value, list):
                length = len(value)
            else:
                length = 1
            if required is not None :
                if required and length < 1:
                    self.gds_collector_.add_message(
                        "Required value {}{} is missing".format(
                            input_name, self.gds_get_node_lineno_()))
            if length < min_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is below "
                    "the minimum allowed, "
                    "expected at least {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        min_occurs, length))
            elif length > max_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is above "
                    "the maximum allowed, "
                    "expected at most {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        max_occurs, length))
        def gds_validate_builtin_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value, input_name=input_name)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_validate_defined_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            # provide default value in case option --disable-xml is used.
            content = ""
            content = etree_.tostring(node, encoding="unicode")
            return content
        @classmethod
        def gds_reverse_node_mapping(cls, mapping):
            return dict(((v, k) for k, v in mapping.items()))
        @staticmethod
        def gds_encode(instring):
            if sys.version_info.major == 2:
                if ExternalEncoding:
                    encoding = ExternalEncoding
                else:
                    encoding = 'utf-8'
                return instring.encode(encoding)
            else:
                return instring
        @staticmethod
        def convert_unicode(instring):
            if isinstance(instring, str):
                result = quote_xml(instring)
            elif sys.version_info.major == 2 and isinstance(instring, unicode):
                result = quote_xml(instring).encode('utf8')
            else:
                result = GeneratedsSuper.gds_encode(str(instring))
            return result
        def __eq__(self, other):
            def excl_select_objs_(obj):
                return (obj[0] != 'parent_object_' and
                        obj[0] != 'gds_collector_')
            if type(self) != type(other):
                return False
            return all(x == y for x, y in zip_longest(
                filter(excl_select_objs_, self.__dict__.items()),
                filter(excl_select_objs_, other.__dict__.items())))
        def __ne__(self, other):
            return not self.__eq__(other)
        # Django ETL transform hooks.
        def gds_djo_etl_transform(self):
            pass
        def gds_djo_etl_transform_db_obj(self, dbobj):
            pass
        # SQLAlchemy ETL transform hooks.
        def gds_sqa_etl_transform(self):
            return 0, None
        def gds_sqa_etl_transform_db_obj(self, dbobj):
            pass
        def gds_get_node_lineno_(self):
            if (hasattr(self, "gds_elementtree_node_") and
                    self.gds_elementtree_node_ is not None):
                return ' near line {}'.format(
                    self.gds_elementtree_node_.sourceline)
            else:
                return ""
    
    
    def getSubclassFromModule_(module, class_):
        '''Get the subclass of a class from a specific module.'''
        name = class_.__name__ + '_Action'
        if hasattr(module, name):
            return getattr(module, name)
        else:
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = ''
# Set this to false in order to deactivate during export, the use of
# name space prefixes captured from the input document.
UseCapturedNS_ = True
CapturedNsmap_ = {}
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')
CDATA_pattern_ = re_.compile(r"<!\[CDATA\[.*?\]\]>", re_.DOTALL)

# Change this to redirect the generated superclass module to use a
# specific subclass module.
CurrentSubclassModule_ = None

#
# Support/utility functions.
#


def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')


def quote_xml(inStr):
    "Escape markup chars, but do not modify CDATA sections."
    if not inStr:
        return ''
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s2 = ''
    pos = 0
    matchobjects = CDATA_pattern_.finditer(s1)
    for mo in matchobjects:
        s3 = s1[pos:mo.start()]
        s2 += quote_xml_aux(s3)
        s2 += s1[mo.start():mo.end()]
        pos = mo.end()
    s3 = s1[pos:]
    s2 += quote_xml_aux(s3)
    return s2


def quote_xml_aux(inStr):
    s1 = inStr.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1


def quote_attrib(inStr):
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1


def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text


def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


def encode_str_2_3(instr):
    return instr


class GDSParseError(Exception):
    pass


def raise_parse_error(node, msg):
    if node is not None:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    TypeBase64 = 8
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace,
               pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(
                outfile, level, namespace, name_=name,
                pretty_print=pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeBase64:
            outfile.write('<%s>%s</%s>' % (
                self.name,
                base64.b64encode(self.value),
                self.name))
    def to_etree(self, element, mapping_=None, nsmap_=None):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                if len(element) > 0:
                    if element[-1].tail is None:
                        element[-1].tail = self.value
                    else:
                        element[-1].tail += self.value
                else:
                    if element.text is None:
                        element.text = self.value
                    else:
                        element.text += self.value
        elif self.category == MixedContainer.CategorySimple:
            subelement = etree_.SubElement(
                element, '%s' % self.name)
            subelement.text = self.to_etree_simple()
        else:    # category == MixedContainer.CategoryComplex
            self.value.to_etree(element)
    def to_etree_simple(self, mapping_=None, nsmap_=None):
        if self.content_type == MixedContainer.TypeString:
            text = self.value
        elif (self.content_type == MixedContainer.TypeInteger or
                self.content_type == MixedContainer.TypeBoolean):
            text = '%d' % self.value
        elif (self.content_type == MixedContainer.TypeFloat or
                self.content_type == MixedContainer.TypeDecimal):
            text = '%f' % self.value
        elif self.content_type == MixedContainer.TypeDouble:
            text = '%g' % self.value
        elif self.content_type == MixedContainer.TypeBase64:
            text = '%s' % base64.b64encode(self.value)
        return text
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s",\n' % (
                    self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0,
            optional=0, child_attrs=None, choice=None):
        self.name = name
        self.data_type = data_type
        self.container = container
        self.child_attrs = child_attrs
        self.choice = choice
        self.optional = optional
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container
    def set_child_attrs(self, child_attrs): self.child_attrs = child_attrs
    def get_child_attrs(self): return self.child_attrs
    def set_choice(self, choice): self.choice = choice
    def get_choice(self): return self.choice
    def set_optional(self, optional): self.optional = optional
    def get_optional(self): return self.optional


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#


class response(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, next_page=None, next_page_id=None, system_info=None, entities=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.next_page = _cast(None, next_page)
        self.next_page_nsprefix_ = None
        self.next_page_id = _cast(None, next_page_id)
        self.next_page_id_nsprefix_ = None
        self.system_info = system_info
        self.system_info_nsprefix_ = None
        self.entities = entities
        self.entities_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, response)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if response.subclass:
            return response.subclass(*args_, **kwargs_)
        else:
            return response(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_system_info(self):
        return self.system_info
    def set_system_info(self, system_info):
        self.system_info = system_info
    def get_entities(self):
        return self.entities
    def set_entities(self, entities):
        self.entities = entities
    def get_next_page(self):
        return self.next_page
    def set_next_page(self, next_page):
        self.next_page = next_page
    def get_next_page_id(self):
        return self.next_page_id
    def set_next_page_id(self, next_page_id):
        self.next_page_id = next_page_id
    def hasContent_(self):
        if (
            self.system_info is not None or
            self.entities is not None
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.response_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        if self.next_page is not None:
            dbobj.next_page = self.next_page
        if self.next_page_id is not None:
            dbobj.next_page_id = self.next_page_id
    def exportDjangoChildren(self, dbobj):
        if self.system_info is not None:
            child_dbobj = self.system_info.exportDjango()
            dbobj.system_infoType_model_system_info = child_dbobj
            child_dbobj.save()
        if self.entities is not None:
            child_dbobj = self.entities.exportDjango()
            dbobj.entitiesType_model_entities = child_dbobj
            child_dbobj.save()
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('next_page', node)
        if value is not None and 'next_page' not in already_processed:
            already_processed.add('next_page')
            self.next_page = value
        value = find_attr_value_('next_page_id', node)
        if value is not None and 'next_page_id' not in already_processed:
            already_processed.add('next_page_id')
            self.next_page_id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'system_info':
            obj_ = system_infoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.system_info = obj_
            obj_.original_tagname_ = 'system_info'
        elif nodeName_ == 'entities':
            obj_ = entitiesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.entities = obj_
            obj_.original_tagname_ = 'entities'
# end class response


class system_infoType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, created_at=None, total=None, count=None, took=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if isinstance(created_at, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = created_at
        self.created_at = initvalue_
        self.created_at_nsprefix_ = None
        self.total = total
        self.total_nsprefix_ = None
        self.count = count
        self.count_nsprefix_ = None
        self.took = took
        self.took_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, system_infoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if system_infoType.subclass:
            return system_infoType.subclass(*args_, **kwargs_)
        else:
            return system_infoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_created_at(self):
        return self.created_at
    def set_created_at(self, created_at):
        self.created_at = created_at
    def get_total(self):
        return self.total
    def set_total(self, total):
        self.total = total
    def get_count(self):
        return self.count
    def set_count(self, count):
        self.count = count
    def get_took(self):
        return self.took
    def set_took(self, took):
        self.took = took
    def hasContent_(self):
        if (
            self.created_at is not None or
            self.total is not None or
            self.count is not None or
            self.took is not None
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.system_infoType_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        pass
    def exportDjangoChildren(self, dbobj):
        if self.created_at is not None:
            dbobj.created_at = self.created_at
        if self.total is not None:
            dbobj.total = self.total
        if self.count is not None:
            dbobj.count = self.count
        if self.took is not None:
            dbobj.took = self.took
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'created_at':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.created_at = dval_
            self.created_at_nsprefix_ = child_.prefix
        elif nodeName_ == 'total' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'total')
            ival_ = self.gds_validate_integer(ival_, node, 'total')
            self.total = ival_
            self.total_nsprefix_ = child_.prefix
        elif nodeName_ == 'count' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'count')
            ival_ = self.gds_validate_integer(ival_, node, 'count')
            self.count = ival_
            self.count_nsprefix_ = child_.prefix
        elif nodeName_ == 'took' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'took')
            ival_ = self.gds_validate_integer(ival_, node, 'took')
            self.took = ival_
            self.took_nsprefix_ = child_.prefix
# end class system_infoType


class entitiesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, entity=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if entity is None:
            self.entity = []
        else:
            self.entity = entity
        self.entity_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, entitiesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if entitiesType.subclass:
            return entitiesType.subclass(*args_, **kwargs_)
        else:
            return entitiesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_entity(self):
        return self.entity
    def set_entity(self, entity):
        self.entity = entity
    def add_entity(self, value):
        self.entity.append(value)
    def insert_entity_at(self, index, value):
        self.entity.insert(index, value)
    def replace_entity_at(self, index, value):
        self.entity[index] = value
    def hasContent_(self):
        if (
            self.entity
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.entitiesType_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        pass
    def exportDjangoChildren(self, dbobj):
        for child in self.entity:
            child_dbobj = child.exportDjango()
            dbobj.entityType_model_entity.add(child_dbobj)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'entity':
            obj_ = entityType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.entity.append(obj_)
            obj_.original_tagname_ = 'entity'
# end class entitiesType


class entityType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, type_=None, system_id=None, updated_at=None, updated_at_sec=None, full_name=None, dob=None, dob_extra=None, dod=None, dod_extra=None, pob=None, pob_extra=None, dead=None, gender=None, names=None, translit_names=None, category_407=None, jobs=None, incomes=None, ownerships=None, biography=None, relatives=None, persdocs=None, countries=None, categories=None, addresses=None, contact_infos=None, sanlists=None, licenses=None, sanctions=None, watch_lists=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = None
        self.system_id = system_id
        self.system_id_nsprefix_ = None
        if isinstance(updated_at, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = updated_at
        self.updated_at = initvalue_
        self.updated_at_nsprefix_ = None
        self.updated_at_sec = updated_at_sec
        self.updated_at_sec_nsprefix_ = None
        self.full_name = full_name
        self.full_name_nsprefix_ = None
        self.dob = dob
        self.dob_nsprefix_ = None
        self.dob_extra = dob_extra
        self.dob_extra_nsprefix_ = None
        self.dod = dod
        self.dod_nsprefix_ = None
        self.dod_extra = dod_extra
        self.dod_extra_nsprefix_ = None
        self.pob = pob
        self.pob_nsprefix_ = None
        self.pob_extra = pob_extra
        self.pob_extra_nsprefix_ = None
        self.dead = dead
        self.validate_boolean_or_empty_string(self.dead)
        self.dead_nsprefix_ = None
        self.gender = gender
        self.gender_nsprefix_ = None
        self.names = names
        self.names_nsprefix_ = None
        self.translit_names = translit_names
        self.translit_names_nsprefix_ = None
        self.category_407 = category_407
        self.category_407_nsprefix_ = None
        self.jobs = jobs
        self.jobs_nsprefix_ = None
        self.incomes = incomes
        self.incomes_nsprefix_ = None
        self.ownerships = ownerships
        self.ownerships_nsprefix_ = None
        self.biography = biography
        self.biography_nsprefix_ = None
        self.relatives = relatives
        self.relatives_nsprefix_ = None
        self.persdocs = persdocs
        self.persdocs_nsprefix_ = None
        self.countries = countries
        self.countries_nsprefix_ = None
        self.categories = categories
        self.categories_nsprefix_ = None
        self.addresses = addresses
        self.addresses_nsprefix_ = None
        self.contact_infos = contact_infos
        self.contact_infos_nsprefix_ = None
        self.sanlists = sanlists
        self.sanlists_nsprefix_ = None
        self.licenses = licenses
        self.licenses_nsprefix_ = None
        self.sanctions = sanctions
        self.sanctions_nsprefix_ = None
        self.watch_lists = watch_lists
        self.watch_lists_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, entityType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if entityType.subclass:
            return entityType.subclass(*args_, **kwargs_)
        else:
            return entityType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_system_id(self):
        return self.system_id
    def set_system_id(self, system_id):
        self.system_id = system_id
    def get_updated_at(self):
        return self.updated_at
    def set_updated_at(self, updated_at):
        self.updated_at = updated_at
    def get_updated_at_sec(self):
        return self.updated_at_sec
    def set_updated_at_sec(self, updated_at_sec):
        self.updated_at_sec = updated_at_sec
    def get_full_name(self):
        return self.full_name
    def set_full_name(self, full_name):
        self.full_name = full_name
    def get_dob(self):
        return self.dob
    def set_dob(self, dob):
        self.dob = dob
    def get_dob_extra(self):
        return self.dob_extra
    def set_dob_extra(self, dob_extra):
        self.dob_extra = dob_extra
    def get_dod(self):
        return self.dod
    def set_dod(self, dod):
        self.dod = dod
    def get_dod_extra(self):
        return self.dod_extra
    def set_dod_extra(self, dod_extra):
        self.dod_extra = dod_extra
    def get_pob(self):
        return self.pob
    def set_pob(self, pob):
        self.pob = pob
    def get_pob_extra(self):
        return self.pob_extra
    def set_pob_extra(self, pob_extra):
        self.pob_extra = pob_extra
    def get_dead(self):
        return self.dead
    def set_dead(self, dead):
        self.dead = dead
    def get_gender(self):
        return self.gender
    def set_gender(self, gender):
        self.gender = gender
    def get_names(self):
        return self.names
    def set_names(self, names):
        self.names = names
    def get_translit_names(self):
        return self.translit_names
    def set_translit_names(self, translit_names):
        self.translit_names = translit_names
    def get_category_407(self):
        return self.category_407
    def set_category_407(self, category_407):
        self.category_407 = category_407
    def get_jobs(self):
        return self.jobs
    def set_jobs(self, jobs):
        self.jobs = jobs
    def get_incomes(self):
        return self.incomes
    def set_incomes(self, incomes):
        self.incomes = incomes
    def get_ownerships(self):
        return self.ownerships
    def set_ownerships(self, ownerships):
        self.ownerships = ownerships
    def get_biography(self):
        return self.biography
    def set_biography(self, biography):
        self.biography = biography
    def get_relatives(self):
        return self.relatives
    def set_relatives(self, relatives):
        self.relatives = relatives
    def get_persdocs(self):
        return self.persdocs
    def set_persdocs(self, persdocs):
        self.persdocs = persdocs
    def get_countries(self):
        return self.countries
    def set_countries(self, countries):
        self.countries = countries
    def get_categories(self):
        return self.categories
    def set_categories(self, categories):
        self.categories = categories
    def get_addresses(self):
        return self.addresses
    def set_addresses(self, addresses):
        self.addresses = addresses
    def get_contact_infos(self):
        return self.contact_infos
    def set_contact_infos(self, contact_infos):
        self.contact_infos = contact_infos
    def get_sanlists(self):
        return self.sanlists
    def set_sanlists(self, sanlists):
        self.sanlists = sanlists
    def get_licenses(self):
        return self.licenses
    def set_licenses(self, licenses):
        self.licenses = licenses
    def get_sanctions(self):
        return self.sanctions
    def set_sanctions(self, sanctions):
        self.sanctions = sanctions
    def get_watch_lists(self):
        return self.watch_lists
    def set_watch_lists(self, watch_lists):
        self.watch_lists = watch_lists
    def get_type(self):
        return self.type_
    def set_type(self, type_):
        self.type_ = type_
    def validate_boolean_or_empty_string(self, value):
        result = True
        # Validate type boolean_or_empty_string, a restriction on xs:string.
        pass
        return result
    def hasContent_(self):
        if (
            self.system_id is not None or
            self.updated_at is not None or
            self.updated_at_sec is not None or
            self.full_name is not None or
            self.dob is not None or
            self.dob_extra is not None or
            self.dod is not None or
            self.dod_extra is not None or
            self.pob is not None or
            self.pob_extra is not None or
            self.dead is not None or
            self.gender is not None or
            self.names is not None or
            self.translit_names is not None or
            self.category_407 is not None or
            self.jobs is not None or
            self.incomes is not None or
            self.ownerships is not None or
            self.biography is not None or
            self.relatives is not None or
            self.persdocs is not None or
            self.countries is not None or
            self.categories is not None or
            self.addresses is not None or
            self.contact_infos is not None or
            self.sanlists is not None or
            self.licenses is not None or
            self.sanctions is not None or
            self.watch_lists is not None
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.entityType_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        if self.type_ is not None:
            dbobj.type_x = self.type_
    def exportDjangoChildren(self, dbobj):
        if self.system_id is not None:
            dbobj.system_id = self.system_id
        if self.updated_at is not None:
            dbobj.updated_at = self.updated_at
        if self.updated_at_sec is not None:
            dbobj.updated_at_sec = self.updated_at_sec
        if self.full_name is not None:
            dbobj.full_name = self.full_name
        if self.dob is not None:
            dbobj.dob = self.dob
        if self.dob_extra is not None:
            child_dbobj = self.dob_extra.exportDjango()
            dbobj.dob_extraType_model_dob_extra = child_dbobj
            child_dbobj.save()
        if self.dod is not None:
            dbobj.dod = self.dod
        if self.dod_extra is not None:
            child_dbobj = self.dod_extra.exportDjango()
            dbobj.dod_extraType_model_dod_extra = child_dbobj
            child_dbobj.save()
        if self.pob is not None:
            dbobj.pob = self.pob
        if self.pob_extra is not None:
            child_dbobj = self.pob_extra.exportDjango()
            dbobj.pob_extraType_model_pob_extra = child_dbobj
            child_dbobj.save()
        if self.dead is not None:
            dbobj.dead = self.dead
        if self.gender is not None:
            dbobj.gender = self.gender
        if self.names is not None:
            child_dbobj = self.names.exportDjango()
            dbobj.namesType_model_names = child_dbobj
            child_dbobj.save()
        if self.translit_names is not None:
            child_dbobj = self.translit_names.exportDjango()
            dbobj.translit_namesType_model_translit_names = child_dbobj
            child_dbobj.save()
        if self.category_407 is not None:
            child_dbobj = self.category_407.exportDjango()
            dbobj.category_407Type_model_category_407 = child_dbobj
            child_dbobj.save()
        if self.jobs is not None:
            child_dbobj = self.jobs.exportDjango()
            dbobj.jobsType_model_jobs = child_dbobj
            child_dbobj.save()
        if self.incomes is not None:
            child_dbobj = self.incomes.exportDjango()
            dbobj.incomesType_model_incomes = child_dbobj
            child_dbobj.save()
        if self.ownerships is not None:
            child_dbobj = self.ownerships.exportDjango()
            dbobj.ownershipsType_model_ownerships = child_dbobj
            child_dbobj.save()
        if self.biography is not None:
            dbobj.biography = self.biography
        if self.relatives is not None:
            child_dbobj = self.relatives.exportDjango()
            dbobj.relativesType_model_relatives = child_dbobj
            child_dbobj.save()
        if self.persdocs is not None:
            child_dbobj = self.persdocs.exportDjango()
            dbobj.persdocsType_model_persdocs = child_dbobj
            child_dbobj.save()
        if self.countries is not None:
            child_dbobj = self.countries.exportDjango()
            dbobj.countriesType_model_countries = child_dbobj
            child_dbobj.save()
        if self.categories is not None:
            child_dbobj = self.categories.exportDjango()
            dbobj.categoriesType_model_categories = child_dbobj
            child_dbobj.save()
        if self.addresses is not None:
            child_dbobj = self.addresses.exportDjango()
            dbobj.addressesType_model_addresses = child_dbobj
            child_dbobj.save()
        if self.contact_infos is not None:
            child_dbobj = self.contact_infos.exportDjango()
            dbobj.contact_infosType_model_contact_infos = child_dbobj
            child_dbobj.save()
        if self.sanlists is not None:
            child_dbobj = self.sanlists.exportDjango()
            dbobj.sanlistsType_model_sanlists = child_dbobj
            child_dbobj.save()
        if self.licenses is not None:
            child_dbobj = self.licenses.exportDjango()
            dbobj.licensesType_model_licenses = child_dbobj
            child_dbobj.save()
        if self.sanctions is not None:
            child_dbobj = self.sanctions.exportDjango()
            dbobj.sanctionsType_model_sanctions = child_dbobj
            child_dbobj.save()
        if self.watch_lists is not None:
            child_dbobj = self.watch_lists.exportDjango()
            dbobj.watch_listsType_model_watch_lists = child_dbobj
            child_dbobj.save()
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'system_id' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'system_id')
            ival_ = self.gds_validate_integer(ival_, node, 'system_id')
            self.system_id = ival_
            self.system_id_nsprefix_ = child_.prefix
        elif nodeName_ == 'updated_at':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.updated_at = dval_
            self.updated_at_nsprefix_ = child_.prefix
        elif nodeName_ == 'updated_at_sec' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'updated_at_sec')
            ival_ = self.gds_validate_integer(ival_, node, 'updated_at_sec')
            self.updated_at_sec = ival_
            self.updated_at_sec_nsprefix_ = child_.prefix
        elif nodeName_ == 'full_name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'full_name')
            value_ = self.gds_validate_string(value_, node, 'full_name')
            self.full_name = value_
            self.full_name_nsprefix_ = child_.prefix
        elif nodeName_ == 'dob':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'dob')
            value_ = self.gds_validate_string(value_, node, 'dob')
            self.dob = value_
            self.dob_nsprefix_ = child_.prefix
        elif nodeName_ == 'dob_extra':
            obj_ = dob_extraType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.dob_extra = obj_
            obj_.original_tagname_ = 'dob_extra'
        elif nodeName_ == 'dod':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'dod')
            value_ = self.gds_validate_string(value_, node, 'dod')
            self.dod = value_
            self.dod_nsprefix_ = child_.prefix
        elif nodeName_ == 'dod_extra':
            obj_ = dod_extraType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.dod_extra = obj_
            obj_.original_tagname_ = 'dod_extra'
        elif nodeName_ == 'pob':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'pob')
            value_ = self.gds_validate_string(value_, node, 'pob')
            self.pob = value_
            self.pob_nsprefix_ = child_.prefix
        elif nodeName_ == 'pob_extra':
            obj_ = pob_extraType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.pob_extra = obj_
            obj_.original_tagname_ = 'pob_extra'
        elif nodeName_ == 'dead':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'dead')
            value_ = self.gds_validate_string(value_, node, 'dead')
            self.dead = value_
            self.dead_nsprefix_ = child_.prefix
            # validate type boolean_or_empty_string
            self.validate_boolean_or_empty_string(self.dead)
        elif nodeName_ == 'gender':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'gender')
            value_ = self.gds_validate_string(value_, node, 'gender')
            self.gender = value_
            self.gender_nsprefix_ = child_.prefix
        elif nodeName_ == 'names':
            obj_ = namesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.names = obj_
            obj_.original_tagname_ = 'names'
        elif nodeName_ == 'translit_names':
            obj_ = translit_namesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.translit_names = obj_
            obj_.original_tagname_ = 'translit_names'
        elif nodeName_ == 'category_407':
            obj_ = category_407Type.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.category_407 = obj_
            obj_.original_tagname_ = 'category_407'
        elif nodeName_ == 'jobs':
            obj_ = jobsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.jobs = obj_
            obj_.original_tagname_ = 'jobs'
        elif nodeName_ == 'incomes':
            obj_ = incomesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.incomes = obj_
            obj_.original_tagname_ = 'incomes'
        elif nodeName_ == 'ownerships':
            obj_ = ownershipsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ownerships = obj_
            obj_.original_tagname_ = 'ownerships'
        elif nodeName_ == 'biography':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'biography')
            value_ = self.gds_validate_string(value_, node, 'biography')
            self.biography = value_
            self.biography_nsprefix_ = child_.prefix
        elif nodeName_ == 'relatives':
            obj_ = relativesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.relatives = obj_
            obj_.original_tagname_ = 'relatives'
        elif nodeName_ == 'persdocs':
            obj_ = persdocsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.persdocs = obj_
            obj_.original_tagname_ = 'persdocs'
        elif nodeName_ == 'countries':
            obj_ = countriesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.countries = obj_
            obj_.original_tagname_ = 'countries'
        elif nodeName_ == 'categories':
            obj_ = categoriesType12.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.categories = obj_
            obj_.original_tagname_ = 'categories'
        elif nodeName_ == 'addresses':
            obj_ = addressesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.addresses = obj_
            obj_.original_tagname_ = 'addresses'
        elif nodeName_ == 'contact_infos':
            obj_ = contact_infosType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.contact_infos = obj_
            obj_.original_tagname_ = 'contact_infos'
        elif nodeName_ == 'sanlists':
            obj_ = sanlistsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.sanlists = obj_
            obj_.original_tagname_ = 'sanlists'
        elif nodeName_ == 'licenses':
            obj_ = licensesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.licenses = obj_
            obj_.original_tagname_ = 'licenses'
        elif nodeName_ == 'sanctions':
            obj_ = sanctionsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.sanctions = obj_
            obj_.original_tagname_ = 'sanctions'
        elif nodeName_ == 'watch_lists':
            obj_ = watch_listsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.watch_lists = obj_
            obj_.original_tagname_ = 'watch_lists'
# end class entityType


class dob_extraType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, item=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if item is None:
            self.item = []
        else:
            self.item = item
        self.item_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, dob_extraType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if dob_extraType.subclass:
            return dob_extraType.subclass(*args_, **kwargs_)
        else:
            return dob_extraType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_item(self):
        return self.item
    def set_item(self, item):
        self.item = item
    def add_item(self, value):
        self.item.append(value)
    def insert_item_at(self, index, value):
        self.item.insert(index, value)
    def replace_item_at(self, index, value):
        self.item[index] = value
    def hasContent_(self):
        if (
            self.item
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.dob_extraType_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        pass
    def exportDjangoChildren(self, dbobj):
        for child in self.item:
            child_dbobj = child.exportDjango()
            dbobj.itemType_model_item.add(child_dbobj)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'item':
            obj_ = itemType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.item.append(obj_)
            obj_.original_tagname_ = 'item'
# end class dob_extraType


class itemType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(int, id)
        self.id_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, itemType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if itemType.subclass:
            return itemType.subclass(*args_, **kwargs_)
        else:
            return itemType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.itemType_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        if self.id is not None:
            dbobj.id_x = self.id
    def exportDjangoChildren(self, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = self.gds_parse_integer(value, node, 'id')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class itemType


class dod_extraType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, item=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if item is None:
            self.item = []
        else:
            self.item = item
        self.item_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, dod_extraType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if dod_extraType.subclass:
            return dod_extraType.subclass(*args_, **kwargs_)
        else:
            return dod_extraType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_item(self):
        return self.item
    def set_item(self, item):
        self.item = item
    def add_item(self, value):
        self.item.append(value)
    def insert_item_at(self, index, value):
        self.item.insert(index, value)
    def replace_item_at(self, index, value):
        self.item[index] = value
    def hasContent_(self):
        if (
            self.item
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.dod_extraType_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        pass
    def exportDjangoChildren(self, dbobj):
        for child in self.item:
            child_dbobj = child.exportDjango()
            dbobj.itemType1_model_item.add(child_dbobj)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'item':
            obj_ = itemType1.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.item.append(obj_)
            obj_.original_tagname_ = 'item'
# end class dod_extraType


class itemType1(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(int, id)
        self.id_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, itemType1)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if itemType1.subclass:
            return itemType1.subclass(*args_, **kwargs_)
        else:
            return itemType1(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.itemType1_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        if self.id is not None:
            dbobj.id_x = self.id
    def exportDjangoChildren(self, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = self.gds_parse_integer(value, node, 'id')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class itemType1


class pob_extraType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, item=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if item is None:
            self.item = []
        else:
            self.item = item
        self.item_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, pob_extraType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if pob_extraType.subclass:
            return pob_extraType.subclass(*args_, **kwargs_)
        else:
            return pob_extraType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_item(self):
        return self.item
    def set_item(self, item):
        self.item = item
    def add_item(self, value):
        self.item.append(value)
    def insert_item_at(self, index, value):
        self.item.insert(index, value)
    def replace_item_at(self, index, value):
        self.item[index] = value
    def hasContent_(self):
        if (
            self.item
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.pob_extraType_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        pass
    def exportDjangoChildren(self, dbobj):
        for child in self.item:
            child_dbobj = child.exportDjango()
            dbobj.itemType2_model_item.add(child_dbobj)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'item':
            obj_ = itemType2.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.item.append(obj_)
            obj_.original_tagname_ = 'item'
# end class pob_extraType


class itemType2(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(int, id)
        self.id_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, itemType2)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if itemType2.subclass:
            return itemType2.subclass(*args_, **kwargs_)
        else:
            return itemType2(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.itemType2_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        if self.id is not None:
            dbobj.id_x = self.id
    def exportDjangoChildren(self, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = self.gds_parse_integer(value, node, 'id')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class itemType2


class namesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, item=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if item is None:
            self.item = []
        else:
            self.item = item
        self.item_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, namesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if namesType.subclass:
            return namesType.subclass(*args_, **kwargs_)
        else:
            return namesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_item(self):
        return self.item
    def set_item(self, item):
        self.item = item
    def add_item(self, value):
        self.item.append(value)
    def insert_item_at(self, index, value):
        self.item.insert(index, value)
    def replace_item_at(self, index, value):
        self.item[index] = value
    def hasContent_(self):
        if (
            self.item
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.namesType_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        pass
    def exportDjangoChildren(self, dbobj):
        for child in self.item:
            child_dbobj = child.exportDjango()
            dbobj.itemType3_model_item.add(child_dbobj)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'item':
            obj_ = itemType3.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.item.append(obj_)
            obj_.original_tagname_ = 'item'
# end class namesType


class itemType3(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, locale=None, updated_at=None, last_name=None, first_name=None, middle_name=None, name=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(int, id)
        self.id_nsprefix_ = None
        self.locale = _cast(None, locale)
        self.locale_nsprefix_ = None
        if isinstance(updated_at, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = updated_at
        self.updated_at = initvalue_
        self.last_name = last_name
        self.last_name_nsprefix_ = None
        self.first_name = first_name
        self.first_name_nsprefix_ = None
        self.middle_name = middle_name
        self.middle_name_nsprefix_ = None
        self.name = name
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, itemType3)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if itemType3.subclass:
            return itemType3.subclass(*args_, **kwargs_)
        else:
            return itemType3(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_last_name(self):
        return self.last_name
    def set_last_name(self, last_name):
        self.last_name = last_name
    def get_first_name(self):
        return self.first_name
    def set_first_name(self, first_name):
        self.first_name = first_name
    def get_middle_name(self):
        return self.middle_name
    def set_middle_name(self, middle_name):
        self.middle_name = middle_name
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_locale(self):
        return self.locale
    def set_locale(self, locale):
        self.locale = locale
    def get_updated_at(self):
        return self.updated_at
    def set_updated_at(self, updated_at):
        self.updated_at = updated_at
    def hasContent_(self):
        if (
            self.last_name is not None or
            self.first_name is not None or
            self.middle_name is not None or
            self.name is not None
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.itemType3_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        if self.id is not None:
            dbobj.id_x = self.id
        if self.locale is not None:
            dbobj.locale = self.locale
        if self.updated_at is not None:
            dbobj.updated_at = self.updated_at
    def exportDjangoChildren(self, dbobj):
        if self.last_name is not None:
            dbobj.last_name = self.last_name
        if self.first_name is not None:
            dbobj.first_name = self.first_name
        if self.middle_name is not None:
            dbobj.middle_name = self.middle_name
        if self.name is not None:
            dbobj.name = self.name
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = self.gds_parse_integer(value, node, 'id')
        value = find_attr_value_('locale', node)
        if value is not None and 'locale' not in already_processed:
            already_processed.add('locale')
            self.locale = value
        value = find_attr_value_('updated_at', node)
        if value is not None and 'updated_at' not in already_processed:
            already_processed.add('updated_at')
            try:
                self.updated_at = self.gds_parse_datetime(value)
            except ValueError as exp:
                raise ValueError('Bad date-time attribute (updated_at): %s' % exp)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'last_name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'last_name')
            value_ = self.gds_validate_string(value_, node, 'last_name')
            self.last_name = value_
            self.last_name_nsprefix_ = child_.prefix
        elif nodeName_ == 'first_name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'first_name')
            value_ = self.gds_validate_string(value_, node, 'first_name')
            self.first_name = value_
            self.first_name_nsprefix_ = child_.prefix
        elif nodeName_ == 'middle_name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'middle_name')
            value_ = self.gds_validate_string(value_, node, 'middle_name')
            self.middle_name = value_
            self.middle_name_nsprefix_ = child_.prefix
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
# end class itemType3


class translit_namesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, item=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if item is None:
            self.item = []
        else:
            self.item = item
        self.item_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, translit_namesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if translit_namesType.subclass:
            return translit_namesType.subclass(*args_, **kwargs_)
        else:
            return translit_namesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_item(self):
        return self.item
    def set_item(self, item):
        self.item = item
    def add_item(self, value):
        self.item.append(value)
    def insert_item_at(self, index, value):
        self.item.insert(index, value)
    def replace_item_at(self, index, value):
        self.item[index] = value
    def hasContent_(self):
        if (
            self.item
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.translit_namesType_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        pass
    def exportDjangoChildren(self, dbobj):
        dbobj.item = json_.dumps(self.item, separators=(',', ':'))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'item':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'item')
            value_ = self.gds_validate_string(value_, node, 'item')
            self.item.append(value_)
            self.item_nsprefix_ = child_.prefix
# end class translit_namesType


class category_407Type(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, item=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if item is None:
            self.item = []
        else:
            self.item = item
        self.item_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, category_407Type)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if category_407Type.subclass:
            return category_407Type.subclass(*args_, **kwargs_)
        else:
            return category_407Type(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_item(self):
        return self.item
    def set_item(self, item):
        self.item = item
    def add_item(self, value):
        self.item.append(value)
    def insert_item_at(self, index, value):
        self.item.insert(index, value)
    def replace_item_at(self, index, value):
        self.item[index] = value
    def hasContent_(self):
        if (
            self.item
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.category_407Type_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        pass
    def exportDjangoChildren(self, dbobj):
        dbobj.item = json_.dumps(self.item, separators=(',', ':'))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'item' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'item')
            ival_ = self.gds_validate_integer(ival_, node, 'item')
            self.item.append(ival_)
            self.item_nsprefix_ = child_.prefix
# end class category_407Type


class jobsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, item=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if item is None:
            self.item = []
        else:
            self.item = item
        self.item_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, jobsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if jobsType.subclass:
            return jobsType.subclass(*args_, **kwargs_)
        else:
            return jobsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_item(self):
        return self.item
    def set_item(self, item):
        self.item = item
    def add_item(self, value):
        self.item.append(value)
    def insert_item_at(self, index, value):
        self.item.insert(index, value)
    def replace_item_at(self, index, value):
        self.item[index] = value
    def hasContent_(self):
        if (
            self.item
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.jobsType_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        pass
    def exportDjangoChildren(self, dbobj):
        for child in self.item:
            child_dbobj = child.exportDjango()
            dbobj.itemType4_model_item.add(child_dbobj)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'item':
            obj_ = itemType4.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.item.append(obj_)
            obj_.original_tagname_ = 'item'
# end class jobsType


class itemType4(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, updated_at=None, date_start=None, date_end=None, source=None, main=None, unactive=None, name=None, authority=None, categories=None, category_407=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(int, id)
        self.id_nsprefix_ = None
        if isinstance(updated_at, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = updated_at
        self.updated_at = initvalue_
        self.date_start = _cast(None, date_start)
        self.date_start_nsprefix_ = None
        self.date_end = _cast(None, date_end)
        self.date_end_nsprefix_ = None
        self.source = _cast(None, source)
        self.source_nsprefix_ = None
        self.main = _cast(None, main)
        self.main_nsprefix_ = None
        self.unactive = _cast(None, unactive)
        self.unactive_nsprefix_ = None
        self.name = name
        self.name_nsprefix_ = None
        self.authority = authority
        self.authority_nsprefix_ = None
        self.categories = categories
        self.categories_nsprefix_ = None
        self.category_407 = category_407
        self.category_407_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, itemType4)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if itemType4.subclass:
            return itemType4.subclass(*args_, **kwargs_)
        else:
            return itemType4(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_authority(self):
        return self.authority
    def set_authority(self, authority):
        self.authority = authority
    def get_categories(self):
        return self.categories
    def set_categories(self, categories):
        self.categories = categories
    def get_category_407(self):
        return self.category_407
    def set_category_407(self, category_407):
        self.category_407 = category_407
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_updated_at(self):
        return self.updated_at
    def set_updated_at(self, updated_at):
        self.updated_at = updated_at
    def get_date_start(self):
        return self.date_start
    def set_date_start(self, date_start):
        self.date_start = date_start
    def get_date_end(self):
        return self.date_end
    def set_date_end(self, date_end):
        self.date_end = date_end
    def get_source(self):
        return self.source
    def set_source(self, source):
        self.source = source
    def get_main(self):
        return self.main
    def set_main(self, main):
        self.main = main
    def get_unactive(self):
        return self.unactive
    def set_unactive(self, unactive):
        self.unactive = unactive
    def validate_boolean_or_empty_string(self, value):
        # Validate type boolean_or_empty_string, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.name is not None or
            self.authority is not None or
            self.categories is not None or
            self.category_407 is not None
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.itemType4_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        if self.id is not None:
            dbobj.id_x = self.id
        if self.updated_at is not None:
            dbobj.updated_at = self.updated_at
        if self.date_start is not None:
            dbobj.date_start = self.date_start
        if self.date_end is not None:
            dbobj.date_end = self.date_end
        if self.source is not None:
            dbobj.source = self.source
        if self.main is not None:
            dbobj.main = self.main
        if self.unactive is not None:
            dbobj.unactive = self.unactive
    def exportDjangoChildren(self, dbobj):
        if self.name is not None:
            dbobj.name = self.name
        if self.authority is not None:
            child_dbobj = self.authority.exportDjango()
            dbobj.authorityType_model_authority = child_dbobj
            child_dbobj.save()
        if self.categories is not None:
            child_dbobj = self.categories.exportDjango()
            dbobj.categoriesType_model_categories = child_dbobj
            child_dbobj.save()
        if self.category_407 is not None:
            child_dbobj = self.category_407.exportDjango()
            dbobj.category_407Type_model_category_407 = child_dbobj
            child_dbobj.save()
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = self.gds_parse_integer(value, node, 'id')
        value = find_attr_value_('updated_at', node)
        if value is not None and 'updated_at' not in already_processed:
            already_processed.add('updated_at')
            try:
                self.updated_at = self.gds_parse_datetime(value)
            except ValueError as exp:
                raise ValueError('Bad date-time attribute (updated_at): %s' % exp)
        value = find_attr_value_('date_start', node)
        if value is not None and 'date_start' not in already_processed:
            already_processed.add('date_start')
            self.date_start = value
        value = find_attr_value_('date_end', node)
        if value is not None and 'date_end' not in already_processed:
            already_processed.add('date_end')
            self.date_end = value
        value = find_attr_value_('source', node)
        if value is not None and 'source' not in already_processed:
            already_processed.add('source')
            self.source = value
        value = find_attr_value_('main', node)
        if value is not None and 'main' not in already_processed:
            already_processed.add('main')
            self.main = value
            self.validate_boolean_or_empty_string(self.main)    # validate type boolean_or_empty_string
        value = find_attr_value_('unactive', node)
        if value is not None and 'unactive' not in already_processed:
            already_processed.add('unactive')
            self.unactive = value
            self.validate_boolean_or_empty_string(self.unactive)    # validate type boolean_or_empty_string
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
        elif nodeName_ == 'authority':
            obj_ = authorityType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.authority = obj_
            obj_.original_tagname_ = 'authority'
        elif nodeName_ == 'categories':
            obj_ = categoriesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.categories = obj_
            obj_.original_tagname_ = 'categories'
        elif nodeName_ == 'category_407':
            obj_ = category_407Type5.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.category_407 = obj_
            obj_.original_tagname_ = 'category_407'
# end class itemType4


class authorityType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, reg_id=None, address=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.reg_id = _cast(None, reg_id)
        self.reg_id_nsprefix_ = None
        self.address = _cast(None, address)
        self.address_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, authorityType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if authorityType.subclass:
            return authorityType.subclass(*args_, **kwargs_)
        else:
            return authorityType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_reg_id(self):
        return self.reg_id
    def set_reg_id(self, reg_id):
        self.reg_id = reg_id
    def get_address(self):
        return self.address
    def set_address(self, address):
        self.address = address
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.authorityType_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        if self.reg_id is not None:
            dbobj.reg_id = self.reg_id
        if self.address is not None:
            dbobj.address = self.address
    def exportDjangoChildren(self, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('reg_id', node)
        if value is not None and 'reg_id' not in already_processed:
            already_processed.add('reg_id')
            self.reg_id = value
        value = find_attr_value_('address', node)
        if value is not None and 'address' not in already_processed:
            already_processed.add('address')
            self.address = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class authorityType


class categoriesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, item=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if item is None:
            self.item = []
        else:
            self.item = item
        self.item_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, categoriesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if categoriesType.subclass:
            return categoriesType.subclass(*args_, **kwargs_)
        else:
            return categoriesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_item(self):
        return self.item
    def set_item(self, item):
        self.item = item
    def add_item(self, value):
        self.item.append(value)
    def insert_item_at(self, index, value):
        self.item.insert(index, value)
    def replace_item_at(self, index, value):
        self.item[index] = value
    def hasContent_(self):
        if (
            self.item
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.categoriesType_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        pass
    def exportDjangoChildren(self, dbobj):
        dbobj.item = json_.dumps(self.item, separators=(',', ':'))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'item':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'item')
            value_ = self.gds_validate_string(value_, node, 'item')
            self.item.append(value_)
            self.item_nsprefix_ = child_.prefix
# end class categoriesType


class category_407Type5(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, item=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if item is None:
            self.item = []
        else:
            self.item = item
        self.item_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, category_407Type5)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if category_407Type5.subclass:
            return category_407Type5.subclass(*args_, **kwargs_)
        else:
            return category_407Type5(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_item(self):
        return self.item
    def set_item(self, item):
        self.item = item
    def add_item(self, value):
        self.item.append(value)
    def insert_item_at(self, index, value):
        self.item.insert(index, value)
    def replace_item_at(self, index, value):
        self.item[index] = value
    def hasContent_(self):
        if (
            self.item
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.category_407Type5_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        pass
    def exportDjangoChildren(self, dbobj):
        dbobj.item = json_.dumps(self.item, separators=(',', ':'))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'item' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'item')
            ival_ = self.gds_validate_integer(ival_, node, 'item')
            self.item.append(ival_)
            self.item_nsprefix_ = child_.prefix
# end class category_407Type5


class incomesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, item=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if item is None:
            self.item = []
        else:
            self.item = item
        self.item_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, incomesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if incomesType.subclass:
            return incomesType.subclass(*args_, **kwargs_)
        else:
            return incomesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_item(self):
        return self.item
    def set_item(self, item):
        self.item = item
    def add_item(self, value):
        self.item.append(value)
    def insert_item_at(self, index, value):
        self.item.insert(index, value)
    def replace_item_at(self, index, value):
        self.item[index] = value
    def hasContent_(self):
        if (
            self.item
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.incomesType_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        pass
    def exportDjangoChildren(self, dbobj):
        for child in self.item:
            child_dbobj = child.exportDjango()
            dbobj.itemType6_model_item.add(child_dbobj)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'item':
            obj_ = itemType6.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.item.append(obj_)
            obj_.original_tagname_ = 'item'
# end class incomesType


class itemType6(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, updated_at=None, date_start=None, date_end=None, source=None, income=None, owner=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(int, id)
        self.id_nsprefix_ = None
        if isinstance(updated_at, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = updated_at
        self.updated_at = initvalue_
        self.date_start = _cast(None, date_start)
        self.date_start_nsprefix_ = None
        self.date_end = _cast(None, date_end)
        self.date_end_nsprefix_ = None
        self.source = _cast(None, source)
        self.source_nsprefix_ = None
        self.income = income
        self.income_nsprefix_ = None
        self.owner = owner
        self.owner_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, itemType6)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if itemType6.subclass:
            return itemType6.subclass(*args_, **kwargs_)
        else:
            return itemType6(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_income(self):
        return self.income
    def set_income(self, income):
        self.income = income
    def get_owner(self):
        return self.owner
    def set_owner(self, owner):
        self.owner = owner
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_updated_at(self):
        return self.updated_at
    def set_updated_at(self, updated_at):
        self.updated_at = updated_at
    def get_date_start(self):
        return self.date_start
    def set_date_start(self, date_start):
        self.date_start = date_start
    def get_date_end(self):
        return self.date_end
    def set_date_end(self, date_end):
        self.date_end = date_end
    def get_source(self):
        return self.source
    def set_source(self, source):
        self.source = source
    def hasContent_(self):
        if (
            self.income is not None or
            self.owner is not None
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.itemType6_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        if self.id is not None:
            dbobj.id_x = self.id
        if self.updated_at is not None:
            dbobj.updated_at = self.updated_at
        if self.date_start is not None:
            dbobj.date_start = self.date_start
        if self.date_end is not None:
            dbobj.date_end = self.date_end
        if self.source is not None:
            dbobj.source = self.source
    def exportDjangoChildren(self, dbobj):
        if self.income is not None:
            child_dbobj = self.income.exportDjango()
            dbobj.incomeType_model_income = child_dbobj
            child_dbobj.save()
        if self.owner is not None:
            child_dbobj = self.owner.exportDjango()
            dbobj.ownerType_model_owner = child_dbobj
            child_dbobj.save()
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = self.gds_parse_integer(value, node, 'id')
        value = find_attr_value_('updated_at', node)
        if value is not None and 'updated_at' not in already_processed:
            already_processed.add('updated_at')
            try:
                self.updated_at = self.gds_parse_datetime(value)
            except ValueError as exp:
                raise ValueError('Bad date-time attribute (updated_at): %s' % exp)
        value = find_attr_value_('date_start', node)
        if value is not None and 'date_start' not in already_processed:
            already_processed.add('date_start')
            self.date_start = value
        value = find_attr_value_('date_end', node)
        if value is not None and 'date_end' not in already_processed:
            already_processed.add('date_end')
            self.date_end = value
        value = find_attr_value_('source', node)
        if value is not None and 'source' not in already_processed:
            already_processed.add('source')
            self.source = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'income':
            obj_ = incomeType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.income = obj_
            obj_.original_tagname_ = 'income'
        elif nodeName_ == 'owner':
            obj_ = ownerType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.owner = obj_
            obj_.original_tagname_ = 'owner'
# end class itemType6


class incomeType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, cur=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.cur = _cast(None, cur)
        self.cur_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, incomeType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if incomeType.subclass:
            return incomeType.subclass(*args_, **kwargs_)
        else:
            return incomeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_cur(self):
        return self.cur
    def set_cur(self, cur):
        self.cur = cur
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.incomeType_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        if self.cur is not None:
            dbobj.cur = self.cur
    def exportDjangoChildren(self, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('cur', node)
        if value is not None and 'cur' not in already_processed:
            already_processed.add('cur')
            self.cur = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class incomeType


class ownerType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, system_id=None, type_=None, type_id=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.system_id = _cast(None, system_id)
        self.system_id_nsprefix_ = None
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = None
        self.type_id = _cast(None, type_id)
        self.type_id_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ownerType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ownerType.subclass:
            return ownerType.subclass(*args_, **kwargs_)
        else:
            return ownerType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_system_id(self):
        return self.system_id
    def set_system_id(self, system_id):
        self.system_id = system_id
    def get_type(self):
        return self.type_
    def set_type(self, type_):
        self.type_ = type_
    def get_type_id(self):
        return self.type_id
    def set_type_id(self, type_id):
        self.type_id = type_id
    def validate_int_or_empty_string(self, value):
        # Validate type int_or_empty_string, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.ownerType_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        if self.system_id is not None:
            dbobj.system_id = self.system_id
        if self.type_ is not None:
            dbobj.type_x = self.type_
        if self.type_id is not None:
            dbobj.type_id = self.type_id
    def exportDjangoChildren(self, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('system_id', node)
        if value is not None and 'system_id' not in already_processed:
            already_processed.add('system_id')
            self.system_id = value
            self.validate_int_or_empty_string(self.system_id)    # validate type int_or_empty_string
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
        value = find_attr_value_('type_id', node)
        if value is not None and 'type_id' not in already_processed:
            already_processed.add('type_id')
            self.type_id = value
            self.validate_int_or_empty_string(self.type_id)    # validate type int_or_empty_string
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class ownerType


class ownershipsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, item=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if item is None:
            self.item = []
        else:
            self.item = item
        self.item_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ownershipsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ownershipsType.subclass:
            return ownershipsType.subclass(*args_, **kwargs_)
        else:
            return ownershipsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_item(self):
        return self.item
    def set_item(self, item):
        self.item = item
    def add_item(self, value):
        self.item.append(value)
    def insert_item_at(self, index, value):
        self.item.insert(index, value)
    def replace_item_at(self, index, value):
        self.item[index] = value
    def hasContent_(self):
        if (
            self.item
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.ownershipsType_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        pass
    def exportDjangoChildren(self, dbobj):
        for child in self.item:
            child_dbobj = child.exportDjango()
            dbobj.itemType7_model_item.add(child_dbobj)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'item':
            obj_ = itemType7.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.item.append(obj_)
            obj_.original_tagname_ = 'item'
# end class ownershipsType


class itemType7(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, updated_at=None, date_start=None, date_end=None, source=None, ownership=None, owner=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(int, id)
        self.id_nsprefix_ = None
        if isinstance(updated_at, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = updated_at
        self.updated_at = initvalue_
        self.date_start = _cast(None, date_start)
        self.date_start_nsprefix_ = None
        self.date_end = _cast(None, date_end)
        self.date_end_nsprefix_ = None
        self.source = _cast(None, source)
        self.source_nsprefix_ = None
        self.ownership = ownership
        self.ownership_nsprefix_ = None
        self.owner = owner
        self.owner_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, itemType7)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if itemType7.subclass:
            return itemType7.subclass(*args_, **kwargs_)
        else:
            return itemType7(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ownership(self):
        return self.ownership
    def set_ownership(self, ownership):
        self.ownership = ownership
    def get_owner(self):
        return self.owner
    def set_owner(self, owner):
        self.owner = owner
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_updated_at(self):
        return self.updated_at
    def set_updated_at(self, updated_at):
        self.updated_at = updated_at
    def get_date_start(self):
        return self.date_start
    def set_date_start(self, date_start):
        self.date_start = date_start
    def get_date_end(self):
        return self.date_end
    def set_date_end(self, date_end):
        self.date_end = date_end
    def get_source(self):
        return self.source
    def set_source(self, source):
        self.source = source
    def hasContent_(self):
        if (
            self.ownership is not None or
            self.owner is not None
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.itemType7_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        if self.id is not None:
            dbobj.id_x = self.id
        if self.updated_at is not None:
            dbobj.updated_at = self.updated_at
        if self.date_start is not None:
            dbobj.date_start = self.date_start
        if self.date_end is not None:
            dbobj.date_end = self.date_end
        if self.source is not None:
            dbobj.source = self.source
    def exportDjangoChildren(self, dbobj):
        if self.ownership is not None:
            child_dbobj = self.ownership.exportDjango()
            dbobj.ownershipType_model_ownership = child_dbobj
            child_dbobj.save()
        if self.owner is not None:
            child_dbobj = self.owner.exportDjango()
            dbobj.ownerType_model_owner = child_dbobj
            child_dbobj.save()
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = self.gds_parse_integer(value, node, 'id')
        value = find_attr_value_('updated_at', node)
        if value is not None and 'updated_at' not in already_processed:
            already_processed.add('updated_at')
            try:
                self.updated_at = self.gds_parse_datetime(value)
            except ValueError as exp:
                raise ValueError('Bad date-time attribute (updated_at): %s' % exp)
        value = find_attr_value_('date_start', node)
        if value is not None and 'date_start' not in already_processed:
            already_processed.add('date_start')
            self.date_start = value
        value = find_attr_value_('date_end', node)
        if value is not None and 'date_end' not in already_processed:
            already_processed.add('date_end')
            self.date_end = value
        value = find_attr_value_('source', node)
        if value is not None and 'source' not in already_processed:
            already_processed.add('source')
            self.source = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ownership':
            obj_ = ownershipType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ownership = obj_
            obj_.original_tagname_ = 'ownership'
        elif nodeName_ == 'owner':
            obj_ = ownerType8.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.owner = obj_
            obj_.original_tagname_ = 'owner'
# end class itemType7


class ownershipType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, type_=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.type_ = _cast(int, type_)
        self.type__nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ownershipType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ownershipType.subclass:
            return ownershipType.subclass(*args_, **kwargs_)
        else:
            return ownershipType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_type(self):
        return self.type_
    def set_type(self, type_):
        self.type_ = type_
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.ownershipType_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        if self.type_ is not None:
            dbobj.type_x = self.type_
    def exportDjangoChildren(self, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = self.gds_parse_integer(value, node, 'type')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class ownershipType


class ownerType8(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, system_id=None, type_=None, type_id=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.system_id = _cast(None, system_id)
        self.system_id_nsprefix_ = None
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = None
        self.type_id = _cast(None, type_id)
        self.type_id_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ownerType8)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ownerType8.subclass:
            return ownerType8.subclass(*args_, **kwargs_)
        else:
            return ownerType8(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_system_id(self):
        return self.system_id
    def set_system_id(self, system_id):
        self.system_id = system_id
    def get_type(self):
        return self.type_
    def set_type(self, type_):
        self.type_ = type_
    def get_type_id(self):
        return self.type_id
    def set_type_id(self, type_id):
        self.type_id = type_id
    def validate_int_or_empty_string(self, value):
        # Validate type int_or_empty_string, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.ownerType8_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        if self.system_id is not None:
            dbobj.system_id = self.system_id
        if self.type_ is not None:
            dbobj.type_x = self.type_
        if self.type_id is not None:
            dbobj.type_id = self.type_id
    def exportDjangoChildren(self, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('system_id', node)
        if value is not None and 'system_id' not in already_processed:
            already_processed.add('system_id')
            self.system_id = value
            self.validate_int_or_empty_string(self.system_id)    # validate type int_or_empty_string
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
        value = find_attr_value_('type_id', node)
        if value is not None and 'type_id' not in already_processed:
            already_processed.add('type_id')
            self.type_id = value
            self.validate_int_or_empty_string(self.type_id)    # validate type int_or_empty_string
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class ownerType8


class relativesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, item=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if item is None:
            self.item = []
        else:
            self.item = item
        self.item_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, relativesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if relativesType.subclass:
            return relativesType.subclass(*args_, **kwargs_)
        else:
            return relativesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_item(self):
        return self.item
    def set_item(self, item):
        self.item = item
    def add_item(self, value):
        self.item.append(value)
    def insert_item_at(self, index, value):
        self.item.insert(index, value)
    def replace_item_at(self, index, value):
        self.item[index] = value
    def hasContent_(self):
        if (
            self.item
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.relativesType_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        pass
    def exportDjangoChildren(self, dbobj):
        for child in self.item:
            child_dbobj = child.exportDjango()
            dbobj.itemType9_model_item.add(child_dbobj)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'item':
            obj_ = itemType9.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.item.append(obj_)
            obj_.original_tagname_ = 'item'
# end class relativesType


class itemType9(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, type_id=None, updated_at=None, type_=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(int, id)
        self.id_nsprefix_ = None
        self.type_id = _cast(int, type_id)
        self.type_id_nsprefix_ = None
        if isinstance(updated_at, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = updated_at
        self.updated_at = initvalue_
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, itemType9)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if itemType9.subclass:
            return itemType9.subclass(*args_, **kwargs_)
        else:
            return itemType9(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_type_id(self):
        return self.type_id
    def set_type_id(self, type_id):
        self.type_id = type_id
    def get_updated_at(self):
        return self.updated_at
    def set_updated_at(self, updated_at):
        self.updated_at = updated_at
    def get_type(self):
        return self.type_
    def set_type(self, type_):
        self.type_ = type_
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.itemType9_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        if self.id is not None:
            dbobj.id_x = self.id
        if self.type_id is not None:
            dbobj.type_id = self.type_id
        if self.updated_at is not None:
            dbobj.updated_at = self.updated_at
        if self.type_ is not None:
            dbobj.type_x = self.type_
    def exportDjangoChildren(self, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = self.gds_parse_integer(value, node, 'id')
        value = find_attr_value_('type_id', node)
        if value is not None and 'type_id' not in already_processed:
            already_processed.add('type_id')
            self.type_id = self.gds_parse_integer(value, node, 'type_id')
        value = find_attr_value_('updated_at', node)
        if value is not None and 'updated_at' not in already_processed:
            already_processed.add('updated_at')
            try:
                self.updated_at = self.gds_parse_datetime(value)
            except ValueError as exp:
                raise ValueError('Bad date-time attribute (updated_at): %s' % exp)
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class itemType9


class persdocsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, item=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if item is None:
            self.item = []
        else:
            self.item = item
        self.item_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, persdocsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if persdocsType.subclass:
            return persdocsType.subclass(*args_, **kwargs_)
        else:
            return persdocsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_item(self):
        return self.item
    def set_item(self, item):
        self.item = item
    def add_item(self, value):
        self.item.append(value)
    def insert_item_at(self, index, value):
        self.item.insert(index, value)
    def replace_item_at(self, index, value):
        self.item[index] = value
    def hasContent_(self):
        if (
            self.item
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.persdocsType_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        pass
    def exportDjangoChildren(self, dbobj):
        for child in self.item:
            child_dbobj = child.exportDjango()
            dbobj.itemType10_model_item.add(child_dbobj)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'item':
            obj_ = itemType10.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.item.append(obj_)
            obj_.original_tagname_ = 'item'
# end class persdocsType


class itemType10(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, updated_at=None, date_start=None, date_end=None, name=None, mserial=None, number=None, common=None, issuing_country=None, issue=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(int, id)
        self.id_nsprefix_ = None
        if isinstance(updated_at, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = updated_at
        self.updated_at = initvalue_
        self.date_start = _cast(None, date_start)
        self.date_start_nsprefix_ = None
        self.date_end = _cast(None, date_end)
        self.date_end_nsprefix_ = None
        self.name = name
        self.name_nsprefix_ = None
        self.mserial = mserial
        self.mserial_nsprefix_ = None
        self.number = number
        self.number_nsprefix_ = None
        self.common = common
        self.common_nsprefix_ = None
        self.issuing_country = issuing_country
        self.issuing_country_nsprefix_ = None
        self.issue = issue
        self.issue_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, itemType10)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if itemType10.subclass:
            return itemType10.subclass(*args_, **kwargs_)
        else:
            return itemType10(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_mserial(self):
        return self.mserial
    def set_mserial(self, mserial):
        self.mserial = mserial
    def get_number(self):
        return self.number
    def set_number(self, number):
        self.number = number
    def get_common(self):
        return self.common
    def set_common(self, common):
        self.common = common
    def get_issuing_country(self):
        return self.issuing_country
    def set_issuing_country(self, issuing_country):
        self.issuing_country = issuing_country
    def get_issue(self):
        return self.issue
    def set_issue(self, issue):
        self.issue = issue
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_updated_at(self):
        return self.updated_at
    def set_updated_at(self, updated_at):
        self.updated_at = updated_at
    def get_date_start(self):
        return self.date_start
    def set_date_start(self, date_start):
        self.date_start = date_start
    def get_date_end(self):
        return self.date_end
    def set_date_end(self, date_end):
        self.date_end = date_end
    def hasContent_(self):
        if (
            self.name is not None or
            self.mserial is not None or
            self.number is not None or
            self.common is not None or
            self.issuing_country is not None or
            self.issue is not None
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.itemType10_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        if self.id is not None:
            dbobj.id_x = self.id
        if self.updated_at is not None:
            dbobj.updated_at = self.updated_at
        if self.date_start is not None:
            dbobj.date_start = self.date_start
        if self.date_end is not None:
            dbobj.date_end = self.date_end
    def exportDjangoChildren(self, dbobj):
        if self.name is not None:
            dbobj.name = self.name
        if self.mserial is not None:
            dbobj.mserial = self.mserial
        if self.number is not None:
            dbobj.number = self.number
        if self.common is not None:
            dbobj.common = self.common
        if self.issuing_country is not None:
            dbobj.issuing_country = self.issuing_country
        if self.issue is not None:
            dbobj.issue = self.issue
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = self.gds_parse_integer(value, node, 'id')
        value = find_attr_value_('updated_at', node)
        if value is not None and 'updated_at' not in already_processed:
            already_processed.add('updated_at')
            try:
                self.updated_at = self.gds_parse_datetime(value)
            except ValueError as exp:
                raise ValueError('Bad date-time attribute (updated_at): %s' % exp)
        value = find_attr_value_('date_start', node)
        if value is not None and 'date_start' not in already_processed:
            already_processed.add('date_start')
            self.date_start = value
        value = find_attr_value_('date_end', node)
        if value is not None and 'date_end' not in already_processed:
            already_processed.add('date_end')
            self.date_end = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
        elif nodeName_ == 'mserial':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'mserial')
            value_ = self.gds_validate_string(value_, node, 'mserial')
            self.mserial = value_
            self.mserial_nsprefix_ = child_.prefix
        elif nodeName_ == 'number':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'number')
            value_ = self.gds_validate_string(value_, node, 'number')
            self.number = value_
            self.number_nsprefix_ = child_.prefix
        elif nodeName_ == 'common':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'common')
            value_ = self.gds_validate_string(value_, node, 'common')
            self.common = value_
            self.common_nsprefix_ = child_.prefix
        elif nodeName_ == 'issuing_country':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'issuing_country')
            value_ = self.gds_validate_string(value_, node, 'issuing_country')
            self.issuing_country = value_
            self.issuing_country_nsprefix_ = child_.prefix
        elif nodeName_ == 'issue':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'issue')
            value_ = self.gds_validate_string(value_, node, 'issue')
            self.issue = value_
            self.issue_nsprefix_ = child_.prefix
# end class itemType10


class countriesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, item=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if item is None:
            self.item = []
        else:
            self.item = item
        self.item_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, countriesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if countriesType.subclass:
            return countriesType.subclass(*args_, **kwargs_)
        else:
            return countriesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_item(self):
        return self.item
    def set_item(self, item):
        self.item = item
    def add_item(self, value):
        self.item.append(value)
    def insert_item_at(self, index, value):
        self.item.insert(index, value)
    def replace_item_at(self, index, value):
        self.item[index] = value
    def hasContent_(self):
        if (
            self.item
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.countriesType_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        pass
    def exportDjangoChildren(self, dbobj):
        for child in self.item:
            child_dbobj = child.exportDjango()
            dbobj.itemType11_model_item.add(child_dbobj)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'item':
            obj_ = itemType11.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.item.append(obj_)
            obj_.original_tagname_ = 'item'
# end class countriesType


class itemType11(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, updated_at=None, iso=None, en=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(int, id)
        self.id_nsprefix_ = None
        if isinstance(updated_at, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = updated_at
        self.updated_at = initvalue_
        self.iso = _cast(None, iso)
        self.iso_nsprefix_ = None
        self.en = _cast(None, en)
        self.en_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, itemType11)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if itemType11.subclass:
            return itemType11.subclass(*args_, **kwargs_)
        else:
            return itemType11(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_updated_at(self):
        return self.updated_at
    def set_updated_at(self, updated_at):
        self.updated_at = updated_at
    def get_iso(self):
        return self.iso
    def set_iso(self, iso):
        self.iso = iso
    def get_en(self):
        return self.en
    def set_en(self, en):
        self.en = en
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.itemType11_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        if self.id is not None:
            dbobj.id_x = self.id
        if self.updated_at is not None:
            dbobj.updated_at = self.updated_at
        if self.iso is not None:
            dbobj.iso = self.iso
        if self.en is not None:
            dbobj.en = self.en
    def exportDjangoChildren(self, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = self.gds_parse_integer(value, node, 'id')
        value = find_attr_value_('updated_at', node)
        if value is not None and 'updated_at' not in already_processed:
            already_processed.add('updated_at')
            try:
                self.updated_at = self.gds_parse_datetime(value)
            except ValueError as exp:
                raise ValueError('Bad date-time attribute (updated_at): %s' % exp)
        value = find_attr_value_('iso', node)
        if value is not None and 'iso' not in already_processed:
            already_processed.add('iso')
            self.iso = value
        value = find_attr_value_('en', node)
        if value is not None and 'en' not in already_processed:
            already_processed.add('en')
            self.en = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class itemType11


class categoriesType12(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, item=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if item is None:
            self.item = []
        else:
            self.item = item
        self.item_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, categoriesType12)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if categoriesType12.subclass:
            return categoriesType12.subclass(*args_, **kwargs_)
        else:
            return categoriesType12(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_item(self):
        return self.item
    def set_item(self, item):
        self.item = item
    def add_item(self, value):
        self.item.append(value)
    def insert_item_at(self, index, value):
        self.item.insert(index, value)
    def replace_item_at(self, index, value):
        self.item[index] = value
    def hasContent_(self):
        if (
            self.item
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.categoriesType12_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        pass
    def exportDjangoChildren(self, dbobj):
        dbobj.item = json_.dumps(self.item, separators=(',', ':'))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'item':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'item')
            value_ = self.gds_validate_string(value_, node, 'item')
            self.item.append(value_)
            self.item_nsprefix_ = child_.prefix
# end class categoriesType12


class addressesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, item=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if item is None:
            self.item = []
        else:
            self.item = item
        self.item_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, addressesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if addressesType.subclass:
            return addressesType.subclass(*args_, **kwargs_)
        else:
            return addressesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_item(self):
        return self.item
    def set_item(self, item):
        self.item = item
    def add_item(self, value):
        self.item.append(value)
    def insert_item_at(self, index, value):
        self.item.insert(index, value)
    def replace_item_at(self, index, value):
        self.item[index] = value
    def hasContent_(self):
        if (
            self.item
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.addressesType_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        pass
    def exportDjangoChildren(self, dbobj):
        for child in self.item:
            child_dbobj = child.exportDjango()
            dbobj.itemType13_model_item.add(child_dbobj)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'item':
            obj_ = itemType13.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.item.append(obj_)
            obj_.original_tagname_ = 'item'
# end class addressesType


class itemType13(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, updated_at=None, city=None, address=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(int, id)
        self.id_nsprefix_ = None
        if isinstance(updated_at, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = updated_at
        self.updated_at = initvalue_
        self.city = city
        self.city_nsprefix_ = None
        self.address = address
        self.address_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, itemType13)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if itemType13.subclass:
            return itemType13.subclass(*args_, **kwargs_)
        else:
            return itemType13(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_city(self):
        return self.city
    def set_city(self, city):
        self.city = city
    def get_address(self):
        return self.address
    def set_address(self, address):
        self.address = address
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_updated_at(self):
        return self.updated_at
    def set_updated_at(self, updated_at):
        self.updated_at = updated_at
    def hasContent_(self):
        if (
            self.city is not None or
            self.address is not None
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.itemType13_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        if self.id is not None:
            dbobj.id_x = self.id
        if self.updated_at is not None:
            dbobj.updated_at = self.updated_at
    def exportDjangoChildren(self, dbobj):
        if self.city is not None:
            dbobj.city = self.city
        if self.address is not None:
            dbobj.address = self.address
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = self.gds_parse_integer(value, node, 'id')
        value = find_attr_value_('updated_at', node)
        if value is not None and 'updated_at' not in already_processed:
            already_processed.add('updated_at')
            try:
                self.updated_at = self.gds_parse_datetime(value)
            except ValueError as exp:
                raise ValueError('Bad date-time attribute (updated_at): %s' % exp)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'city':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'city')
            value_ = self.gds_validate_string(value_, node, 'city')
            self.city = value_
            self.city_nsprefix_ = child_.prefix
        elif nodeName_ == 'address':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'address')
            value_ = self.gds_validate_string(value_, node, 'address')
            self.address = value_
            self.address_nsprefix_ = child_.prefix
# end class itemType13


class contact_infosType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, item=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if item is None:
            self.item = []
        else:
            self.item = item
        self.item_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, contact_infosType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if contact_infosType.subclass:
            return contact_infosType.subclass(*args_, **kwargs_)
        else:
            return contact_infosType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_item(self):
        return self.item
    def set_item(self, item):
        self.item = item
    def add_item(self, value):
        self.item.append(value)
    def insert_item_at(self, index, value):
        self.item.insert(index, value)
    def replace_item_at(self, index, value):
        self.item[index] = value
    def hasContent_(self):
        if (
            self.item
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.contact_infosType_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        pass
    def exportDjangoChildren(self, dbobj):
        for child in self.item:
            child_dbobj = child.exportDjango()
            dbobj.itemType14_model_item.add(child_dbobj)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'item':
            obj_ = itemType14.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.item.append(obj_)
            obj_.original_tagname_ = 'item'
# end class contact_infosType


class itemType14(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, type_=None, updated_at=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(int, id)
        self.id_nsprefix_ = None
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = None
        if isinstance(updated_at, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = updated_at
        self.updated_at = initvalue_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, itemType14)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if itemType14.subclass:
            return itemType14.subclass(*args_, **kwargs_)
        else:
            return itemType14(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_type(self):
        return self.type_
    def set_type(self, type_):
        self.type_ = type_
    def get_updated_at(self):
        return self.updated_at
    def set_updated_at(self, updated_at):
        self.updated_at = updated_at
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.itemType14_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        if self.id is not None:
            dbobj.id_x = self.id
        if self.type_ is not None:
            dbobj.type_x = self.type_
        if self.updated_at is not None:
            dbobj.updated_at = self.updated_at
    def exportDjangoChildren(self, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = self.gds_parse_integer(value, node, 'id')
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
        value = find_attr_value_('updated_at', node)
        if value is not None and 'updated_at' not in already_processed:
            already_processed.add('updated_at')
            try:
                self.updated_at = self.gds_parse_datetime(value)
            except ValueError as exp:
                raise ValueError('Bad date-time attribute (updated_at): %s' % exp)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class itemType14


class sanlistsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, item=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if item is None:
            self.item = []
        else:
            self.item = item
        self.item_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, sanlistsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if sanlistsType.subclass:
            return sanlistsType.subclass(*args_, **kwargs_)
        else:
            return sanlistsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_item(self):
        return self.item
    def set_item(self, item):
        self.item = item
    def add_item(self, value):
        self.item.append(value)
    def insert_item_at(self, index, value):
        self.item.insert(index, value)
    def replace_item_at(self, index, value):
        self.item[index] = value
    def hasContent_(self):
        if (
            self.item
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.sanlistsType_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        pass
    def exportDjangoChildren(self, dbobj):
        for child in self.item:
            child_dbobj = child.exportDjango()
            dbobj.itemType15_model_item.add(child_dbobj)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'item':
            obj_ = itemType15.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.item.append(obj_)
            obj_.original_tagname_ = 'item'
# end class sanlistsType


class itemType15(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, updated_at=None, sanlist_id=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(int, id)
        self.id_nsprefix_ = None
        if isinstance(updated_at, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = updated_at
        self.updated_at = initvalue_
        self.sanlist_id = _cast(int, sanlist_id)
        self.sanlist_id_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, itemType15)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if itemType15.subclass:
            return itemType15.subclass(*args_, **kwargs_)
        else:
            return itemType15(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_updated_at(self):
        return self.updated_at
    def set_updated_at(self, updated_at):
        self.updated_at = updated_at
    def get_sanlist_id(self):
        return self.sanlist_id
    def set_sanlist_id(self, sanlist_id):
        self.sanlist_id = sanlist_id
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.itemType15_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        if self.id is not None:
            dbobj.id_x = self.id
        if self.updated_at is not None:
            dbobj.updated_at = self.updated_at
        if self.sanlist_id is not None:
            dbobj.sanlist_id = self.sanlist_id
    def exportDjangoChildren(self, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = self.gds_parse_integer(value, node, 'id')
        value = find_attr_value_('updated_at', node)
        if value is not None and 'updated_at' not in already_processed:
            already_processed.add('updated_at')
            try:
                self.updated_at = self.gds_parse_datetime(value)
            except ValueError as exp:
                raise ValueError('Bad date-time attribute (updated_at): %s' % exp)
        value = find_attr_value_('sanlist_id', node)
        if value is not None and 'sanlist_id' not in already_processed:
            already_processed.add('sanlist_id')
            self.sanlist_id = self.gds_parse_integer(value, node, 'sanlist_id')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class itemType15


class licensesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, item=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if item is None:
            self.item = []
        else:
            self.item = item
        self.item_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, licensesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if licensesType.subclass:
            return licensesType.subclass(*args_, **kwargs_)
        else:
            return licensesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_item(self):
        return self.item
    def set_item(self, item):
        self.item = item
    def add_item(self, value):
        self.item.append(value)
    def insert_item_at(self, index, value):
        self.item.insert(index, value)
    def replace_item_at(self, index, value):
        self.item[index] = value
    def hasContent_(self):
        if (
            self.item
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.licensesType_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        pass
    def exportDjangoChildren(self, dbobj):
        for child in self.item:
            child_dbobj = child.exportDjango()
            dbobj.itemType16_model_item.add(child_dbobj)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'item':
            obj_ = itemType16.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.item.append(obj_)
            obj_.original_tagname_ = 'item'
# end class licensesType


class itemType16(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, date_end=None, date_start=None, id=None, updated_at=None, sanlist_id=None, sanlist=None, source=None, fifty=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.date_end = _cast(None, date_end)
        self.date_end_nsprefix_ = None
        self.date_start = _cast(None, date_start)
        self.date_start_nsprefix_ = None
        self.id = _cast(int, id)
        self.id_nsprefix_ = None
        if isinstance(updated_at, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = updated_at
        self.updated_at = initvalue_
        self.sanlist_id = _cast(int, sanlist_id)
        self.sanlist_id_nsprefix_ = None
        self.sanlist = _cast(None, sanlist)
        self.sanlist_nsprefix_ = None
        self.source = _cast(None, source)
        self.source_nsprefix_ = None
        self.fifty = _cast(bool, fifty)
        self.fifty_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, itemType16)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if itemType16.subclass:
            return itemType16.subclass(*args_, **kwargs_)
        else:
            return itemType16(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_date_end(self):
        return self.date_end
    def set_date_end(self, date_end):
        self.date_end = date_end
    def get_date_start(self):
        return self.date_start
    def set_date_start(self, date_start):
        self.date_start = date_start
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_updated_at(self):
        return self.updated_at
    def set_updated_at(self, updated_at):
        self.updated_at = updated_at
    def get_sanlist_id(self):
        return self.sanlist_id
    def set_sanlist_id(self, sanlist_id):
        self.sanlist_id = sanlist_id
    def get_sanlist(self):
        return self.sanlist
    def set_sanlist(self, sanlist):
        self.sanlist = sanlist
    def get_source(self):
        return self.source
    def set_source(self, source):
        self.source = source
    def get_fifty(self):
        return self.fifty
    def set_fifty(self, fifty):
        self.fifty = fifty
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.itemType16_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        if self.date_end is not None:
            dbobj.date_end = self.date_end
        if self.date_start is not None:
            dbobj.date_start = self.date_start
        if self.id is not None:
            dbobj.id_x = self.id
        if self.updated_at is not None:
            dbobj.updated_at = self.updated_at
        if self.sanlist_id is not None:
            dbobj.sanlist_id = self.sanlist_id
        if self.sanlist is not None:
            dbobj.sanlist = self.sanlist
        if self.source is not None:
            dbobj.source = self.source
        if self.fifty is not None:
            dbobj.fifty = self.fifty
    def exportDjangoChildren(self, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('date_end', node)
        if value is not None and 'date_end' not in already_processed:
            already_processed.add('date_end')
            self.date_end = value
        value = find_attr_value_('date_start', node)
        if value is not None and 'date_start' not in already_processed:
            already_processed.add('date_start')
            self.date_start = value
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = self.gds_parse_integer(value, node, 'id')
        value = find_attr_value_('updated_at', node)
        if value is not None and 'updated_at' not in already_processed:
            already_processed.add('updated_at')
            try:
                self.updated_at = self.gds_parse_datetime(value)
            except ValueError as exp:
                raise ValueError('Bad date-time attribute (updated_at): %s' % exp)
        value = find_attr_value_('sanlist_id', node)
        if value is not None and 'sanlist_id' not in already_processed:
            already_processed.add('sanlist_id')
            self.sanlist_id = self.gds_parse_integer(value, node, 'sanlist_id')
        value = find_attr_value_('sanlist', node)
        if value is not None and 'sanlist' not in already_processed:
            already_processed.add('sanlist')
            self.sanlist = value
        value = find_attr_value_('source', node)
        if value is not None and 'source' not in already_processed:
            already_processed.add('source')
            self.source = value
        value = find_attr_value_('fifty', node)
        if value is not None and 'fifty' not in already_processed:
            already_processed.add('fifty')
            if value in ('true', '1'):
                self.fifty = True
            elif value in ('false', '0'):
                self.fifty = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class itemType16


class sanctionsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, item=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if item is None:
            self.item = []
        else:
            self.item = item
        self.item_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, sanctionsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if sanctionsType.subclass:
            return sanctionsType.subclass(*args_, **kwargs_)
        else:
            return sanctionsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_item(self):
        return self.item
    def set_item(self, item):
        self.item = item
    def add_item(self, value):
        self.item.append(value)
    def insert_item_at(self, index, value):
        self.item.insert(index, value)
    def replace_item_at(self, index, value):
        self.item[index] = value
    def hasContent_(self):
        if (
            self.item
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.sanctionsType_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        pass
    def exportDjangoChildren(self, dbobj):
        for child in self.item:
            child_dbobj = child.exportDjango()
            dbobj.itemType17_model_item.add(child_dbobj)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'item':
            obj_ = itemType17.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.item.append(obj_)
            obj_.original_tagname_ = 'item'
# end class sanctionsType


class itemType17(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, updated_at=None, date_start=None, date_end=None, sanction=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(int, id)
        self.id_nsprefix_ = None
        if isinstance(updated_at, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = updated_at
        self.updated_at = initvalue_
        self.date_start = _cast(None, date_start)
        self.date_start_nsprefix_ = None
        self.date_end = _cast(None, date_end)
        self.date_end_nsprefix_ = None
        self.sanction = sanction
        self.sanction_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, itemType17)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if itemType17.subclass:
            return itemType17.subclass(*args_, **kwargs_)
        else:
            return itemType17(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_sanction(self):
        return self.sanction
    def set_sanction(self, sanction):
        self.sanction = sanction
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_updated_at(self):
        return self.updated_at
    def set_updated_at(self, updated_at):
        self.updated_at = updated_at
    def get_date_start(self):
        return self.date_start
    def set_date_start(self, date_start):
        self.date_start = date_start
    def get_date_end(self):
        return self.date_end
    def set_date_end(self, date_end):
        self.date_end = date_end
    def hasContent_(self):
        if (
            self.sanction is not None
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.itemType17_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        if self.id is not None:
            dbobj.id_x = self.id
        if self.updated_at is not None:
            dbobj.updated_at = self.updated_at
        if self.date_start is not None:
            dbobj.date_start = self.date_start
        if self.date_end is not None:
            dbobj.date_end = self.date_end
    def exportDjangoChildren(self, dbobj):
        if self.sanction is not None:
            child_dbobj = self.sanction.exportDjango()
            dbobj.sanctionType_model_sanction = child_dbobj
            child_dbobj.save()
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = self.gds_parse_integer(value, node, 'id')
        value = find_attr_value_('updated_at', node)
        if value is not None and 'updated_at' not in already_processed:
            already_processed.add('updated_at')
            try:
                self.updated_at = self.gds_parse_datetime(value)
            except ValueError as exp:
                raise ValueError('Bad date-time attribute (updated_at): %s' % exp)
        value = find_attr_value_('date_start', node)
        if value is not None and 'date_start' not in already_processed:
            already_processed.add('date_start')
            self.date_start = value
        value = find_attr_value_('date_end', node)
        if value is not None and 'date_end' not in already_processed:
            already_processed.add('date_end')
            self.date_end = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'sanction':
            obj_ = sanctionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.sanction = obj_
            obj_.original_tagname_ = 'sanction'
# end class itemType17


class sanctionType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, sanlist_id=None, sanction_id=None, source=None, reason_inclusion=None, sanlist=None, country=None, extra_informations=None, uid=None, last_update_in_source=None, reference_number=None, program_number=None, type_name=None, type_tag=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.sanlist_id = _cast(int, sanlist_id)
        self.sanlist_id_nsprefix_ = None
        self.sanction_id = _cast(int, sanction_id)
        self.sanction_id_nsprefix_ = None
        self.source = _cast(None, source)
        self.source_nsprefix_ = None
        self.reason_inclusion = _cast(None, reason_inclusion)
        self.reason_inclusion_nsprefix_ = None
        self.sanlist = _cast(None, sanlist)
        self.sanlist_nsprefix_ = None
        self.country = _cast(None, country)
        self.country_nsprefix_ = None
        self.extra_informations = _cast(None, extra_informations)
        self.extra_informations_nsprefix_ = None
        self.uid = _cast(None, uid)
        self.uid_nsprefix_ = None
        self.last_update_in_source = _cast(None, last_update_in_source)
        self.last_update_in_source_nsprefix_ = None
        self.reference_number = _cast(None, reference_number)
        self.reference_number_nsprefix_ = None
        self.program_number = _cast(None, program_number)
        self.program_number_nsprefix_ = None
        self.type_name = _cast(None, type_name)
        self.type_name_nsprefix_ = None
        self.type_tag = _cast(None, type_tag)
        self.type_tag_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, sanctionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if sanctionType.subclass:
            return sanctionType.subclass(*args_, **kwargs_)
        else:
            return sanctionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_sanlist_id(self):
        return self.sanlist_id
    def set_sanlist_id(self, sanlist_id):
        self.sanlist_id = sanlist_id
    def get_sanction_id(self):
        return self.sanction_id
    def set_sanction_id(self, sanction_id):
        self.sanction_id = sanction_id
    def get_source(self):
        return self.source
    def set_source(self, source):
        self.source = source
    def get_reason_inclusion(self):
        return self.reason_inclusion
    def set_reason_inclusion(self, reason_inclusion):
        self.reason_inclusion = reason_inclusion
    def get_sanlist(self):
        return self.sanlist
    def set_sanlist(self, sanlist):
        self.sanlist = sanlist
    def get_country(self):
        return self.country
    def set_country(self, country):
        self.country = country
    def get_extra_informations(self):
        return self.extra_informations
    def set_extra_informations(self, extra_informations):
        self.extra_informations = extra_informations
    def get_uid(self):
        return self.uid
    def set_uid(self, uid):
        self.uid = uid
    def get_last_update_in_source(self):
        return self.last_update_in_source
    def set_last_update_in_source(self, last_update_in_source):
        self.last_update_in_source = last_update_in_source
    def get_reference_number(self):
        return self.reference_number
    def set_reference_number(self, reference_number):
        self.reference_number = reference_number
    def get_program_number(self):
        return self.program_number
    def set_program_number(self, program_number):
        self.program_number = program_number
    def get_type_name(self):
        return self.type_name
    def set_type_name(self, type_name):
        self.type_name = type_name
    def get_type_tag(self):
        return self.type_tag
    def set_type_tag(self, type_tag):
        self.type_tag = type_tag
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.sanctionType_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        if self.sanlist_id is not None:
            dbobj.sanlist_id = self.sanlist_id
        if self.sanction_id is not None:
            dbobj.sanction_id = self.sanction_id
        if self.source is not None:
            dbobj.source = self.source
        if self.reason_inclusion is not None:
            dbobj.reason_inclusion = self.reason_inclusion
        if self.sanlist is not None:
            dbobj.sanlist = self.sanlist
        if self.country is not None:
            dbobj.country = self.country
        if self.extra_informations is not None:
            dbobj.extra_informations = self.extra_informations
        if self.uid is not None:
            dbobj.uid = self.uid
        if self.last_update_in_source is not None:
            dbobj.last_update_in_source = self.last_update_in_source
        if self.reference_number is not None:
            dbobj.reference_number = self.reference_number
        if self.program_number is not None:
            dbobj.program_number = self.program_number
        if self.type_name is not None:
            dbobj.type_name = self.type_name
        if self.type_tag is not None:
            dbobj.type_tag = self.type_tag
    def exportDjangoChildren(self, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('sanlist_id', node)
        if value is not None and 'sanlist_id' not in already_processed:
            already_processed.add('sanlist_id')
            self.sanlist_id = self.gds_parse_integer(value, node, 'sanlist_id')
        value = find_attr_value_('sanction_id', node)
        if value is not None and 'sanction_id' not in already_processed:
            already_processed.add('sanction_id')
            self.sanction_id = self.gds_parse_integer(value, node, 'sanction_id')
        value = find_attr_value_('source', node)
        if value is not None and 'source' not in already_processed:
            already_processed.add('source')
            self.source = value
        value = find_attr_value_('reason_inclusion', node)
        if value is not None and 'reason_inclusion' not in already_processed:
            already_processed.add('reason_inclusion')
            self.reason_inclusion = value
        value = find_attr_value_('sanlist', node)
        if value is not None and 'sanlist' not in already_processed:
            already_processed.add('sanlist')
            self.sanlist = value
        value = find_attr_value_('country', node)
        if value is not None and 'country' not in already_processed:
            already_processed.add('country')
            self.country = value
        value = find_attr_value_('extra_informations', node)
        if value is not None and 'extra_informations' not in already_processed:
            already_processed.add('extra_informations')
            self.extra_informations = value
        value = find_attr_value_('uid', node)
        if value is not None and 'uid' not in already_processed:
            already_processed.add('uid')
            self.uid = value
        value = find_attr_value_('last_update_in_source', node)
        if value is not None and 'last_update_in_source' not in already_processed:
            already_processed.add('last_update_in_source')
            self.last_update_in_source = value
        value = find_attr_value_('reference_number', node)
        if value is not None and 'reference_number' not in already_processed:
            already_processed.add('reference_number')
            self.reference_number = value
        value = find_attr_value_('program_number', node)
        if value is not None and 'program_number' not in already_processed:
            already_processed.add('program_number')
            self.program_number = value
        value = find_attr_value_('type_name', node)
        if value is not None and 'type_name' not in already_processed:
            already_processed.add('type_name')
            self.type_name = value
        value = find_attr_value_('type_tag', node)
        if value is not None and 'type_tag' not in already_processed:
            already_processed.add('type_tag')
            self.type_tag = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class sanctionType


class watch_listsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, item=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if item is None:
            self.item = []
        else:
            self.item = item
        self.item_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, watch_listsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if watch_listsType.subclass:
            return watch_listsType.subclass(*args_, **kwargs_)
        else:
            return watch_listsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_item(self):
        return self.item
    def set_item(self, item):
        self.item = item
    def add_item(self, value):
        self.item.append(value)
    def insert_item_at(self, index, value):
        self.item.insert(index, value)
    def replace_item_at(self, index, value):
        self.item[index] = value
    def hasContent_(self):
        if (
            self.item
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.watch_listsType_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        pass
    def exportDjangoChildren(self, dbobj):
        for child in self.item:
            child_dbobj = child.exportDjango()
            dbobj.itemType18_model_item.add(child_dbobj)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'item':
            obj_ = itemType18.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.item.append(obj_)
            obj_.original_tagname_ = 'item'
# end class watch_listsType


class itemType18(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, updated_at=None, date_start=None, date_end=None, watch_list=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(int, id)
        self.id_nsprefix_ = None
        if isinstance(updated_at, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = updated_at
        self.updated_at = initvalue_
        self.date_start = _cast(None, date_start)
        self.date_start_nsprefix_ = None
        self.date_end = _cast(None, date_end)
        self.date_end_nsprefix_ = None
        self.watch_list = watch_list
        self.watch_list_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, itemType18)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if itemType18.subclass:
            return itemType18.subclass(*args_, **kwargs_)
        else:
            return itemType18(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_watch_list(self):
        return self.watch_list
    def set_watch_list(self, watch_list):
        self.watch_list = watch_list
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_updated_at(self):
        return self.updated_at
    def set_updated_at(self, updated_at):
        self.updated_at = updated_at
    def get_date_start(self):
        return self.date_start
    def set_date_start(self, date_start):
        self.date_start = date_start
    def get_date_end(self):
        return self.date_end
    def set_date_end(self, date_end):
        self.date_end = date_end
    def hasContent_(self):
        if (
            self.watch_list is not None
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.itemType18_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        if self.id is not None:
            dbobj.id_x = self.id
        if self.updated_at is not None:
            dbobj.updated_at = self.updated_at
        if self.date_start is not None:
            dbobj.date_start = self.date_start
        if self.date_end is not None:
            dbobj.date_end = self.date_end
    def exportDjangoChildren(self, dbobj):
        if self.watch_list is not None:
            child_dbobj = self.watch_list.exportDjango()
            dbobj.watch_listType_model_watch_list = child_dbobj
            child_dbobj.save()
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = self.gds_parse_integer(value, node, 'id')
        value = find_attr_value_('updated_at', node)
        if value is not None and 'updated_at' not in already_processed:
            already_processed.add('updated_at')
            try:
                self.updated_at = self.gds_parse_datetime(value)
            except ValueError as exp:
                raise ValueError('Bad date-time attribute (updated_at): %s' % exp)
        value = find_attr_value_('date_start', node)
        if value is not None and 'date_start' not in already_processed:
            already_processed.add('date_start')
            self.date_start = value
        value = find_attr_value_('date_end', node)
        if value is not None and 'date_end' not in already_processed:
            already_processed.add('date_end')
            self.date_end = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'watch_list':
            obj_ = watch_listType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.watch_list = obj_
            obj_.original_tagname_ = 'watch_list'
# end class itemType18


class watch_listType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, list_id=None, country=None, authority=None, extra_information=None, source=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.list_id = _cast(int, list_id)
        self.list_id_nsprefix_ = None
        self.country = _cast(None, country)
        self.country_nsprefix_ = None
        self.authority = _cast(None, authority)
        self.authority_nsprefix_ = None
        self.extra_information = _cast(None, extra_information)
        self.extra_information_nsprefix_ = None
        self.source = _cast(None, source)
        self.source_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, watch_listType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if watch_listType.subclass:
            return watch_listType.subclass(*args_, **kwargs_)
        else:
            return watch_listType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_list_id(self):
        return self.list_id
    def set_list_id(self, list_id):
        self.list_id = list_id
    def get_country(self):
        return self.country
    def set_country(self, country):
        self.country = country
    def get_authority(self):
        return self.authority
    def set_authority(self, authority):
        self.authority = authority
    def get_extra_information(self):
        return self.extra_information
    def set_extra_information(self, extra_information):
        self.extra_information = extra_information
    def get_source(self):
        return self.source
    def set_source(self, source):
        self.source = source
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def exportDjango(self):
        """Export to Django database/ORM.
        Must run in the Django environment.
        Example:
            $ python manage.py shell
            IPython 6.5.0 -- An enhanced Interactive Python.
            Type '?' for help.
            In [1]:
            In [1]: %run load_my_data.py mailbox01.xml
        where load_my_data.py is a python script that (1) uses a
            module generated by generateDS to parse an
            XML instance doc, then (2) calls the exportDjango
            method.
            Example:
                import gds_mod
                rootObj = gds_mod.parse(infilename, silence=True)
                rootObj.exportDjango()
        """
        self.gds_djo_etl_transform()
        dbobj = models_.watch_listType_model()
        dbobj.save()
        self.exportDjangoAttributes(dbobj)
        self.exportDjangoChildren(dbobj)
        dbobj.save()
        self.gds_djo_etl_transform_db_obj(dbobj)
        return dbobj
    def exportDjangoAttributes(self, dbobj):
        if self.list_id is not None:
            dbobj.list_id = self.list_id
        if self.country is not None:
            dbobj.country = self.country
        if self.authority is not None:
            dbobj.authority = self.authority
        if self.extra_information is not None:
            dbobj.extra_information = self.extra_information
        if self.source is not None:
            dbobj.source = self.source
    def exportDjangoChildren(self, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('list_id', node)
        if value is not None and 'list_id' not in already_processed:
            already_processed.add('list_id')
            self.list_id = self.gds_parse_integer(value, node, 'list_id')
        value = find_attr_value_('country', node)
        if value is not None and 'country' not in already_processed:
            already_processed.add('country')
            self.country = value
        value = find_attr_value_('authority', node)
        if value is not None and 'authority' not in already_processed:
            already_processed.add('authority')
            self.authority = value
        value = find_attr_value_('extra_information', node)
        if value is not None and 'extra_information' not in already_processed:
            already_processed.add('extra_information')
            self.extra_information = value
        value = find_attr_value_('source', node)
        if value is not None and 'source' not in already_processed:
            already_processed.add('source')
            self.source = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class watch_listType


GDSClassesMapping = {
}


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = GDSClassesMapping.get(tag)
    if rootClass is None:
        rootClass = globals().get(tag)
    return tag, rootClass


def get_required_ns_prefix_defs(rootNode):
    '''Get all name space prefix definitions required in this XML doc.
    Return a dictionary of definitions and a char string of definitions.
    '''
    nsmap = {
        prefix: uri
        for node in rootNode.iter()
        for (prefix, uri) in node.nsmap.items()
        if prefix is not None
    }
    namespacedefs = ' '.join([
        'xmlns:{}="{}"'.format(prefix, uri)
        for prefix, uri in nsmap.items()
    ])
    return nsmap, namespacedefs


def parse(inFileName, silence=False, print_warnings=True):
    global CapturedNsmap_
    gds_collector = GdsCollector_()
    parser = None
    doc = parsexml_(inFileName, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'response'
        rootClass = response
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    CapturedNsmap_, namespacedefs = get_required_ns_prefix_defs(rootNode)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_=namespacedefs,
            pretty_print=True)
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseEtree(inFileName, silence=False, print_warnings=True,
               mapping=None, nsmap=None):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'response'
        rootClass = response
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if mapping is None:
        mapping = {}
    rootElement = rootObj.to_etree(
        None, name_=rootTag, mapping_=mapping, nsmap_=nsmap)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(str(content))
        sys.stdout.write('\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False, print_warnings=True):
    '''Parse a string, create the object tree, and export it.

    Arguments:
    - inString -- A string.  This XML fragment should not start
      with an XML declaration containing an encoding.
    - silence -- A boolean.  If False, export the object.
    Returns -- The root object in the tree.
    '''
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    gds_collector = GdsCollector_()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'response'
        rootClass = response
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseLiteral(inFileName, silence=False, print_warnings=True):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'response'
        rootClass = response
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from People3 import *\n\n')
        sys.stdout.write('import People3 as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

RenameMappings_ = {
}

#
# Mapping of namespaces to types defined in them
# and the file in which each is defined.
# simpleTypes are marked "ST" and complexTypes "CT".
NamespaceToDefMappings_ = {}

__all__ = [
    "addressesType",
    "authorityType",
    "categoriesType",
    "categoriesType12",
    "category_407Type",
    "category_407Type5",
    "contact_infosType",
    "countriesType",
    "dob_extraType",
    "dod_extraType",
    "entitiesType",
    "entityType",
    "incomeType",
    "incomesType",
    "itemType",
    "itemType1",
    "itemType10",
    "itemType11",
    "itemType13",
    "itemType14",
    "itemType15",
    "itemType16",
    "itemType17",
    "itemType18",
    "itemType2",
    "itemType3",
    "itemType4",
    "itemType6",
    "itemType7",
    "itemType9",
    "jobsType",
    "licensesType",
    "namesType",
    "ownerType",
    "ownerType8",
    "ownershipType",
    "ownershipsType",
    "persdocsType",
    "pob_extraType",
    "relativesType",
    "response",
    "sanctionType",
    "sanctionsType",
    "sanlistsType",
    "system_infoType",
    "translit_namesType",
    "watch_listType",
    "watch_listsType"
]
