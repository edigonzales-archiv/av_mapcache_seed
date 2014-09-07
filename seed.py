#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
import pwd

USER = "www-data"

pw = pwd.getpwnam(USER)
env={"TERM":"xterm","USER":pw.pw_name,"HOME":pw.pw_dir,"SHELL":pw.pw_shell,"LOGNAME":pw.pw_name,"PATH":"/usr/bin:/bin:/opt/bin"};
os.setgid(pw.pw_gid);
os.setuid(pw.pw_uid);

print "Hallo Stefan."
