from pathlib import Path

PATH_TO_ROOT       = str(Path.cwd().parent)
IMAGES_PATH        = PATH_TO_ROOT + '/data/fprdata/DB2_B'
PREP_IMAGES        = PATH_TO_ROOT + '/data/fprdata/training2'
TEST_IMAGES        = PATH_TO_ROOT + '/data/fprdata/test'
MAX_FEATURES       = 100
GOOD_MATCH_PERCENT = 0.25
DIST_THRESHOLD     = 70
TRAIN_PER_CLASS    = 6
EXT 			   = ".png" 	# ".tif" #   
