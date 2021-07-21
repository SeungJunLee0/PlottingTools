#!/bin/bash



for i in /Users/noise/service/code/mybuild/lib/lib*.so ; do
install_name_tool -add_rpath /Users/noise/service/code/mybuild/lib $i
done
