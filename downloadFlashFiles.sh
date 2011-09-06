#!/bin/bash
lsof | grep Flash | awk 'BEGIN { FS=" "; print "#!/bin/bash"} { FILE=substr($4,1,length($4-1)); print "cp /proc/" $2 "/fd/" FILE " ~/Videos/"FILE".flv"  }' | sh
