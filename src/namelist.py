
# basic information
#! the path changed when using different computer
# progdir = 'F:/Data/Project_Xiaoshan/' #! YF-G15
progdir = 'D:/data/Project_Xiaoshan/' #! A275-Desktop
datadir = progdir + '202209/'
runID   = 'XS_2209'

# simulation data file
# gridfile = progdir + 'GRIDCRO2D_2022234.nc' #! YF-G15
gridfile = progdir + 'GRIDCRO2D_2022234.nc' #! A275-Desktop
mcipfile = datadir + runID + '_mcip.nc'
cmaqfile = datadir + runID + '_chem.nc'
pafile   = datadir + runID + '_pa.nc'
isamfile = datadir + runID + '_isam.nc'

# observation data file
obshz = datadir + 'obsdata/hz_avg_2209.xlsx'
obs6city = datadir + 'obsdata/6city_avg_2209.xlsx'

# shapefile
shphz   = progdir + 'shapefile/杭州市/杭州市.shp'
shpxs = progdir + 'shapefile/萧山区/萧山区.shp'
shpmap   = progdir + 'shapefile/杭州市各区/杭州市各区.shp'

# time range
timestart = '2022-09-01T00'
timeend   = '2022-09-30T23'
