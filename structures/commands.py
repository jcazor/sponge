# coding: utf-8
'''
Copyright 2012 juan cañete (jcazor@komlog.org)
Licensed under The Apache License (2.0) 
http://www.apache.org/licenses/LICENSE-2.0.html

commands.py - Command configuration structures and methods
'''

import sys
from config import logger

class Command(object):
    def __init__(self,xml_command):
        try:
            for attr in ['name','cmd_line']:
                setattr(self,attr,str(xml_command.getElementsByTagName(attr)[0].childNodes[0].toxml()))
        except IndexError:
            logger.log("Attribute not found: "+attr)
            sys.exit(0)
        