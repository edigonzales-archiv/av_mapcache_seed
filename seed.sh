#!/bin/bash

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/mapcache/mapcache_master/lib
#export PATH=$PATH:/usr/local/gdal/gdal-dev/bin
#export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/gdal/gdal-dev/lib
#export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python2.6/dist-packages/GDAL-2.0.0-py2.6-linux-x86_64.egg

/usr/local/mapcache/mapcache_master/bin/mapcache_seed -c /usr/local/mapcache/config/mapcache.xml -t ch.so.agi.grundbuchplan-farbe -g 21781 -p 3 -f -d /home/avdpool/Apps/av_avdpool_ch/av_lieferungen.shp
/usr/local/mapcache/mapcache_master/bin/mapcache_seed -c /usr/local/mapcache/config/mapcache.xml -t ch.so.agi.grundbuchplan-sw -g 21781 -p 3 -f -d /home/avdpool/Apps/av_avdpool_ch/av_lieferungen.shp
/usr/local/mapcache/mapcache_master/bin/mapcache_seed -c /usr/local/mapcache/config/mapcache.xml -t ch.so.agi.grundbuchplan-grau -g 21781 -p 3 -f -d /home/avdpool/Apps/av_avdpool_ch/av_lieferungen.shp


