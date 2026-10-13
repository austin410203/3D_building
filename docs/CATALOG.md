# TownKit 建築資產目錄 / Building Asset Catalog

Procedurally built in Blender 5.2 (`scripts/`), placed on one island template (`TownKit.blend`). Every building is walkable inside (stairs, doors, furnished rooms) and carries machine-readable metadata.

## 快速索引 Quick index

| asset_id | 名稱 | Name | 風格 Style | Tier | Type | Floors | Size W×D×H (m) | Game styles |
|---|---|---|---|---|---|---|---|---|
| `american_diner` | 海港餐車 | Harborline Diner | 美式復古餐車 / 1950s American Diner | budget | diner | 1 | 19.0 × 16.0 × 5.9 | retro, realistic, horror, road-movie, cartoon |
| `capsule_tower` | 蜂巢膠囊旅館 | Hive Capsule Hotel | 膠囊旅館 / Capsule Hotel Tower | budget | capsule hotel | 7 | 14.0 × 16.0 × 23.7 | cyberpunk, anime, sci-fi, realistic, japan |
| `gas_station` | 海港加油站 | Harbor Gas & Go | 公路加油站 / Roadside Gas Station | budget | gas station | 1 | 24.0 × 25.0 × 6.5 | realistic, road-movie, survival, horror, open-world |
| `hk_tonglau` | 旺角唐樓 | Hong Kong Tong Lau | 香港唐樓 / Hong Kong Tenement | budget | tenement | 6 | 13.0 × 17.0 × 24.1 | cyberpunk, noir, realistic, action, hk-cinema |
| `izakaya_suikei` | 居酒屋 酔鯨 | Izakaya Drunken Whale | 日式居酒屋 / Japanese Izakaya | budget | bar + flat | 2 | 14.0 × 15.0 × 9.4 | anime, slice-of-life, japan, realistic, noir |
| `laundromat_flats` | 泡泡自助洗衣 | Bubbles Laundromat | 自助洗衣公寓 / Urban Laundromat Walk-up | budget | laundromat + flats | 3 | 13.0 × 15.0 × 12.7 | slice-of-life, anime, realistic, noir |
| `seaview_motel` | 海景汽車旅館 | Seaview Motor Inn | 公路汽車旅館 / American Roadside Motel | budget | motel | 2 | 29.0 × 20.1 × 6.8 | road-movie, horror, noir, realistic, retro |
| `shop_neon_corner` | 藍調轉角雜貨 | Blue Corner Bodega | 霓虹轉角店 / Neon Corner Shop Diorama | budget | shop + flat | 2 | 15.5 × 14.0 × 10.0 | cyberpunk, anime, slice-of-life, diorama, realistic |
| `tower_cyber_narrow` | 霓虹窄塔 | Neon Sliver Tower | 賽博龐克窄樓 / Cyberpunk Vertical Block | budget | mixed-use tower | 5 | 9.2 × 10.0 × 22.1 | cyberpunk, sci-fi, neo-noir, realistic |
| `data_center` | 雲端資料中心 | Nimbus Data Center | 資料中心 / Hyperscale Data Center | utility | data center | 2 | 30.0 × 19.0 × 9.9 | cyberpunk, sci-fi, thriller, realistic, hacker |
| `station_arctic` | 極光貨櫃研究站 | Aurora Container Research Station | 極地貨櫃前哨站 / Polar Container Outpost | utility | research station | 2 | 28.6 × 15.7 × 10.7 | realistic, survival, sci-fi, thriller, post-apocalyptic |
| `fire_station` | 海港消防局 | Harbor Fire Station | 消防局 / Civic Fire Station | civic | fire station | 2 | 26.0 × 22.0 × 15.4 | realistic, rescue-sim, anime, action |
| `hospital_general` | 仁心綜合醫院 | Renxin General Hospital | 現代醫院 / Modern Hospital | civic | hospital | 3 | 27.0 × 24.0 × 13.5 | realistic, horror, medical-drama, zombie, anime |
| `kindergarten` | 彩虹幼兒園 | Rainbow Kindergarten | 童趣幼兒園 / Playful Kindergarten | civic | kindergarten | 1 | 19.0 × 19.0 × 7.6 | anime, slice-of-life, cozy, horror, cartoon |
| `library_brutalist` | 市立混凝土圖書館 | Concrete Public Library | 粗獷主義 / Brutalist | civic | library | 2 | 23.0 × 21.0 × 9.4 | realistic, dystopian, mystery, anime, post-apocalyptic |
| `police_station` | 海港警察局 | Harbor Police Station | 警察局 / Civic Police Station | civic | police station | 2 | 23.0 × 22.0 × 10.0 | realistic, crime, action, detective, anime |
| `post_office` | 海港郵局 | Harbor Post Office | 郵局 / Civic Post Office | civic | post office | 1 | 17.0 × 15.0 × 4.7 | realistic, slice-of-life, anime, rpg-village |
| `school_primary` | 海港國民小學 | Harbor Primary School | 公立學校 / Asian Public School | civic | school | 3 | 31.0 × 24.5 × 11.1 | slice-of-life, anime, horror, realistic, school-life |
| `a_frame_cabin` | 森林A字木屋 | Forest A-Frame Cabin | A字型木屋 / A-Frame Cabin | standard | cabin | 2 | 15.8 × 16.4 × 7.6 | cozy, horror, survival, realistic, winter |
| `apt_block_6f` | 朝陽社區公寓 | Sunrise Walk-up Apartments | 台式公寓 / Taiwanese Walk-up Apartment | standard | apartment block | 6 | 19.0 × 15.1 × 22.0 | realistic, slice-of-life, anime, urban-survival |
| `apt_urban_5f` | 夜巷住商公寓 | Night Alley Mixed-Use Apartment | 都市亞洲住商 / Urban Asian Mixed-Use | standard | apartment | 5 | 13.2 × 13.4 × 22.5 | realistic, anime, slice-of-life, cyberpunk-lite |
| `bakery_corner` | 麥香麵包坊 | Wheat & Hearth Bakery | 歐式麵包店 / European Bakery | standard | bakery + flat | 2 | 14.0 × 15.0 × 10.7 | cozy, anime, slice-of-life, realistic, ghibli |
| `bookstore_cafe` | 書與咖啡 | Books & Beans | 紅磚書店咖啡 / Brick Bookshop Café | standard | bookstore + café | 3 | 15.0 × 16.0 × 10.5 | cozy, anime, slice-of-life, realistic, mystery |
| `canal_twin_tower` | 運河雙子樓 | Canal Twin Houses | 港灣運河樓房 / Harbour Canal Townhouses | standard | mixed-use townhouses | 6 | 22.9 × 36.2 × 21.8 | realistic, anime, ghibli, fantasy-port, slice-of-life |
| `florist_petal` | 花語花店 | Petal Talk Florist | 鄉村花店 / Cottage Flower Shop | standard | shop + flat | 2 | 13.0 × 15.5 × 10.1 | cozy, anime, romance, slice-of-life, ghibli |
| `galaxy_arcade` | 銀河遊戲中心 | Galaxy Game Center | 霓虹遊樂場 / Neon Game Arcade | standard | arcade | 2 | 19.0 × 17.0 × 7.7 | cyberpunk, anime, retro, nightlife, realistic |
| `house_teal_lantern` | 青瓦燈籠茶屋 | Teal Lantern Teahouse | 吉卜力海邊高腳屋 / Ghibli Seaside Stilt House | standard | house+shop | 2 | 18.1 × 17.7 × 12.0 | anime, ghibli, cozy, fantasy, realistic |
| `karaoke_stardust` | 星光KTV | Stardust Karaoke Club | 霓虹KTV / Neon Karaoke Club | standard | karaoke club | 4 | 17.0 × 17.0 × 13.9 | cyberpunk, anime, nightlife, realistic, kdrama |
| `kyoto_machiya` | 京都町家 | Kyoto Machiya Townhouse | 日式町家 / Japanese Machiya | standard | shop + house | 2 | 13.0 × 17.0 × 8.8 | anime, realistic, slice-of-life, japan, cozy |
| `london_terrace` | 倫敦紅磚聯排 | London Victorian Terrace | 維多利亞聯排屋 / Victorian Terrace | standard | townhouse | 3 | 14.0 × 16.0 × 15.2 | realistic, detective, europe, steampunk, horror |
| `medieval_tavern` | 躍馬旅店 | The Prancing Stag Tavern | 中世紀酒館 / Medieval Fantasy Tavern | standard | tavern + inn | 2 | 26.0 × 16.3 × 13.9 | fantasy, medieval, rpg, realistic, anime |
| `nordic_cabin` | 北歐黑木小屋 | Nordic Black Cabin | 北歐小屋 / Scandinavian Cabin | standard | cabin | 1 | 13.0 × 14.0 × 7.9 | realistic, survival, horror, cozy, winter |
| `power_gym` | 能量健身工廠 | PowerHouse Gym | 工業風健身房 / Industrial Fitness Hall | standard | gym | 1 | 21.0 × 17.0 × 6.8 | realistic, sports, slice-of-life, anime |
| `steampunk_works` | 齒輪蒸汽工坊 | Cog & Steam Works | 蒸汽龐克工坊 / Steampunk Workshop | standard | workshop | 3 | 20.0 × 16.0 × 20.5 | steampunk, fantasy, victorian, anime, rpg |
| `supermarket` | 好鄰居超市 | Good Neighbor Supermarket | 郊區超市 / Suburban Supermarket | standard | supermarket | 1 | 29.0 × 31.0 × 5.9 | realistic, survival, zombie, slice-of-life, sims |
| `treehouse_oak` | 老橡樹樹屋 | Old Oak Treehouse | 童話樹屋 / Storybook Treehouse | standard | treehouse | 2 | 16.2 × 19.0 × 17.9 | cozy, ghibli, adventure, cartoon, fantasy |
| `tudor_inn` | 皇冠都鐸酒館 | The Crown Tudor Inn | 英式都鐸 / English Tudor | standard | pub + inn | 2 | 17.0 × 16.0 × 13.5 | medieval, fantasy, rpg-village, realistic, europe |
| `warehouse_loft` | 紅磚倉庫Loft | Red-Brick Warehouse Lofts | 工業倉庫改建 / Industrial Warehouse Loft | standard | loft + workshop | 2 | 25.0 × 19.0 × 10.8 | realistic, industrial, crime, cyberpunk, post-apocalyptic |
| `bauhaus_house` | 包浩斯白宅 | Bauhaus White House | 包浩斯 / Bauhaus Modernism | upscale | house | 2 | 17.8 × 15.6 × 9.5 | realistic, modern, architectural, anime |
| `cafe_container` | 貨櫃森林咖啡館 | Container Grove Café | 工業貨櫃現代 / Industrial Container Modern | upscale | café / commercial | 2 | 23.1 × 14.8 × 9.7 | realistic, modern, slice-of-life, anime |
| `eco_apartments` | 綠廊生態公寓 | Green Terrace Eco Apartments | 綠建築生態宅 / Biophilic Eco Housing | upscale | apartment | 5 | 19.0 × 17.0 × 19.4 | solarpunk, realistic, modern, anime, utopia |
| `glass_cube_office` | 黑玻璃創意辦公 | Obsidian Cube Offices | 當代玻璃辦公 / Contemporary Glass Office | upscale | office | 4 | 21.0 × 23.0 × 17.7 | modern, corporate, cyberpunk, realistic, thriller |
| `greenhouse_cafe` | 玻璃溫室咖啡 | Glasshouse Garden Café | 玻璃溫室 / Victorian Glasshouse | upscale | café | 1 | 17.0 × 15.0 × 6.1 | cozy, ghibli, romance, solarpunk, realistic |
| `house_eastasian_tile` | 青瓦庭院宅 | Slate-Roof Garden House | 東亞傳統瓦屋 / East Asian Traditional | upscale | house | 2 | 18.5 × 17.3 × 9.2 | realistic, anime, wuxia-modern, cozy, rpg-village |
| `korean_hanok` | 韓式韓屋 | Korean Hanok | 韓屋 / Korean Hanok | upscale | house | 1 | 20.4 × 16.5 × 7.4 | historical, kdrama, realistic, anime |
| `med_villa` | 地中海白屋 | Mediterranean White House | 地中海風 / Mediterranean | upscale | house | 2 | 17.0 × 15.0 × 9.0 | realistic, summer, romance, anime |
| `midcentury_house` | 中世紀現代宅 | Palm Springs Mid-Century House | 中世紀現代 / Mid-Century Modern | upscale | house | 1 | 30.0 × 15.0 × 4.7 | retro, realistic, mad-men, modern, gta-like |
| `moroccan_riad` | 摩洛哥庭園宅 | Moroccan Riad House | 摩洛哥風 / Moroccan Riad | upscale | guesthouse | 2 | 17.0 × 17.0 × 9.5 | fantasy, desert, realistic, adventure |
| `nyc_brownstone` | 紐約褐石排屋 | Brooklyn Brownstone | 紐約褐石屋 / New York Brownstone | upscale | townhouse | 4 | 13.0 × 19.5 × 16.2 | realistic, noir, sitcom, crime, urban |
| `paris_haussmann` | 巴黎奧斯曼公寓 | Parisian Haussmann Apartment | 巴黎奧斯曼式 / Haussmann Parisian | upscale | apartment | 4 | 19.0 × 17.5 × 17.6 | realistic, romance, anime, noir, europe |
| `pod_solar` | 日光艙屋 | Solar Pod Home | 科幻離網艙屋 / Sci-Fi Off-Grid Module | upscale | house | 2 | 18.0 × 16.0 × 11.4 | sci-fi, solarpunk, post-apocalyptic, anime, realistic |
| `spanish_hacienda` | 西班牙莊園 | Spanish Hacienda | 西班牙殖民風 / Spanish Colonial | upscale | house | 1 | 21.0 × 18.5 × 5.6 | western, realistic, telenovela, rpg-village |
| `swiss_chalet` | 阿爾卑斯木屋 | Alpine Swiss Chalet | 瑞士山屋 / Swiss Alpine Chalet | upscale | house | 2 | 16.0 × 15.0 × 10.0 | realistic, cozy, winter, anime, europe |
| `bank_classical` | 海港儲蓄銀行 | Harbor Savings Bank | 新古典銀行 / Neoclassical Bank | luxury | bank | 2 | 19.0 × 22.0 × 10.5 | realistic, heist, noir, western, civic |
| `concrete_minimal` | 清水模住宅 | Fair-faced Concrete House | 日式清水模 / Japanese Minimalist Concrete | luxury | house | 2 | 16.4 × 17.8 × 7.0 | realistic, modern, thriller, zen, architectural |
| `hotel_artdeco` | 裝飾藝術大飯店 | Grand Deco Hotel | 裝飾藝術風 / Art Deco Hotel | luxury | hotel | 6 | 21.0 × 21.0 × 28.2 | noir, 1920s, realistic, mystery, bioshock-like |
| `office_glass_tower` | 海港金融中心 | Harbor Finance Tower | 現代玻璃帷幕大樓 / Modern Glass High-rise | luxury | office high-rise | 10 | 26.0 × 25.5 × 41.9 | realistic, modern, corporate, thriller, cyberpunk |
| `villa_luxury_modern` | 白崖現代豪宅 | White Cliff Modern Villa | 奢華現代主義別墅 / Luxury Modernist Villa | luxury | villa | 2 | 31.8 × 25.3 × 7.8 | realistic, modern, thriller, life-sim, anime |
| `villa_neon_circuit` | 霓光電路別墅 | Neon Circuit Villa | 近未來科技別墅 / Near-Future Tech Villa | luxury | villa | 2 | 24.0 × 23.0 × 7.3 | cyberpunk, sci-fi, near-future, realistic, anime |
| `castle_keep` | 獅鷲城堡塔 | Griffin Castle Keep | 中世紀城堡 / Medieval Castle Keep | landmark | castle | 4 | 22.0 × 17.0 × 21.3 | fantasy, medieval, rpg, strategy, realistic |
| `lighthouse_cape` | 海角燈塔 | Cape Lighthouse | 海事燈塔 / Maritime Lighthouse | landmark | lighthouse | 5 | 18.4 × 20.0 × 21.1 | realistic, horror, mystery, adventure, ghibli |
| `observatory_dome` | 星穹天文台 | Starvault Observatory | 圓頂天文台 / Domed Observatory | landmark | observatory | 2 | 14.0 × 16.0 × 12.8 | sci-fi, realistic, mystery, anime, academy |
| `shinto_shrine` | 朱鳥神社 | Vermilion Bird Shrine | 日式神社 / Japanese Shinto Shrine | landmark | shrine | 1 | 20.3 × 20.0 × 6.8 | anime, japan, fantasy, horror, realistic |
| `stone_chapel` | 海角石砌教堂 | Cape Stone Chapel | 哥德復興教堂 / Gothic Revival Chapel | landmark | chapel | 1 | 21.2 × 22.9 × 19.7 | realistic, horror, romance, fantasy, wedding |
| `temple_pagoda` | 天界樓閣 | Heaven Gate Pavilion | 中式樓閣廟宇 / Chinese Pagoda Temple (neo-oriental) | landmark | temple / landmark | 3 | 24.0 × 30.0 × 20.5 | wuxia, fantasy, cyberpunk-oriental, anime, realistic |
| `windmill_dutch` | 風車磨坊 | Old Dutch Windmill | 荷蘭風車 / Dutch Tower Windmill | landmark | windmill | 3 | 15.2 × 16.0 × 17.2 | rpg-village, fantasy, cozy, farming-sim, realistic |
| `wizard_tower` | 星辰法師塔 | Starlight Wizard Tower | 奇幻法師塔 / High-Fantasy Wizard Tower | landmark | tower | 4 | 14.0 × 16.0 × 22.1 | fantasy, rpg, anime, magic-school, ghibli |

## 如何取用 How to fetch an asset

* **Blender (append/link):** `TownKit.blend` → collection `BLD_<asset_id>` (marked as Asset with tags; root empty `BLD_<asset_id>`). Labels live in the child collection `LBL_<asset_id>` — exclude it for in-game use.
```python
import bpy
path = r"C:/Users/Administrator/Documents/Gaming/TownKit/TownKit.blend"
with bpy.data.libraries.load(path, link=False) as (src, dst):
    dst.collections = ["BLD_cafe_container"]
for c in dst.collections:
    bpy.context.scene.collection.children.link(c)
```
* **Game engines:** `export/glb/<asset_id>.glb` — origin = plot centre at ground level, front = glTF +Z (Blender −Y), metres, Y-up. Node custom properties arrive as glTF `extras` (see conventions below). Labels are not included.
* **Compressed (recommended for games / web):** `export/glb_draco/<asset_id>.glb` — Draco geometry + 512 px WebP textures, ~5–12 MB each (full-res originals in `export/glb/`). Needs a Draco decoder (three.js DRACOLoader, Godot 4 / Blender native, Unity glTFast + Draco package).
* **Whole island:** `export/glb/town_full.glb` (everything placed) and `export/glb/island_town.glb` (terrain/streets only).
* **Machine catalog:** `export/catalog.json` (all fields below + entrances/spawns/interactables/object counts).
* **Rebuild / edit:** `blender -b --factory-startup -P scripts/build.py` (all) or `-- --only <id>`; then `blender -b TownKit.blend -P scripts/export.py`.

## 慣例 Conventions (glTF extras / Blender custom props)

* `kind` — wall|floor|stair|door|window|railing|collider|furniture|light|light_fixture|sign|label|trim|structure|roof|elevator|spawn|vegetation|terrain|water|cable|ladder
* `walkable` — true on floors / stairs / ramps / decks
* `collider` — 'ramp' (invisible stair ramp) or 'wall' (invisible rail blocker)
* `interact` — sit|sleep|open|use|cook|wash|shop|play|work|elevator|elevator_call|climb
* `openable` — hinge (rotate Z by open_angle deg from closed_rot_z) | slide (move by open_offset) | drawer | tilt
* `use_points` — JSON list of local [x,y,z] seat/use anchors
* `levels` — elevator car: JSON list of floor heights
* front: local -Y in Blender (glTF +Z); plot centre at origin; ground level z=0
* object names: <asset_id>.<part>  e.g. cafe_container.Cafe_WallS

## 建築明細 Buildings

### 海港餐車 Harborline Diner — `american_diner`

![day](renders/american_diner_front_day.png) ![night](renders/american_diner_front.png) ![plan](renders/american_diner_cut_day.png)

* **Style:** 美式復古餐車 / 1950s American Diner · **Tier:** budget · **Type:** diner · **Floors:** 1
* **Fits game styles:** retro, realistic, horror, road-movie, cartoon
* **Description:** Single-storey steel diner: counter with stools, booth tables, kitchen, striped awning, big neon roof sign.
* **Size:** 19.0 × 16.0 m footprint, 5.9 m tall · 87 objects · ~65672 tris · 2 lights · 47 furniture pieces
* **Exterior doors:** F1_S2(S side) · interior doors: 0
* **Spawn points (local m):** front (-0.5, -7.0, 0)
* **Interactions:** open, shop, sit, use
* **Placed on island at:** (-32.5, -45.2, 0.15), rotZ 0° · **Files:** `export/glb/american_diner.glb`, Blender collection `BLD_american_diner`

### 蜂巢膠囊旅館 Hive Capsule Hotel — `capsule_tower`

![day](renders/capsule_tower_front_day.png) ![night](renders/capsule_tower_front.png) ![plan](renders/capsule_tower_cut_day.png)

* **Style:** 膠囊旅館 / Capsule Hotel Tower · **Tier:** budget · **Type:** capsule hotel · **Floors:** 7
* **Fits game styles:** cyberpunk, anime, sci-fi, realistic, japan
* **Description:** 7-storey slim capsule hotel: lobby, floors of stacked bunk capsules + lounges, roof terrace, neon blade sign.
* **Size:** 14.0 × 16.0 m footprint, 23.7 m tall · 449 objects · ~123456 tris · 22 lights · 89 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E2(E side), PH_W0(W side) · interior doors: 14
* **Spawn points (local m):** front (-2.4, -8.0, 0)
* **Interactions:** open, shop, sit, sleep, use, wash
* **Placed on island at:** (139.0, -77.8, 0.15), rotZ 180° · **Files:** `export/glb/capsule_tower.glb`, Blender collection `BLD_capsule_tower`

### 海港加油站 Harbor Gas & Go — `gas_station`

![day](renders/gas_station_front_day.png) ![night](renders/gas_station_front.png) ![plan](renders/gas_station_cut_day.png)

* **Style:** 公路加油站 / Roadside Gas Station · **Tier:** budget · **Type:** gas station · **Floors:** 1
* **Fits game styles:** realistic, road-movie, survival, horror, open-world
* **Description:** Convenience kiosk with shelves and counter, big illuminated canopy over four pumps, price pylon.
* **Size:** 24.0 × 25.0 m footprint, 6.5 m tall · 60 objects · ~107836 tris · 3 lights · 19 furniture pieces
* **Exterior doors:** F1_S2(S side) · interior doors: 0
* **Spawn points (local m):** front (-2.0, -7.0, 0)
* **Interactions:** open, shop, use
* **Placed on island at:** (82.0, -36.2, 0.15), rotZ 0° · **Files:** `export/glb/gas_station.glb`, Blender collection `BLD_gas_station`

### 旺角唐樓 Hong Kong Tong Lau — `hk_tonglau`

![day](renders/hk_tonglau_front_day.png) ![night](renders/hk_tonglau_front.png) ![plan](renders/hk_tonglau_cut_day.png)

* **Style:** 香港唐樓 / Hong Kong Tenement · **Tier:** budget · **Type:** tenement · **Floors:** 6
* **Fits game styles:** cyberpunk, noir, realistic, action, hk-cinema
* **Description:** 6-storey mosaic tenement: cha chaan teng diner, caged balconies, AC units, neon blade sign, laundry, rooftop.
* **Size:** 13.0 × 17.0 m footprint, 24.1 m tall · 460 objects · ~126020 tris · 19 lights · 124 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_E2(E side), F2_S1(S side), F4_S1(S side), F6_S1(S side), PH_W0(W side) · interior doors: 12
* **Spawn points (local m):** front (-2.0, -8.5, 0)
* **Interactions:** cook, open, sit, sleep, use, work
* **Placed on island at:** (91.5, -16.3, 0.15), rotZ 180° · **Files:** `export/glb/hk_tonglau.glb`, Blender collection `BLD_hk_tonglau`

### 居酒屋 酔鯨 Izakaya Drunken Whale — `izakaya_suikei`

![day](renders/izakaya_suikei_front_day.png) ![night](renders/izakaya_suikei_front.png) ![plan](renders/izakaya_suikei_cut_day.png)

* **Style:** 日式居酒屋 / Japanese Izakaya · **Tier:** budget · **Type:** bar + flat · **Floors:** 2
* **Fits game styles:** anime, slice-of-life, japan, realistic, noir
* **Description:** Timber-fronted izakaya: counter bar with stools, tables, kitchen, red lanterns and noren; small flat above; slate gable.
* **Size:** 14.0 × 15.0 m footprint, 9.4 m tall · 180 objects · ~74140 tris · 12 lights · 43 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side) · interior doors: 4
* **Spawn points (local m):** front (-1.0, -7.5, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, work
* **Placed on island at:** (153.0, -46.7, 0.15), rotZ 0° · **Files:** `export/glb/izakaya_suikei.glb`, Blender collection `BLD_izakaya_suikei`

### 泡泡自助洗衣 Bubbles Laundromat — `laundromat_flats`

![day](renders/laundromat_flats_front_day.png) ![night](renders/laundromat_flats_front.png) ![plan](renders/laundromat_flats_cut_day.png)

* **Style:** 自助洗衣公寓 / Urban Laundromat Walk-up · **Tier:** budget · **Type:** laundromat + flats · **Floors:** 3
* **Fits game styles:** slice-of-life, anime, realistic, noir
* **Description:** Narrow 3-storey mosaic block: G/F coin laundry with washer wall and bench, two small flats above.
* **Size:** 13.0 × 15.0 m footprint, 12.7 m tall · 207 objects · ~102868 tris · 10 lights · 52 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_E1(E side), PH_W0(W side) · interior doors: 6
* **Spawn points (local m):** front (-2.4, -7.5, 0)
* **Interactions:** open, shop, sit, sleep, use, work
* **Placed on island at:** (-75.5, -77.3, 0.15), rotZ 180° · **Files:** `export/glb/laundromat_flats.glb`, Blender collection `BLD_laundromat_flats`

### 海景汽車旅館 Seaview Motor Inn — `seaview_motel`

![day](renders/seaview_motel_front_day.png) ![night](renders/seaview_motel_front.png) ![plan](renders/seaview_motel_cut_day.png)

* **Style:** 公路汽車旅館 / American Roadside Motel · **Tier:** budget · **Type:** motel · **Floors:** 2
* **Fits game styles:** road-movie, horror, noir, realistic, retro
* **Description:** Two-storey motel strip: office/lobby, rows of guest rooms each with its own balcony walkway, neon MOTEL sign, parking.
* **Size:** 29.0 × 20.1 m footprint, 6.8 m tall · 315 objects · ~117340 tris · 20 lights · 100 furniture pieces
* **Exterior doors:** F1_S6(S side), F1_E1(E side), F2_S0(S side), F2_S1(S side), F2_S2(S side), F2_S3(S side), F2_S4(S side) · interior doors: 18
* **Spawn points (local m):** front (-9.6, -7.5, 0)
* **Interactions:** open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (108.5, -41.7, 0.15), rotZ 0° · **Files:** `export/glb/seaview_motel.glb`, Blender collection `BLD_seaview_motel`

### 藍調轉角雜貨 Blue Corner Bodega — `shop_neon_corner`

![day](renders/shop_neon_corner_front_day.png) ![night](renders/shop_neon_corner_front.png) ![plan](renders/shop_neon_corner_cut_day.png)

* **Style:** 霓虹轉角店 / Neon Corner Shop Diorama · **Tier:** budget · **Type:** shop + flat · **Floors:** 2
* **Fits game styles:** cyberpunk, anime, slice-of-life, diorama, realistic
* **Description:** Corner shop with open frontage (raised roller shutters) on two streets: record & game corner, snack counter, shelves, arcade. Upper blue flat with wrap balcony and LED under-glow, rooftop garden with palms.
* **Size:** 15.5 × 14.0 m footprint, 10.0 m tall · 151 objects · ~111104 tris · 7 lights · 50 furniture pieces
* **Exterior doors:** GF_S0(S side), GF_S1(S side), GF_E0(E side), GF_E1(E side), UF_S1(S side), UF_W0(W side) · interior doors: 1
* **Spawn points (local m):** corner (6.5, -6.0, 0)
* **Interactions:** climb, open, play, shop, sit, sleep, use, work
* **Placed on island at:** (62.5, 14.6, 0.15), rotZ 0° · **Files:** `export/glb/shop_neon_corner.glb`, Blender collection `BLD_shop_neon_corner`

### 霓虹窄塔 Neon Sliver Tower — `tower_cyber_narrow`

![day](renders/tower_cyber_narrow_front_day.png) ![night](renders/tower_cyber_narrow_front.png) ![plan](renders/tower_cyber_narrow_cut_day.png)

* **Style:** 賽博龐克窄樓 / Cyberpunk Vertical Block · **Tier:** budget · **Type:** mixed-use tower · **Floors:** 5
* **Fits game styles:** cyberpunk, sci-fi, neo-noir, realistic
* **Description:** 6x7 m five-storey neon tower: G/F DVD & gadget shop, 2F hacker den with servers, 3F capsule hostel, 4F neon bar, 5F loft, roof hut with antennas. Grimy steel cladding, fans, pipes, vertical neon signs.
* **Size:** 9.2 × 10.0 m footprint, 22.1 m tall · 318 objects · ~119132 tris · 14 lights · 53 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_S2(S side), Hut_W0(W side) · interior doors: 0
* **Spawn points (local m):** front (-0.2, -5.1, 0)
* **Interactions:** open, play, shop, sit, sleep, use, work
* **Placed on island at:** (44.0, 12.5, 0.15), rotZ 0° · **Files:** `export/glb/tower_cyber_narrow.glb`, Blender collection `BLD_tower_cyber_narrow`

### 雲端資料中心 Nimbus Data Center — `data_center`

![day](renders/data_center_front_day.png) ![night](renders/data_center_front.png) ![plan](renders/data_center_cut_day.png)

* **Style:** 資料中心 / Hyperscale Data Center · **Tier:** utility · **Type:** data center · **Floors:** 2
* **Fits game styles:** cyberpunk, sci-fi, thriller, realistic, hacker
* **Description:** Windowless steel data hall: server rooms with rack rows and consoles, NOC office, roof chillers, backup generators.
* **Size:** 30.0 × 19.0 m footprint, 9.9 m tall · 209 objects · ~110784 tris · 10 lights · 102 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_E0(E side) · interior doors: 8
* **Spawn points (local m):** front (-5.0, -9.5, 0)
* **Interactions:** open, sit, use, wash, work
* **Placed on island at:** (117.0, -79.3, 0.15), rotZ 180° · **Files:** `export/glb/data_center.glb`, Blender collection `BLD_data_center`

### 極光貨櫃研究站 Aurora Container Research Station — `station_arctic`

![day](renders/station_arctic_front_day.png) ![night](renders/station_arctic_front.png) ![plan](renders/station_arctic_cut_day.png)

* **Style:** 極地貨櫃前哨站 / Polar Container Outpost · **Tier:** utility · **Type:** research station · **Floors:** 2
* **Fits game styles:** realistic, survival, sci-fi, thriller, post-apocalyptic
* **Description:** Four containers (blue 20ft bunks, yellow 40ft lab, grey 20ft mess, grey 40ft comms/lounge) on stilts around a glass stair tower; twin front stairs, upper balcony walkway + slanted canopy, antenna mast, dish, fuel drums.
* **Size:** 28.6 × 15.7 m footprint, 10.7 m tall · 203 objects · ~110954 tris · 14 lights · 31 furniture pieces
* **Exterior doors:** Tower_S1(S side), Bunks_S1(S side), Lab_S1(S side), Comms_S1(S side) · interior doors: 0
* **Spawn points (local m):** stairs_left (-5.5, -6.14, 0)
* **Interactions:** cook, open, sit, sleep, use, work
* **Placed on island at:** (-2.0, 86.0, 7.0), rotZ 0° · **Files:** `export/glb/station_arctic.glb`, Blender collection `BLD_station_arctic`

### 海港消防局 Harbor Fire Station — `fire_station`

![day](renders/fire_station_front_day.png) ![night](renders/fire_station_front.png) ![plan](renders/fire_station_cut_day.png)

* **Style:** 消防局 / Civic Fire Station · **Tier:** civic · **Type:** fire station · **Floors:** 2
* **Fits game styles:** realistic, rescue-sim, anime, action
* **Description:** Brick 2-storey station: double apparatus bay with two ladder trucks behind roller doors, hose tower, upstairs dorm + lounge.
* **Size:** 26.0 × 22.0 m footprint, 15.4 m tall · 166 objects · ~82724 tris · 10 lights · 38 furniture pieces
* **Exterior doors:** F1_S0(S side), F1_S1(S side), F1_S2(S side), F1_E2(E side) · interior doors: 8
* **Spawn points (local m):** front (7.0, -9.5, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, wash
* **Placed on island at:** (112.0, -20.3, 0.15), rotZ 180° · **Files:** `export/glb/fire_station.glb`, Blender collection `BLD_fire_station`

### 仁心綜合醫院 Renxin General Hospital — `hospital_general`

![day](renders/hospital_general_front_day.png) ![night](renders/hospital_general_front.png) ![plan](renders/hospital_general_cut_day.png)

* **Style:** 現代醫院 / Modern Hospital · **Tier:** civic · **Type:** hospital · **Floors:** 3
* **Fits game styles:** realistic, horror, medical-drama, zombie, anime
* **Description:** 3-storey tiled hospital: lobby + triage clinics, wards with beds, exam rooms, roof terrace, drop-off canopy, ambulance, red cross.
* **Size:** 27.0 × 24.0 m footprint, 13.5 m tall · 320 objects · ~111996 tris · 19 lights · 82 furniture pieces
* **Exterior doors:** F1_S6(S side), F1_E2(E side), PH_W0(W side) · interior doors: 15
* **Spawn points (local m):** front (-5.0, -10.0, 0)
* **Interactions:** open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (-150.5, -40.2, 0.15), rotZ 0° · **Files:** `export/glb/hospital_general.glb`, Blender collection `BLD_hospital_general`

### 彩虹幼兒園 Rainbow Kindergarten — `kindergarten`

![day](renders/kindergarten_front_day.png) ![night](renders/kindergarten_front.png) ![plan](renders/kindergarten_cut_day.png)

* **Style:** 童趣幼兒園 / Playful Kindergarten · **Tier:** civic · **Type:** kindergarten · **Floors:** 1
* **Fits game styles:** anime, slice-of-life, cozy, horror, cartoon
* **Description:** Single-storey cheerful kindergarten: classroom + play lounge, red tile gable, playground with slide, swings and sandbox.
* **Size:** 19.0 × 19.0 m footprint, 7.6 m tall · 114 objects · ~69848 tris · 2 lights · 71 furniture pieces
* **Exterior doors:** F1_S4(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -7.5, 0)
* **Interactions:** open, play, sit, use, work
* **Placed on island at:** (59.5, -42.7, 0.15), rotZ 0° · **Files:** `export/glb/kindergarten.glb`, Blender collection `BLD_kindergarten`

### 市立混凝土圖書館 Concrete Public Library — `library_brutalist`

![day](renders/library_brutalist_front_day.png) ![night](renders/library_brutalist_front.png) ![plan](renders/library_brutalist_cut_day.png)

* **Style:** 粗獷主義 / Brutalist · **Tier:** civic · **Type:** library · **Floors:** 2
* **Fits game styles:** realistic, dystopian, mystery, anime, post-apocalyptic
* **Description:** Massive exposed-concrete library: tall reading hall of stacks, upper reading room + meeting room, deep concrete fins and slab crown.
* **Size:** 23.0 × 21.0 m footprint, 9.4 m tall · 167 objects · ~122576 tris · 8 lights · 55 furniture pieces
* **Exterior doors:** F1_S4(S side), F1_E1(E side) · interior doors: 6
* **Spawn points (local m):** front (-3.0, -9.5, 0)
* **Interactions:** open, sit, use, wash
* **Placed on island at:** (-92.5, -42.7, 0.15), rotZ 0° · **Files:** `export/glb/library_brutalist.glb`, Blender collection `BLD_library_brutalist`

### 海港警察局 Harbor Police Station — `police_station`

![day](renders/police_station_front_day.png) ![night](renders/police_station_front.png) ![plan](renders/police_station_cut_day.png)

* **Style:** 警察局 / Civic Police Station · **Tier:** civic · **Type:** police station · **Floors:** 2
* **Fits game styles:** realistic, crime, action, detective, anime
* **Description:** Concrete 2-storey precinct: public lobby with front desk, squad office, holding/storage, upstairs open office, briefing room, server room.
* **Size:** 23.0 × 22.0 m footprint, 10.0 m tall · 245 objects · ~118340 tris · 13 lights · 109 furniture pieces
* **Exterior doors:** F1_S5(S side), F1_E2(E side) · interior doors: 8
* **Spawn points (local m):** front (-4.0, -9.0, 0)
* **Interactions:** open, shop, sit, use, wash, work
* **Placed on island at:** (136.5, -20.8, 0.15), rotZ 180° · **Files:** `export/glb/police_station.glb`, Blender collection `BLD_police_station`

### 海港郵局 Harbor Post Office — `post_office`

![day](renders/post_office_front_day.png) ![night](renders/post_office_front.png) ![plan](renders/post_office_cut_day.png)

* **Style:** 郵局 / Civic Post Office · **Tier:** civic · **Type:** post office · **Floors:** 1
* **Fits game styles:** realistic, slice-of-life, anime, rpg-village
* **Description:** Single-storey cream-brick post office: counter hall with rope queue, parcel storage, green post box, flag.
* **Size:** 17.0 × 15.0 m footprint, 4.7 m tall · 52 objects · ~62204 tris · 2 lights · 10 furniture pieces
* **Exterior doors:** F1_S3(S side) · interior doors: 0
* **Spawn points (local m):** front (-2.0, -7.5, 0)
* **Interactions:** open, shop, sit, use
* **Placed on island at:** (-51.5, -46.7, 0.15), rotZ 0° · **Files:** `export/glb/post_office.glb`, Blender collection `BLD_post_office`

### 海港國民小學 Harbor Primary School — `school_primary`

![day](renders/school_primary_front_day.png) ![night](renders/school_primary_front.png) ![plan](renders/school_primary_cut_day.png)

* **Style:** 公立學校 / Asian Public School · **Tier:** civic · **Type:** school · **Floors:** 3
* **Fits game styles:** slice-of-life, anime, horror, realistic, school-life
* **Description:** 3-storey brick school: classrooms with desks/whiteboards on every floor, library, front-yard basketball court, flagpole, clock.
* **Size:** 31.0 × 24.5 m footprint, 11.1 m tall · 718 objects · ~141760 tris · 18 lights · 497 furniture pieces
* **Exterior doors:** F1_S8(S side), F1_E2(E side) · interior doors: 15
* **Spawn points (local m):** front (0.4, -9.0, 0)
* **Interactions:** open, shop, sit, use, wash, work
* **Placed on island at:** (-120.5, -38.7, 0.15), rotZ 0° · **Files:** `export/glb/school_primary.glb`, Blender collection `BLD_school_primary`

### 森林A字木屋 Forest A-Frame Cabin — `a_frame_cabin`

![day](renders/a_frame_cabin_front_day.png) ![night](renders/a_frame_cabin_front.png) ![plan](renders/a_frame_cabin_cut_day.png)

* **Style:** A字型木屋 / A-Frame Cabin · **Tier:** standard · **Type:** cabin · **Floors:** 2
* **Fits game styles:** cozy, horror, survival, realistic, winter
* **Description:** Steep A-frame timber cabin: glazed front gable with door, living + kitchenette below, sleeping loft reached by a centre stair, deck.
* **Size:** 15.8 × 16.4 m footprint, 7.6 m tall · 48 objects · ~50688 tris · 3 lights · 12 furniture pieces
* **Exterior doors:** FrontDoor(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -7.5, 0)
* **Interactions:** cook, open, sit, sleep, use
* **Placed on island at:** (153.0, -78.3, 0.15), rotZ 180° · **Files:** `export/glb/a_frame_cabin.glb`, Blender collection `BLD_a_frame_cabin`

### 朝陽社區公寓 Sunrise Walk-up Apartments — `apt_block_6f`

![day](renders/apt_block_6f_front_day.png) ![night](renders/apt_block_6f_front.png) ![plan](renders/apt_block_6f_cut_day.png)

* **Style:** 台式公寓 / Taiwanese Walk-up Apartment · **Tier:** standard · **Type:** apartment block · **Floors:** 6
* **Fits game styles:** realistic, slice-of-life, anime, urban-survival
* **Description:** 6-storey mosaic-tile walk-up: arcade with convenience store + breakfast shop, 10 one-bedroom flats (2 per floor), central U-stair, grilled windows, balconies with laundry, rooftop iron-sheet addition with water tanks.
* **Size:** 19.0 × 15.1 m footprint, 22.0 m tall · 929 objects · ~223348 tris · 62 lights · 312 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_S2(S side), F1_S3(S side), F1_S4(S side), F2_S1(S side), F2_S3(S side), F3_S1(S side), F3_S3(S side), F4_S1(S side), F4_S3(S side), F5_S1(S side), F5_S3(S side), F6_S1(S side), F6_S3(S side), Shack_S0(S side) · interior doors: 31
* **Spawn points (local m):** arcade (0.0, -7.5, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (-50.0, 14.6, 0.15), rotZ 0° · **Files:** `export/glb/apt_block_6f.glb`, Blender collection `BLD_apt_block_6f`

### 夜巷住商公寓 Night Alley Mixed-Use Apartment — `apt_urban_5f`

![day](renders/apt_urban_5f_front_day.png) ![night](renders/apt_urban_5f_front.png) ![plan](renders/apt_urban_5f_cut_day.png)

* **Style:** 都市亞洲住商 / Urban Asian Mixed-Use · **Tier:** standard · **Type:** apartment · **Floors:** 5
* **Fits game styles:** realistic, anime, slice-of-life, cyberpunk-lite
* **Description:** 5F walk-up: G/F ramen shop with counter seating, 2F-4F one-bedroom flats with balcony, 5F loft studio, roof terrace with water tank. Shared U-stair core.
* **Size:** 13.2 × 13.4 m footprint, 22.5 m tall · 505 objects · ~141232 tris · 40 lights · 129 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_S3(S side), F1_N1(N side), F2_S1(S side), F3_S1(S side), F4_S1(S side), F5_S1(S side), PH_S0(S side) · interior doors: 11
* **Spawn points (local m):** front_door (3.7, -6.1, 0), shop_door (0.1, -6.1, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (-26.0, 14.3, 0.15), rotZ 0° · **Files:** `export/glb/apt_urban_5f.glb`, Blender collection `BLD_apt_urban_5f`

### 麥香麵包坊 Wheat & Hearth Bakery — `bakery_corner`

![day](renders/bakery_corner_front_day.png) ![night](renders/bakery_corner_front.png) ![plan](renders/bakery_corner_cut_day.png)

* **Style:** 歐式麵包店 / European Bakery · **Tier:** standard · **Type:** bakery + flat · **Floors:** 2
* **Fits game styles:** cozy, anime, slice-of-life, realistic, ghibli
* **Description:** Cream-brick 2-storey bakery: bread display, oven, café table, striped awning; baker's flat upstairs.
* **Size:** 14.0 × 15.0 m footprint, 10.7 m tall · 123 objects · ~82772 tris · 6 lights · 26 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side) · interior doors: 4
* **Spawn points (local m):** front (-2.4, -7.5, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, work
* **Placed on island at:** (-15.0, -46.7, 0.15), rotZ 0° · **Files:** `export/glb/bakery_corner.glb`, Blender collection `BLD_bakery_corner`

### 書與咖啡 Books & Beans — `bookstore_cafe`

![day](renders/bookstore_cafe_front_day.png) ![night](renders/bookstore_cafe_front.png) ![plan](renders/bookstore_cafe_cut_day.png)

* **Style:** 紅磚書店咖啡 / Brick Bookshop Café · **Tier:** standard · **Type:** bookstore + café · **Floors:** 3
* **Fits game styles:** cozy, anime, slice-of-life, realistic, mystery
* **Description:** 3-storey brick bookshop: G/F bookstacks, 2F café with counter and tables, 3F reading loft flat, green awning.
* **Size:** 15.0 × 16.0 m footprint, 10.5 m tall · 211 objects · ~102426 tris · 11 lights · 58 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side) · interior doors: 8
* **Spawn points (local m):** front (-2.4, -8.0, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (-90.5, -77.8, 0.15), rotZ 180° · **Files:** `export/glb/bookstore_cafe.glb`, Blender collection `BLD_bookstore_cafe`

### 運河雙子樓 Canal Twin Houses — `canal_twin_tower`

![day](renders/canal_twin_tower_front_day.png) ![night](renders/canal_twin_tower_front.png) ![plan](renders/canal_twin_tower_cut_day.png)

* **Style:** 港灣運河樓房 / Harbour Canal Townhouses · **Tier:** standard · **Type:** mixed-use townhouses · **Floors:** 6
* **Fits game styles:** realistic, anime, ghibli, fantasy-port, slice-of-life
* **Description:** Stone quay platform in the water with a teal 5-storey and an ochre 6-storey tower sharing one U-stair; G/F grocery + noodle bar, flats above, roof terrace, lanterns, jetty with two rowing boats, boardwalk to shore.
* **Size:** 22.9 × 36.2 m footprint, 21.8 m tall · 558 objects · ~154586 tris · 32 lights · 122 furniture pieces
* **Exterior doors:** B1_S1(S side), A1_S1(S side), A2_S1(S side), A3_S1(S side), A4_S1(S side), A5_S1(S side) · interior doors: 11
* **Spawn points (local m):** boardwalk (0.0, -26.0, -0.02)
* **Interactions:** cook, open, shop, sit, sleep, use
* **Placed on island at:** (160.0, -125.0, 0.15), rotZ 180° · **Files:** `export/glb/canal_twin_tower.glb`, Blender collection `BLD_canal_twin_tower`

### 花語花店 Petal Talk Florist — `florist_petal`

![day](renders/florist_petal_front_day.png) ![night](renders/florist_petal_front.png) ![plan](renders/florist_petal_cut_day.png)

* **Style:** 鄉村花店 / Cottage Flower Shop · **Tier:** standard · **Type:** shop + flat · **Floors:** 2
* **Fits game styles:** cozy, anime, romance, slice-of-life, ghibli
* **Description:** White clapboard 2-storey flower shop: plant-filled shop floor, flower stands on the pavement, green awning, flat above with flower boxes.
* **Size:** 13.0 × 15.5 m footprint, 10.1 m tall · 124 objects · ~81424 tris · 6 lights · 31 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side) · interior doors: 4
* **Spawn points (local m):** front (-1.8, -7.25, 0)
* **Interactions:** open, shop, sit, sleep, use, work
* **Placed on island at:** (-41.5, -78.05, 0.15), rotZ 180° · **Files:** `export/glb/florist_petal.glb`, Blender collection `BLD_florist_petal`

### 銀河遊戲中心 Galaxy Game Center — `galaxy_arcade`

![day](renders/galaxy_arcade_front_day.png) ![night](renders/galaxy_arcade_front.png) ![plan](renders/galaxy_arcade_cut_day.png)

* **Style:** 霓虹遊樂場 / Neon Game Arcade · **Tier:** standard · **Type:** arcade · **Floors:** 2
* **Fits game styles:** cyberpunk, anime, retro, nightlife, realistic
* **Description:** 2-storey black game centre: rows of arcade cabinets, claw machines, upstairs arcade + bar, neon signage.
* **Size:** 19.0 × 17.0 m footprint, 7.7 m tall · 171 objects · ~106524 tris · 10 lights · 62 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side) · interior doors: 7
* **Spawn points (local m):** front (-3.5, -8.5, 0)
* **Interactions:** open, play, shop, sit, use, wash
* **Placed on island at:** (-58.5, -78.3, 0.15), rotZ 180° · **Files:** `export/glb/galaxy_arcade.glb`, Blender collection `BLD_galaxy_arcade`

### 青瓦燈籠茶屋 Teal Lantern Teahouse — `house_teal_lantern`

![day](renders/house_teal_lantern_front_day.png) ![night](renders/house_teal_lantern_front.png) ![plan](renders/house_teal_lantern_cut_day.png)

* **Style:** 吉卜力海邊高腳屋 / Ghibli Seaside Stilt House · **Tier:** standard · **Type:** house+shop · **Floors:** 2
* **Fits game styles:** anime, ghibli, cozy, fantasy, realistic
* **Description:** Teal clapboard 2-storey teahouse on a raised timber deck around an old tree trunk; red-framed bay windows, paper lanterns, roof terrace with antennas.
* **Size:** 18.1 × 17.7 m footprint, 12.0 m tall · 191 objects · ~114028 tris · 11 lights · 39 furniture pieces
* **Exterior doors:** GF_S1(S side) · interior doors: 1
* **Spawn points (local m):** stair_foot (0.0, -10.16, 0)
* **Interactions:** open, shop, sit, sleep, use, work
* **Placed on island at:** (-55.0, -18.5, 0.15), rotZ 180° · **Files:** `export/glb/house_teal_lantern.glb`, Blender collection `BLD_house_teal_lantern`

### 星光KTV Stardust Karaoke Club — `karaoke_stardust`

![day](renders/karaoke_stardust_front_day.png) ![night](renders/karaoke_stardust_front.png) ![plan](renders/karaoke_stardust_cut_day.png)

* **Style:** 霓虹KTV / Neon Karaoke Club · **Tier:** standard · **Type:** karaoke club · **Floors:** 4
* **Fits game styles:** cyberpunk, anime, nightlife, realistic, kdrama
* **Description:** 4-storey black KTV: G/F bar, private karaoke lounges on upper floors (sofa + TV), neon floor bands, vertical blade sign.
* **Size:** 17.0 × 17.0 m footprint, 13.9 m tall · 333 objects · ~97492 tris · 20 lights · 91 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E2(E side) · interior doors: 15
* **Spawn points (local m):** front (-2.5, -8.5, 0)
* **Interactions:** cook, open, shop, sit, use, wash
* **Placed on island at:** (-107.5, -78.3, 0.15), rotZ 180° · **Files:** `export/glb/karaoke_stardust.glb`, Blender collection `BLD_karaoke_stardust`

### 京都町家 Kyoto Machiya Townhouse — `kyoto_machiya`

![day](renders/kyoto_machiya_front_day.png) ![night](renders/kyoto_machiya_front.png) ![plan](renders/kyoto_machiya_cut_day.png)

* **Style:** 日式町家 / Japanese Machiya · **Tier:** standard · **Type:** shop + house · **Floors:** 2
* **Fits game styles:** anime, realistic, slice-of-life, japan, cozy
* **Description:** Narrow timber townhouse: G/F sweets shop with noren curtain and lanterns, tatami living above, sliding lattice windows, slate gable.
* **Size:** 13.0 × 17.0 m footprint, 8.8 m tall · 154 objects · ~90484 tris · 8 lights · 21 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E2(E side) · interior doors: 4
* **Spawn points (local m):** front (-1.0, -8.5, 0)
* **Interactions:** cook, open, shop, sit, sleep, use
* **Placed on island at:** (151.5, 16.3, 0.15), rotZ 0° · **Files:** `export/glb/kyoto_machiya.glb`, Blender collection `BLD_kyoto_machiya`

### 倫敦紅磚聯排 London Victorian Terrace — `london_terrace`

![day](renders/london_terrace_front_day.png) ![night](renders/london_terrace_front.png) ![plan](renders/london_terrace_cut_day.png)

* **Style:** 維多利亞聯排屋 / Victorian Terrace · **Tier:** standard · **Type:** townhouse · **Floors:** 3
* **Fits game styles:** realistic, detective, europe, steampunk, horror
* **Description:** Red-brick 3-storey Victorian terrace: bay window, black front door with fanlight, slate gable roof, chimney stacks.
* **Size:** 14.0 × 16.0 m footprint, 15.2 m tall · 188 objects · ~83848 tris · 11 lights · 36 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_E1(E side) · interior doors: 6
* **Spawn points (local m):** front (1.2, -8.0, 0)
* **Interactions:** cook, open, sit, sleep, use, wash, work
* **Placed on island at:** (-118.0, 15.8, 0.15), rotZ 0° · **Files:** `export/glb/london_terrace.glb`, Blender collection `BLD_london_terrace`

### 躍馬旅店 The Prancing Stag Tavern — `medieval_tavern`

![day](renders/medieval_tavern_front_day.png) ![night](renders/medieval_tavern_front.png) ![plan](renders/medieval_tavern_cut_day.png)

* **Style:** 中世紀酒館 / Medieval Fantasy Tavern · **Tier:** standard · **Type:** tavern + inn · **Floors:** 2
* **Fits game styles:** fantasy, medieval, rpg, realistic, anime
* **Description:** Stone-and-timber tavern: great hearth, bar, kitchen; half-timbered guest rooms upstairs; slate roof, hanging sign, ale barrels, well.
* **Size:** 26.0 × 16.3 m footprint, 13.9 m tall · 199 objects · ~88780 tris · 13 lights · 68 furniture pieces
* **Exterior doors:** F1_S3(S side), F1_E1(E side) · interior doors: 9
* **Spawn points (local m):** front (-1.0, -8.0, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (22.0, -102.2, 0.15), rotZ 0° · **Files:** `export/glb/medieval_tavern.glb`, Blender collection `BLD_medieval_tavern`

### 北歐黑木小屋 Nordic Black Cabin — `nordic_cabin`

![day](renders/nordic_cabin_front_day.png) ![night](renders/nordic_cabin_front.png) ![plan](renders/nordic_cabin_cut_day.png)

* **Style:** 北歐小屋 / Scandinavian Cabin · **Tier:** standard · **Type:** cabin · **Floors:** 1
* **Fits game styles:** realistic, survival, horror, cozy, winter
* **Description:** Single-storey black-timber cabin with a steep slate gable, big picture window, fireplace, firewood stack.
* **Size:** 13.0 × 14.0 m footprint, 7.9 m tall · 60 objects · ~61480 tris · 4 lights · 18 furniture pieces
* **Exterior doors:** F1_S2(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -7.0, 0)
* **Interactions:** open, sit, sleep, use, work
* **Placed on island at:** (137.5, 14.8, 0.15), rotZ 0° · **Files:** `export/glb/nordic_cabin.glb`, Blender collection `BLD_nordic_cabin`

### 能量健身工廠 PowerHouse Gym — `power_gym`

![day](renders/power_gym_front_day.png) ![night](renders/power_gym_front.png) ![plan](renders/power_gym_cut_day.png)

* **Style:** 工業風健身房 / Industrial Fitness Hall · **Tier:** standard · **Type:** gym · **Floors:** 1
* **Fits game styles:** realistic, sports, slice-of-life, anime
* **Description:** Steel-clad sawtooth hall full of treadmills and weight benches, glass front, neon sign.
* **Size:** 21.0 × 17.0 m footprint, 6.8 m tall · 57 objects · ~67128 tris · 1 lights · 20 furniture pieces
* **Exterior doors:** F1_S4(S side) · interior doors: 0
* **Spawn points (local m):** front (-5.0, -8.5, 0)
* **Interactions:** open, use
* **Placed on island at:** (38.5, -45.7, 0.15), rotZ 0° · **Files:** `export/glb/power_gym.glb`, Blender collection `BLD_power_gym`

### 齒輪蒸汽工坊 Cog & Steam Works — `steampunk_works`

![day](renders/steampunk_works_front_day.png) ![night](renders/steampunk_works_front.png) ![plan](renders/steampunk_works_cut_day.png)

* **Style:** 蒸汽龐克工坊 / Steampunk Workshop · **Tier:** standard · **Type:** workshop · **Floors:** 3
* **Fits game styles:** steampunk, fantasy, victorian, anime, rpg
* **Description:** 3-storey copper-and-brick workshop: machine shop, drafting library, inventor's loft; giant brass gears, steam pipes, smokestacks, airship mooring mast.
* **Size:** 20.0 × 16.0 m footprint, 20.5 m tall · 226 objects · ~111756 tris · 13 lights · 42 furniture pieces
* **Exterior doors:** F1_S3(S side), F1_E1(E side) · interior doors: 8
* **Spawn points (local m):** front (1.8, -8.0, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (61.0, -102.2, 0.15), rotZ 0° · **Files:** `export/glb/steampunk_works.glb`, Blender collection `BLD_steampunk_works`

### 好鄰居超市 Good Neighbor Supermarket — `supermarket`

![day](renders/supermarket_front_day.png) ![night](renders/supermarket_front.png) ![plan](renders/supermarket_cut_day.png)

* **Style:** 郊區超市 / Suburban Supermarket · **Tier:** standard · **Type:** supermarket · **Floors:** 1
* **Fits game styles:** realistic, survival, zombie, slice-of-life, sims
* **Description:** Large steel-clad supermarket: aisles of double shelves, wall of drink fridges, checkout counters, carts, front parking.
* **Size:** 29.0 × 31.0 m footprint, 5.9 m tall · 148 objects · ~339100 tris · 1 lights · 107 furniture pieces
* **Exterior doors:** F1_S2(S side) · interior doors: 0
* **Spawn points (local m):** front (-6.0, -11.5, 0)
* **Interactions:** open, shop, use
* **Placed on island at:** (-131.5, -89.3, 0.15), rotZ 180° · **Files:** `export/glb/supermarket.glb`, Blender collection `BLD_supermarket`

### 老橡樹樹屋 Old Oak Treehouse — `treehouse_oak`

![day](renders/treehouse_oak_front_day.png) ![night](renders/treehouse_oak_front.png) ![plan](renders/treehouse_oak_cut_day.png)

* **Style:** 童話樹屋 / Storybook Treehouse · **Tier:** standard · **Type:** treehouse · **Floors:** 2
* **Fits game styles:** cozy, ghibli, adventure, cartoon, fantasy
* **Description:** Giant oak with a wrap deck at 4.5 m reached by a timber stair, a gabled cabin (bed, desk, lantern) and a rope ladder to a crow's-nest lookout.
* **Size:** 16.2 × 19.0 m footprint, 17.9 m tall · 73 objects · ~70380 tris · 7 lights · 3 furniture pieces
* **Exterior doors:** Cabin_S0(S side) · interior doors: 0
* **Spawn points (local m):** front (2.35, -6.1, 0)
* **Interactions:** climb, open, play, sleep, work
* **Placed on island at:** (43.0, -96.2, 0.15), rotZ 0° · **Files:** `export/glb/treehouse_oak.glb`, Blender collection `BLD_treehouse_oak`

### 皇冠都鐸酒館 The Crown Tudor Inn — `tudor_inn`

![day](renders/tudor_inn_front_day.png) ![night](renders/tudor_inn_front.png) ![plan](renders/tudor_inn_cut_day.png)

* **Style:** 英式都鐸 / English Tudor · **Tier:** standard · **Type:** pub + inn · **Floors:** 2
* **Fits game styles:** medieval, fantasy, rpg-village, realistic, europe
* **Description:** Stone ground-floor pub with bar and booths, half-timbered upper floor of guest rooms, steep tile gable, lanterns, hanging sign.
* **Size:** 17.0 × 16.0 m footprint, 13.5 m tall · 164 objects · ~67900 tris · 10 lights · 49 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side) · interior doors: 6
* **Spawn points (local m):** front (-1.13, -8.0, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (105.5, 15.8, 0.15), rotZ 0° · **Files:** `export/glb/tudor_inn.glb`, Blender collection `BLD_tudor_inn`

### 紅磚倉庫Loft Red-Brick Warehouse Lofts — `warehouse_loft`

![day](renders/warehouse_loft_front_day.png) ![night](renders/warehouse_loft_front.png) ![plan](renders/warehouse_loft_cut_day.png)

* **Style:** 工業倉庫改建 / Industrial Warehouse Loft · **Tier:** standard · **Type:** loft + workshop · **Floors:** 2
* **Fits game styles:** realistic, industrial, crime, cyberpunk, post-apocalyptic
* **Description:** Converted brick warehouse: G/F workshop and garage bay with roller door, two double-height studio lofts above, sawtooth glazed roof.
* **Size:** 25.0 × 19.0 m footprint, 10.8 m tall · 167 objects · ~100752 tris · 10 lights · 42 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_S3(S side), F1_E1(E side) · interior doors: 8
* **Spawn points (local m):** front (-2.4, -9.5, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (88.5, -79.3, 0.15), rotZ 180° · **Files:** `export/glb/warehouse_loft.glb`, Blender collection `BLD_warehouse_loft`

### 包浩斯白宅 Bauhaus White House — `bauhaus_house`

![day](renders/bauhaus_house_front_day.png) ![night](renders/bauhaus_house_front.png) ![plan](renders/bauhaus_house_cut_day.png)

* **Style:** 包浩斯 / Bauhaus Modernism · **Tier:** upscale · **Type:** house · **Floors:** 2
* **Fits game styles:** realistic, modern, architectural, anime
* **Description:** Crisp white cubic 2-storey house: ribbon windows, flat roof terrace, cantilever entrance canopy, red accent panel.
* **Size:** 17.8 × 15.6 m footprint, 9.5 m tall · 196 objects · ~79004 tris · 11 lights · 55 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_E1(E side), PH_W0(W side) · interior doors: 8
* **Spawn points (local m):** front (-2.0, -7.5, 0)
* **Interactions:** cook, open, sit, sleep, use, wash, work
* **Placed on island at:** (-25.5, -77.3, 0.15), rotZ 180° · **Files:** `export/glb/bauhaus_house.glb`, Blender collection `BLD_bauhaus_house`

### 貨櫃森林咖啡館 Container Grove Café — `cafe_container`

![day](renders/cafe_container_front_day.png) ![night](renders/cafe_container_front.png) ![plan](renders/cafe_container_cut_day.png)

* **Style:** 工業貨櫃現代 / Industrial Container Modern · **Tier:** upscale · **Type:** café / commercial · **Floors:** 2
* **Fits game styles:** realistic, modern, slice-of-life, anime
* **Description:** Raised concrete podium, timber post-and-beam café with full glazing, 20ft black container kitchen, outdoor stair to a planted terrace, 40ft yellow container lounge with sliding glass wall, timber canopy roof.
* **Size:** 23.1 × 14.8 m footprint, 9.7 m tall · 172 objects · ~109328 tris · 15 lights · 55 furniture pieces
* **Exterior doors:** Cafe_S1(S side), Kitchen_N0(N side), Lounge_S1(S side) · interior doors: 0
* **Spawn points (local m):** front_steps (-4.3, -7.06, 0)
* **Interactions:** cook, open, shop, sit, use
* **Placed on island at:** (85.0, 15.6, 0.15), rotZ 0° · **Files:** `export/glb/cafe_container.glb`, Blender collection `BLD_cafe_container`

### 綠廊生態公寓 Green Terrace Eco Apartments — `eco_apartments`

![day](renders/eco_apartments_front_day.png) ![night](renders/eco_apartments_front.png) ![plan](renders/eco_apartments_cut_day.png)

* **Style:** 綠建築生態宅 / Biophilic Eco Housing · **Tier:** upscale · **Type:** apartment · **Floors:** 5
* **Fits game styles:** solarpunk, realistic, modern, anime, utopia
* **Description:** 5-storey timber-clad eco block: every flat has a planted balcony with trailing greenery, roof garden with trees and solar.
* **Size:** 19.0 × 17.0 m footprint, 19.4 m tall · 571 objects · ~169412 tris · 25 lights · 171 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E2(E side), F2_S1(S side), F2_S4(S side), F3_S1(S side), F3_S4(S side), F4_S1(S side), F4_S4(S side), F5_S1(S side), F5_S4(S side), PH_W0(W side) · interior doors: 19
* **Spawn points (local m):** front (-3.0, -8.5, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (-107.5, -101.7, 0.15), rotZ 0° · **Files:** `export/glb/eco_apartments.glb`, Blender collection `BLD_eco_apartments`

### 黑玻璃創意辦公 Obsidian Cube Offices — `glass_cube_office`

![day](renders/glass_cube_office_front_day.png) ![night](renders/glass_cube_office_front.png) ![plan](renders/glass_cube_office_cut_day.png)

* **Style:** 當代玻璃辦公 / Contemporary Glass Office · **Tier:** upscale · **Type:** office · **Floors:** 4
* **Fits game styles:** modern, corporate, cyberpunk, realistic, thriller
* **Description:** 4-storey dark glass cube: lobby + café, open-plan offices and meeting rooms, roof terrace with solar canopy.
* **Size:** 21.0 × 23.0 m footprint, 17.7 m tall · 529 objects · ~176888 tris · 21 lights · 269 furniture pieces
* **Exterior doors:** F1_S3(S side), F1_E2(E side), PH_W0(W side) · interior doors: 16
* **Spawn points (local m):** front (-3.6, -10.5, 0)
* **Interactions:** open, shop, sit, use, wash, work
* **Placed on island at:** (64.5, -82.3, 0.15), rotZ 180° · **Files:** `export/glb/glass_cube_office.glb`, Blender collection `BLD_glass_cube_office`

### 玻璃溫室咖啡 Glasshouse Garden Café — `greenhouse_cafe`

![day](renders/greenhouse_cafe_front_day.png) ![night](renders/greenhouse_cafe_front.png) ![plan](renders/greenhouse_cafe_cut_day.png)

* **Style:** 玻璃溫室 / Victorian Glasshouse · **Tier:** upscale · **Type:** café · **Floors:** 1
* **Fits game styles:** cozy, ghibli, romance, solarpunk, realistic
* **Description:** Single-storey white-framed glasshouse with a glass gable roof: café counter, tables among potted palms and ferns.
* **Size:** 17.0 × 15.0 m footprint, 6.1 m tall · 93 objects · ~86260 tris · 1 lights · 68 furniture pieces
* **Exterior doors:** F1_S2(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -7.0, 0)
* **Interactions:** open, shop, sit, use
* **Placed on island at:** (-88.5, -102.2, 0.15), rotZ 0° · **Files:** `export/glb/greenhouse_cafe.glb`, Blender collection `BLD_greenhouse_cafe`

### 青瓦庭院宅 Slate-Roof Garden House — `house_eastasian_tile`

![day](renders/house_eastasian_tile_front_day.png) ![night](renders/house_eastasian_tile_front.png) ![plan](renders/house_eastasian_tile_cut_day.png)

* **Style:** 東亞傳統瓦屋 / East Asian Traditional · **Tier:** upscale · **Type:** house · **Floors:** 2
* **Fits game styles:** realistic, anime, wuxia-modern, cozy, rpg-village
* **Description:** Stone plinth, dark timber G/F with living/kitchen/bath, half-timbered plaster upper floor with tatami room and bedroom, blue slate hip roofs with upturned corners, covered balcony + outside stair, garden with lantern.
* **Size:** 18.5 × 17.3 m footprint, 9.2 m tall · 176 objects · ~99944 tris · 9 lights · 46 furniture pieces
* **Exterior doors:** GF_S1(S side) · interior doors: 4
* **Spawn points (local m):** garden_gate (-1.7, -8.4, 0)
* **Interactions:** cook, open, sit, sleep, use, wash
* **Placed on island at:** (-82.0, -17.5, 0.15), rotZ 180° · **Files:** `export/glb/house_eastasian_tile.glb`, Blender collection `BLD_house_eastasian_tile`

### 韓式韓屋 Korean Hanok — `korean_hanok`

![day](renders/korean_hanok_front_day.png) ![night](renders/korean_hanok_front.png) ![plan](renders/korean_hanok_cut_day.png)

* **Style:** 韓屋 / Korean Hanok · **Tier:** upscale · **Type:** house · **Floors:** 1
* **Fits game styles:** historical, kdrama, realistic, anime
* **Description:** Single-storey hanok on a stone plinth: timber posts, raised wooden maru veranda, paper sliding doors, curved tiled hip roof.
* **Size:** 20.4 × 16.5 m footprint, 7.4 m tall · 97 objects · ~45234 tris · 3 lights · 21 furniture pieces
* **Exterior doors:** F1_S2(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -7.0, 0)
* **Interactions:** cook, open, sit, sleep, use, work
* **Placed on island at:** (74.5, -16.8, 0.15), rotZ 180° · **Files:** `export/glb/korean_hanok.glb`, Blender collection `BLD_korean_hanok`

### 地中海白屋 Mediterranean White House — `med_villa`

![day](renders/med_villa_front_day.png) ![night](renders/med_villa_front.png) ![plan](renders/med_villa_cut_day.png)

* **Style:** 地中海風 / Mediterranean · **Tier:** upscale · **Type:** house · **Floors:** 2
* **Fits game styles:** realistic, summer, romance, anime
* **Description:** Whitewashed 2-storey house with blue door and shutters, terracotta hip roof, balcony, bougainvillea boxes.
* **Size:** 17.0 × 15.0 m footprint, 9.0 m tall · 191 objects · ~76794 tris · 10 lights · 50 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side), F2_S1(S side), F2_S3(S side) · interior doors: 8
* **Spawn points (local m):** front (-1.13, -7.5, 0)
* **Interactions:** cook, open, sit, sleep, use, wash, work
* **Placed on island at:** (-150.5, -15.3, 0.15), rotZ 180° · **Files:** `export/glb/med_villa.glb`, Blender collection `BLD_med_villa`

### 中世紀現代宅 Palm Springs Mid-Century House — `midcentury_house`

![day](renders/midcentury_house_front_day.png) ![night](renders/midcentury_house_front.png) ![plan](renders/midcentury_house_cut_day.png)

* **Style:** 中世紀現代 / Mid-Century Modern · **Tier:** upscale · **Type:** house · **Floors:** 1
* **Fits game styles:** retro, realistic, mad-men, modern, gta-like
* **Description:** Low single-storey timber house with floor-to-ceiling glass, butterfly-flat shed roof with deep eaves, stone chimney, carport.
* **Size:** 30.0 × 15.0 m footprint, 4.7 m tall · 70 objects · ~72408 tris · 3 lights · 24 furniture pieces
* **Exterior doors:** F1_S3(S side) · interior doors: 0
* **Spawn points (local m):** front (-2.0, -7.5, 0)
* **Interactions:** cook, open, sit, sleep, use, work
* **Placed on island at:** (23.0, -77.3, 0.15), rotZ 180° · **Files:** `export/glb/midcentury_house.glb`, Blender collection `BLD_midcentury_house`

### 摩洛哥庭園宅 Moroccan Riad House — `moroccan_riad`

![day](renders/moroccan_riad_front_day.png) ![night](renders/moroccan_riad_front.png) ![plan](renders/moroccan_riad_cut_day.png)

* **Style:** 摩洛哥風 / Moroccan Riad · **Tier:** upscale · **Type:** guesthouse · **Floors:** 2
* **Fits game styles:** fantasy, desert, realistic, adventure
* **Description:** Ochre 2-storey riad: carved arch door, mashrabiya grilles, tiled lounge, guest rooms, roof terrace with lanterns.
* **Size:** 17.0 × 17.0 m footprint, 9.5 m tall · 203 objects · ~87348 tris · 15 lights · 51 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E2(E side), PH_W0(W side) · interior doors: 8
* **Spawn points (local m):** front (-2.0, -8.5, 0)
* **Interactions:** cook, open, sit, sleep, use, wash, work
* **Placed on island at:** (-110.5, -16.3, 0.15), rotZ 180° · **Files:** `export/glb/moroccan_riad.glb`, Blender collection `BLD_moroccan_riad`

### 紐約褐石排屋 Brooklyn Brownstone — `nyc_brownstone`

![day](renders/nyc_brownstone_front_day.png) ![night](renders/nyc_brownstone_front.png) ![plan](renders/nyc_brownstone_cut_day.png)

* **Style:** 紐約褐石屋 / New York Brownstone · **Tier:** upscale · **Type:** townhouse · **Floors:** 4
* **Fits game styles:** realistic, noir, sitcom, crime, urban
* **Description:** Narrow 4-storey brownstone with raised stoop, double timber door, cornice, sash windows, flat roof with water tank.
* **Size:** 13.0 × 19.5 m footprint, 16.2 m tall · 254 objects · ~93460 tris · 14 lights · 54 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_E2(E side) · interior doors: 8
* **Spawn points (local m):** front (-1.6, -9.0, 0)
* **Interactions:** cook, open, sit, sleep, use, work
* **Placed on island at:** (-132.5, 18.3, 0.15), rotZ 0° · **Files:** `export/glb/nyc_brownstone.glb`, Blender collection `BLD_nyc_brownstone`

### 巴黎奧斯曼公寓 Parisian Haussmann Apartment — `paris_haussmann`

![day](renders/paris_haussmann_front_day.png) ![night](renders/paris_haussmann_front.png) ![plan](renders/paris_haussmann_cut_day.png)

* **Style:** 巴黎奧斯曼式 / Haussmann Parisian · **Tier:** upscale · **Type:** apartment · **Floors:** 4
* **Fits game styles:** realistic, romance, anime, noir, europe
* **Description:** Cream stone 4-storey block: corner café with terrace, wrought-iron balconies, mansard slate roof with dormers, cornice.
* **Size:** 19.0 × 17.5 m footprint, 17.6 m tall · 412 objects · ~136908 tris · 19 lights · 121 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side), F2_S1(S side), F2_S2(S side), F3_S1(S side), F3_S2(S side), F4_S1(S side), F4_S2(S side) · interior doors: 15
* **Spawn points (local m):** front (-4.0, -8.0, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (-149.5, 17.3, 0.15), rotZ 0° · **Files:** `export/glb/paris_haussmann.glb`, Blender collection `BLD_paris_haussmann`

### 日光艙屋 Solar Pod Home — `pod_solar`

![day](renders/pod_solar_front_day.png) ![night](renders/pod_solar_front.png) ![plan](renders/pod_solar_cut_day.png)

* **Style:** 科幻離網艙屋 / Sci-Fi Off-Grid Module · **Tier:** upscale · **Type:** house · **Floors:** 2
* **Fits game styles:** sci-fi, solarpunk, post-apocalyptic, anime, realistic
* **Description:** Raised copper module house: pipe-frame base + deck, lower glazed kitchen/lab pod, interior stair to an upper sleeping module with wrap balcony, roof hatch, two large tilting solar panels, antenna mast, hydroponic planters.
* **Size:** 18.0 × 16.0 m footprint, 11.4 m tall · 117 objects · ~75152 tris · 5 lights · 24 furniture pieces
* **Exterior doors:** Lo_S1(S side), Up_S1(S side) · interior doors: 0
* **Spawn points (local m):** deck_stair (1.2, -6.32, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, work
* **Placed on island at:** (56.0, -17.0, 0.15), rotZ 180° · **Files:** `export/glb/pod_solar.glb`, Blender collection `BLD_pod_solar`

### 西班牙莊園 Spanish Hacienda — `spanish_hacienda`

![day](renders/spanish_hacienda_front_day.png) ![night](renders/spanish_hacienda_front.png) ![plan](renders/spanish_hacienda_cut_day.png)

* **Style:** 西班牙殖民風 / Spanish Colonial · **Tier:** upscale · **Type:** house · **Floors:** 1
* **Fits game styles:** western, realistic, telenovela, rpg-village
* **Description:** Long single-storey stucco ranch house with arched veranda, terracotta roof, living/dining/kitchen/bedrooms.
* **Size:** 21.0 × 18.5 m footprint, 5.6 m tall · 93 objects · ~67898 tris · 6 lights · 30 furniture pieces
* **Exterior doors:** F1_S3(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -8.0, 0)
* **Interactions:** cook, open, sit, sleep, use, work
* **Placed on island at:** (-130.5, -18.3, 0.15), rotZ 180° · **Files:** `export/glb/spanish_hacienda.glb`, Blender collection `BLD_spanish_hacienda`

### 阿爾卑斯木屋 Alpine Swiss Chalet — `swiss_chalet`

![day](renders/swiss_chalet_front_day.png) ![night](renders/swiss_chalet_front.png) ![plan](renders/swiss_chalet_cut_day.png)

* **Style:** 瑞士山屋 / Swiss Alpine Chalet · **Tier:** upscale · **Type:** house · **Floors:** 2
* **Fits game styles:** realistic, cozy, winter, anime, europe
* **Description:** Stone base + log upper storey, wide low gable with deep eaves, wrap balcony with flower boxes, red shutters.
* **Size:** 16.0 × 15.0 m footprint, 10.0 m tall · 178 objects · ~76692 tris · 9 lights · 44 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side), F2_S1(S side), F2_S3(S side) · interior doors: 7
* **Spawn points (local m):** front (-1.13, -7.5, 0)
* **Interactions:** cook, open, sit, sleep, use, wash, work
* **Placed on island at:** (123.0, 15.3, 0.15), rotZ 0° · **Files:** `export/glb/swiss_chalet.glb`, Blender collection `BLD_swiss_chalet`

### 海港儲蓄銀行 Harbor Savings Bank — `bank_classical`

![day](renders/bank_classical_front_day.png) ![night](renders/bank_classical_front.png) ![plan](renders/bank_classical_cut_day.png)

* **Style:** 新古典銀行 / Neoclassical Bank · **Tier:** luxury · **Type:** bank · **Floors:** 2
* **Fits game styles:** realistic, heist, noir, western, civic
* **Description:** Granite neoclassical bank on a podium: columned portico with pediment, banking hall with teller counter, vault/server room, offices upstairs.
* **Size:** 19.0 × 22.0 m footprint, 10.5 m tall · 171 objects · ~89940 tris · 7 lights · 60 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side) · interior doors: 5
* **Spawn points (local m):** front (-1.0, -9.0, 0)
* **Interactions:** open, shop, sit, use, wash, work
* **Placed on island at:** (-70.5, -41.2, 0.15), rotZ 0° · **Files:** `export/glb/bank_classical.glb`, Blender collection `BLD_bank_classical`

### 清水模住宅 Fair-faced Concrete House — `concrete_minimal`

![day](renders/concrete_minimal_front_day.png) ![night](renders/concrete_minimal_front.png) ![plan](renders/concrete_minimal_cut_day.png)

* **Style:** 日式清水模 / Japanese Minimalist Concrete · **Tier:** luxury · **Type:** house · **Floors:** 2
* **Fits game styles:** realistic, modern, thriller, zen, architectural
* **Description:** Introverted fair-faced concrete 2-storey house: few deep windows, minimal interior, flat roof, single maple tree.
* **Size:** 16.4 × 17.8 m footprint, 7.0 m tall · 118 objects · ~82250 tris · 7 lights · 31 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_E0(E side) · interior doors: 5
* **Spawn points (local m):** front (-2.4, -8.5, 0)
* **Interactions:** cook, open, sit, sleep, use, wash, work
* **Placed on island at:** (45.5, -78.3, 0.15), rotZ 180° · **Files:** `export/glb/concrete_minimal.glb`, Blender collection `BLD_concrete_minimal`

### 裝飾藝術大飯店 Grand Deco Hotel — `hotel_artdeco`

![day](renders/hotel_artdeco_front_day.png) ![night](renders/hotel_artdeco_front.png) ![plan](renders/hotel_artdeco_cut_day.png)

* **Style:** 裝飾藝術風 / Art Deco Hotel · **Tier:** luxury · **Type:** hotel · **Floors:** 6
* **Fits game styles:** noir, 1920s, realistic, mystery, bioshock-like
* **Description:** 6-storey Art Deco hotel: black-marble lobby with reception + bar, restaurant, 24 guest rooms, brass-trimmed stepped crown, vertical fins.
* **Size:** 21.0 × 21.0 m footprint, 28.2 m tall · 609 objects · ~137704 tris · 40 lights · 188 furniture pieces
* **Exterior doors:** F1_S3(S side), F1_E2(E side) · interior doors: 34
* **Spawn points (local m):** front (-3.0, -9.5, 0)
* **Interactions:** open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (134.5, -42.7, 0.15), rotZ 0° · **Files:** `export/glb/hotel_artdeco.glb`, Blender collection `BLD_hotel_artdeco`

### 海港金融中心 Harbor Finance Tower — `office_glass_tower`

![day](renders/office_glass_tower_front_day.png) ![night](renders/office_glass_tower_front.png) ![plan](renders/office_glass_tower_cut_day.png)

* **Style:** 現代玻璃帷幕大樓 / Modern Glass High-rise · **Tier:** luxury · **Type:** office high-rise · **Floors:** 10
* **Fits game styles:** realistic, modern, corporate, thriller, cyberpunk
* **Description:** 20x20 m, 10 floors: marble lobby + reception, 2 elevator shafts (car objects with level data) + fire stair, open-plan offices / meeting / pantry / server room, 5 vacant shell floors for custom fit-out, executive suite, roof with helipad and plant.
* **Size:** 26.0 × 25.5 m footprint, 41.9 m tall · 1205 objects · ~290760 tris · 105 lights · 479 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_S2(S side), F1_N1(N side), RoofCore_S0(S side) · interior doors: 23
* **Spawn points (local m):** forecourt (0.0, -14.0, 0)
* **Interactions:** cook, elevator, elevator_call, open, shop, sit, use, wash, work
* **Placed on island at:** (20.0, 20.5, 0.15), rotZ 0° · **Files:** `export/glb/office_glass_tower.glb`, Blender collection `BLD_office_glass_tower`

### 白崖現代豪宅 White Cliff Modern Villa — `villa_luxury_modern`

![day](renders/villa_luxury_modern_front_day.png) ![night](renders/villa_luxury_modern_front.png) ![plan](renders/villa_luxury_modern_cut_day.png)

* **Style:** 奢華現代主義別墅 / Luxury Modernist Villa · **Tier:** luxury · **Type:** villa · **Floors:** 2
* **Fits game styles:** realistic, modern, thriller, life-sim, anime
* **Description:** Glass-walled concrete living pavilion (living/dining/kitchen island), floating stair, cantilevered upper volume with master suite + ensuite, 2nd bedroom, study, garage with car, roof terrace, infinity pool & deck.
* **Size:** 31.8 × 25.3 m footprint, 7.8 m tall · 188 objects · ~92416 tris · 15 lights · 64 furniture pieces
* **Exterior doors:** A_S1(S side), B_S0(S side), B_W0(W side), C_E0(E side) · interior doors: 4
* **Spawn points (local m):** front_gate (1.8, -12.5, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (-82.0, 19.0, 0.15), rotZ 0° · **Files:** `export/glb/villa_luxury_modern.glb`, Blender collection `BLD_villa_luxury_modern`

### 霓光電路別墅 Neon Circuit Villa — `villa_neon_circuit`

![day](renders/villa_neon_circuit_front_day.png) ![night](renders/villa_neon_circuit_front.png) ![plan](renders/villa_neon_circuit_cut_day.png)

* **Style:** 近未來科技別墅 / Near-Future Tech Villa · **Tier:** luxury · **Type:** villa · **Floors:** 2
* **Fits game styles:** cyberpunk, sci-fi, near-future, realistic, anime
* **Description:** Charcoal composite villa with cyan circuit-trace lighting: gated courtyard, glowing steps, G/F lounge + kitchen + game room, 2F suite with balcony, west wing with roof terrace reached by an outside stair.
* **Size:** 24.0 × 23.0 m footprint, 7.3 m tall · 180 objects · ~79288 tris · 15 lights · 45 furniture pieces
* **Exterior doors:** M_S1(S side), M_W0(W side), U_S1(S side), U_W0(W side), Wg_S1(S side) · interior doors: 3
* **Spawn points (local m):** gate (0.0, -11.5, 0)
* **Interactions:** cook, open, play, sit, sleep, use, wash, work
* **Placed on island at:** (26.0, -20.5, 0.15), rotZ 180° · **Files:** `export/glb/villa_neon_circuit.glb`, Blender collection `BLD_villa_neon_circuit`

### 獅鷲城堡塔 Griffin Castle Keep — `castle_keep`

![day](renders/castle_keep_front_day.png) ![night](renders/castle_keep_front.png) ![plan](renders/castle_keep_cut_day.png)

* **Style:** 中世紀城堡 / Medieval Castle Keep · **Tier:** landmark · **Type:** castle · **Floors:** 4
* **Fits game styles:** fantasy, medieval, rpg, strategy, realistic
* **Description:** 4-storey square stone keep with corner turrets: great hall, armoury/storage, lord's chamber + library, crenellated roof walk with banners.
* **Size:** 22.0 × 17.0 m footprint, 21.3 m tall · 370 objects · ~131780 tris · 17 lights · 92 furniture pieces
* **Exterior doors:** F1_S3(S side), F1_E2(E side), PH_W0(W side) · interior doors: 12
* **Spawn points (local m):** front (-2.0, -8.5, 0)
* **Interactions:** open, shop, sit, sleep, use, work
* **Placed on island at:** (-22.0, -101.7, 0.15), rotZ 0° · **Files:** `export/glb/castle_keep.glb`, Blender collection `BLD_castle_keep`

### 海角燈塔 Cape Lighthouse — `lighthouse_cape`

![day](renders/lighthouse_cape_front_day.png) ![night](renders/lighthouse_cape_front.png) ![plan](renders/lighthouse_cape_cut_day.png)

* **Style:** 海事燈塔 / Maritime Lighthouse · **Tier:** landmark · **Type:** lighthouse · **Floors:** 5
* **Fits game styles:** realistic, horror, mystery, adventure, ghibli
* **Description:** Red/white striped 5-storey round tower with spiral stair, gallery deck, glazed lantern room with glowing lens; keeper's cottage.
* **Size:** 18.4 × 20.0 m footprint, 21.1 m tall · 418 objects · ~95048 tris · 7 lights · 7 furniture pieces
* **Exterior doors:** F1_8_0(S side), Lantern_8_0(S side), Cottage_S0(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -5.7, 0)
* **Interactions:** open, sit, sleep, use
* **Placed on island at:** (-56.0, -99.7, 0.15), rotZ 0° · **Files:** `export/glb/lighthouse_cape.glb`, Blender collection `BLD_lighthouse_cape`

### 星穹天文台 Starvault Observatory — `observatory_dome`

![day](renders/observatory_dome_front_day.png) ![night](renders/observatory_dome_front.png) ![plan](renders/observatory_dome_cut_day.png)

* **Style:** 圓頂天文台 / Domed Observatory · **Tier:** landmark · **Type:** observatory · **Floors:** 2
* **Fits game styles:** sci-fi, realistic, mystery, anime, academy
* **Description:** 12-sided white drum: visitor/lab floor, control room, telescope floor under a copper dome with an opening slit and a large telescope.
* **Size:** 14.0 × 16.0 m footprint, 12.8 m tall · 168 objects · ~75716 tris · 3 lights · 14 furniture pieces
* **Exterior doors:** F1_8_0(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -7.5, 0)
* **Interactions:** open, sit, use, work
* **Placed on island at:** (78.0, -101.7, 0.15), rotZ 0° · **Files:** `export/glb/observatory_dome.glb`, Blender collection `BLD_observatory_dome`

### 朱鳥神社 Vermilion Bird Shrine — `shinto_shrine`

![day](renders/shinto_shrine_front_day.png) ![night](renders/shinto_shrine_front.png) ![plan](renders/shinto_shrine_cut_day.png)

* **Style:** 日式神社 / Japanese Shinto Shrine · **Tier:** landmark · **Type:** shrine · **Floors:** 1
* **Fits game styles:** anime, japan, fantasy, horror, realistic
* **Description:** Vermilion shrine hall on a stone plinth with sliding paper doors and a curved slate gable; torii gate, stone lanterns, offering box, bell, sacred tree.
* **Size:** 20.3 × 20.0 m footprint, 6.8 m tall · 69 objects · ~60756 tris · 1 lights · 12 furniture pieces
* **Exterior doors:** F1_S2(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -6.5, 0)
* **Interactions:** open, sit, use
* **Placed on island at:** (95.0, -96.7, 0.15), rotZ 0° · **Files:** `export/glb/shinto_shrine.glb`, Blender collection `BLD_shinto_shrine`

### 海角石砌教堂 Cape Stone Chapel — `stone_chapel`

![day](renders/stone_chapel_front_day.png) ![night](renders/stone_chapel_front.png) ![plan](renders/stone_chapel_cut_day.png)

* **Style:** 哥德復興教堂 / Gothic Revival Chapel · **Tier:** landmark · **Type:** chapel · **Floors:** 1
* **Fits game styles:** realistic, horror, romance, fantasy, wedding
* **Description:** Stone nave with tall lancet windows, rows of pews and altar, steep slate gable, square bell tower with brass bell and spire.
* **Size:** 21.2 × 22.9 m footprint, 19.7 m tall · 74 objects · ~67556 tris · 1 lights · 27 furniture pieces
* **Exterior doors:** F1_S2(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -11.0, 0)
* **Interactions:** open, sit, use
* **Placed on island at:** (18.0, -43.2, 0.15), rotZ 0° · **Files:** `export/glb/stone_chapel.glb`, Blender collection `BLD_stone_chapel`

### 天界樓閣 Heaven Gate Pavilion — `temple_pagoda`

![day](renders/temple_pagoda_front_day.png) ![night](renders/temple_pagoda_front.png) ![plan](renders/temple_pagoda_cut_day.png)

* **Style:** 中式樓閣廟宇 / Chinese Pagoda Temple (neo-oriental) · **Tier:** landmark · **Type:** temple / landmark · **Floors:** 3
* **Fits game styles:** wuxia, fantasy, cyberpunk-oriental, anime, realistic
* **Description:** Stone podium with front stair, 3-storey timber pavilion (altar hall / scripture library / lookout) linked by interior stairs, verandas with red columns, triple curled hip roofs, neon-lit paifang gate and red lantern strings.
* **Size:** 24.0 × 30.0 m footprint, 20.5 m tall · 243 objects · ~133308 tris · 11 lights · 18 furniture pieces
* **Exterior doors:** T1_S6(S side), T2_S4(S side), T2_N4(N side), T2_W2(W side) · interior doors: 0
* **Spawn points (local m):** gate (0.0, -18.0, 0)
* **Interactions:** open, sit, use
* **Placed on island at:** (-28.0, -27.0, 0.15), rotZ 180° · **Files:** `export/glb/temple_pagoda.glb`, Blender collection `BLD_temple_pagoda`

### 風車磨坊 Old Dutch Windmill — `windmill_dutch`

![day](renders/windmill_dutch_front_day.png) ![night](renders/windmill_dutch_front.png) ![plan](renders/windmill_dutch_cut_day.png)

* **Style:** 荷蘭風車 / Dutch Tower Windmill · **Tier:** landmark · **Type:** windmill · **Floors:** 3
* **Fits game styles:** rpg-village, fantasy, cozy, farming-sim, realistic
* **Description:** 8-sided brick windmill: grain store, millstone floor with reefing gallery, miller's loft; timber cap with four lattice sails (rotate prop).
* **Size:** 15.2 × 16.0 m footprint, 17.2 m tall · 201 objects · ~64816 tris · 4 lights · 9 furniture pieces
* **Exterior doors:** F1_5_0(S side), F2_5_0(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -5.9, 0)
* **Interactions:** open, sleep, use
* **Placed on island at:** (-40.0, -101.7, 0.15), rotZ 0° · **Files:** `export/glb/windmill_dutch.glb`, Blender collection `BLD_windmill_dutch`

### 星辰法師塔 Starlight Wizard Tower — `wizard_tower`

![day](renders/wizard_tower_front_day.png) ![night](renders/wizard_tower_front.png) ![plan](renders/wizard_tower_cut_day.png)

* **Style:** 奇幻法師塔 / High-Fantasy Wizard Tower · **Tier:** landmark · **Type:** tower · **Floors:** 4
* **Fits game styles:** fantasy, rpg, anime, magic-school, ghibli
* **Description:** 12-sided stone tower: library, alchemy lab, bedchamber and star-gazing study linked by a spiral stair; tall blue cone roof, glowing crystals.
* **Size:** 14.0 × 16.0 m footprint, 22.1 m tall · 294 objects · ~91672 tris · 6 lights · 17 furniture pieces
* **Exterior doors:** F1_8_0(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -6.7, 0)
* **Interactions:** cook, open, sleep, use
* **Placed on island at:** (-72.0, -101.7, 0.15), rotZ 0° · **Files:** `export/glb/wizard_tower.glb`, Blender collection `BLD_wizard_tower`

## 環境 Environment — `island_town`

Island ~300×225 m: town flats, two crossing streets with sidewalks, curbs, lane markings, zebra crossings, street lamps, beach palms, snowy north hill (polar station plateau, z = 7 m), sea plane at z = −0.6 m. File: `export/glb/island_town.glb`.
