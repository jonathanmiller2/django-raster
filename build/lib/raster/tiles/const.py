from math import pi

WEB_MERCATOR_SRID = 3857

WEB_MERCATOR_WORLDSIZE = 2 * pi * 6378137

WEB_MERCATOR_TILESHIFT = WEB_MERCATOR_WORLDSIZE / 2.0

WEB_MERCATOR_TILESIZE = 256

GLOBAL_MAX_ZOOM_LEVEL = 18

MIN_ZOOMLEVEL_TASK_PARALLEL = 10

QUADRANT_SIZE = 50

BATCH_STEP_SIZE = 500

INTERMEDIATE_RASTER_FORMAT = 'tif'
