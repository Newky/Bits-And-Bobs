#!/bin/bash
lsof -nP | grep /tmp/Flash | awk 'BEGIN { FS=" "; print "#!/bin/bash"} { FILE=substr($4,1,length($4-1)); DEST="~/Videos/"FILE".flv"; print "cp /proc/" $2 "/fd/" FILE " " DEST; print "echo copied to "DEST }' | sh
