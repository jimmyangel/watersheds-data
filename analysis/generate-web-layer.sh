#!/bin/bash

mapshaper watersheds4web/watersheds4web.shp -snap -simplify 30% keep-shapes -proj wgs84 -o watersheds.json format=geojson precision=0.0001
