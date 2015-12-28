#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import osgeo.gdal
from osgeo import ogr

DB_HOST = "localhost"
DB_NAME = "xanadu2"
DB_USER = "mspublic"
DB_PWD = "mspublic"
DB_SCHEMA = "av_avdpool_ch"
DB_LAYER = "av_avdpool_ch.gemeindegrenzen_gemeindegrenze"
PATH = "/home/stefan/Projekte/av_mapcache_seed"

# Enable exceptions
ogr.UseExceptions() 


connString = "PG: host=%s dbname=%s user=%s password=%s" %(DB_HOST, DB_NAME, DB_USER, DB_PWD)
conn = ogr.Open(connString)

lyr = conn.GetLayer(DB_LAYER)
print lyr

# Falls keine Lieferungen gefunden werden, wird ein leeres Shape
# erzeugt. Soweit i.O. -> was macht MapCache daraus?
lyr.SetAttributeFilter("lieferdatum = current_date")

driver = ogr.GetDriverByName("ESRI Shapefile")
out_datasource = driver.CreateDataSource(PATH + "/av_lieferungen_fubar.shp")

# Es werden OHNE ein Union alle einzelnen Feature/Geometrien exportiert.
# Funktioniert das mit MapCache?
out_layer = out_datasource.CopyLayer(lyr, "av_lieferungen")
out_datasource.Destroy()
conn.Destroy()

print "Hallo Stefan."
