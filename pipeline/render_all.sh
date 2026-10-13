#!/bin/bash
# renders every preview used by the catalog (all buildings in TownKit.blend)
B="/c/Program Files/Blender Foundation/Blender 5.2/blender.exe"
F=../TownKit.blend
declare -A CUT=( [house_teal_lantern]=4.6 [apt_block_6f]=5.6 [office_glass_tower]=6.4 [villa_luxury_modern]=5.4 [station_arctic]=3.2
 [temple_pagoda]=3.6 [nyc_brownstone]=3.6 [bank_classical]=3.6 [korean_hanok]=2.8 [shinto_shrine]=3.0 [castle_keep]=3.0
 [treehouse_oak]=6.4 [cafe_container]=2.6 [house_eastasian_tile]=2.6 [pod_solar]=2.6 [villa_neon_circuit]=2.6 )
"$B" -b $F -P render.py -- --bld all --view front --res 1200 --day < /dev/null 2>&1 | grep -c "rendered"
"$B" -b $F -P render.py -- --bld all --view front --res 1200 < /dev/null 2>&1 | grep -c "rendered"
IDS=$("$B" -b $F --python-expr "import bpy;print('IDS:'+','.join(o.name[4:] for o in bpy.data.objects if o.name.startswith('BLD_') and o.type=='EMPTY'))" < /dev/null 2>&1 | grep IDS: | sed 's/IDS://')
for k in ${IDS//,/ }; do c=${CUT[$k]:-2.4}; "$B" -b $F -P render.py -- --bld $k --view cut --cutz $c --res 1200 --day < /dev/null 2>&1 | grep -i "Traceback"; done
"$B" -b $F -P render.py -- --view overview --res 2000 --day < /dev/null 2>&1 | grep -i "Traceback"
"$B" -b $F -P render.py -- --view overview --res 2000 < /dev/null 2>&1 | grep -i "Traceback"
echo ALLDONE
