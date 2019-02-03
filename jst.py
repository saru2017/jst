# -*- coding: utf-8 -*-

import sys
from datetime import datetime
import pytz
from dateutil import parser


sys.argv.pop(0)
line = " ".join(sys.argv)
#print(line)
dt = parser.parse(line)

jst_now = dt.astimezone(pytz.timezone('Japan'))
#print(jst_now)
print(jst_now.strftime("%Y/%m/%d %H:%M %Z"))

