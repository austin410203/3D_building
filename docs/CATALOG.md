# TownKit 建築資產目錄 / Building Asset Catalog

Procedurally built in Blender 5.2 (`scripts/`), placed on one island template (`TownKit.blend`). Every building is walkable inside (stairs, doors, furnished rooms) and carries machine-readable metadata.

## 快速索引 Quick index

| asset_id | 名稱 | Name | 風格 Style | Tier | Type | Floors | Size W×D×H (m) | Game styles |
|---|---|---|---|---|---|---|---|---|
| `american_diner` | 海港餐車 | Harborline Diner | 美式復古餐車 / 1950s American Diner | budget | diner | 1 | 19.0 × 16.0 × 5.9 | retro, realistic, horror, road-movie, cartoon |
| `auto_repair` | 老王汽車修理廠 | Wang's Auto Repair | 汽車修理廠 / Auto Repair Garage | budget | garage | 1 | 22.0 × 15.0 × 5.1 | realistic, gta-like, slice-of-life, crime |
| `backpacker_hostel` | 背包客棧 | Backpackers' Hostel | 背包客棧 / Asian Backpacker Hostel | budget | hostel | 5 | 15.0 × 16.0 × 19.1 | slice-of-life, anime, realistic, adventure |
| `bento_shop` | 池上便當店 | Railway Bento Shop | 便當店 / Taiwanese Bento Shop | budget | restaurant | 2 | 13.0 × 15.0 × 7.3 | taiwan, slice-of-life, anime |
| `blacksmith_forge` | 鐵匠鋪 | Ironhand Blacksmith | 鐵匠鋪 / Medieval Blacksmith | budget | forge | 1 | 15.0 × 13.0 × 7.5 | medieval, fantasy, rpg, survival |
| `bubble_tea_flats` | 珍珠奶茶公寓 | Boba Tea Walk-up | 台式店面 / Taiwanese Shop Walk-up | budget | shop + flats | 3 | 12.0 × 15.0 × 10.5 | taiwan, slice-of-life, anime |
| `capsule_tower` | 蜂巢膠囊旅館 | Hive Capsule Hotel | 膠囊旅館 / Capsule Hotel Tower | budget | capsule hotel | 7 | 14.0 × 16.0 × 23.7 | cyberpunk, anime, sci-fi, realistic, japan |
| `container_flats` | 三色貨櫃公寓 | Tricolour Container Flats | 貨櫃公寓 / Shipping-Container Apartments | budget | apartment | 3 | 17.0 × 15.0 × 12.7 | industrial, post-apocalyptic, modern, realistic |
| `cyberware_clinic` | 義體改造診所 | Cyberware Clinic | 賽博義體診所 / Cyberpunk Ripperdoc | budget | clinic | 3 | 13.0 × 15.0 × 10.5 | cyberpunk, sci-fi, horror, neo-noir |
| `electronics_shop` | 光華電器行 | Guanghua Electronics | 電器行 / Asian Electronics Store | budget | shop | 3 | 14.0 × 16.0 × 10.5 | cyberpunk, slice-of-life, anime, realistic |
| `favela_stack` | 里約彩色堆疊屋 | Rio Hillside Stack | 巴西彩色堆疊屋 / Brazilian Favela Block | budget | apartment | 4 | 13.0 × 15.0 × 18.5 | realistic, action, urban-survival, gta-like |
| `gas_station` | 海港加油站 | Harbor Gas & Go | 公路加油站 / Roadside Gas Station | budget | gas station | 1 | 24.0 × 25.0 × 6.5 | realistic, road-movie, survival, horror, open-world |
| `haunted_house` | 荒山鬼屋 | Hollow Hill Haunted House | 鬼屋 / Haunted Victorian | budget | house | 2 | 16.7 × 14.9 × 13.5 | horror, halloween, mystery, zombie |
| `hk_tonglau` | 旺角唐樓 | Hong Kong Tong Lau | 香港唐樓 / Hong Kong Tenement | budget | tenement | 6 | 13.0 × 17.0 × 24.1 | cyberpunk, noir, realistic, action, hk-cinema |
| `izakaya_suikei` | 居酒屋 酔鯨 | Izakaya Drunken Whale | 日式居酒屋 / Japanese Izakaya | budget | bar + flat | 2 | 14.0 × 15.0 × 9.4 | anime, slice-of-life, japan, realistic, noir |
| `kr_mart_gosiwon` | 首爾便利店考試院 | Seoul Mart & Gosiwon | 韓式住商 / Korean Mixed-use Walk-up | budget | shop + dorm | 4 | 14.0 × 16.0 × 15.9 | kdrama, slice-of-life, realistic, horror |
| `laundromat_flats` | 泡泡自助洗衣 | Bubbles Laundromat | 自助洗衣公寓 / Urban Laundromat Walk-up | budget | laundromat + flats | 3 | 13.0 × 15.0 × 12.7 | slice-of-life, anime, realistic, noir |
| `manga_netcafe` | 漫畫網咖 | Manga & Net Café | 漫畫網咖 / Japanese Manga Café | budget | net café | 3 | 14.0 × 16.0 × 10.5 | anime, japan, cyberpunk, slice-of-life |
| `mongol_yurt` | 草原蒙古包 | Steppe Ger (Yurt) | 蒙古包 / Mongolian Ger | budget | yurt | 1 | 14.0 × 16.0 × 5.4 | nomad, survival, historical, cozy |
| `night_market_row` | 夜市攤商街屋 | Night Market Row | 台灣夜市 / Taiwanese Night Market | budget | market | 1 | 21.0 × 16.5 × 4.8 | taiwan, slice-of-life, anime, realistic |
| `pirate_tavern` | 黑帆海盜酒館 | Black Sail Pirate Tavern | 海盜酒館 / Pirate Port Tavern | budget | tavern | 2 | 17.0 × 15.0 × 9.6 | pirate, fantasy, adventure, rpg |
| `red_barn` | 美式紅穀倉 | Red Prairie Barn | 美式穀倉 / American Barn | budget | barn | 2 | 24.0 × 17.0 × 10.4 | farming-sim, western, horror, americana |
| `seaview_motel` | 海景汽車旅館 | Seaview Motor Inn | 公路汽車旅館 / American Roadside Motel | budget | motel | 2 | 29.0 × 20.1 × 6.8 | road-movie, horror, noir, realistic, retro |
| `sheriff_office` | 警長辦公室 | Sheriff's Office | 西部警長屋 / Wild West Jailhouse | budget | jail | 1 | 14.0 × 13.0 × 5.2 | western, cartoon, rpg, realistic |
| `shop_neon_corner` | 藍調轉角雜貨 | Blue Corner Bodega | 霓虹轉角店 / Neon Corner Shop Diorama | budget | shop + flat | 2 | 15.5 × 14.0 × 10.0 | cyberpunk, anime, slice-of-life, diorama, realistic |
| `tipi_camp` | 平原帳篷營地 | Plains Tipi Camp | 帳篷營地 / Plains Tipi Encampment | budget | camp | 1 | 20.0 × 18.0 × 7.5 | western, survival, historical, nomad |
| `tower_cyber_narrow` | 霓虹窄塔 | Neon Sliver Tower | 賽博龐克窄樓 / Cyberpunk Vertical Block | budget | mixed-use tower | 5 | 9.2 × 10.0 × 22.1 | cyberpunk, sci-fi, neo-noir, realistic |
| `vn_tube_house` | 河內管狀屋 | Hanoi Tube House | 越南管狀屋 / Vietnamese Tube House | budget | house + café | 5 | 9.0 × 21.0 × 18.3 | realistic, southeast-asia, slice-of-life |
| `western_saloon` | 荒野西部酒館 | Dusty Spur Saloon | 西部酒館 / Wild West Saloon | budget | saloon | 2 | 17.0 × 16.0 × 9.2 | western, realistic, cartoon, rpg |
| `witch_cottage` | 林間女巫小屋 | Witch's Woodland Cottage | 女巫小屋 / Storybook Witch Cottage | budget | cottage | 1 | 13.1 × 12.0 × 11.0 | fantasy, horror, ghibli, halloween |
| `cold_storage` | 冷鏈冷凍廠 | Cold-Chain Plant | 冷凍廠 / Cold Storage Facility | utility | factory | 1 | 21.0 × 17.0 × 7.6 | realistic, horror, thriller, industrial |
| `data_center` | 雲端資料中心 | Nimbus Data Center | 資料中心 / Hyperscale Data Center | utility | data center | 2 | 30.0 × 19.0 × 9.9 | cyberpunk, sci-fi, thriller, realistic, hacker |
| `drone_hub` | 無人機物流站 | Drone Delivery Hub | 無人機站 / Drone Logistics Hub | utility | logistics | 3 | 17.0 × 17.0 × 12.7 | sci-fi, modern, cyberpunk |
| `logistics_warehouse` | 物流倉儲中心 | Logistics Warehouse | 物流倉庫 / Distribution Warehouse | utility | warehouse | 1 | 28.0 × 30.0 × 7.9 | realistic, industrial, zombie, action |
| `parking_tower` | 立體停車塔 | Multi-storey Car Park | 立體停車場 / Parking Structure | utility | parking | 5 | 21.0 × 19.0 × 16.4 | realistic, action, gta-like, urban |
| `station_arctic` | 極光貨櫃研究站 | Aurora Container Research Station | 極地貨櫃前哨站 / Polar Container Outpost | utility | research station | 2 | 28.6 × 15.7 × 10.7 | realistic, survival, sci-fi, thriller, post-apocalyptic |
| `vertical_farm` | 垂直農場 | Vertical Farm Tower | 垂直農場 / Vertical Farm | utility | farm | 5 | 19.0 × 17.0 × 19.1 | solarpunk, sci-fi, farming-sim, realistic |
| `fire_station` | 海港消防局 | Harbor Fire Station | 消防局 / Civic Fire Station | civic | fire station | 2 | 26.0 × 22.0 × 15.4 | realistic, rescue-sim, anime, action |
| `hospital_general` | 仁心綜合醫院 | Renxin General Hospital | 現代醫院 / Modern Hospital | civic | hospital | 3 | 27.0 × 24.0 × 13.5 | realistic, horror, medical-drama, zombie, anime |
| `kindergarten` | 彩虹幼兒園 | Rainbow Kindergarten | 童趣幼兒園 / Playful Kindergarten | civic | kindergarten | 1 | 19.0 × 19.0 × 7.6 | anime, slice-of-life, cozy, horror, cartoon |
| `knight_barracks` | 騎士兵營 | Knights' Barracks | 騎士兵營 / Medieval Barracks | civic | barracks | 2 | 21.0 × 18.0 × 10.4 | medieval, fantasy, strategy, rpg |
| `library_brutalist` | 市立混凝土圖書館 | Concrete Public Library | 粗獷主義 / Brutalist | civic | library | 2 | 23.0 × 21.0 × 9.4 | realistic, dystopian, mystery, anime, post-apocalyptic |
| `police_station` | 海港警察局 | Harbor Police Station | 警察局 / Civic Police Station | civic | police station | 2 | 23.0 × 22.0 × 10.0 | realistic, crime, action, detective, anime |
| `post_office` | 海港郵局 | Harbor Post Office | 郵局 / Civic Post Office | civic | post office | 1 | 17.0 × 15.0 × 4.7 | realistic, slice-of-life, anime, rpg-village |
| `school_primary` | 海港國民小學 | Harbor Primary School | 公立學校 / Asian Public School | civic | school | 3 | 31.0 × 24.5 × 11.1 | slice-of-life, anime, horror, realistic, school-life |
| `a_frame_cabin` | 森林A字木屋 | Forest A-Frame Cabin | A字型木屋 / A-Frame Cabin | standard | cabin | 2 | 15.8 × 16.4 × 7.6 | cozy, horror, survival, realistic, winter |
| `apt_block_6f` | 朝陽社區公寓 | Sunrise Walk-up Apartments | 台式公寓 / Taiwanese Walk-up Apartment | standard | apartment block | 6 | 19.0 × 15.1 × 22.0 | realistic, slice-of-life, anime, urban-survival |
| `apt_urban_5f` | 夜巷住商公寓 | Night Alley Mixed-Use Apartment | 都市亞洲住商 / Urban Asian Mixed-Use | standard | apartment | 5 | 13.2 × 13.4 × 22.5 | realistic, anime, slice-of-life, cyberpunk-lite |
| `bakery_corner` | 麥香麵包坊 | Wheat & Hearth Bakery | 歐式麵包店 / European Bakery | standard | bakery + flat | 2 | 14.0 × 15.0 × 10.7 | cozy, anime, slice-of-life, realistic, ghibli |
| `bookstore_cafe` | 書與咖啡 | Books & Beans | 紅磚書店咖啡 / Brick Bookshop Café | standard | bookstore + café | 3 | 15.0 × 16.0 × 10.5 | cozy, anime, slice-of-life, realistic, mystery |
| `brick_heritage_cafe` | 紅磚老宅咖啡 | Red-Brick Heritage Café | 老宅咖啡 / Taiwanese Heritage House | standard | café | 2 | 14.0 × 16.0 × 7.3 | taiwan, cozy, slice-of-life, realistic |
| `canal_twin_tower` | 運河雙子樓 | Canal Twin Houses | 港灣運河樓房 / Harbour Canal Townhouses | standard | mixed-use townhouses | 6 | 22.9 × 36.2 × 21.8 | realistic, anime, ghibli, fantasy-port, slice-of-life |
| `chicago_walkup` | 芝加哥紅磚公寓 | Chicago Brick Three-Flat | 芝加哥公寓 / Chicago Greystone/Brick Flat | standard | apartment | 4 | 17.0 × 17.0 × 14.8 | noir, crime, realistic, americana |
| `club_nova` | 新星夜店 | Club Nova | 霓虹夜店 / Neon Nightclub | standard | nightclub | 2 | 19.0 × 17.0 × 8.3 | cyberpunk, nightlife, crime, anime |
| `corner_pharmacy` | 健康藥局 | Health Pharmacy | 社區藥局 / Asian Neighbourhood Pharmacy | standard | pharmacy | 3 | 13.0 × 15.0 × 10.5 | slice-of-life, realistic, zombie |
| `cowork_hub` | 共享辦公大樓 | Co-Work Hub | 共享辦公 / Co-working Office | standard | office | 4 | 19.0 × 17.0 × 15.9 | modern, slice-of-life, realistic |
| `craft_brewery` | 精釀啤酒廠 | Harbor Craft Brewery | 精釀酒廠 / Craft Brewery Taproom | standard | brewery | 2 | 24.0 × 17.0 × 9.6 | realistic, slice-of-life, industrial, rpg |
| `dwarf_stonehall` | 矮人石廳 | Dwarven Stonehall | 矮人石屋 / Dwarven Hall | standard | forge hall | 1 | 15.0 × 14.0 × 5.8 | fantasy, rpg, medieval, dnd |
| `english_cottage` | 英式茅草小屋 | English Thatched Cottage | 英式鄉村小屋 / English Country Cottage | standard | cottage | 2 | 14.0 × 15.6 × 11.9 | cozy, europe, farming-sim, anime, ghibli |
| `ev_charging_hub` | 電動車超充站 | EV Supercharge Hub | 電動車充電站 / EV Charging Station | standard | charging station | 1 | 24.0 × 23.0 × 5.0 | modern, sci-fi, gta-like, realistic |
| `florist_petal` | 花語花店 | Petal Talk Florist | 鄉村花店 / Cottage Flower Shop | standard | shop + flat | 2 | 13.0 × 15.5 × 10.1 | cozy, anime, romance, slice-of-life, ghibli |
| `galaxy_arcade` | 銀河遊戲中心 | Galaxy Game Center | 霓虹遊樂場 / Neon Game Arcade | standard | arcade | 2 | 19.0 × 17.0 × 7.7 | cyberpunk, anime, retro, nightlife, realistic |
| `german_fachwerk` | 德式木筋屋 | German Fachwerk House | 德國木筋屋 / German Half-Timbered | standard | house + shop | 3 | 16.0 × 15.0 × 17.2 | europe, fantasy, rpg-village, christmas, realistic |
| `gingerbread_house` | 薑餅糖果屋 | Gingerbread Candy House | 糖果屋 / Fairy-tale Candy House | standard | house | 1 | 13.0 × 13.0 × 7.1 | fantasy, christmas, cartoon, family |
| `hk_dimsum_hall` | 金龍酒家 | Golden Dragon Dim Sum Hall | 港式茶樓 / Hong Kong Teahouse | standard | restaurant | 3 | 19.0 × 17.0 × 10.5 | hk-cinema, action, realistic, noir |
| `hobbit_hole` | 哈比山丘洞屋 | Hillside Smial | 哈比洞屋 / Halfling Hill House | standard | house | 1 | 17.0 × 17.9 × 2.8 | fantasy, cozy, ghibli, rpg-village |
| `house_teal_lantern` | 青瓦燈籠茶屋 | Teal Lantern Teahouse | 吉卜力海邊高腳屋 / Ghibli Seaside Stilt House | standard | house+shop | 2 | 18.1 × 17.7 × 12.0 | anime, ghibli, cozy, fantasy, realistic |
| `iceland_turf_house` | 冰島草頂屋 | Icelandic Turf House | 冰島草屋 / Icelandic Turf House | standard | house | 1 | 14.0 × 12.0 × 7.6 | fantasy, viking, survival, cozy |
| `irish_pub` | 奧馬利愛爾蘭酒吧 | O'Malley's Irish Pub | 愛爾蘭酒吧 / Irish Pub | standard | pub | 2 | 15.0 × 15.0 × 7.3 | europe, realistic, slice-of-life, crime |
| `jp_family_house` | 日式獨棟住宅 | Japanese Family House | 日式住宅 / Contemporary Japanese House | standard | house | 2 | 15.0 × 14.5 × 9.2 | anime, slice-of-life, japan, realistic |
| `karaoke_stardust` | 星光KTV | Stardust Karaoke Club | 霓虹KTV / Neon Karaoke Club | standard | karaoke club | 4 | 17.0 × 17.0 × 13.9 | cyberpunk, anime, nightlife, realistic, kdrama |
| `kyoto_machiya` | 京都町家 | Kyoto Machiya Townhouse | 日式町家 / Japanese Machiya | standard | shop + house | 2 | 13.0 × 17.0 × 8.8 | anime, realistic, slice-of-life, japan, cozy |
| `lisbon_tile_house` | 里斯本磁磚屋 | Lisbon Azulejo House | 葡萄牙磁磚屋 / Portuguese Azulejo | standard | townhouse | 3 | 13.0 × 16.0 × 12.8 | europe, summer, realistic, romance |
| `london_terrace` | 倫敦紅磚聯排 | London Victorian Terrace | 維多利亞聯排屋 / Victorian Terrace | standard | townhouse | 3 | 14.0 × 16.0 × 15.2 | realistic, detective, europe, steampunk, horror |
| `medieval_tavern` | 躍馬旅店 | The Prancing Stag Tavern | 中世紀酒館 / Medieval Fantasy Tavern | standard | tavern + inn | 2 | 26.0 × 16.3 × 13.9 | fantasy, medieval, rpg, realistic, anime |
| `mexico_casa` | 墨西哥彩色屋 | Casa Colorida | 墨西哥彩屋 / Mexican Colonial | standard | house | 2 | 14.0 × 14.5 × 9.5 | summer, cartoon, realistic, coco-like |
| `nola_iron_balcony` | 紐奧良鐵花陽台屋 | New Orleans Gallery House | 紐奧良法國區 / French Quarter Creole | standard | townhouse | 3 | 15.0 × 16.0 × 10.5 | noir, jazz-age, realistic, horror |
| `nordic_cabin` | 北歐黑木小屋 | Nordic Black Cabin | 北歐小屋 / Scandinavian Cabin | standard | cabin | 1 | 13.0 × 14.0 × 7.9 | realistic, survival, horror, cozy, winter |
| `pachinko_parlor` | 幸運小鋼珠 | Lucky 777 Pachinko | 小鋼珠店 / Japanese Pachinko Parlor | standard | game parlor | 2 | 19.0 × 17.0 × 7.9 | japan, cyberpunk, anime, crime |
| `potion_shop` | 月影藥水店 | Moonshade Potion Shop | 藥水店 / Fantasy Apothecary | standard | shop | 2 | 12.0 × 14.0 × 10.9 | fantasy, rpg, anime, cozy |
| `power_gym` | 能量健身工廠 | PowerHouse Gym | 工業風健身房 / Industrial Fitness Hall | standard | gym | 1 | 21.0 × 17.0 × 6.8 | realistic, sports, slice-of-life, anime |
| `printed_dome_home` | 3D列印圓頂屋 | 3D-Printed Dome Home | 3D列印建築 / 3D-Printed Concrete Dome | standard | house | 1 | 14.0 × 16.0 × 6.0 | sci-fi, solarpunk, post-apocalyptic, mars-colony |
| `russian_izba` | 俄羅斯木刻屋 | Russian Izba | 俄羅斯木屋 / Russian Log Izba | standard | house | 1 | 14.0 × 13.0 × 9.0 | fantasy, folk-tale, winter, realistic |
| `scottish_stone_house` | 蘇格蘭石屋 | Highland Stone House | 蘇格蘭石屋 / Scottish Stone House | standard | house | 2 | 15.0 × 13.6 × 11.3 | europe, realistic, mystery, fantasy |
| `sg_shophouse` | 南洋店屋 | Straits Shophouse | 南洋店屋 / Peranakan Shophouse | standard | shophouse | 3 | 12.0 × 19.5 × 11.9 | realistic, southeast-asia, slice-of-life, historical |
| `shanghai_shikumen` | 上海石庫門 | Shanghai Shikumen | 石庫門 / Shikumen Lane House | standard | townhouse | 3 | 13.0 × 18.0 × 13.7 | historical, noir, 1930s, realistic |
| `solar_row_house` | 太陽能社區屋 | Solar Row House | 太陽能住宅 / Net-Zero Row House | standard | house | 2 | 14.0 × 15.0 × 9.8 | solarpunk, modern, realistic |
| `spanish_plaza_house` | 西班牙廣場拱廊屋 | Spanish Plaza Arcade House | 西班牙拱廊屋 / Andalusian Arcade House | standard | house + shop | 2 | 17.0 × 15.0 × 9.0 | europe, summer, western, realistic |
| `steampunk_works` | 齒輪蒸汽工坊 | Cog & Steam Works | 蒸汽龐克工坊 / Steampunk Workshop | standard | workshop | 3 | 20.0 × 16.0 × 20.5 | steampunk, fantasy, victorian, anime, rpg |
| `stream_studio` | 直播工作室 | Live-Stream Studio | 直播工作室 / Creator Studio Loft | standard | studio | 3 | 14.0 × 15.0 × 10.5 | modern, slice-of-life, anime, cyberpunk |
| `supermarket` | 好鄰居超市 | Good Neighbor Supermarket | 郊區超市 / Suburban Supermarket | standard | supermarket | 1 | 29.0 × 31.0 × 5.9 | realistic, survival, zombie, slice-of-life, sims |
| `swedish_red_cottage` | 瑞典法倫紅屋 | Swedish Falu-Red Cottage | 瑞典紅木屋 / Swedish Stuga | standard | house | 2 | 15.0 × 13.6 × 10.1 | europe, cozy, realistic, anime, winter |
| `thai_stilt_house` | 泰式高腳屋 | Thai Stilt House | 泰式高腳屋 / Thai Teak Stilt House | standard | house | 1 | 15.0 × 16.5 × 9.5 | southeast-asia, realistic, adventure, cozy |
| `totem_lodge` | 圖騰長屋 | Totem Plank Lodge | 西北海岸長屋 / Pacific Northwest Plank House | standard | lodge | 1 | 22.0 × 14.0 × 5.5 | historical, adventure, survival, fantasy |
| `treehouse_oak` | 老橡樹樹屋 | Old Oak Treehouse | 童話樹屋 / Storybook Treehouse | standard | treehouse | 2 | 16.2 × 19.0 × 17.9 | cozy, ghibli, adventure, cartoon, fantasy |
| `tudor_inn` | 皇冠都鐸酒館 | The Crown Tudor Inn | 英式都鐸 / English Tudor | standard | pub + inn | 2 | 17.0 × 16.0 × 13.5 | medieval, fantasy, rpg-village, realistic, europe |
| `tw_townhouse` | 台式透天厝 | Taiwanese Townhouse | 台式透天厝 / Taiwanese Townhouse | standard | house | 4 | 10.0 × 19.0 × 15.9 | realistic, slice-of-life, taiwan, horror |
| `viking_longhouse` | 維京長屋 | Viking Longhouse | 維京長屋 / Norse Longhouse | standard | longhouse | 1 | 25.0 × 13.0 × 8.9 | viking, fantasy, survival, rpg, medieval |
| `warehouse_loft` | 紅磚倉庫Loft | Red-Brick Warehouse Lofts | 工業倉庫改建 / Industrial Warehouse Loft | standard | loft + workshop | 2 | 25.0 × 19.0 × 10.8 | realistic, industrial, crime, cyberpunk, post-apocalyptic |
| `wuxia_inn` | 龍門客棧 | Dragon Gate Inn | 武俠客棧 / Wuxia Desert Inn | standard | inn | 2 | 19.0 × 16.0 × 10.8 | wuxia, historical, fantasy, action |
| `american_colonial` | 美式殖民宅 | New England Colonial | 美式殖民 / American Colonial | upscale | house | 2 | 19.0 × 18.0 × 11.0 | realistic, horror, sitcom, americana |
| `bauhaus_house` | 包浩斯白宅 | Bauhaus White House | 包浩斯 / Bauhaus Modernism | upscale | house | 2 | 17.8 × 15.6 × 9.5 | realistic, modern, architectural, anime |
| `beijing_siheyuan_gate` | 北京四合院門樓 | Beijing Siheyuan Gatehouse | 北京四合院 / Beijing Siheyuan | upscale | house | 1 | 19.0 × 16.0 × 6.6 | historical, wuxia, realistic, kdrama |
| `cafe_container` | 貨櫃森林咖啡館 | Container Grove Café | 工業貨櫃現代 / Industrial Container Modern | upscale | café / commercial | 2 | 23.1 × 14.8 × 9.7 | realistic, modern, slice-of-life, anime |
| `canadian_lodge` | 加拿大木屋旅館 | Canadian Timber Lodge | 加拿大木屋 / Canadian Log Lodge | upscale | lodge | 2 | 21.0 × 16.0 × 11.4 | winter, cozy, survival, realistic |
| `dutch_canal_house` | 阿姆斯特丹運河屋 | Amsterdam Canal House | 荷蘭運河屋 / Dutch Canal House | upscale | townhouse | 4 | 10.0 × 17.0 × 17.6 | europe, realistic, romance, anime |
| `eco_apartments` | 綠廊生態公寓 | Green Terrace Eco Apartments | 綠建築生態宅 / Biophilic Eco Housing | upscale | apartment | 5 | 19.0 × 17.0 × 19.4 | solarpunk, realistic, modern, anime, utopia |
| `esports_arena` | 電競競技館 | Esports Arena | 電競館 / Esports Venue | upscale | arena | 2 | 23.0 × 19.0 × 9.3 | cyberpunk, modern, anime, sports |
| `glass_cube_office` | 黑玻璃創意辦公 | Obsidian Cube Offices | 當代玻璃辦公 / Contemporary Glass Office | upscale | office | 4 | 21.0 × 23.0 × 17.7 | modern, corporate, cyberpunk, realistic, thriller |
| `green_roof_house` | 綠屋頂住宅 | Living-Roof House | 綠屋頂 / Eco Green-Roof House | upscale | house | 2 | 17.0 × 15.0 × 8.4 | solarpunk, modern, cozy, realistic |
| `greenhouse_cafe` | 玻璃溫室咖啡 | Glasshouse Garden Café | 玻璃溫室 / Victorian Glasshouse | upscale | café | 1 | 17.0 × 15.0 × 6.1 | cozy, ghibli, romance, solarpunk, realistic |
| `hanok_cafe` | 韓屋咖啡廳 | Hanok Café | 韓屋咖啡 / Korean Hanok Café | upscale | café | 1 | 17.0 × 14.5 × 6.9 | kdrama, cozy, realistic, anime |
| `house_eastasian_tile` | 青瓦庭院宅 | Slate-Roof Garden House | 東亞傳統瓦屋 / East Asian Traditional | upscale | house | 2 | 18.5 × 17.3 × 9.2 | realistic, anime, wuxia-modern, cozy, rpg-village |
| `jp_ryokan` | 月見溫泉旅館 | Tsukimi Hot-Spring Ryokan | 溫泉旅館 / Japanese Ryokan | upscale | ryokan | 2 | 21.0 × 17.0 × 10.1 | anime, japan, cozy, romance, realistic |
| `jp_tea_room` | 侘寂茶室 | Wabi Tea Room | 日式茶室 / Japanese Tea House | upscale | tea house | 1 | 12.0 × 15.0 × 5.7 | japan, zen, anime, realistic |
| `korean_hanok` | 韓式韓屋 | Korean Hanok | 韓屋 / Korean Hanok | upscale | house | 1 | 20.4 × 16.5 × 7.4 | historical, kdrama, realistic, anime |
| `med_villa` | 地中海白屋 | Mediterranean White House | 地中海風 / Mediterranean | upscale | house | 2 | 17.0 × 15.0 × 9.0 | realistic, summer, romance, anime |
| `midcentury_house` | 中世紀現代宅 | Palm Springs Mid-Century House | 中世紀現代 / Mid-Century Modern | upscale | house | 1 | 30.0 × 15.0 × 4.7 | retro, realistic, mad-men, modern, gta-like |
| `minimal_white_box` | 極簡白盒屋 | Minimal White Box | 極簡主義 / Minimalist Modern | upscale | house | 2 | 16.8 × 15.4 × 9.5 | modern, realistic, architectural, anime |
| `minnan_sanheyuan` | 閩南三合院 | Minnan Courtyard House | 閩南三合院 / Minnan Sanheyuan | upscale | house | 1 | 23.0 × 19.5 × 6.2 | historical, taiwan, wuxia, rpg-village, realistic |
| `moroccan_riad` | 摩洛哥庭園宅 | Moroccan Riad House | 摩洛哥風 / Moroccan Riad | upscale | guesthouse | 2 | 17.0 × 17.0 × 9.5 | fantasy, desert, realistic, adventure |
| `nyc_brownstone` | 紐約褐石排屋 | Brooklyn Brownstone | 紐約褐石屋 / New York Brownstone | upscale | townhouse | 4 | 13.0 × 19.5 × 16.2 | realistic, noir, sitcom, crime, urban |
| `paris_haussmann` | 巴黎奧斯曼公寓 | Parisian Haussmann Apartment | 巴黎奧斯曼式 / Haussmann Parisian | upscale | apartment | 4 | 19.0 × 17.5 × 17.6 | realistic, romance, anime, noir, europe |
| `pod_apartments` | 未來膠囊陽台公寓 | Pod Balcony Apartments | 未來公寓 / Futurist Pod Housing | upscale | apartment | 6 | 17.0 × 16.0 × 21.3 | sci-fi, modern, solarpunk, anime |
| `pod_solar` | 日光艙屋 | Solar Pod Home | 科幻離網艙屋 / Sci-Fi Off-Grid Module | upscale | house | 2 | 18.0 × 16.0 × 11.4 | sci-fi, solarpunk, post-apocalyptic, anime, realistic |
| `rajasthan_haveli` | 拉賈斯坦哈維利 | Rajasthani Haveli | 印度哈維利 / Indian Haveli | upscale | mansion | 3 | 17.0 × 17.0 × 12.9 | historical, fantasy, adventure, realistic |
| `santorini_house` | 聖托里尼藍頂屋 | Santorini Blue-Dome House | 希臘聖托里尼 / Cycladic Greek | upscale | house | 2 | 14.0 × 14.0 × 10.7 | summer, romance, realistic, anime |
| `sf_painted_lady` | 舊金山彩繪淑女屋 | San Francisco Painted Lady | 維多利亞彩屋 / Victorian Painted Lady | upscale | townhouse | 3 | 10.6 × 17.0 × 15.0 | realistic, sitcom, romance, americana |
| `spanish_hacienda` | 西班牙莊園 | Spanish Hacienda | 西班牙殖民風 / Spanish Colonial | upscale | house | 1 | 21.0 × 18.5 × 5.6 | western, realistic, telenovela, rpg-village |
| `startup_hq` | 新創科技總部 | Startup HQ | 科技新創 / Tech Startup Office | upscale | office | 3 | 21.0 × 19.0 × 14.1 | modern, corporate, slice-of-life, cyberpunk |
| `swiss_chalet` | 阿爾卑斯木屋 | Alpine Swiss Chalet | 瑞士山屋 / Swiss Alpine Chalet | upscale | house | 2 | 16.0 × 15.0 × 10.0 | realistic, cozy, winter, anime, europe |
| `tuscan_farmhouse` | 托斯卡尼農舍 | Tuscan Farmhouse | 義大利托斯卡尼 / Tuscan Casale | upscale | farmhouse | 2 | 19.9 × 19.4 × 9.6 | europe, romance, farming-sim, realistic |
| `arcology_block` | 生態巨構塊 | Arcology Block | 生態巨構 / Arcology Megablock | luxury | megablock | 8 | 21.0 × 21.0 × 27.8 | solarpunk, sci-fi, utopia, cyberpunk |
| `bali_villa` | 峇里島茅頂別墅 | Bali Thatch Villa | 峇里島villa / Balinese Villa | luxury | villa | 1 | 21.9 × 17.1 × 8.9 | resort, realistic, romance, tropical |
| `bank_classical` | 海港儲蓄銀行 | Harbor Savings Bank | 新古典銀行 / Neoclassical Bank | luxury | bank | 2 | 19.0 × 22.0 × 10.5 | realistic, heist, noir, western, civic |
| `cantilever_house` | 懸挑清水宅 | Cantilever Concrete House | 懸挑住宅 / Brutalist Cantilever | luxury | house | 2 | 26.0 × 15.0 × 7.0 | modern, thriller, architectural, realistic |
| `concrete_minimal` | 清水模住宅 | Fair-faced Concrete House | 日式清水模 / Japanese Minimalist Concrete | luxury | house | 2 | 16.4 × 17.8 × 7.0 | realistic, modern, thriller, zen, architectural |
| `desert_palace` | 沙漠蘇丹宮殿 | Desert Sultan's Palace | 中東宮殿 / Arabian Palace | luxury | palace | 2 | 28.0 × 19.0 × 16.2 | fantasy, desert, aladdin, rpg, adventure |
| `gothic_manor` | 血月哥德莊園 | Bloodmoon Gothic Manor | 哥德莊園 / Gothic Revival Manor | luxury | mansion | 3 | 20.1 × 18.5 × 15.7 | horror, gothic, vampire, mystery, otome |
| `hotel_artdeco` | 裝飾藝術大飯店 | Grand Deco Hotel | 裝飾藝術風 / Art Deco Hotel | luxury | hotel | 6 | 21.0 × 21.0 × 28.2 | noir, 1920s, realistic, mystery, bioshock-like |
| `loire_chateau` | 羅亞爾小城堡 | Loire Petit Château | 法式城堡 / French Château | luxury | mansion | 3 | 26.0 × 17.0 × 16.9 | europe, romance, fantasy, mystery, otome |
| `lucky7_casino` | 幸運7賭場 | Lucky 7 Casino | 拉斯維加斯賭場 / Las Vegas Casino | luxury | casino | 2 | 23.0 × 19.0 × 8.5 | crime, heist, gta-like, neon, retro |
| `malibu_beach_house` | 馬里布海灘屋 | Malibu Beach House | 加州海灘屋 / California Beach House | luxury | beach house | 2 | 17.0 × 15.0 × 9.0 | summer, realistic, gta-like, modern |
| `office_glass_tower` | 海港金融中心 | Harbor Finance Tower | 現代玻璃帷幕大樓 / Modern Glass High-rise | luxury | office high-rise | 10 | 26.0 × 25.5 × 41.9 | realistic, modern, corporate, thriller, cyberpunk |
| `villa_luxury_modern` | 白崖現代豪宅 | White Cliff Modern Villa | 奢華現代主義別墅 / Luxury Modernist Villa | luxury | villa | 2 | 31.8 × 25.3 × 7.8 | realistic, modern, thriller, life-sim, anime |
| `villa_neon_circuit` | 霓光電路別墅 | Neon Circuit Villa | 近未來科技別墅 / Near-Future Tech Villa | luxury | villa | 2 | 24.0 × 23.0 × 7.3 | cyberpunk, sci-fi, near-future, realistic, anime |
| `adventurers_guild` | 冒險者公會 | Adventurers' Guild Hall | 冒險者公會 / Fantasy Guild Hall | landmark | guild | 3 | 21.0 × 17.0 × 17.4 | fantasy, rpg, anime, isekai, dnd |
| `alchemy_tower` | 翠焰煉金塔 | Emerald Alchemy Tower | 煉金塔 / Alchemist Tower | landmark | tower | 4 | 14.0 × 16.0 × 19.3 | fantasy, steampunk, rpg, magic-school |
| `castle_keep` | 獅鷲城堡塔 | Griffin Castle Keep | 中世紀城堡 / Medieval Castle Keep | landmark | castle | 4 | 22.0 × 17.0 × 21.3 | fantasy, medieval, rpg, strategy, realistic |
| `egyptian_temple` | 尼羅神殿 | Temple of the Nile | 埃及神殿 / Ancient Egyptian Temple | landmark | temple | 1 | 22.0 × 23.0 × 9.8 | historical, fantasy, adventure, mummy |
| `harbor_aquarium` | 海港水族館 | Harbor Aquarium | 水族館 / Public Aquarium | landmark | aquarium | 1 | 23.0 × 19.0 × 9.2 | family, modern, slice-of-life, anime |
| `hyperloop_station` | 超迴路列車站 | Hyperloop Station | 超迴路車站 / Hyperloop Terminal | landmark | station | 1 | 34.6 × 18.0 × 6.2 | sci-fi, modern, cyberpunk |
| `japanese_castle` | 白鷺天守閣 | White Heron Castle Keep | 日式天守閣 / Japanese Castle Tenshu | landmark | castle | 3 | 20.0 × 20.0 × 18.0 | japan, samurai, anime, historical, strategy |
| `lantern_festival_tower` | 元宵燈籠塔 | Lantern Festival Tower | 燈籠塔 / Chinese Lantern Tower | landmark | tower | 3 | 14.0 × 16.0 × 14.7 | wuxia, festival, anime, fantasy |
| `lighthouse_cape` | 海角燈塔 | Cape Lighthouse | 海事燈塔 / Maritime Lighthouse | landmark | lighthouse | 5 | 18.4 × 20.0 × 21.1 | realistic, horror, mystery, adventure, ghibli |
| `mage_academy` | 星輝魔法學院 | Astral Mage Academy | 魔法學院 / Fantasy Magic Academy | landmark | academy | 3 | 28.0 × 19.0 × 18.5 | fantasy, anime, magic-school, rpg |
| `maya_pyramid` | 羽蛇金字塔 | Feathered Serpent Pyramid | 馬雅金字塔 / Mesoamerican Step Pyramid | landmark | pyramid | 2 | 30.0 × 31.5 × 14.2 | adventure, historical, fantasy, tomb-raider |
| `observatory_dome` | 星穹天文台 | Starvault Observatory | 圓頂天文台 / Domed Observatory | landmark | observatory | 2 | 14.0 × 16.0 × 12.8 | sci-fi, realistic, mystery, anime, academy |
| `science_museum` | 海港科學館 | Harbor Science Museum | 科學館 / Science Museum | landmark | museum | 2 | 25.0 × 19.0 × 10.4 | family, sci-fi, mystery, realistic |
| `shinto_shrine` | 朱鳥神社 | Vermilion Bird Shrine | 日式神社 / Japanese Shinto Shrine | landmark | shrine | 1 | 20.3 × 20.0 × 6.8 | anime, japan, fantasy, horror, realistic |
| `space_colony_dome` | 火星殖民穹頂 | Mars Colony Dome | 太空殖民地 / Sci-Fi Habitat Dome | landmark | habitat | 1 | 20.0 × 22.0 × 8.7 | sci-fi, survival, mars, solarpunk |
| `stone_chapel` | 海角石砌教堂 | Cape Stone Chapel | 哥德復興教堂 / Gothic Revival Chapel | landmark | chapel | 1 | 21.2 × 22.9 × 19.7 | realistic, horror, romance, fantasy, wedding |
| `taoist_temple` | 紫霄道觀 | Purple Cloud Taoist Temple | 道觀 / Taoist Temple | landmark | temple | 1 | 17.0 × 20.0 × 9.9 | wuxia, fantasy, xianxia, realistic |
| `temple_pagoda` | 天界樓閣 | Heaven Gate Pavilion | 中式樓閣廟宇 / Chinese Pagoda Temple (neo-oriental) | landmark | temple / landmark | 3 | 24.0 × 30.0 × 20.5 | wuxia, fantasy, cyberpunk-oriental, anime, realistic |
| `tw_folk_temple` | 福德宮 | Fude Folk Temple | 台灣廟宇 / Taiwanese Folk Temple | landmark | temple | 1 | 17.0 × 21.0 × 9.6 | taiwan, wuxia, fantasy, horror, realistic |
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
* **Placed on island at:** (124.5, -16.8, 0.15), rotZ 180° · **Files:** `export/glb/american_diner.glb`, Blender collection `BLD_american_diner`

### 老王汽車修理廠 Wang's Auto Repair — `auto_repair`

![day](renders/auto_repair_front_day.png) ![night](renders/auto_repair_front.png) ![plan](renders/auto_repair_cut_day.png)

* **Style:** 汽車修理廠 / Auto Repair Garage · **Tier:** budget · **Type:** garage · **Floors:** 1
* **Fits game styles:** realistic, gta-like, slice-of-life, crime
* **Description:** Single-storey steel garage: two service bays with roller doors and cars on stands, workbenches, tyre stacks.
* **Size:** 22.0 × 15.0 m footprint, 5.1 m tall · 52 objects · ~67400 tris · 2 lights · 12 furniture pieces
* **Exterior doors:** F1_S0(S side), F1_S1(S side), F1_S2(S side) · interior doors: 0
* **Spawn points (local m):** front (6.2, -7.5, 0)
* **Interactions:** open, use, work
* **Placed on island at:** (66.0, -133.3, 0.15), rotZ 180° · **Files:** `export/glb/auto_repair.glb`, Blender collection `BLD_auto_repair`

### 背包客棧 Backpackers' Hostel — `backpacker_hostel`

![day](renders/backpacker_hostel_front_day.png) ![night](renders/backpacker_hostel_front.png) ![plan](renders/backpacker_hostel_cut_day.png)

* **Style:** 背包客棧 / Asian Backpacker Hostel · **Tier:** budget · **Type:** hostel · **Floors:** 5
* **Fits game styles:** slice-of-life, anime, realistic, adventure
* **Description:** 5-storey hostel: lobby + bar, dorm floors with bunks, private rooms, roof terrace.
* **Size:** 15.0 × 16.0 m footprint, 19.1 m tall · 340 objects · ~111660 tris · 17 lights · 86 furniture pieces
* **Exterior doors:** F1_S3(S side), F1_E1(E side), PH_W0(W side) · interior doors: 11
* **Spawn points (local m):** front (-2.4, -8.0, 0)
* **Interactions:** open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (174.5, -77.8, 0.15), rotZ 180° · **Files:** `export/glb/backpacker_hostel.glb`, Blender collection `BLD_backpacker_hostel`

### 池上便當店 Railway Bento Shop — `bento_shop`

![day](renders/bento_shop_front_day.png) ![night](renders/bento_shop_front.png) ![plan](renders/bento_shop_cut_day.png)

* **Style:** 便當店 / Taiwanese Bento Shop · **Tier:** budget · **Type:** restaurant · **Floors:** 2
* **Fits game styles:** taiwan, slice-of-life, anime
* **Description:** 2-storey mosaic shop: bento counter with dining tables, kitchen behind, owner's flat upstairs.
* **Size:** 13.0 × 15.0 m footprint, 7.3 m tall · 130 objects · ~72488 tris · 6 lights · 36 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side) · interior doors: 4
* **Spawn points (local m):** front (-1.8, -7.5, 0)
* **Interactions:** cook, open, sit, sleep, use, work
* **Placed on island at:** (67.5, -77.3, 0.15), rotZ 180° · **Files:** `export/glb/bento_shop.glb`, Blender collection `BLD_bento_shop`

### 鐵匠鋪 Ironhand Blacksmith — `blacksmith_forge`

![day](renders/blacksmith_forge_front_day.png) ![night](renders/blacksmith_forge_front.png) ![plan](renders/blacksmith_forge_cut_day.png)

* **Style:** 鐵匠鋪 / Medieval Blacksmith · **Tier:** budget · **Type:** forge · **Floors:** 1
* **Fits game styles:** medieval, fantasy, rpg, survival
* **Description:** Stone forge with half-timber gable: furnace, anvil, workbench and an open front for customers.
* **Size:** 15.0 × 13.0 m footprint, 7.5 m tall · 34 objects · ~61956 tris · 2 lights · 4 furniture pieces
* **Exterior doors:** F1_S1(S side) · interior doors: 0
* **Spawn points (local m):** front (3.4, -6.5, 0)
* **Interactions:** open, use, work
* **Placed on island at:** (-101.5, -155.7, 0.15), rotZ 0° · **Files:** `export/glb/blacksmith_forge.glb`, Blender collection `BLD_blacksmith_forge`

### 珍珠奶茶公寓 Boba Tea Walk-up — `bubble_tea_flats`

![day](renders/bubble_tea_flats_front_day.png) ![night](renders/bubble_tea_flats_front.png) ![plan](renders/bubble_tea_flats_cut_day.png)

* **Style:** 台式店面 / Taiwanese Shop Walk-up · **Tier:** budget · **Type:** shop + flats · **Floors:** 3
* **Fits game styles:** taiwan, slice-of-life, anime
* **Description:** 3-storey white-tiled walk-up with a bubble-tea counter shop and flats above.
* **Size:** 12.0 × 15.0 m footprint, 10.5 m tall · 175 objects · ~87896 tris · 9 lights · 43 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side) · interior doors: 6
* **Spawn points (local m):** front (-1.4, -7.5, 0)
* **Interactions:** open, shop, sit, sleep, use, work
* **Placed on island at:** (55.0, -77.3, 0.15), rotZ 180° · **Files:** `export/glb/bubble_tea_flats.glb`, Blender collection `BLD_bubble_tea_flats`

### 蜂巢膠囊旅館 Hive Capsule Hotel — `capsule_tower`

![day](renders/capsule_tower_front_day.png) ![night](renders/capsule_tower_front.png) ![plan](renders/capsule_tower_cut_day.png)

* **Style:** 膠囊旅館 / Capsule Hotel Tower · **Tier:** budget · **Type:** capsule hotel · **Floors:** 7
* **Fits game styles:** cyberpunk, anime, sci-fi, realistic, japan
* **Description:** 7-storey slim capsule hotel: lobby, floors of stacked bunk capsules + lounges, roof terrace, neon blade sign.
* **Size:** 14.0 × 16.0 m footprint, 23.7 m tall · 449 objects · ~123456 tris · 22 lights · 89 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E2(E side), PH_W0(W side) · interior doors: 14
* **Spawn points (local m):** front (-2.4, -8.0, 0)
* **Interactions:** open, shop, sit, sleep, use, wash
* **Placed on island at:** (-38.0, -46.2, 0.15), rotZ 0° · **Files:** `export/glb/capsule_tower.glb`, Blender collection `BLD_capsule_tower`

### 三色貨櫃公寓 Tricolour Container Flats — `container_flats`

![day](renders/container_flats_front_day.png) ![night](renders/container_flats_front.png) ![plan](renders/container_flats_cut_day.png)

* **Style:** 貨櫃公寓 / Shipping-Container Apartments · **Tier:** budget · **Type:** apartment · **Floors:** 3
* **Fits game styles:** industrial, post-apocalyptic, modern, realistic
* **Description:** 3-storey stack clad in blue / yellow / grey corrugated container steel, plywood interiors, roof terrace.
* **Size:** 17.0 × 15.0 m footprint, 12.7 m tall · 310 objects · ~105488 tris · 16 lights · 83 furniture pieces
* **Exterior doors:** F1_S3(S side), F1_E1(E side), F2_S1(S side), F2_S3(S side), PH_W0(W side) · interior doors: 12
* **Spawn points (local m):** front (-1.13, -7.5, 0)
* **Interactions:** cook, open, sit, sleep, use, wash, work
* **Placed on island at:** (-204.5, -133.3, 0.15), rotZ 180° · **Files:** `export/glb/container_flats.glb`, Blender collection `BLD_container_flats`

### 義體改造診所 Cyberware Clinic — `cyberware_clinic`

![day](renders/cyberware_clinic_front_day.png) ![night](renders/cyberware_clinic_front.png) ![plan](renders/cyberware_clinic_cut_day.png)

* **Style:** 賽博義體診所 / Cyberpunk Ripperdoc · **Tier:** budget · **Type:** clinic · **Floors:** 3
* **Fits game styles:** cyberpunk, sci-fi, horror, neo-noir
* **Description:** 3-storey grimy teal clinic: neon-lit surgery bay with exam beds, server room, cramped quarters.
* **Size:** 13.0 × 15.0 m footprint, 10.5 m tall · 172 objects · ~100788 tris · 9 lights · 35 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_E1(E side) · interior doors: 6
* **Spawn points (local m):** front (-2.0, -7.5, 0)
* **Interactions:** open, sit, sleep, use, work
* **Placed on island at:** (-20.5, -133.3, 0.15), rotZ 180° · **Files:** `export/glb/cyberware_clinic.glb`, Blender collection `BLD_cyberware_clinic`

### 光華電器行 Guanghua Electronics — `electronics_shop`

![day](renders/electronics_shop_front_day.png) ![night](renders/electronics_shop_front.png) ![plan](renders/electronics_shop_cut_day.png)

* **Style:** 電器行 / Asian Electronics Store · **Tier:** budget · **Type:** shop · **Floors:** 3
* **Fits game styles:** cyberpunk, slice-of-life, anime, realistic
* **Description:** 3-storey pink-tile electronics store: TV walls and gadget shelves, neon sign, storeroom and flat above.
* **Size:** 14.0 × 16.0 m footprint, 10.5 m tall · 187 objects · ~117208 tris · 9 lights · 48 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side) · interior doors: 6
* **Spawn points (local m):** front (-2.2, -8.0, 0)
* **Interactions:** open, shop, sit, sleep, use, work
* **Placed on island at:** (96.0, -77.8, 0.15), rotZ 180° · **Files:** `export/glb/electronics_shop.glb`, Blender collection `BLD_electronics_shop`

### 里約彩色堆疊屋 Rio Hillside Stack — `favela_stack`

![day](renders/favela_stack_front_day.png) ![night](renders/favela_stack_front.png) ![plan](renders/favela_stack_cut_day.png)

* **Style:** 巴西彩色堆疊屋 / Brazilian Favela Block · **Tier:** budget · **Type:** apartment · **Floors:** 4
* **Fits game styles:** realistic, action, urban-survival, gta-like
* **Description:** 4-storey self-built stack: every floor a different colour, rebar on the roof, AC units, tangled cables.
* **Size:** 13.0 × 15.0 m footprint, 18.5 m tall · 312 objects · ~98200 tris · 13 lights · 65 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_E1(E side), PH_W0(W side) · interior doors: 8
* **Spawn points (local m):** front (-2.0, -7.5, 0)
* **Interactions:** cook, open, sit, sleep, use, work
* **Placed on island at:** (89.5, -102.7, 0.15), rotZ 0° · **Files:** `export/glb/favela_stack.glb`, Blender collection `BLD_favela_stack`

### 海港加油站 Harbor Gas & Go — `gas_station`

![day](renders/gas_station_front_day.png) ![night](renders/gas_station_front.png) ![plan](renders/gas_station_cut_day.png)

* **Style:** 公路加油站 / Roadside Gas Station · **Tier:** budget · **Type:** gas station · **Floors:** 1
* **Fits game styles:** realistic, road-movie, survival, horror, open-world
* **Description:** Convenience kiosk with shelves and counter, big illuminated canopy over four pumps, price pylon.
* **Size:** 24.0 × 25.0 m footprint, 6.5 m tall · 60 objects · ~107896 tris · 3 lights · 19 furniture pieces
* **Exterior doors:** F1_S2(S side) · interior doors: 0
* **Spawn points (local m):** front (-2.0, -7.0, 0)
* **Interactions:** open, shop, use
* **Placed on island at:** (147.0, -25.8, 0.15), rotZ 180° · **Files:** `export/glb/gas_station.glb`, Blender collection `BLD_gas_station`

### 荒山鬼屋 Hollow Hill Haunted House — `haunted_house`

![day](renders/haunted_house_front_day.png) ![night](renders/haunted_house_front.png) ![plan](renders/haunted_house_cut_day.png)

* **Style:** 鬼屋 / Haunted Victorian · **Tier:** budget · **Type:** house · **Floors:** 2
* **Fits game styles:** horror, halloween, mystery, zombie
* **Description:** Decaying 2-storey timber house: boarded-up windows, rusted tin gable, creaky interior, cold blue light upstairs.
* **Size:** 16.7 × 14.9 m footprint, 13.5 m tall · 167 objects · ~67586 tris · 10 lights · 45 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_E1(E side) · interior doors: 7
* **Spawn points (local m):** front (-1.13, -7.0, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (86.5, -155.2, 0.15), rotZ 0° · **Files:** `export/glb/haunted_house.glb`, Blender collection `BLD_haunted_house`

### 旺角唐樓 Hong Kong Tong Lau — `hk_tonglau`

![day](renders/hk_tonglau_front_day.png) ![night](renders/hk_tonglau_front.png) ![plan](renders/hk_tonglau_cut_day.png)

* **Style:** 香港唐樓 / Hong Kong Tenement · **Tier:** budget · **Type:** tenement · **Floors:** 6
* **Fits game styles:** cyberpunk, noir, realistic, action, hk-cinema
* **Description:** 6-storey mosaic tenement: cha chaan teng diner, caged balconies, AC units, neon blade sign, laundry, rooftop.
* **Size:** 13.0 × 17.0 m footprint, 24.1 m tall · 460 objects · ~126116 tris · 19 lights · 124 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_E2(E side), F2_S1(S side), F4_S1(S side), F6_S1(S side), PH_W0(W side) · interior doors: 12
* **Spawn points (local m):** front (-2.0, -8.5, 0)
* **Interactions:** cook, open, sit, sleep, use, work
* **Placed on island at:** (155.5, 16.3, 0.15), rotZ 0° · **Files:** `export/glb/hk_tonglau.glb`, Blender collection `BLD_hk_tonglau`

### 居酒屋 酔鯨 Izakaya Drunken Whale — `izakaya_suikei`

![day](renders/izakaya_suikei_front_day.png) ![night](renders/izakaya_suikei_front.png) ![plan](renders/izakaya_suikei_cut_day.png)

* **Style:** 日式居酒屋 / Japanese Izakaya · **Tier:** budget · **Type:** bar + flat · **Floors:** 2
* **Fits game styles:** anime, slice-of-life, japan, realistic, noir
* **Description:** Timber-fronted izakaya: counter bar with stools, tables, kitchen, red lanterns and noren; small flat above; slate gable.
* **Size:** 14.0 × 15.0 m footprint, 9.4 m tall · 180 objects · ~74164 tris · 12 lights · 43 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side) · interior doors: 4
* **Spawn points (local m):** front (-1.0, -7.5, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, work
* **Placed on island at:** (-232.0, -46.7, 0.15), rotZ 0° · **Files:** `export/glb/izakaya_suikei.glb`, Blender collection `BLD_izakaya_suikei`

### 首爾便利店考試院 Seoul Mart & Gosiwon — `kr_mart_gosiwon`

![day](renders/kr_mart_gosiwon_front_day.png) ![night](renders/kr_mart_gosiwon_front.png) ![plan](renders/kr_mart_gosiwon_cut_day.png)

* **Style:** 韓式住商 / Korean Mixed-use Walk-up · **Tier:** budget · **Type:** shop + dorm · **Floors:** 4
* **Fits game styles:** kdrama, slice-of-life, realistic, horror
* **Description:** 4-storey cream brick: 24h convenience store, tiny gosiwon study rooms above, rooftop.
* **Size:** 14.0 × 16.0 m footprint, 15.9 m tall · 285 objects · ~120440 tris · 16 lights · 72 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side), PH_W0(W side) · interior doors: 11
* **Spawn points (local m):** front (-2.0, -8.0, 0)
* **Interactions:** open, shop, sit, sleep, use, work
* **Placed on island at:** (-156.0, -77.8, 0.15), rotZ 180° · **Files:** `export/glb/kr_mart_gosiwon.glb`, Blender collection `BLD_kr_mart_gosiwon`

### 泡泡自助洗衣 Bubbles Laundromat — `laundromat_flats`

![day](renders/laundromat_flats_front_day.png) ![night](renders/laundromat_flats_front.png) ![plan](renders/laundromat_flats_cut_day.png)

* **Style:** 自助洗衣公寓 / Urban Laundromat Walk-up · **Tier:** budget · **Type:** laundromat + flats · **Floors:** 3
* **Fits game styles:** slice-of-life, anime, realistic, noir
* **Description:** Narrow 3-storey mosaic block: G/F coin laundry with washer wall and bench, two small flats above.
* **Size:** 13.0 × 15.0 m footprint, 12.7 m tall · 207 objects · ~102916 tris · 10 lights · 52 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_E1(E side), PH_W0(W side) · interior doors: 6
* **Spawn points (local m):** front (-2.4, -7.5, 0)
* **Interactions:** open, shop, sit, sleep, use, work
* **Placed on island at:** (231.5, -15.3, 0.15), rotZ 180° · **Files:** `export/glb/laundromat_flats.glb`, Blender collection `BLD_laundromat_flats`

### 漫畫網咖 Manga & Net Café — `manga_netcafe`

![day](renders/manga_netcafe_front_day.png) ![night](renders/manga_netcafe_front.png) ![plan](renders/manga_netcafe_cut_day.png)

* **Style:** 漫畫網咖 / Japanese Manga Café · **Tier:** budget · **Type:** net café · **Floors:** 3
* **Fits game styles:** anime, japan, cyberpunk, slice-of-life
* **Description:** 3-storey manga café: G/F manga library, PC booth floors above, neon sign.
* **Size:** 14.0 × 16.0 m footprint, 10.5 m tall · 197 objects · ~104816 tris · 9 lights · 57 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side) · interior doors: 6
* **Spawn points (local m):** front (-2.0, -8.0, 0)
* **Interactions:** open, sit, use, wash, work
* **Placed on island at:** (-170.0, -77.8, 0.15), rotZ 180° · **Files:** `export/glb/manga_netcafe.glb`, Blender collection `BLD_manga_netcafe`

### 草原蒙古包 Steppe Ger (Yurt) — `mongol_yurt`

![day](renders/mongol_yurt_front_day.png) ![night](renders/mongol_yurt_front.png) ![plan](renders/mongol_yurt_cut_day.png)

* **Style:** 蒙古包 / Mongolian Ger · **Tier:** budget · **Type:** yurt · **Floors:** 1
* **Fits game styles:** nomad, survival, historical, cozy
* **Description:** 16-sided felt ger with a low cone roof: stove, beds and rugs around a central hearth.
* **Size:** 14.0 × 16.0 m footprint, 5.4 m tall · 54 objects · ~46844 tris · 1 lights · 4 furniture pieces
* **Exterior doors:** F1_11_0(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -6.1, 0)
* **Interactions:** open, sleep, use
* **Placed on island at:** (-126.0, -186.3, 0.15), rotZ 180° · **Files:** `export/glb/mongol_yurt.glb`, Blender collection `BLD_mongol_yurt`

### 夜市攤商街屋 Night Market Row — `night_market_row`

![day](renders/night_market_row_front_day.png) ![night](renders/night_market_row_front.png) ![plan](renders/night_market_row_cut_day.png)

* **Style:** 台灣夜市 / Taiwanese Night Market · **Tier:** budget · **Type:** market · **Floors:** 1
* **Fits game styles:** taiwan, slice-of-life, anime, realistic
* **Description:** Tin-roofed open-front food hall with tables, five neon food stalls on the street, lanterns.
* **Size:** 21.0 × 16.5 m footprint, 4.8 m tall · 139 objects · ~85936 tris · 6 lights · 95 furniture pieces
* **Exterior doors:** - · interior doors: 0
* **Spawn points (local m):** front (0.0, -7.0, 0)
* **Interactions:** shop, sit, use
* **Placed on island at:** (37.5, -79.3, 0.15), rotZ 180° · **Files:** `export/glb/night_market_row.glb`, Blender collection `BLD_night_market_row`

### 黑帆海盜酒館 Black Sail Pirate Tavern — `pirate_tavern`

![day](renders/pirate_tavern_front_day.png) ![night](renders/pirate_tavern_front.png) ![plan](renders/pirate_tavern_cut_day.png)

* **Style:** 海盜酒館 / Pirate Port Tavern · **Tier:** budget · **Type:** tavern · **Floors:** 2
* **Fits game styles:** pirate, fantasy, adventure, rpg
* **Description:** 2-storey tarred-timber tavern: rum bar and tables, rooms upstairs, ship's-wheel sign, rope festoons, barrels.
* **Size:** 17.0 × 15.0 m footprint, 9.6 m tall · 187 objects · ~84644 tris · 10 lights · 53 furniture pieces
* **Exterior doors:** F1_S3(S side), F1_E1(E side) · interior doors: 6
* **Spawn points (local m):** front (2.0, -7.5, 0)
* **Interactions:** open, shop, sit, sleep, use, work
* **Placed on island at:** (117.5, -154.7, 0.15), rotZ 0° · **Files:** `export/glb/pirate_tavern.glb`, Blender collection `BLD_pirate_tavern`

### 美式紅穀倉 Red Prairie Barn — `red_barn`

![day](renders/red_barn_front_day.png) ![night](renders/red_barn_front.png) ![plan](renders/red_barn_cut_day.png)

* **Style:** 美式穀倉 / American Barn · **Tier:** budget · **Type:** barn · **Floors:** 2
* **Fits game styles:** farming-sim, western, horror, americana
* **Description:** Big red gambrel barn: tractor/garage bay and workshop with roller door, hay loft above, steel grain silo.
* **Size:** 24.0 × 17.0 m footprint, 10.4 m tall · 152 objects · ~77952 tris · 8 lights · 47 furniture pieces
* **Exterior doors:** F1_S0(S side), F1_S1(S side), F1_E1(E side) · interior doors: 6
* **Spawn points (local m):** front (3.0, -8.5, 0)
* **Interactions:** open, shop, sit, use, wash, work
* **Placed on island at:** (-43.0, -101.7, 0.15), rotZ 0° · **Files:** `export/glb/red_barn.glb`, Blender collection `BLD_red_barn`

### 海景汽車旅館 Seaview Motor Inn — `seaview_motel`

![day](renders/seaview_motel_front_day.png) ![night](renders/seaview_motel_front.png) ![plan](renders/seaview_motel_cut_day.png)

* **Style:** 公路汽車旅館 / American Roadside Motel · **Tier:** budget · **Type:** motel · **Floors:** 2
* **Fits game styles:** road-movie, horror, noir, realistic, retro
* **Description:** Two-storey motel strip: office/lobby, rows of guest rooms each with its own balcony walkway, neon MOTEL sign, parking.
* **Size:** 29.0 × 20.1 m footprint, 6.8 m tall · 315 objects · ~117376 tris · 20 lights · 100 furniture pieces
* **Exterior doors:** F1_S6(S side), F1_E1(E side), F2_S0(S side), F2_S1(S side), F2_S2(S side), F2_S3(S side), F2_S4(S side) · interior doors: 18
* **Spawn points (local m):** front (-9.6, -7.5, 0)
* **Interactions:** open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (173.5, -20.3, 0.15), rotZ 180° · **Files:** `export/glb/seaview_motel.glb`, Blender collection `BLD_seaview_motel`

### 警長辦公室 Sheriff's Office — `sheriff_office`

![day](renders/sheriff_office_front_day.png) ![night](renders/sheriff_office_front.png) ![plan](renders/sheriff_office_cut_day.png)

* **Style:** 西部警長屋 / Wild West Jailhouse · **Tier:** budget · **Type:** jail · **Floors:** 1
* **Fits game styles:** western, cartoon, rpg, realistic
* **Description:** Single-storey timber sheriff's office with false front, desk and a barred cell.
* **Size:** 14.0 × 13.0 m footprint, 5.2 m tall · 55 objects · ~65720 tris · 2 lights · 16 furniture pieces
* **Exterior doors:** F1_S2(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -6.5, 0)
* **Interactions:** open, shop, sit, work
* **Placed on island at:** (16.0, -103.7, 0.15), rotZ 0° · **Files:** `export/glb/sheriff_office.glb`, Blender collection `BLD_sheriff_office`

### 藍調轉角雜貨 Blue Corner Bodega — `shop_neon_corner`

![day](renders/shop_neon_corner_front_day.png) ![night](renders/shop_neon_corner_front.png) ![plan](renders/shop_neon_corner_cut_day.png)

* **Style:** 霓虹轉角店 / Neon Corner Shop Diorama · **Tier:** budget · **Type:** shop + flat · **Floors:** 2
* **Fits game styles:** cyberpunk, anime, slice-of-life, diorama, realistic
* **Description:** Corner shop with open frontage (raised roller shutters) on two streets: record & game corner, snack counter, shelves, arcade. Upper blue flat with wrap balcony and LED under-glow, rooftop garden with palms.
* **Size:** 15.5 × 14.0 m footprint, 10.0 m tall · 151 objects · ~111152 tris · 7 lights · 50 furniture pieces
* **Exterior doors:** GF_S0(S side), GF_S1(S side), GF_E0(E side), GF_E1(E side), UF_S1(S side), UF_W0(W side) · interior doors: 1
* **Spawn points (local m):** corner (6.5, -6.0, 0)
* **Interactions:** climb, open, play, shop, sit, sleep, use, work
* **Placed on island at:** (62.5, 14.6, 0.15), rotZ 0° · **Files:** `export/glb/shop_neon_corner.glb`, Blender collection `BLD_shop_neon_corner`

### 平原帳篷營地 Plains Tipi Camp — `tipi_camp`

![day](renders/tipi_camp_front_day.png) ![night](renders/tipi_camp_front.png) ![plan](renders/tipi_camp_cut_day.png)

* **Style:** 帳篷營地 / Plains Tipi Encampment · **Tier:** budget · **Type:** camp · **Floors:** 1
* **Fits game styles:** western, survival, historical, nomad
* **Description:** Three hide tipis around a stone-ringed campfire, drying rack and log seats.
* **Size:** 20.0 × 18.0 m footprint, 7.5 m tall · 17 objects · ~58948 tris · 1 lights · 4 furniture pieces
* **Exterior doors:** - · interior doors: 0
* **Spawn points (local m):** front (0.0, -5.5, 0)
* **Interactions:** sit, use
* **Placed on island at:** (-25.0, -187.3, 0.15), rotZ 180° · **Files:** `export/glb/tipi_camp.glb`, Blender collection `BLD_tipi_camp`

### 霓虹窄塔 Neon Sliver Tower — `tower_cyber_narrow`

![day](renders/tower_cyber_narrow_front_day.png) ![night](renders/tower_cyber_narrow_front.png) ![plan](renders/tower_cyber_narrow_cut_day.png)

* **Style:** 賽博龐克窄樓 / Cyberpunk Vertical Block · **Tier:** budget · **Type:** mixed-use tower · **Floors:** 5
* **Fits game styles:** cyberpunk, sci-fi, neo-noir, realistic
* **Description:** 6x7 m five-storey neon tower: G/F DVD & gadget shop, 2F hacker den with servers, 3F capsule hostel, 4F neon bar, 5F loft, roof hut with antennas. Grimy steel cladding, fans, pipes, vertical neon signs.
* **Size:** 9.2 × 10.0 m footprint, 22.1 m tall · 318 objects · ~119120 tris · 14 lights · 53 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_S2(S side), Hut_W0(W side) · interior doors: 0
* **Spawn points (local m):** front (-0.2, -5.1, 0)
* **Interactions:** open, play, shop, sit, sleep, use, work
* **Placed on island at:** (44.0, 12.5, 0.15), rotZ 0° · **Files:** `export/glb/tower_cyber_narrow.glb`, Blender collection `BLD_tower_cyber_narrow`

### 河內管狀屋 Hanoi Tube House — `vn_tube_house`

![day](renders/vn_tube_house_front_day.png) ![night](renders/vn_tube_house_front.png) ![plan](renders/vn_tube_house_cut_day.png)

* **Style:** 越南管狀屋 / Vietnamese Tube House · **Tier:** budget · **Type:** house + café · **Floors:** 5
* **Fits game styles:** realistic, southeast-asia, slice-of-life
* **Description:** 5-storey 5.6 m-wide tube house: ground-floor cà phê, one room per floor, plant balconies, roof terrace.
* **Size:** 9.0 × 21.0 m footprint, 18.3 m tall · 357 objects · ~101316 tris · 16 lights · 86 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_E3(E side), F2_S1(S side), F4_S1(S side), PH_W0(W side) · interior doors: 10
* **Spawn points (local m):** front (-1.4, -10.5, 0)
* **Interactions:** cook, open, shop, sit, sleep, use
* **Placed on island at:** (-112.5, -80.3, 0.15), rotZ 180° · **Files:** `export/glb/vn_tube_house.glb`, Blender collection `BLD_vn_tube_house`

### 荒野西部酒館 Dusty Spur Saloon — `western_saloon`

![day](renders/western_saloon_front_day.png) ![night](renders/western_saloon_front.png) ![plan](renders/western_saloon_cut_day.png)

* **Style:** 西部酒館 / Wild West Saloon · **Tier:** budget · **Type:** saloon · **Floors:** 2
* **Fits game styles:** western, realistic, cartoon, rpg
* **Description:** 2-storey timber saloon with false front, swinging doors, bar, card tables, rooms upstairs off a wooden balcony.
* **Size:** 17.0 × 16.0 m footprint, 9.2 m tall · 178 objects · ~82868 tris · 8 lights · 55 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side), F2_S1(S side), F2_S3(S side) · interior doors: 6
* **Spawn points (local m):** front (0.0, -8.0, 0)
* **Interactions:** open, shop, sit, sleep, use, work
* **Placed on island at:** (-22.5, -102.2, 0.15), rotZ 0° · **Files:** `export/glb/western_saloon.glb`, Blender collection `BLD_western_saloon`

### 林間女巫小屋 Witch's Woodland Cottage — `witch_cottage`

![day](renders/witch_cottage_front_day.png) ![night](renders/witch_cottage_front.png) ![plan](renders/witch_cottage_cut_day.png)

* **Style:** 女巫小屋 / Storybook Witch Cottage · **Tier:** budget · **Type:** cottage · **Floors:** 1
* **Fits game styles:** fantasy, horror, ghibli, halloween
* **Description:** Tiny dark timber cottage with a needle-steep roof, crooked chimney, bubbling green cauldron, herb shelves.
* **Size:** 13.1 × 12.0 m footprint, 11.0 m tall · 39 objects · ~78676 tris · 2 lights · 7 furniture pieces
* **Exterior doors:** F1_S2(S side) · interior doors: 0
* **Spawn points (local m):** front (1.2, -6.0, 0)
* **Interactions:** cook, open, shop
* **Placed on island at:** (-115.0, -156.2, 0.15), rotZ 0° · **Files:** `export/glb/witch_cottage.glb`, Blender collection `BLD_witch_cottage`

### 冷鏈冷凍廠 Cold-Chain Plant — `cold_storage`

![day](renders/cold_storage_front_day.png) ![night](renders/cold_storage_front.png) ![plan](renders/cold_storage_cut_day.png)

* **Style:** 冷凍廠 / Cold Storage Facility · **Tier:** utility · **Type:** factory · **Floors:** 1
* **Fits game styles:** realistic, horror, thriller, industrial
* **Description:** Windowless white insulated-panel plant: freezer storage halls, control office, roof chillers.
* **Size:** 21.0 × 17.0 m footprint, 7.6 m tall · 74 objects · ~74760 tris · 2 lights · 43 furniture pieces
* **Exterior doors:** F1_S1(S side) · interior doors: 0
* **Spawn points (local m):** front (5.0, -8.5, 0)
* **Interactions:** open, shop, sit, work
* **Placed on island at:** (19.5, -134.3, 0.15), rotZ 180° · **Files:** `export/glb/cold_storage.glb`, Blender collection `BLD_cold_storage`

### 雲端資料中心 Nimbus Data Center — `data_center`

![day](renders/data_center_front_day.png) ![night](renders/data_center_front.png) ![plan](renders/data_center_cut_day.png)

* **Style:** 資料中心 / Hyperscale Data Center · **Tier:** utility · **Type:** data center · **Floors:** 2
* **Fits game styles:** cyberpunk, sci-fi, thriller, realistic, hacker
* **Description:** Windowless steel data hall: server rooms with rack rows and consoles, NOC office, roof chillers, backup generators.
* **Size:** 30.0 × 19.0 m footprint, 9.9 m tall · 209 objects · ~110724 tris · 10 lights · 102 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_E0(E side) · interior doors: 8
* **Spawn points (local m):** front (-5.0, -9.5, 0)
* **Interactions:** open, sit, use, wash, work
* **Placed on island at:** (24.0, -44.7, 0.15), rotZ 0° · **Files:** `export/glb/data_center.glb`, Blender collection `BLD_data_center`

### 無人機物流站 Drone Delivery Hub — `drone_hub`

![day](renders/drone_hub_front_day.png) ![night](renders/drone_hub_front.png) ![plan](renders/drone_hub_cut_day.png)

* **Style:** 無人機站 / Drone Logistics Hub · **Tier:** utility · **Type:** logistics · **Floors:** 3
* **Fits game styles:** sci-fi, modern, cyberpunk
* **Description:** 3-storey steel hub: parcel storage and control room, roof landing pads with delivery drones.
* **Size:** 17.0 × 17.0 m footprint, 12.7 m tall · 277 objects · ~120564 tris · 13 lights · 94 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E2(E side), PH_W0(W side) · interior doors: 9
* **Spawn points (local m):** front (-2.0, -8.5, 0)
* **Interactions:** open, shop, sit, use, work
* **Placed on island at:** (193.5, -134.3, 0.15), rotZ 180° · **Files:** `export/glb/drone_hub.glb`, Blender collection `BLD_drone_hub`

### 物流倉儲中心 Logistics Warehouse — `logistics_warehouse`

![day](renders/logistics_warehouse_front_day.png) ![night](renders/logistics_warehouse_front.png) ![plan](renders/logistics_warehouse_cut_day.png)

* **Style:** 物流倉庫 / Distribution Warehouse · **Tier:** utility · **Type:** warehouse · **Floors:** 1
* **Fits game styles:** realistic, industrial, zombie, action
* **Description:** Single tall steel warehouse: racking aisles, three roller loading docks, delivery trucks in the yard.
* **Size:** 28.0 × 30.0 m footprint, 7.9 m tall · 65 objects · ~92244 tris · 1 lights · 26 furniture pieces
* **Exterior doors:** F1_S0(S side), F1_S1(S side), F1_S2(S side), F1_S3(S side) · interior doors: 0
* **Spawn points (local m):** front (9.0, -10.5, 0)
* **Interactions:** open, shop, use
* **Placed on island at:** (-41.0, -145.3, 0.15), rotZ 180° · **Files:** `export/glb/logistics_warehouse.glb`, Blender collection `BLD_logistics_warehouse`

### 立體停車塔 Multi-storey Car Park — `parking_tower`

![day](renders/parking_tower_front_day.png) ![night](renders/parking_tower_front.png) ![plan](renders/parking_tower_cut_day.png)

* **Style:** 立體停車場 / Parking Structure · **Tier:** utility · **Type:** parking · **Floors:** 5
* **Fits game styles:** realistic, action, gta-like, urban
* **Description:** 5-storey open concrete car park with parked cars on every deck, stair core, big P sign.
* **Size:** 21.0 × 19.0 m footprint, 16.4 m tall · 209 objects · ~71832 tris · 20 lights · 25 furniture pieces
* **Exterior doors:** F1_E1(E side) · interior doors: 15
* **Spawn points (local m):** front (0.0, -9.5, 0)
* **Interactions:** open, use, work
* **Placed on island at:** (-66.5, -135.3, 0.15), rotZ 180° · **Files:** `export/glb/parking_tower.glb`, Blender collection `BLD_parking_tower`

### 極光貨櫃研究站 Aurora Container Research Station — `station_arctic`

![day](renders/station_arctic_front_day.png) ![night](renders/station_arctic_front.png) ![plan](renders/station_arctic_cut_day.png)

* **Style:** 極地貨櫃前哨站 / Polar Container Outpost · **Tier:** utility · **Type:** research station · **Floors:** 2
* **Fits game styles:** realistic, survival, sci-fi, thriller, post-apocalyptic
* **Description:** Four containers (blue 20ft bunks, yellow 40ft lab, grey 20ft mess, grey 40ft comms/lounge) on stilts around a glass stair tower; twin front stairs, upper balcony walkway + slanted canopy, antenna mast, dish, fuel drums.
* **Size:** 28.6 × 15.7 m footprint, 10.7 m tall · 203 objects · ~111014 tris · 14 lights · 31 furniture pieces
* **Exterior doors:** Tower_S1(S side), Bunks_S1(S side), Lab_S1(S side), Comms_S1(S side) · interior doors: 0
* **Spawn points (local m):** stairs_left (-5.5, -6.14, 0)
* **Interactions:** cook, open, sit, sleep, use, work
* **Placed on island at:** (-2.0, 86.0, 7.0), rotZ 0° · **Files:** `export/glb/station_arctic.glb`, Blender collection `BLD_station_arctic`

### 垂直農場 Vertical Farm Tower — `vertical_farm`

![day](renders/vertical_farm_front_day.png) ![night](renders/vertical_farm_front.png) ![plan](renders/vertical_farm_cut_day.png)

* **Style:** 垂直農場 / Vertical Farm · **Tier:** utility · **Type:** farm · **Floors:** 5
* **Fits game styles:** solarpunk, sci-fi, farming-sim, realistic
* **Description:** 5-storey glass tower of LED-lit hydroponic racks, shop for produce, solar roof.
* **Size:** 19.0 × 17.0 m footprint, 19.1 m tall · 464 objects · ~185352 tris · 16 lights · 192 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E2(E side), PH_W0(W side) · interior doors: 10
* **Spawn points (local m):** front (-3.0, -8.5, 0)
* **Interactions:** open, shop, sit, use
* **Placed on island at:** (124.5, -134.3, 0.15), rotZ 180° · **Files:** `export/glb/vertical_farm.glb`, Blender collection `BLD_vertical_farm`

### 海港消防局 Harbor Fire Station — `fire_station`

![day](renders/fire_station_front_day.png) ![night](renders/fire_station_front.png) ![plan](renders/fire_station_cut_day.png)

* **Style:** 消防局 / Civic Fire Station · **Tier:** civic · **Type:** fire station · **Floors:** 2
* **Fits game styles:** realistic, rescue-sim, anime, action
* **Description:** Brick 2-storey station: double apparatus bay with two ladder trucks behind roller doors, hose tower, upstairs dorm + lounge.
* **Size:** 26.0 × 22.0 m footprint, 15.4 m tall · 166 objects · ~82628 tris · 10 lights · 38 furniture pieces
* **Exterior doors:** F1_S0(S side), F1_S1(S side), F1_S2(S side), F1_E2(E side) · interior doors: 8
* **Spawn points (local m):** front (7.0, -9.5, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, wash
* **Placed on island at:** (176.0, 20.3, 0.15), rotZ 0° · **Files:** `export/glb/fire_station.glb`, Blender collection `BLD_fire_station`

### 仁心綜合醫院 Renxin General Hospital — `hospital_general`

![day](renders/hospital_general_front_day.png) ![night](renders/hospital_general_front.png) ![plan](renders/hospital_general_cut_day.png)

* **Style:** 現代醫院 / Modern Hospital · **Tier:** civic · **Type:** hospital · **Floors:** 3
* **Fits game styles:** realistic, horror, medical-drama, zombie, anime
* **Description:** 3-storey tiled hospital: lobby + triage clinics, wards with beds, exam rooms, roof terrace, drop-off canopy, ambulance, red cross.
* **Size:** 27.0 × 24.0 m footprint, 13.5 m tall · 320 objects · ~111996 tris · 19 lights · 82 furniture pieces
* **Exterior doors:** F1_S6(S side), F1_E2(E side), PH_W0(W side) · interior doors: 15
* **Spawn points (local m):** front (-5.0, -10.0, 0)
* **Interactions:** open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (-225.5, -21.8, 0.15), rotZ 180° · **Files:** `export/glb/hospital_general.glb`, Blender collection `BLD_hospital_general`

### 彩虹幼兒園 Rainbow Kindergarten — `kindergarten`

![day](renders/kindergarten_front_day.png) ![night](renders/kindergarten_front.png) ![plan](renders/kindergarten_cut_day.png)

* **Style:** 童趣幼兒園 / Playful Kindergarten · **Tier:** civic · **Type:** kindergarten · **Floors:** 1
* **Fits game styles:** anime, slice-of-life, cozy, horror, cartoon
* **Description:** Single-storey cheerful kindergarten: classroom + play lounge, red tile gable, playground with slide, swings and sandbox.
* **Size:** 19.0 × 19.0 m footprint, 7.6 m tall · 114 objects · ~69848 tris · 2 lights · 71 furniture pieces
* **Exterior doors:** F1_S4(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -7.5, 0)
* **Interactions:** open, play, sit, use, work
* **Placed on island at:** (74.5, -19.3, 0.15), rotZ 180° · **Files:** `export/glb/kindergarten.glb`, Blender collection `BLD_kindergarten`

### 騎士兵營 Knights' Barracks — `knight_barracks`

![day](renders/knight_barracks_front_day.png) ![night](renders/knight_barracks_front.png) ![plan](renders/knight_barracks_cut_day.png)

* **Style:** 騎士兵營 / Medieval Barracks · **Tier:** civic · **Type:** barracks · **Floors:** 2
* **Fits game styles:** medieval, fantasy, strategy, rpg
* **Description:** 2-storey stone barracks with crenellated roof walk and banners: mess hall, armoury, bunk rooms, training yard with dummies.
* **Size:** 21.0 × 18.0 m footprint, 10.4 m tall · 226 objects · ~79264 tris · 9 lights · 58 furniture pieces
* **Exterior doors:** F1_S3(S side), F1_E1(E side), PH_W0(W side) · interior doors: 6
* **Spawn points (local m):** front (-2.0, -7.5, 0)
* **Interactions:** open, shop, sit, sleep, use, work
* **Placed on island at:** (-66.5, -151.7, 0.15), rotZ 0° · **Files:** `export/glb/knight_barracks.glb`, Blender collection `BLD_knight_barracks`

### 市立混凝土圖書館 Concrete Public Library — `library_brutalist`

![day](renders/library_brutalist_front_day.png) ![night](renders/library_brutalist_front.png) ![plan](renders/library_brutalist_cut_day.png)

* **Style:** 粗獷主義 / Brutalist · **Tier:** civic · **Type:** library · **Floors:** 2
* **Fits game styles:** realistic, dystopian, mystery, anime, post-apocalyptic
* **Description:** Massive exposed-concrete library: tall reading hall of stacks, upper reading room + meeting room, deep concrete fins and slab crown.
* **Size:** 23.0 × 21.0 m footprint, 9.4 m tall · 167 objects · ~122576 tris · 8 lights · 55 furniture pieces
* **Exterior doors:** F1_S4(S side), F1_E1(E side) · interior doors: 6
* **Spawn points (local m):** front (-3.0, -9.5, 0)
* **Interactions:** open, sit, use, wash
* **Placed on island at:** (224.5, 19.3, 0.15), rotZ 0° · **Files:** `export/glb/library_brutalist.glb`, Blender collection `BLD_library_brutalist`

### 海港警察局 Harbor Police Station — `police_station`

![day](renders/police_station_front_day.png) ![night](renders/police_station_front.png) ![plan](renders/police_station_cut_day.png)

* **Style:** 警察局 / Civic Police Station · **Tier:** civic · **Type:** police station · **Floors:** 2
* **Fits game styles:** realistic, crime, action, detective, anime
* **Description:** Concrete 2-storey precinct: public lobby with front desk, squad office, holding/storage, upstairs open office, briefing room, server room.
* **Size:** 23.0 × 22.0 m footprint, 10.0 m tall · 245 objects · ~118052 tris · 13 lights · 109 furniture pieces
* **Exterior doors:** F1_S5(S side), F1_E2(E side) · interior doors: 8
* **Spawn points (local m):** front (-4.0, -9.0, 0)
* **Interactions:** open, shop, sit, use, wash, work
* **Placed on island at:** (200.5, 20.8, 0.15), rotZ 0° · **Files:** `export/glb/police_station.glb`, Blender collection `BLD_police_station`

### 海港郵局 Harbor Post Office — `post_office`

![day](renders/post_office_front_day.png) ![night](renders/post_office_front.png) ![plan](renders/post_office_cut_day.png)

* **Style:** 郵局 / Civic Post Office · **Tier:** civic · **Type:** post office · **Floors:** 1
* **Fits game styles:** realistic, slice-of-life, anime, rpg-village
* **Description:** Single-storey cream-brick post office: counter hall with rope queue, parcel storage, green post box, flag.
* **Size:** 17.0 × 15.0 m footprint, 4.7 m tall · 52 objects · ~62084 tris · 2 lights · 10 furniture pieces
* **Exterior doors:** F1_S3(S side) · interior doors: 0
* **Spawn points (local m):** front (-2.0, -7.5, 0)
* **Interactions:** open, shop, sit, use
* **Placed on island at:** (-150.5, -15.3, 0.15), rotZ 180° · **Files:** `export/glb/post_office.glb`, Blender collection `BLD_post_office`

### 海港國民小學 Harbor Primary School — `school_primary`

![day](renders/school_primary_front_day.png) ![night](renders/school_primary_front.png) ![plan](renders/school_primary_cut_day.png)

* **Style:** 公立學校 / Asian Public School · **Tier:** civic · **Type:** school · **Floors:** 3
* **Fits game styles:** slice-of-life, anime, horror, realistic, school-life
* **Description:** 3-storey brick school: classrooms with desks/whiteboards on every floor, library, front-yard basketball court, flagpole, clock.
* **Size:** 31.0 × 24.5 m footprint, 11.1 m tall · 718 objects · ~141724 tris · 18 lights · 497 furniture pieces
* **Exterior doors:** F1_S8(S side), F1_E2(E side) · interior doors: 15
* **Spawn points (local m):** front (0.4, -9.0, 0)
* **Interactions:** open, shop, sit, use, wash, work
* **Placed on island at:** (-195.5, -23.3, 0.15), rotZ 180° · **Files:** `export/glb/school_primary.glb`, Blender collection `BLD_school_primary`

### 森林A字木屋 Forest A-Frame Cabin — `a_frame_cabin`

![day](renders/a_frame_cabin_front_day.png) ![night](renders/a_frame_cabin_front.png) ![plan](renders/a_frame_cabin_cut_day.png)

* **Style:** A字型木屋 / A-Frame Cabin · **Tier:** standard · **Type:** cabin · **Floors:** 2
* **Fits game styles:** cozy, horror, survival, realistic, winter
* **Description:** Steep A-frame timber cabin: glazed front gable with door, living + kitchenette below, sleeping loft reached by a centre stair, deck.
* **Size:** 15.8 × 16.4 m footprint, 7.6 m tall · 48 objects · ~50688 tris · 3 lights · 12 furniture pieces
* **Exterior doors:** FrontDoor(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -7.5, 0)
* **Interactions:** cook, open, sit, sleep, use
* **Placed on island at:** (66.0, -45.7, 0.15), rotZ 0° · **Files:** `export/glb/a_frame_cabin.glb`, Blender collection `BLD_a_frame_cabin`

### 朝陽社區公寓 Sunrise Walk-up Apartments — `apt_block_6f`

![day](renders/apt_block_6f_front_day.png) ![night](renders/apt_block_6f_front.png) ![plan](renders/apt_block_6f_cut_day.png)

* **Style:** 台式公寓 / Taiwanese Walk-up Apartment · **Tier:** standard · **Type:** apartment block · **Floors:** 6
* **Fits game styles:** realistic, slice-of-life, anime, urban-survival
* **Description:** 6-storey mosaic-tile walk-up: arcade with convenience store + breakfast shop, 10 one-bedroom flats (2 per floor), central U-stair, grilled windows, balconies with laundry, rooftop iron-sheet addition with water tanks.
* **Size:** 19.0 × 15.1 m footprint, 22.0 m tall · 929 objects · ~223504 tris · 62 lights · 312 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_S2(S side), F1_S3(S side), F1_S4(S side), F2_S1(S side), F2_S3(S side), F3_S1(S side), F3_S3(S side), F4_S1(S side), F4_S3(S side), F5_S1(S side), F5_S3(S side), F6_S1(S side), F6_S3(S side), Shack_S0(S side) · interior doors: 31
* **Spawn points (local m):** arcade (0.0, -7.5, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (-50.0, 14.6, 0.15), rotZ 0° · **Files:** `export/glb/apt_block_6f.glb`, Blender collection `BLD_apt_block_6f`

### 夜巷住商公寓 Night Alley Mixed-Use Apartment — `apt_urban_5f`

![day](renders/apt_urban_5f_front_day.png) ![night](renders/apt_urban_5f_front.png) ![plan](renders/apt_urban_5f_cut_day.png)

* **Style:** 都市亞洲住商 / Urban Asian Mixed-Use · **Tier:** standard · **Type:** apartment · **Floors:** 5
* **Fits game styles:** realistic, anime, slice-of-life, cyberpunk-lite
* **Description:** 5F walk-up: G/F ramen shop with counter seating, 2F-4F one-bedroom flats with balcony, 5F loft studio, roof terrace with water tank. Shared U-stair core.
* **Size:** 13.2 × 13.4 m footprint, 22.5 m tall · 505 objects · ~141208 tris · 40 lights · 129 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_S3(S side), F1_N1(N side), F2_S1(S side), F3_S1(S side), F4_S1(S side), F5_S1(S side), PH_S0(S side) · interior doors: 11
* **Spawn points (local m):** front_door (3.7, -6.1, 0), shop_door (0.1, -6.1, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (-26.0, 14.3, 0.15), rotZ 0° · **Files:** `export/glb/apt_urban_5f.glb`, Blender collection `BLD_apt_urban_5f`

### 麥香麵包坊 Wheat & Hearth Bakery — `bakery_corner`

![day](renders/bakery_corner_front_day.png) ![night](renders/bakery_corner_front.png) ![plan](renders/bakery_corner_cut_day.png)

* **Style:** 歐式麵包店 / European Bakery · **Tier:** standard · **Type:** bakery + flat · **Floors:** 2
* **Fits game styles:** cozy, anime, slice-of-life, realistic, ghibli
* **Description:** Cream-brick 2-storey bakery: bread display, oven, café table, striped awning; baker's flat upstairs.
* **Size:** 14.0 × 15.0 m footprint, 10.7 m tall · 123 objects · ~82688 tris · 6 lights · 26 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side) · interior doors: 4
* **Spawn points (local m):** front (-2.4, -7.5, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, work
* **Placed on island at:** (218.0, -15.3, 0.15), rotZ 180° · **Files:** `export/glb/bakery_corner.glb`, Blender collection `BLD_bakery_corner`

### 書與咖啡 Books & Beans — `bookstore_cafe`

![day](renders/bookstore_cafe_front_day.png) ![night](renders/bookstore_cafe_front.png) ![plan](renders/bookstore_cafe_cut_day.png)

* **Style:** 紅磚書店咖啡 / Brick Bookshop Café · **Tier:** standard · **Type:** bookstore + café · **Floors:** 3
* **Fits game styles:** cozy, anime, slice-of-life, realistic, mystery
* **Description:** 3-storey brick bookshop: G/F bookstacks, 2F café with counter and tables, 3F reading loft flat, green awning.
* **Size:** 15.0 × 16.0 m footprint, 10.5 m tall · 211 objects · ~102186 tris · 11 lights · 58 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side) · interior doors: 8
* **Spawn points (local m):** front (-2.4, -8.0, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (-199.5, -46.2, 0.15), rotZ 0° · **Files:** `export/glb/bookstore_cafe.glb`, Blender collection `BLD_bookstore_cafe`

### 紅磚老宅咖啡 Red-Brick Heritage Café — `brick_heritage_cafe`

![day](renders/brick_heritage_cafe_front_day.png) ![night](renders/brick_heritage_cafe_front.png) ![plan](renders/brick_heritage_cafe_cut_day.png)

* **Style:** 老宅咖啡 / Taiwanese Heritage House · **Tier:** standard · **Type:** café · **Floors:** 2
* **Fits game styles:** taiwan, cozy, slice-of-life, realistic
* **Description:** Restored 1930s red-brick house: café downstairs, gallery loft upstairs, arched windows, potted plants.
* **Size:** 14.0 × 16.0 m footprint, 7.3 m tall · 133 objects · ~92880 tris · 6 lights · 35 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side) · interior doors: 4
* **Spawn points (local m):** front (-2.0, -8.0, 0)
* **Interactions:** cook, open, shop, sit, sleep, use
* **Placed on island at:** (160.0, -77.8, 0.15), rotZ 180° · **Files:** `export/glb/brick_heritage_cafe.glb`, Blender collection `BLD_brick_heritage_cafe`

### 運河雙子樓 Canal Twin Houses — `canal_twin_tower`

![day](renders/canal_twin_tower_front_day.png) ![night](renders/canal_twin_tower_front.png) ![plan](renders/canal_twin_tower_cut_day.png)

* **Style:** 港灣運河樓房 / Harbour Canal Townhouses · **Tier:** standard · **Type:** mixed-use townhouses · **Floors:** 6
* **Fits game styles:** realistic, anime, ghibli, fantasy-port, slice-of-life
* **Description:** Stone quay platform in the water with a teal 5-storey and an ochre 6-storey tower sharing one U-stair; G/F grocery + noodle bar, flats above, roof terrace, lanterns, jetty with two rowing boats, boardwalk to shore.
* **Size:** 22.9 × 36.2 m footprint, 21.8 m tall · 558 objects · ~154898 tris · 32 lights · 122 furniture pieces
* **Exterior doors:** B1_S1(S side), A1_S1(S side), A2_S1(S side), A3_S1(S side), A4_S1(S side), A5_S1(S side) · interior doors: 11
* **Spawn points (local m):** boardwalk (0.0, -26.0, -0.02)
* **Interactions:** cook, open, shop, sit, sleep, use
* **Placed on island at:** (237.0, -190.0, 0.15), rotZ 180° · **Files:** `export/glb/canal_twin_tower.glb`, Blender collection `BLD_canal_twin_tower`

### 芝加哥紅磚公寓 Chicago Brick Three-Flat — `chicago_walkup`

![day](renders/chicago_walkup_front_day.png) ![night](renders/chicago_walkup_front.png) ![plan](renders/chicago_walkup_cut_day.png)

* **Style:** 芝加哥公寓 / Chicago Greystone/Brick Flat · **Tier:** standard · **Type:** apartment · **Floors:** 4
* **Fits game styles:** noir, crime, realistic, americana
* **Description:** 4-storey red-brick walk-up with black steel fire-escape balconies, cornice, one flat per floor.
* **Size:** 17.0 × 17.0 m footprint, 14.8 m tall · 359 objects · ~112420 tris · 20 lights · 101 furniture pieces
* **Exterior doors:** F1_S3(S side), F1_E2(E side) · interior doors: 16
* **Spawn points (local m):** front (-3.0, -8.5, 0)
* **Interactions:** cook, open, sit, sleep, use, wash, work
* **Placed on island at:** (151.5, -101.7, 0.15), rotZ 0° · **Files:** `export/glb/chicago_walkup.glb`, Blender collection `BLD_chicago_walkup`

### 新星夜店 Club Nova — `club_nova`

![day](renders/club_nova_front_day.png) ![night](renders/club_nova_front.png) ![plan](renders/club_nova_cut_day.png)

* **Style:** 霓虹夜店 / Neon Nightclub · **Tier:** standard · **Type:** nightclub · **Floors:** 2
* **Fits game styles:** cyberpunk, nightlife, crime, anime
* **Description:** 2-storey black nightclub: dance floor + bar, VIP lounge upstairs, neon bands, queue rope.
* **Size:** 19.0 × 17.0 m footprint, 8.3 m tall · 172 objects · ~65016 tris · 9 lights · 69 furniture pieces
* **Exterior doors:** F1_S4(S side), F1_E0(E side) · interior doors: 7
* **Spawn points (local m):** front (-2.0, -8.5, 0)
* **Interactions:** open, shop, sit, use, wash, work
* **Placed on island at:** (86.5, -134.3, 0.15), rotZ 180° · **Files:** `export/glb/club_nova.glb`, Blender collection `BLD_club_nova`

### 健康藥局 Health Pharmacy — `corner_pharmacy`

![day](renders/corner_pharmacy_front_day.png) ![night](renders/corner_pharmacy_front.png) ![plan](renders/corner_pharmacy_cut_day.png)

* **Style:** 社區藥局 / Asian Neighbourhood Pharmacy · **Tier:** standard · **Type:** pharmacy · **Floors:** 3
* **Fits game styles:** slice-of-life, realistic, zombie
* **Description:** 3-storey white-tile pharmacy with shelves and counter, green cross sign, flats above.
* **Size:** 13.0 × 15.0 m footprint, 10.5 m tall · 171 objects · ~100284 tris · 9 lights · 36 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side) · interior doors: 6
* **Spawn points (local m):** front (-1.8, -7.5, 0)
* **Interactions:** open, shop, sit, sleep, use, work
* **Placed on island at:** (81.5, -77.3, 0.15), rotZ 180° · **Files:** `export/glb/corner_pharmacy.glb`, Blender collection `BLD_corner_pharmacy`

### 共享辦公大樓 Co-Work Hub — `cowork_hub`

![day](renders/cowork_hub_front_day.png) ![night](renders/cowork_hub_front.png) ![plan](renders/cowork_hub_cut_day.png)

* **Style:** 共享辦公 / Co-working Office · **Tier:** standard · **Type:** office · **Floors:** 4
* **Fits game styles:** modern, slice-of-life, realistic
* **Description:** 4-storey brick-and-glass co-working building: café lobby, hot-desk floors, meeting pods, roof terrace.
* **Size:** 19.0 × 17.0 m footprint, 15.9 m tall · 437 objects · ~119868 tris · 18 lights · 188 furniture pieces
* **Exterior doors:** F1_S4(S side), F1_E2(E side), PH_W0(W side) · interior doors: 13
* **Spawn points (local m):** front (-3.0, -8.5, 0)
* **Interactions:** open, shop, sit, use, wash, work
* **Placed on island at:** (-111.5, -134.3, 0.15), rotZ 180° · **Files:** `export/glb/cowork_hub.glb`, Blender collection `BLD_cowork_hub`

### 精釀啤酒廠 Harbor Craft Brewery — `craft_brewery`

![day](renders/craft_brewery_front_day.png) ![night](renders/craft_brewery_front.png) ![plan](renders/craft_brewery_cut_day.png)

* **Style:** 精釀酒廠 / Craft Brewery Taproom · **Tier:** standard · **Type:** brewery · **Floors:** 2
* **Fits game styles:** realistic, slice-of-life, industrial, rpg
* **Description:** 2-storey brick brewhouse: taproom bar downstairs, brewing floor above, row of stainless fermentation tanks outside.
* **Size:** 24.0 × 17.0 m footprint, 9.6 m tall · 179 objects · ~96840 tris · 9 lights · 66 furniture pieces
* **Exterior doors:** F1_S3(S side), F1_E1(E side) · interior doors: 7
* **Spawn points (local m):** front (-3.0, -8.5, 0)
* **Interactions:** open, shop, sit, use, wash, work
* **Placed on island at:** (43.0, -134.3, 0.15), rotZ 180° · **Files:** `export/glb/craft_brewery.glb`, Blender collection `BLD_craft_brewery`

### 矮人石廳 Dwarven Stonehall — `dwarf_stonehall`

![day](renders/dwarf_stonehall_front_day.png) ![night](renders/dwarf_stonehall_front.png) ![plan](renders/dwarf_stonehall_cut_day.png)

* **Style:** 矮人石屋 / Dwarven Hall · **Tier:** standard · **Type:** forge hall · **Floors:** 1
* **Fits game styles:** fantasy, rpg, medieval, dnd
* **Description:** Squat granite hall with a heavy round door, runic lanterns, forge and anvil inside, low stone roof.
* **Size:** 15.0 × 14.0 m footprint, 5.8 m tall · 58 objects · ~50150 tris · 5 lights · 10 furniture pieces
* **Exterior doors:** F1_S2(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -7.0, 0)
* **Interactions:** open, sit, use, work
* **Placed on island at:** (-147.5, -155.2, 0.15), rotZ 0° · **Files:** `export/glb/dwarf_stonehall.glb`, Blender collection `BLD_dwarf_stonehall`

### 英式茅草小屋 English Thatched Cottage — `english_cottage`

![day](renders/english_cottage_front_day.png) ![night](renders/english_cottage_front.png) ![plan](renders/english_cottage_cut_day.png)

* **Style:** 英式鄉村小屋 / English Country Cottage · **Tier:** standard · **Type:** cottage · **Floors:** 2
* **Fits game styles:** cozy, europe, farming-sim, anime, ghibli
* **Description:** 2-storey whitewashed cottage with a thick thatch gable, flower boxes, picket fence and garden path.
* **Size:** 14.0 × 15.6 m footprint, 11.9 m tall · 122 objects · ~79812 tris · 6 lights · 25 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side) · interior doors: 4
* **Spawn points (local m):** front (-1.13, -6.8, 0)
* **Interactions:** cook, open, sit, sleep, use, wash, work
* **Placed on island at:** (-146.0, -101.4, 0.15), rotZ 0° · **Files:** `export/glb/english_cottage.glb`, Blender collection `BLD_english_cottage`

### 電動車超充站 EV Supercharge Hub — `ev_charging_hub`

![day](renders/ev_charging_hub_front_day.png) ![night](renders/ev_charging_hub_front.png) ![plan](renders/ev_charging_hub_cut_day.png)

* **Style:** 電動車充電站 / EV Charging Station · **Tier:** standard · **Type:** charging station · **Floors:** 1
* **Fits game styles:** modern, sci-fi, gta-like, realistic
* **Description:** Lounge kiosk with café and shelves, solar canopy over six fast chargers with parked EVs.
* **Size:** 24.0 × 23.0 m footprint, 5.0 m tall · 97 objects · ~74788 tris · 7 lights · 56 furniture pieces
* **Exterior doors:** F1_S2(S side) · interior doors: 0
* **Spawn points (local m):** front (-2.0, -6.5, 0)
* **Interactions:** open, shop, sit, use
* **Placed on island at:** (-89.0, -142.3, 0.15), rotZ 180° · **Files:** `export/glb/ev_charging_hub.glb`, Blender collection `BLD_ev_charging_hub`

### 花語花店 Petal Talk Florist — `florist_petal`

![day](renders/florist_petal_front_day.png) ![night](renders/florist_petal_front.png) ![plan](renders/florist_petal_cut_day.png)

* **Style:** 鄉村花店 / Cottage Flower Shop · **Tier:** standard · **Type:** shop + flat · **Floors:** 2
* **Fits game styles:** cozy, anime, romance, slice-of-life, ghibli
* **Description:** White clapboard 2-storey flower shop: plant-filled shop floor, flower stands on the pavement, green awning, flat above with flower boxes.
* **Size:** 13.0 × 15.5 m footprint, 10.1 m tall · 124 objects · ~81304 tris · 6 lights · 31 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side) · interior doors: 4
* **Spawn points (local m):** front (-1.8, -7.25, 0)
* **Interactions:** open, shop, sit, sleep, use, work
* **Placed on island at:** (-164.5, -45.95, 0.15), rotZ 0° · **Files:** `export/glb/florist_petal.glb`, Blender collection `BLD_florist_petal`

### 銀河遊戲中心 Galaxy Game Center — `galaxy_arcade`

![day](renders/galaxy_arcade_front_day.png) ![night](renders/galaxy_arcade_front.png) ![plan](renders/galaxy_arcade_cut_day.png)

* **Style:** 霓虹遊樂場 / Neon Game Arcade · **Tier:** standard · **Type:** arcade · **Floors:** 2
* **Fits game styles:** cyberpunk, anime, retro, nightlife, realistic
* **Description:** 2-storey black game centre: rows of arcade cabinets, claw machines, upstairs arcade + bar, neon signage.
* **Size:** 19.0 × 17.0 m footprint, 7.7 m tall · 171 objects · ~106524 tris · 10 lights · 62 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side) · interior doors: 7
* **Spawn points (local m):** front (-3.5, -8.5, 0)
* **Interactions:** open, play, shop, sit, use, wash
* **Placed on island at:** (-181.5, -45.7, 0.15), rotZ 0° · **Files:** `export/glb/galaxy_arcade.glb`, Blender collection `BLD_galaxy_arcade`

### 德式木筋屋 German Fachwerk House — `german_fachwerk`

![day](renders/german_fachwerk_front_day.png) ![night](renders/german_fachwerk_front.png) ![plan](renders/german_fachwerk_cut_day.png)

* **Style:** 德國木筋屋 / German Half-Timbered · **Tier:** standard · **Type:** house + shop · **Floors:** 3
* **Fits game styles:** europe, fantasy, rpg-village, christmas, realistic
* **Description:** 3-storey Fachwerk: stone shop floor, half-timbered upper floors, steep red tile roof, flower boxes.
* **Size:** 16.0 × 15.0 m footprint, 17.2 m tall · 214 objects · ~92356 tris · 11 lights · 53 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side) · interior doors: 8
* **Spawn points (local m):** front (-2.4, -7.5, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, work
* **Placed on island at:** (191.0, -77.3, 0.15), rotZ 180° · **Files:** `export/glb/german_fachwerk.glb`, Blender collection `BLD_german_fachwerk`

### 薑餅糖果屋 Gingerbread Candy House — `gingerbread_house`

![day](renders/gingerbread_house_front_day.png) ![night](renders/gingerbread_house_front.png) ![plan](renders/gingerbread_house_cut_day.png)

* **Style:** 糖果屋 / Fairy-tale Candy House · **Tier:** standard · **Type:** house · **Floors:** 1
* **Fits game styles:** fantasy, christmas, cartoon, family
* **Description:** Gingerbread-brick cottage with icing trim, candy-cane posts and giant lollipops; pink frosting roof.
* **Size:** 13.0 × 13.0 m footprint, 7.1 m tall · 59 objects · ~71552 tris · 2 lights · 18 furniture pieces
* **Exterior doors:** F1_S2(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -6.0, 0)
* **Interactions:** cook, open, sit, use
* **Placed on island at:** (101.5, -155.2, 0.15), rotZ 0° · **Files:** `export/glb/gingerbread_house.glb`, Blender collection `BLD_gingerbread_house`

### 金龍酒家 Golden Dragon Dim Sum Hall — `hk_dimsum_hall`

![day](renders/hk_dimsum_hall_front_day.png) ![night](renders/hk_dimsum_hall_front.png) ![plan](renders/hk_dimsum_hall_cut_day.png)

* **Style:** 港式茶樓 / Hong Kong Teahouse · **Tier:** standard · **Type:** restaurant · **Floors:** 3
* **Fits game styles:** hk-cinema, action, realistic, noir
* **Description:** 3-storey tiled teahouse: banquet dining halls on every floor, kitchen, red/gold signage, lanterns.
* **Size:** 19.0 × 17.0 m footprint, 10.5 m tall · 371 objects · ~112160 tris · 18 lights · 183 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E2(E side) · interior doors: 9
* **Spawn points (local m):** front (-3.0, -8.5, 0)
* **Interactions:** cook, open, sit, use, wash
* **Placed on island at:** (-139.5, -78.3, 0.15), rotZ 180° · **Files:** `export/glb/hk_dimsum_hall.glb`, Blender collection `BLD_hk_dimsum_hall`

### 哈比山丘洞屋 Hillside Smial — `hobbit_hole`

![day](renders/hobbit_hole_front_day.png) ![night](renders/hobbit_hole_front.png) ![plan](renders/hobbit_hole_cut_day.png)

* **Style:** 哈比洞屋 / Halfling Hill House · **Tier:** standard · **Type:** house · **Floors:** 1
* **Fits game styles:** fantasy, cozy, ghibli, rpg-village
* **Description:** Home dug into a grassy mound: round green door, round windows, cosy living room, pantry and bedroom.
* **Size:** 17.0 × 17.9 m footprint, 2.8 m tall · 52 objects · ~48808 tris · 2 lights · 14 furniture pieces
* **Exterior doors:** F1_S2(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -6.5, 0)
* **Interactions:** open, sit, sleep, use, work
* **Placed on island at:** (-130.5, -153.7, 0.15), rotZ 0° · **Files:** `export/glb/hobbit_hole.glb`, Blender collection `BLD_hobbit_hole`

### 青瓦燈籠茶屋 Teal Lantern Teahouse — `house_teal_lantern`

![day](renders/house_teal_lantern_front_day.png) ![night](renders/house_teal_lantern_front.png) ![plan](renders/house_teal_lantern_cut_day.png)

* **Style:** 吉卜力海邊高腳屋 / Ghibli Seaside Stilt House · **Tier:** standard · **Type:** house+shop · **Floors:** 2
* **Fits game styles:** anime, ghibli, cozy, fantasy, realistic
* **Description:** Teal clapboard 2-storey teahouse on a raised timber deck around an old tree trunk; red-framed bay windows, paper lanterns, roof terrace with antennas.
* **Size:** 18.1 × 17.7 m footprint, 12.0 m tall · 191 objects · ~114112 tris · 11 lights · 39 furniture pieces
* **Exterior doors:** GF_S1(S side) · interior doors: 1
* **Spawn points (local m):** stair_foot (0.0, -10.16, 0)
* **Interactions:** open, shop, sit, sleep, use, work
* **Placed on island at:** (-55.0, -18.5, 0.15), rotZ 180° · **Files:** `export/glb/house_teal_lantern.glb`, Blender collection `BLD_house_teal_lantern`

### 冰島草頂屋 Icelandic Turf House — `iceland_turf_house`

![day](renders/iceland_turf_house_front_day.png) ![night](renders/iceland_turf_house_front.png) ![plan](renders/iceland_turf_house_cut_day.png)

* **Style:** 冰島草屋 / Icelandic Turf House · **Tier:** standard · **Type:** house · **Floors:** 1
* **Fits game styles:** fantasy, viking, survival, cozy
* **Description:** Single-storey black timber house with a grass-covered gable roof, stone chimney, living room and bed nook.
* **Size:** 14.0 × 12.0 m footprint, 7.6 m tall · 52 objects · ~57520 tris · 2 lights · 14 furniture pieces
* **Exterior doors:** F1_S2(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -6.0, 0)
* **Interactions:** open, sit, sleep, use, work
* **Placed on island at:** (222.0, -75.8, 0.15), rotZ 180° · **Files:** `export/glb/iceland_turf_house.glb`, Blender collection `BLD_iceland_turf_house`

### 奧馬利愛爾蘭酒吧 O'Malley's Irish Pub — `irish_pub`

![day](renders/irish_pub_front_day.png) ![night](renders/irish_pub_front.png) ![plan](renders/irish_pub_cut_day.png)

* **Style:** 愛爾蘭酒吧 / Irish Pub · **Tier:** standard · **Type:** pub · **Floors:** 2
* **Fits game styles:** europe, realistic, slice-of-life, crime
* **Description:** 2-storey pub with a dark green timber shopfront, gold lettering, hanging baskets; bar downstairs, function room upstairs.
* **Size:** 15.0 × 15.0 m footprint, 7.3 m tall · 136 objects · ~74888 tris · 8 lights · 36 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side) · interior doors: 4
* **Spawn points (local m):** front (-2.0, -7.5, 0)
* **Interactions:** cook, open, shop, sit, use, wash
* **Placed on island at:** (-115.5, -102.7, 0.15), rotZ 0° · **Files:** `export/glb/irish_pub.glb`, Blender collection `BLD_irish_pub`

### 日式獨棟住宅 Japanese Family House — `jp_family_house`

![day](renders/jp_family_house_front_day.png) ![night](renders/jp_family_house_front.png) ![plan](renders/jp_family_house_cut_day.png)

* **Style:** 日式住宅 / Contemporary Japanese House · **Tier:** standard · **Type:** house · **Floors:** 2
* **Fits game styles:** anime, slice-of-life, japan, realistic
* **Description:** Classic 2-storey Japanese suburban house: white siding, sliding windows, slate hip roof, small balcony, AC units.
* **Size:** 15.0 × 14.5 m footprint, 9.2 m tall · 216 objects · ~93106 tris · 10 lights · 53 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side), F2_S0(S side), F2_S1(S side) · interior doors: 8
* **Spawn points (local m):** front (-1.13, -7.25, 0)
* **Interactions:** cook, open, sit, sleep, use, wash, work
* **Placed on island at:** (-207.5, -77.05, 0.15), rotZ 180° · **Files:** `export/glb/jp_family_house.glb`, Blender collection `BLD_jp_family_house`

### 星光KTV Stardust Karaoke Club — `karaoke_stardust`

![day](renders/karaoke_stardust_front_day.png) ![night](renders/karaoke_stardust_front.png) ![plan](renders/karaoke_stardust_cut_day.png)

* **Style:** 霓虹KTV / Neon Karaoke Club · **Tier:** standard · **Type:** karaoke club · **Floors:** 4
* **Fits game styles:** cyberpunk, anime, nightlife, realistic, kdrama
* **Description:** 4-storey black KTV: G/F bar, private karaoke lounges on upper floors (sofa + TV), neon floor bands, vertical blade sign.
* **Size:** 17.0 × 17.0 m footprint, 13.9 m tall · 333 objects · ~97492 tris · 20 lights · 91 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E2(E side) · interior doors: 15
* **Spawn points (local m):** front (-2.5, -8.5, 0)
* **Interactions:** cook, open, shop, sit, use, wash
* **Placed on island at:** (-216.5, -45.7, 0.15), rotZ 0° · **Files:** `export/glb/karaoke_stardust.glb`, Blender collection `BLD_karaoke_stardust`

### 京都町家 Kyoto Machiya Townhouse — `kyoto_machiya`

![day](renders/kyoto_machiya_front_day.png) ![night](renders/kyoto_machiya_front.png) ![plan](renders/kyoto_machiya_cut_day.png)

* **Style:** 日式町家 / Japanese Machiya · **Tier:** standard · **Type:** shop + house · **Floors:** 2
* **Fits game styles:** anime, realistic, slice-of-life, japan, cozy
* **Description:** Narrow timber townhouse: G/F sweets shop with noren curtain and lanterns, tatami living above, sliding lattice windows, slate gable.
* **Size:** 13.0 × 17.0 m footprint, 8.8 m tall · 154 objects · ~90400 tris · 8 lights · 21 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E2(E side) · interior doors: 4
* **Spawn points (local m):** front (-1.0, -8.5, 0)
* **Interactions:** cook, open, shop, sit, sleep, use
* **Placed on island at:** (121.5, 16.3, 0.15), rotZ 0° · **Files:** `export/glb/kyoto_machiya.glb`, Blender collection `BLD_kyoto_machiya`

### 里斯本磁磚屋 Lisbon Azulejo House — `lisbon_tile_house`

![day](renders/lisbon_tile_house_front_day.png) ![night](renders/lisbon_tile_house_front.png) ![plan](renders/lisbon_tile_house_cut_day.png)

* **Style:** 葡萄牙磁磚屋 / Portuguese Azulejo · **Tier:** standard · **Type:** townhouse · **Floors:** 3
* **Fits game styles:** europe, summer, realistic, romance
* **Description:** 3-storey townhouse clad in blue azulejo tiles, wrought-iron balconies, red tile gable.
* **Size:** 13.0 × 16.0 m footprint, 12.8 m tall · 202 objects · ~82844 tris · 9 lights · 42 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_E1(E side), F2_S1(S side), F3_S1(S side) · interior doors: 6
* **Spawn points (local m):** front (-1.13, -8.0, 0)
* **Interactions:** cook, open, sit, sleep, use, work
* **Placed on island at:** (-100.5, -102.2, 0.15), rotZ 0° · **Files:** `export/glb/lisbon_tile_house.glb`, Blender collection `BLD_lisbon_tile_house`

### 倫敦紅磚聯排 London Victorian Terrace — `london_terrace`

![day](renders/london_terrace_front_day.png) ![night](renders/london_terrace_front.png) ![plan](renders/london_terrace_cut_day.png)

* **Style:** 維多利亞聯排屋 / Victorian Terrace · **Tier:** standard · **Type:** townhouse · **Floors:** 3
* **Fits game styles:** realistic, detective, europe, steampunk, horror
* **Description:** Red-brick 3-storey Victorian terrace: bay window, black front door with fanlight, slate gable roof, chimney stacks.
* **Size:** 14.0 × 16.0 m footprint, 15.2 m tall · 188 objects · ~83776 tris · 11 lights · 36 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_E1(E side) · interior doors: 6
* **Spawn points (local m):** front (1.2, -8.0, 0)
* **Interactions:** cook, open, sit, sleep, use, wash, work
* **Placed on island at:** (-198.0, 15.8, 0.15), rotZ 0° · **Files:** `export/glb/london_terrace.glb`, Blender collection `BLD_london_terrace`

### 躍馬旅店 The Prancing Stag Tavern — `medieval_tavern`

![day](renders/medieval_tavern_front_day.png) ![night](renders/medieval_tavern_front.png) ![plan](renders/medieval_tavern_cut_day.png)

* **Style:** 中世紀酒館 / Medieval Fantasy Tavern · **Tier:** standard · **Type:** tavern + inn · **Floors:** 2
* **Fits game styles:** fantasy, medieval, rpg, realistic, anime
* **Description:** Stone-and-timber tavern: great hearth, bar, kitchen; half-timbered guest rooms upstairs; slate roof, hanging sign, ale barrels, well.
* **Size:** 26.0 × 16.3 m footprint, 13.9 m tall · 199 objects · ~88732 tris · 13 lights · 68 furniture pieces
* **Exterior doors:** F1_S3(S side), F1_E1(E side) · interior doors: 9
* **Spawn points (local m):** front (-1.0, -8.0, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (146.0, -46.2, 0.15), rotZ 0° · **Files:** `export/glb/medieval_tavern.glb`, Blender collection `BLD_medieval_tavern`

### 墨西哥彩色屋 Casa Colorida — `mexico_casa`

![day](renders/mexico_casa_front_day.png) ![night](renders/mexico_casa_front.png) ![plan](renders/mexico_casa_cut_day.png)

* **Style:** 墨西哥彩屋 / Mexican Colonial · **Tier:** standard · **Type:** house · **Floors:** 2
* **Fits game styles:** summer, cartoon, realistic, coco-like
* **Description:** 2-storey saturated red casa with blue door, roof terrace strung with papel picado bunting.
* **Size:** 14.0 × 14.5 m footprint, 9.5 m tall · 212 objects · ~74992 tris · 7 lights · 35 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side), PH_W0(W side) · interior doors: 4
* **Spawn points (local m):** front (-1.13, -7.25, 0)
* **Interactions:** cook, open, sit, sleep, use, wash, work
* **Placed on island at:** (76.0, -102.95, 0.15), rotZ 0° · **Files:** `export/glb/mexico_casa.glb`, Blender collection `BLD_mexico_casa`

### 紐奧良鐵花陽台屋 New Orleans Gallery House — `nola_iron_balcony`

![day](renders/nola_iron_balcony_front_day.png) ![night](renders/nola_iron_balcony_front.png) ![plan](renders/nola_iron_balcony_cut_day.png)

* **Style:** 紐奧良法國區 / French Quarter Creole · **Tier:** standard · **Type:** townhouse · **Floors:** 3
* **Fits game styles:** noir, jazz-age, realistic, horror
* **Description:** 3-storey Creole townhouse wrapped in lacy cast-iron galleries, tall shuttered French doors, jazz bar downstairs.
* **Size:** 15.0 × 16.0 m footprint, 10.5 m tall · 255 objects · ~105820 tris · 11 lights · 71 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side), F2_S0(S side), F2_S1(S side), F3_S0(S side), F3_S1(S side) · interior doors: 8
* **Spawn points (local m):** front (-2.4, -8.0, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, work
* **Placed on island at:** (48.5, -102.2, 0.15), rotZ 0° · **Files:** `export/glb/nola_iron_balcony.glb`, Blender collection `BLD_nola_iron_balcony`

### 北歐黑木小屋 Nordic Black Cabin — `nordic_cabin`

![day](renders/nordic_cabin_front_day.png) ![night](renders/nordic_cabin_front.png) ![plan](renders/nordic_cabin_cut_day.png)

* **Style:** 北歐小屋 / Scandinavian Cabin · **Tier:** standard · **Type:** cabin · **Floors:** 1
* **Fits game styles:** realistic, survival, horror, cozy, winter
* **Description:** Single-storey black-timber cabin with a steep slate gable, big picture window, fireplace, firewood stack.
* **Size:** 13.0 × 14.0 m footprint, 7.9 m tall · 60 objects · ~61528 tris · 4 lights · 18 furniture pieces
* **Exterior doors:** F1_S2(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -7.0, 0)
* **Interactions:** open, sit, sleep, use, work
* **Placed on island at:** (-150.5, 14.8, 0.15), rotZ 0° · **Files:** `export/glb/nordic_cabin.glb`, Blender collection `BLD_nordic_cabin`

### 幸運小鋼珠 Lucky 777 Pachinko — `pachinko_parlor`

![day](renders/pachinko_parlor_front_day.png) ![night](renders/pachinko_parlor_front.png) ![plan](renders/pachinko_parlor_cut_day.png)

* **Style:** 小鋼珠店 / Japanese Pachinko Parlor · **Tier:** standard · **Type:** game parlor · **Floors:** 2
* **Fits game styles:** japan, cyberpunk, anime, crime
* **Description:** 2-storey black parlor: rows of machines (arcade cabinets), bar upstairs, giant neon 777 sign.
* **Size:** 19.0 × 17.0 m footprint, 7.9 m tall · 161 objects · ~85356 tris · 8 lights · 58 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side) · interior doors: 6
* **Spawn points (local m):** front (-3.0, -8.5, 0)
* **Interactions:** open, play, shop, sit, use, wash
* **Placed on island at:** (142.5, -78.3, 0.15), rotZ 180° · **Files:** `export/glb/pachinko_parlor.glb`, Blender collection `BLD_pachinko_parlor`

### 月影藥水店 Moonshade Potion Shop — `potion_shop`

![day](renders/potion_shop_front_day.png) ![night](renders/potion_shop_front.png) ![plan](renders/potion_shop_cut_day.png)

* **Style:** 藥水店 / Fantasy Apothecary · **Tier:** standard · **Type:** shop · **Floors:** 2
* **Fits game styles:** fantasy, rpg, anime, cozy
* **Description:** Crooked 2-storey half-timbered apothecary: glowing potion displays outside and in, alchemist's flat upstairs.
* **Size:** 12.0 × 14.0 m footprint, 10.9 m tall · 125 objects · ~86416 tris · 6 lights · 33 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side) · interior doors: 4
* **Spawn points (local m):** front (1.4, -7.0, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, work
* **Placed on island at:** (-87.0, -155.2, 0.15), rotZ 0° · **Files:** `export/glb/potion_shop.glb`, Blender collection `BLD_potion_shop`

### 能量健身工廠 PowerHouse Gym — `power_gym`

![day](renders/power_gym_front_day.png) ![night](renders/power_gym_front.png) ![plan](renders/power_gym_cut_day.png)

* **Style:** 工業風健身房 / Industrial Fitness Hall · **Tier:** standard · **Type:** gym · **Floors:** 1
* **Fits game styles:** realistic, sports, slice-of-life, anime
* **Description:** Steel-clad sawtooth hall full of treadmills and weight benches, glass front, neon sign.
* **Size:** 21.0 × 17.0 m footprint, 6.8 m tall · 57 objects · ~67128 tris · 1 lights · 20 furniture pieces
* **Exterior doors:** F1_S4(S side) · interior doors: 0
* **Spawn points (local m):** front (-5.0, -8.5, 0)
* **Interactions:** open, use
* **Placed on island at:** (-110.5, -16.3, 0.15), rotZ 180° · **Files:** `export/glb/power_gym.glb`, Blender collection `BLD_power_gym`

### 3D列印圓頂屋 3D-Printed Dome Home — `printed_dome_home`

![day](renders/printed_dome_home_front_day.png) ![night](renders/printed_dome_home_front.png) ![plan](renders/printed_dome_home_cut_day.png)

* **Style:** 3D列印建築 / 3D-Printed Concrete Dome · **Tier:** standard · **Type:** house · **Floors:** 1
* **Fits game styles:** sci-fi, solarpunk, post-apocalyptic, mars-colony
* **Description:** Single-storey printed concrete drum with a smooth dome roof, round windows, sleeping and living niches.
* **Size:** 14.0 × 16.0 m footprint, 6.0 m tall · 55 objects · ~69932 tris · 1 lights · 3 furniture pieces
* **Exterior doors:** F1_11_0(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -7.3, 0)
* **Interactions:** cook, open, sit, sleep
* **Placed on island at:** (-188.0, -134.3, 0.15), rotZ 180° · **Files:** `export/glb/printed_dome_home.glb`, Blender collection `BLD_printed_dome_home`

### 俄羅斯木刻屋 Russian Izba — `russian_izba`

![day](renders/russian_izba_front_day.png) ![night](renders/russian_izba_front.png) ![plan](renders/russian_izba_cut_day.png)

* **Style:** 俄羅斯木屋 / Russian Log Izba · **Tier:** standard · **Type:** house · **Floors:** 1
* **Fits game styles:** fantasy, folk-tale, winter, realistic
* **Description:** Log izba with carved teal window surrounds and shutters, steep plank gable, stove and bed inside.
* **Size:** 14.0 × 13.0 m footprint, 9.0 m tall · 56 objects · ~59632 tris · 2 lights · 15 furniture pieces
* **Exterior doors:** F1_S2(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -6.5, 0)
* **Interactions:** open, sit, sleep, use, work
* **Placed on island at:** (-220.0, -103.7, 0.15), rotZ 0° · **Files:** `export/glb/russian_izba.glb`, Blender collection `BLD_russian_izba`

### 蘇格蘭石屋 Highland Stone House — `scottish_stone_house`

![day](renders/scottish_stone_house_front_day.png) ![night](renders/scottish_stone_house_front.png) ![plan](renders/scottish_stone_house_cut_day.png)

* **Style:** 蘇格蘭石屋 / Scottish Stone House · **Tier:** standard · **Type:** house · **Floors:** 2
* **Fits game styles:** europe, realistic, mystery, fantasy
* **Description:** 2-storey granite house with slate gable and twin end chimneys, deep-set windows, cosy hearth.
* **Size:** 15.0 × 13.6 m footprint, 11.3 m tall · 145 objects · ~81114 tris · 9 lights · 36 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_E1(E side) · interior doors: 7
* **Spawn points (local m):** front (-1.13, -6.8, 0)
* **Interactions:** cook, open, sit, sleep, use, wash
* **Placed on island at:** (-131.5, -103.4, 0.15), rotZ 0° · **Files:** `export/glb/scottish_stone_house.glb`, Blender collection `BLD_scottish_stone_house`

### 南洋店屋 Straits Shophouse — `sg_shophouse`

![day](renders/sg_shophouse_front_day.png) ![night](renders/sg_shophouse_front.png) ![plan](renders/sg_shophouse_cut_day.png)

* **Style:** 南洋店屋 / Peranakan Shophouse · **Tier:** standard · **Type:** shophouse · **Floors:** 3
* **Fits game styles:** realistic, southeast-asia, slice-of-life, historical
* **Description:** 3-storey pastel Peranakan shophouse: five-foot-way arcade, louvred shutters, tile gable, shop below, family above.
* **Size:** 12.0 × 19.5 m footprint, 11.9 m tall · 182 objects · ~100356 tris · 9 lights · 41 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_E2(E side) · interior doors: 6
* **Spawn points (local m):** front (-1.5, -9.5, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, work
* **Placed on island at:** (-123.0, -79.8, 0.15), rotZ 180° · **Files:** `export/glb/sg_shophouse.glb`, Blender collection `BLD_sg_shophouse`

### 上海石庫門 Shanghai Shikumen — `shanghai_shikumen`

![day](renders/shanghai_shikumen_front_day.png) ![night](renders/shanghai_shikumen_front.png) ![plan](renders/shanghai_shikumen_cut_day.png)

* **Style:** 石庫門 / Shikumen Lane House · **Tier:** standard · **Type:** townhouse · **Floors:** 3
* **Fits game styles:** historical, noir, 1930s, realistic
* **Description:** 3-storey grey-brick shikumen with a carved stone door frame, black double doors, slate gable, lane-house plan.
* **Size:** 13.0 × 18.0 m footprint, 13.7 m tall · 191 objects · ~72716 tris · 9 lights · 40 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_E2(E side) · interior doors: 6
* **Spawn points (local m):** front (-1.4, -9.0, 0)
* **Interactions:** cook, open, sit, sleep, use, work
* **Placed on island at:** (-46.5, -78.8, 0.15), rotZ 180° · **Files:** `export/glb/shanghai_shikumen.glb`, Blender collection `BLD_shanghai_shikumen`

### 太陽能社區屋 Solar Row House — `solar_row_house`

![day](renders/solar_row_house_front_day.png) ![night](renders/solar_row_house_front.png) ![plan](renders/solar_row_house_cut_day.png)

* **Style:** 太陽能住宅 / Net-Zero Row House · **Tier:** standard · **Type:** house · **Floors:** 2
* **Fits game styles:** solarpunk, modern, realistic
* **Description:** 2-storey net-zero house: whole shed roof is a solar array, heat-pump unit, light timber cladding.
* **Size:** 14.0 × 15.0 m footprint, 9.8 m tall · 120 objects · ~69308 tris · 6 lights · 26 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side) · interior doors: 4
* **Spawn points (local m):** front (-1.13, -7.5, 0)
* **Interactions:** cook, open, sit, sleep, use, wash, work
* **Placed on island at:** (-220.0, -133.3, 0.15), rotZ 180° · **Files:** `export/glb/solar_row_house.glb`, Blender collection `BLD_solar_row_house`

### 西班牙廣場拱廊屋 Spanish Plaza Arcade House — `spanish_plaza_house`

![day](renders/spanish_plaza_house_front_day.png) ![night](renders/spanish_plaza_house_front.png) ![plan](renders/spanish_plaza_house_cut_day.png)

* **Style:** 西班牙拱廊屋 / Andalusian Arcade House · **Tier:** standard · **Type:** house + shop · **Floors:** 2
* **Fits game styles:** europe, summer, western, realistic
* **Description:** 2-storey white stucco house with a ground-floor arcade, iron balconies, terracotta hip roof.
* **Size:** 17.0 × 15.0 m footprint, 9.0 m tall · 189 objects · ~100890 tris · 10 lights · 55 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side), F2_S1(S side), F2_S3(S side) · interior doors: 6
* **Spawn points (local m):** front (0.0, -7.5, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (-84.5, -102.7, 0.15), rotZ 0° · **Files:** `export/glb/spanish_plaza_house.glb`, Blender collection `BLD_spanish_plaza_house`

### 齒輪蒸汽工坊 Cog & Steam Works — `steampunk_works`

![day](renders/steampunk_works_front_day.png) ![night](renders/steampunk_works_front.png) ![plan](renders/steampunk_works_cut_day.png)

* **Style:** 蒸汽龐克工坊 / Steampunk Workshop · **Tier:** standard · **Type:** workshop · **Floors:** 3
* **Fits game styles:** steampunk, fantasy, victorian, anime, rpg
* **Description:** 3-storey copper-and-brick workshop: machine shop, drafting library, inventor's loft; giant brass gears, steam pipes, smokestacks, airship mooring mast.
* **Size:** 20.0 × 16.0 m footprint, 20.5 m tall · 226 objects · ~111744 tris · 13 lights · 42 furniture pieces
* **Exterior doors:** F1_S3(S side), F1_E1(E side) · interior doors: 8
* **Spawn points (local m):** front (1.8, -8.0, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (207.0, -46.2, 0.15), rotZ 0° · **Files:** `export/glb/steampunk_works.glb`, Blender collection `BLD_steampunk_works`

### 直播工作室 Live-Stream Studio — `stream_studio`

![day](renders/stream_studio_front_day.png) ![night](renders/stream_studio_front.png) ![plan](renders/stream_studio_cut_day.png)

* **Style:** 直播工作室 / Creator Studio Loft · **Tier:** standard · **Type:** studio · **Floors:** 3
* **Fits game styles:** modern, slice-of-life, anime, cyberpunk
* **Description:** 3-storey creator building: street-level set, editing suites and a loft flat, pink neon.
* **Size:** 14.0 × 15.0 m footprint, 10.5 m tall · 181 objects · ~84952 tris · 9 lights · 40 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side) · interior doors: 6
* **Spawn points (local m):** front (-2.0, -7.5, 0)
* **Interactions:** cook, open, sit, sleep, use, work
* **Placed on island at:** (-128.0, -133.3, 0.15), rotZ 180° · **Files:** `export/glb/stream_studio.glb`, Blender collection `BLD_stream_studio`

### 好鄰居超市 Good Neighbor Supermarket — `supermarket`

![day](renders/supermarket_front_day.png) ![night](renders/supermarket_front.png) ![plan](renders/supermarket_cut_day.png)

* **Style:** 郊區超市 / Suburban Supermarket · **Tier:** standard · **Type:** supermarket · **Floors:** 1
* **Fits game styles:** realistic, survival, zombie, slice-of-life, sims
* **Description:** Large steel-clad supermarket: aisles of double shelves, wall of drink fridges, checkout counters, carts, front parking.
* **Size:** 29.0 × 31.0 m footprint, 5.9 m tall · 148 objects · ~339280 tris · 1 lights · 107 furniture pieces
* **Exterior doors:** F1_S2(S side) · interior doors: 0
* **Spawn points (local m):** front (-6.0, -11.5, 0)
* **Interactions:** open, shop, use
* **Placed on island at:** (99.5, -27.3, 0.15), rotZ 180° · **Files:** `export/glb/supermarket.glb`, Blender collection `BLD_supermarket`

### 瑞典法倫紅屋 Swedish Falu-Red Cottage — `swedish_red_cottage`

![day](renders/swedish_red_cottage_front_day.png) ![night](renders/swedish_red_cottage_front.png) ![plan](renders/swedish_red_cottage_cut_day.png)

* **Style:** 瑞典紅木屋 / Swedish Stuga · **Tier:** standard · **Type:** house · **Floors:** 2
* **Fits game styles:** europe, cozy, realistic, anime, winter
* **Description:** 2-storey falu-red timber cottage with white corner boards and frames, slate gable, porch.
* **Size:** 15.0 × 13.6 m footprint, 10.1 m tall · 148 objects · ~81206 tris · 9 lights · 38 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_E1(E side) · interior doors: 7
* **Spawn points (local m):** front (-1.13, -6.8, 0)
* **Interactions:** cook, open, sit, sleep, use, wash
* **Placed on island at:** (206.5, -76.6, 0.15), rotZ 180° · **Files:** `export/glb/swedish_red_cottage.glb`, Blender collection `BLD_swedish_red_cottage`

### 泰式高腳屋 Thai Stilt House — `thai_stilt_house`

![day](renders/thai_stilt_house_front_day.png) ![night](renders/thai_stilt_house_front.png) ![plan](renders/thai_stilt_house_cut_day.png)

* **Style:** 泰式高腳屋 / Thai Teak Stilt House · **Tier:** standard · **Type:** house · **Floors:** 1
* **Fits game styles:** southeast-asia, realistic, adventure, cozy
* **Description:** Teak house raised 2 m on a plinth with front stair and porch, steep tile gable, open-plan living + bedroom.
* **Size:** 15.0 × 16.5 m footprint, 9.5 m tall · 61 objects · ~61236 tris · 2 lights · 16 furniture pieces
* **Exterior doors:** F1_S2(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -6.5, 0)
* **Interactions:** open, sit, sleep, use, work
* **Placed on island at:** (-99.5, -79.8, 0.15), rotZ 180° · **Files:** `export/glb/thai_stilt_house.glb`, Blender collection `BLD_thai_stilt_house`

### 圖騰長屋 Totem Plank Lodge — `totem_lodge`

![day](renders/totem_lodge_front_day.png) ![night](renders/totem_lodge_front.png) ![plan](renders/totem_lodge_cut_day.png)

* **Style:** 西北海岸長屋 / Pacific Northwest Plank House · **Tier:** standard · **Type:** lodge · **Floors:** 1
* **Fits game styles:** historical, adventure, survival, fantasy
* **Description:** Cedar plank longhouse with a low gable, painted façade band and two carved totem poles: great room with hearth and sleeping platforms.
* **Size:** 22.0 × 14.0 m footprint, 5.5 m tall · 46 objects · ~63540 tris · 2 lights · 10 furniture pieces
* **Exterior doors:** F1_S4(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -7.0, 0)
* **Interactions:** open, sit, sleep, use
* **Placed on island at:** (-108.0, -184.8, 0.15), rotZ 180° · **Files:** `export/glb/totem_lodge.glb`, Blender collection `BLD_totem_lodge`

### 老橡樹樹屋 Old Oak Treehouse — `treehouse_oak`

![day](renders/treehouse_oak_front_day.png) ![night](renders/treehouse_oak_front.png) ![plan](renders/treehouse_oak_cut_day.png)

* **Style:** 童話樹屋 / Storybook Treehouse · **Tier:** standard · **Type:** treehouse · **Floors:** 2
* **Fits game styles:** cozy, ghibli, adventure, cartoon, fantasy
* **Description:** Giant oak with a wrap deck at 4.5 m reached by a timber stair, a gabled cabin (bed, desk, lantern) and a rope ladder to a crow's-nest lookout.
* **Size:** 16.2 × 19.0 m footprint, 17.9 m tall · 73 objects · ~70380 tris · 7 lights · 3 furniture pieces
* **Exterior doors:** Cabin_S0(S side) · interior doors: 0
* **Spawn points (local m):** front (2.35, -6.1, 0)
* **Interactions:** climb, open, play, sleep, work
* **Placed on island at:** (189.0, -40.2, 0.15), rotZ 0° · **Files:** `export/glb/treehouse_oak.glb`, Blender collection `BLD_treehouse_oak`

### 皇冠都鐸酒館 The Crown Tudor Inn — `tudor_inn`

![day](renders/tudor_inn_front_day.png) ![night](renders/tudor_inn_front.png) ![plan](renders/tudor_inn_cut_day.png)

* **Style:** 英式都鐸 / English Tudor · **Tier:** standard · **Type:** pub + inn · **Floors:** 2
* **Fits game styles:** medieval, fantasy, rpg-village, realistic, europe
* **Description:** Stone ground-floor pub with bar and booths, half-timbered upper floor of guest rooms, steep tile gable, lanterns, hanging sign.
* **Size:** 17.0 × 16.0 m footprint, 13.5 m tall · 164 objects · ~67900 tris · 10 lights · 49 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side) · interior doors: 6
* **Spawn points (local m):** front (-1.13, -8.0, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (-182.5, 15.8, 0.15), rotZ 0° · **Files:** `export/glb/tudor_inn.glb`, Blender collection `BLD_tudor_inn`

### 台式透天厝 Taiwanese Townhouse — `tw_townhouse`

![day](renders/tw_townhouse_front_day.png) ![night](renders/tw_townhouse_front.png) ![plan](renders/tw_townhouse_cut_day.png)

* **Style:** 台式透天厝 / Taiwanese Townhouse · **Tier:** standard · **Type:** house · **Floors:** 4
* **Fits game styles:** realistic, slice-of-life, taiwan, horror
* **Description:** Narrow 4-storey mosaic townhouse: G/F garage with roller door, family floors above, roof terrace with water tank.
* **Size:** 10.0 × 19.0 m footprint, 15.9 m tall · 279 objects · ~100456 tris · 13 lights · 62 furniture pieces
* **Exterior doors:** F1_S0(S side), F1_S1(S side), F1_E2(E side), F2_S1(S side), F4_S1(S side), PH_W0(W side) · interior doors: 8
* **Spawn points (local m):** front (1.6, -9.5, 0)
* **Interactions:** cook, open, sit, sleep, use, work
* **Placed on island at:** (-14.0, 17.3, 0.15), rotZ 0° · **Files:** `export/glb/tw_townhouse.glb`, Blender collection `BLD_tw_townhouse`

### 維京長屋 Viking Longhouse — `viking_longhouse`

![day](renders/viking_longhouse_front_day.png) ![night](renders/viking_longhouse_front.png) ![plan](renders/viking_longhouse_cut_day.png)

* **Style:** 維京長屋 / Norse Longhouse · **Tier:** standard · **Type:** longhouse · **Floors:** 1
* **Fits game styles:** viking, fantasy, survival, rpg, medieval
* **Description:** Long single-storey timber hall with a steep shingled roof and carved dragon-head gable ends: feast hall, hearth, sleeping benches.
* **Size:** 25.0 × 13.0 m footprint, 8.9 m tall · 58 objects · ~56876 tris · 5 lights · 16 furniture pieces
* **Exterior doors:** F1_S3(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -6.5, 0)
* **Interactions:** open, sit, sleep, use
* **Placed on island at:** (173.5, -155.7, 0.15), rotZ 0° · **Files:** `export/glb/viking_longhouse.glb`, Blender collection `BLD_viking_longhouse`

### 紅磚倉庫Loft Red-Brick Warehouse Lofts — `warehouse_loft`

![day](renders/warehouse_loft_front_day.png) ![night](renders/warehouse_loft_front.png) ![plan](renders/warehouse_loft_cut_day.png)

* **Style:** 工業倉庫改建 / Industrial Warehouse Loft · **Tier:** standard · **Type:** loft + workshop · **Floors:** 2
* **Fits game styles:** realistic, industrial, crime, cyberpunk, post-apocalyptic
* **Description:** Converted brick warehouse: G/F workshop and garage bay with roller door, two double-height studio lofts above, sawtooth glazed roof.
* **Size:** 25.0 × 19.0 m footprint, 10.8 m tall · 167 objects · ~100704 tris · 10 lights · 42 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_S3(S side), F1_E1(E side) · interior doors: 8
* **Spawn points (local m):** front (-2.4, -9.5, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (-58.5, -44.7, 0.15), rotZ 0° · **Files:** `export/glb/warehouse_loft.glb`, Blender collection `BLD_warehouse_loft`

### 龍門客棧 Dragon Gate Inn — `wuxia_inn`

![day](renders/wuxia_inn_front_day.png) ![night](renders/wuxia_inn_front.png) ![plan](renders/wuxia_inn_cut_day.png)

* **Style:** 武俠客棧 / Wuxia Desert Inn · **Tier:** standard · **Type:** inn · **Floors:** 2
* **Fits game styles:** wuxia, historical, fantasy, action
* **Description:** 2-storey timber-and-plaster inn: tavern hall of tables and a bar, guest rooms above, curled slate roof, banner pole.
* **Size:** 19.0 × 16.0 m footprint, 10.8 m tall · 189 objects · ~77078 tris · 12 lights · 58 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side) · interior doors: 8
* **Spawn points (local m):** front (0.0, -8.0, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, work
* **Placed on island at:** (150.5, -154.2, 0.15), rotZ 0° · **Files:** `export/glb/wuxia_inn.glb`, Blender collection `BLD_wuxia_inn`

### 美式殖民宅 New England Colonial — `american_colonial`

![day](renders/american_colonial_front_day.png) ![night](renders/american_colonial_front.png) ![plan](renders/american_colonial_cut_day.png)

* **Style:** 美式殖民 / American Colonial · **Tier:** upscale · **Type:** house · **Floors:** 2
* **Fits game styles:** realistic, horror, sitcom, americana
* **Description:** Symmetric 2-storey white clapboard house: columned portico, black shutters, slate gable, twin chimneys, picket fence.
* **Size:** 19.0 × 18.0 m footprint, 11.0 m tall · 175 objects · ~74524 tris · 10 lights · 48 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side) · interior doors: 8
* **Spawn points (local m):** front (0.0, -7.5, 0)
* **Interactions:** cook, open, sit, sleep, use, wash, work
* **Placed on island at:** (-65.5, -99.7, 0.15), rotZ 0° · **Files:** `export/glb/american_colonial.glb`, Blender collection `BLD_american_colonial`

### 包浩斯白宅 Bauhaus White House — `bauhaus_house`

![day](renders/bauhaus_house_front_day.png) ![night](renders/bauhaus_house_front.png) ![plan](renders/bauhaus_house_cut_day.png)

* **Style:** 包浩斯 / Bauhaus Modernism · **Tier:** upscale · **Type:** house · **Floors:** 2
* **Fits game styles:** realistic, modern, architectural, anime
* **Description:** Crisp white cubic 2-storey house: ribbon windows, flat roof terrace, cantilever entrance canopy, red accent panel.
* **Size:** 17.8 × 15.6 m footprint, 9.5 m tall · 196 objects · ~78980 tris · 11 lights · 55 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_E1(E side), PH_W0(W side) · interior doors: 8
* **Spawn points (local m):** front (-2.0, -7.5, 0)
* **Interactions:** cook, open, sit, sleep, use, wash, work
* **Placed on island at:** (-148.5, -46.7, 0.15), rotZ 0° · **Files:** `export/glb/bauhaus_house.glb`, Blender collection `BLD_bauhaus_house`

### 北京四合院門樓 Beijing Siheyuan Gatehouse — `beijing_siheyuan_gate`

![day](renders/beijing_siheyuan_gate_front_day.png) ![night](renders/beijing_siheyuan_gate_front.png) ![plan](renders/beijing_siheyuan_gate_cut_day.png)

* **Style:** 北京四合院 / Beijing Siheyuan · **Tier:** upscale · **Type:** house · **Floors:** 1
* **Fits game styles:** historical, wuxia, realistic, kdrama
* **Description:** Grey-brick courtyard house front range: red lacquered gate, lanterns, stone lions, slate gable, living rooms behind.
* **Size:** 19.0 × 16.0 m footprint, 6.6 m tall · 79 objects · ~79284 tris · 5 lights · 27 furniture pieces
* **Exterior doors:** F1_S2(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -7.0, 0)
* **Interactions:** open, sit, sleep, use, work
* **Placed on island at:** (-29.5, -78.8, 0.15), rotZ 180° · **Files:** `export/glb/beijing_siheyuan_gate.glb`, Blender collection `BLD_beijing_siheyuan_gate`

### 貨櫃森林咖啡館 Container Grove Café — `cafe_container`

![day](renders/cafe_container_front_day.png) ![night](renders/cafe_container_front.png) ![plan](renders/cafe_container_cut_day.png)

* **Style:** 工業貨櫃現代 / Industrial Container Modern · **Tier:** upscale · **Type:** café / commercial · **Floors:** 2
* **Fits game styles:** realistic, modern, slice-of-life, anime
* **Description:** Raised concrete podium, timber post-and-beam café with full glazing, 20ft black container kitchen, outdoor stair to a planted terrace, 40ft yellow container lounge with sliding glass wall, timber canopy roof.
* **Size:** 23.1 × 14.8 m footprint, 9.7 m tall · 172 objects · ~109424 tris · 15 lights · 55 furniture pieces
* **Exterior doors:** Cafe_S1(S side), Kitchen_N0(N side), Lounge_S1(S side) · interior doors: 0
* **Spawn points (local m):** front_steps (-4.3, -7.06, 0)
* **Interactions:** cook, open, shop, sit, use
* **Placed on island at:** (85.0, 15.6, 0.15), rotZ 0° · **Files:** `export/glb/cafe_container.glb`, Blender collection `BLD_cafe_container`

### 加拿大木屋旅館 Canadian Timber Lodge — `canadian_lodge`

![day](renders/canadian_lodge_front_day.png) ![night](renders/canadian_lodge_front.png) ![plan](renders/canadian_lodge_cut_day.png)

* **Style:** 加拿大木屋 / Canadian Log Lodge · **Tier:** upscale · **Type:** lodge · **Floors:** 2
* **Fits game styles:** winter, cozy, survival, realistic
* **Description:** 2-storey log lodge: lobby with stone fireplace and restaurant, guest rooms above, deep timber gable.
* **Size:** 21.0 × 16.0 m footprint, 11.4 m tall · 175 objects · ~86080 tris · 11 lights · 55 furniture pieces
* **Exterior doors:** F1_S3(S side), F1_E1(E side) · interior doors: 9
* **Spawn points (local m):** front (-3.0, -8.0, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (107.5, -102.2, 0.15), rotZ 0° · **Files:** `export/glb/canadian_lodge.glb`, Blender collection `BLD_canadian_lodge`

### 阿姆斯特丹運河屋 Amsterdam Canal House — `dutch_canal_house`

![day](renders/dutch_canal_house_front_day.png) ![night](renders/dutch_canal_house_front.png) ![plan](renders/dutch_canal_house_cut_day.png)

* **Style:** 荷蘭運河屋 / Dutch Canal House · **Tier:** upscale · **Type:** townhouse · **Floors:** 4
* **Fits game styles:** europe, realistic, romance, anime
* **Description:** Tall narrow 4-storey brick canal house with a steep stepped gable, white sash windows and a hoist beam.
* **Size:** 10.0 × 17.0 m footprint, 17.6 m tall · 247 objects · ~89312 tris · 12 lights · 53 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_E2(E side) · interior doors: 8
* **Spawn points (local m):** front (-1.6, -8.5, 0)
* **Interactions:** cook, open, sit, sleep, use, work
* **Placed on island at:** (-14.0, -78.3, 0.15), rotZ 180° · **Files:** `export/glb/dutch_canal_house.glb`, Blender collection `BLD_dutch_canal_house`

### 綠廊生態公寓 Green Terrace Eco Apartments — `eco_apartments`

![day](renders/eco_apartments_front_day.png) ![night](renders/eco_apartments_front.png) ![plan](renders/eco_apartments_cut_day.png)

* **Style:** 綠建築生態宅 / Biophilic Eco Housing · **Tier:** upscale · **Type:** apartment · **Floors:** 5
* **Fits game styles:** solarpunk, realistic, modern, anime, utopia
* **Description:** 5-storey timber-clad eco block: every flat has a planted balcony with trailing greenery, roof garden with trees and solar.
* **Size:** 19.0 × 17.0 m footprint, 19.4 m tall · 571 objects · ~169412 tris · 25 lights · 171 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E2(E side), F2_S1(S side), F2_S4(S side), F3_S1(S side), F3_S4(S side), F4_S1(S side), F4_S4(S side), F5_S1(S side), F5_S4(S side), PH_W0(W side) · interior doors: 19
* **Spawn points (local m):** front (-3.0, -8.5, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (48.5, -45.7, 0.15), rotZ 0° · **Files:** `export/glb/eco_apartments.glb`, Blender collection `BLD_eco_apartments`

### 電競競技館 Esports Arena — `esports_arena`

![day](renders/esports_arena_front_day.png) ![night](renders/esports_arena_front.png) ![plan](renders/esports_arena_cut_day.png)

* **Style:** 電競館 / Esports Venue · **Tier:** upscale · **Type:** arena · **Floors:** 2
* **Fits game styles:** cyberpunk, modern, anime, sports
* **Description:** 2-storey black venue: tall ground floor of gaming PC rows and a stage, lounge & bar upstairs, LED facade.
* **Size:** 23.0 × 19.0 m footprint, 9.3 m tall · 216 objects · ~102522 tris · 9 lights · 96 furniture pieces
* **Exterior doors:** F1_S4(S side), F1_E2(E side) · interior doors: 7
* **Spawn points (local m):** front (2.0, -9.5, 0)
* **Interactions:** open, shop, sit, use, wash, work
* **Placed on island at:** (-147.5, -135.3, 0.15), rotZ 180° · **Files:** `export/glb/esports_arena.glb`, Blender collection `BLD_esports_arena`

### 黑玻璃創意辦公 Obsidian Cube Offices — `glass_cube_office`

![day](renders/glass_cube_office_front_day.png) ![night](renders/glass_cube_office_front.png) ![plan](renders/glass_cube_office_cut_day.png)

* **Style:** 當代玻璃辦公 / Contemporary Glass Office · **Tier:** upscale · **Type:** office · **Floors:** 4
* **Fits game styles:** modern, corporate, cyberpunk, realistic, thriller
* **Description:** 4-storey dark glass cube: lobby + café, open-plan offices and meeting rooms, roof terrace with solar canopy.
* **Size:** 21.0 × 23.0 m footprint, 17.7 m tall · 529 objects · ~176888 tris · 21 lights · 269 furniture pieces
* **Exterior doors:** F1_S3(S side), F1_E2(E side), PH_W0(W side) · interior doors: 16
* **Spawn points (local m):** front (-3.6, -10.5, 0)
* **Interactions:** open, shop, sit, use, wash, work
* **Placed on island at:** (-82.5, -41.7, 0.15), rotZ 0° · **Files:** `export/glb/glass_cube_office.glb`, Blender collection `BLD_glass_cube_office`

### 綠屋頂住宅 Living-Roof House — `green_roof_house`

![day](renders/green_roof_house_front_day.png) ![night](renders/green_roof_house_front.png) ![plan](renders/green_roof_house_cut_day.png)

* **Style:** 綠屋頂 / Eco Green-Roof House · **Tier:** upscale · **Type:** house · **Floors:** 2
* **Fits game styles:** solarpunk, modern, cozy, realistic
* **Description:** Timber 2-storey house with a sedum-planted shed roof, big south glazing and planters.
* **Size:** 17.0 × 15.0 m footprint, 8.4 m tall · 159 objects · ~74200 tris · 9 lights · 43 furniture pieces
* **Exterior doors:** F1_S3(S side), F1_E1(E side) · interior doors: 7
* **Spawn points (local m):** front (-1.13, -7.5, 0)
* **Interactions:** cook, open, sit, sleep, use, wash, work
* **Placed on island at:** (211.5, -102.7, 0.15), rotZ 0° · **Files:** `export/glb/green_roof_house.glb`, Blender collection `BLD_green_roof_house`

### 玻璃溫室咖啡 Glasshouse Garden Café — `greenhouse_cafe`

![day](renders/greenhouse_cafe_front_day.png) ![night](renders/greenhouse_cafe_front.png) ![plan](renders/greenhouse_cafe_cut_day.png)

* **Style:** 玻璃溫室 / Victorian Glasshouse · **Tier:** upscale · **Type:** café · **Floors:** 1
* **Fits game styles:** cozy, ghibli, romance, solarpunk, realistic
* **Description:** Single-storey white-framed glasshouse with a glass gable roof: café counter, tables among potted palms and ferns.
* **Size:** 17.0 × 15.0 m footprint, 6.1 m tall · 93 objects · ~86260 tris · 1 lights · 68 furniture pieces
* **Exterior doors:** F1_S2(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -7.0, 0)
* **Interactions:** open, shop, sit, use
* **Placed on island at:** (-22.5, -46.2, 0.15), rotZ 0° · **Files:** `export/glb/greenhouse_cafe.glb`, Blender collection `BLD_greenhouse_cafe`

### 韓屋咖啡廳 Hanok Café — `hanok_cafe`

![day](renders/hanok_cafe_front_day.png) ![night](renders/hanok_cafe_front.png) ![plan](renders/hanok_cafe_cut_day.png)

* **Style:** 韓屋咖啡 / Korean Hanok Café · **Tier:** upscale · **Type:** café · **Floors:** 1
* **Fits game styles:** kdrama, cozy, realistic, anime
* **Description:** Single-storey hanok converted to a café: curved tile roof, timber posts, café tables inside.
* **Size:** 17.0 × 14.5 m footprint, 6.9 m tall · 110 objects · ~53906 tris · 1 lights · 56 furniture pieces
* **Exterior doors:** F1_S2(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -6.5, 0)
* **Interactions:** open, shop, sit, use
* **Placed on island at:** (123.5, -77.8, 0.15), rotZ 180° · **Files:** `export/glb/hanok_cafe.glb`, Blender collection `BLD_hanok_cafe`

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

### 月見溫泉旅館 Tsukimi Hot-Spring Ryokan — `jp_ryokan`

![day](renders/jp_ryokan_front_day.png) ![night](renders/jp_ryokan_front.png) ![plan](renders/jp_ryokan_cut_day.png)

* **Style:** 溫泉旅館 / Japanese Ryokan · **Tier:** upscale · **Type:** ryokan · **Floors:** 2
* **Fits game styles:** anime, japan, cozy, romance, realistic
* **Description:** 2-storey ryokan: lobby and indoor hot-spring bath, tatami guest rooms upstairs, lanterns, curled slate roof.
* **Size:** 21.0 × 17.0 m footprint, 10.1 m tall · 238 objects · ~88392 tris · 18 lights · 42 furniture pieces
* **Exterior doors:** F1_S4(S side), F1_E2(E side) · interior doors: 9
* **Spawn points (local m):** front (-4.0, -8.5, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (-188.5, -78.3, 0.15), rotZ 180° · **Files:** `export/glb/jp_ryokan.glb`, Blender collection `BLD_jp_ryokan`

### 侘寂茶室 Wabi Tea Room — `jp_tea_room`

![day](renders/jp_tea_room_front_day.png) ![night](renders/jp_tea_room_front.png) ![plan](renders/jp_tea_room_cut_day.png)

* **Style:** 日式茶室 / Japanese Tea House · **Tier:** upscale · **Type:** tea house · **Floors:** 1
* **Fits game styles:** japan, zen, anime, realistic
* **Description:** Tiny single-storey tea room: tatami, low table, slate hip roof, stepping-stone garden with bamboo fence.
* **Size:** 12.0 × 15.0 m footprint, 5.7 m tall · 56 objects · ~53482 tris · 1 lights · 5 furniture pieces
* **Exterior doors:** F1_S2(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -6.0, 0)
* **Interactions:** open, sit, use
* **Placed on island at:** (109.0, -78.8, 0.15), rotZ 180° · **Files:** `export/glb/jp_tea_room.glb`, Blender collection `BLD_jp_tea_room`

### 韓式韓屋 Korean Hanok — `korean_hanok`

![day](renders/korean_hanok_front_day.png) ![night](renders/korean_hanok_front.png) ![plan](renders/korean_hanok_cut_day.png)

* **Style:** 韓屋 / Korean Hanok · **Tier:** upscale · **Type:** house · **Floors:** 1
* **Fits game styles:** historical, kdrama, realistic, anime
* **Description:** Single-storey hanok on a stone plinth: timber posts, raised wooden maru veranda, paper sliding doors, curved tiled hip roof.
* **Size:** 20.4 × 16.5 m footprint, 7.4 m tall · 97 objects · ~45162 tris · 3 lights · 21 furniture pieces
* **Exterior doors:** F1_S2(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -7.0, 0)
* **Interactions:** cook, open, sit, sleep, use, work
* **Placed on island at:** (138.5, 16.8, 0.15), rotZ 0° · **Files:** `export/glb/korean_hanok.glb`, Blender collection `BLD_korean_hanok`

### 地中海白屋 Mediterranean White House — `med_villa`

![day](renders/med_villa_front_day.png) ![night](renders/med_villa_front.png) ![plan](renders/med_villa_cut_day.png)

* **Style:** 地中海風 / Mediterranean · **Tier:** upscale · **Type:** house · **Floors:** 2
* **Fits game styles:** realistic, summer, romance, anime
* **Description:** Whitewashed 2-storey house with blue door and shutters, terracotta hip roof, balcony, bougainvillea boxes.
* **Size:** 17.0 × 15.0 m footprint, 9.0 m tall · 191 objects · ~76830 tris · 10 lights · 50 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side), F2_S1(S side), F2_S3(S side) · interior doors: 8
* **Spawn points (local m):** front (-1.13, -7.5, 0)
* **Interactions:** cook, open, sit, sleep, use, wash, work
* **Placed on island at:** (-134.5, 15.3, 0.15), rotZ 0° · **Files:** `export/glb/med_villa.glb`, Blender collection `BLD_med_villa`

### 中世紀現代宅 Palm Springs Mid-Century House — `midcentury_house`

![day](renders/midcentury_house_front_day.png) ![night](renders/midcentury_house_front.png) ![plan](renders/midcentury_house_cut_day.png)

* **Style:** 中世紀現代 / Mid-Century Modern · **Tier:** upscale · **Type:** house · **Floors:** 1
* **Fits game styles:** retro, realistic, mad-men, modern, gta-like
* **Description:** Low single-storey timber house with floor-to-ceiling glass, butterfly-flat shed roof with deep eaves, stone chimney, carport.
* **Size:** 30.0 × 15.0 m footprint, 4.7 m tall · 70 objects · ~72360 tris · 3 lights · 24 furniture pieces
* **Exterior doors:** F1_S3(S side) · interior doors: 0
* **Spawn points (local m):** front (-2.0, -7.5, 0)
* **Interactions:** cook, open, sit, sleep, use, work
* **Placed on island at:** (-124.0, -46.7, 0.15), rotZ 0° · **Files:** `export/glb/midcentury_house.glb`, Blender collection `BLD_midcentury_house`

### 極簡白盒屋 Minimal White Box — `minimal_white_box`

![day](renders/minimal_white_box_front_day.png) ![night](renders/minimal_white_box_front.png) ![plan](renders/minimal_white_box_cut_day.png)

* **Style:** 極簡主義 / Minimalist Modern · **Tier:** upscale · **Type:** house · **Floors:** 2
* **Fits game styles:** modern, realistic, architectural, anime
* **Description:** Pure white 2-storey box with a few large picture windows, flush door, roof terrace.
* **Size:** 16.8 × 15.4 m footprint, 9.5 m tall · 161 objects · ~69350 tris · 8 lights · 39 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_E1(E side), PH_W0(W side) · interior doors: 5
* **Spawn points (local m):** front (-1.13, -7.25, 0)
* **Interactions:** cook, open, sit, sleep, use, wash, work
* **Placed on island at:** (168.5, -102.95, 0.15), rotZ 0° · **Files:** `export/glb/minimal_white_box.glb`, Blender collection `BLD_minimal_white_box`

### 閩南三合院 Minnan Courtyard House — `minnan_sanheyuan`

![day](renders/minnan_sanheyuan_front_day.png) ![night](renders/minnan_sanheyuan_front.png) ![plan](renders/minnan_sanheyuan_cut_day.png)

* **Style:** 閩南三合院 / Minnan Sanheyuan · **Tier:** upscale · **Type:** house · **Floors:** 1
* **Fits game styles:** historical, taiwan, wuxia, rpg-village, realistic
* **Description:** Red-brick U-shaped courtyard house: ancestral hall in the centre, bedrooms in two wings, curled tile roofs, cobbled courtyard.
* **Size:** 23.0 × 19.5 m footprint, 6.2 m tall · 118 objects · ~63486 tris · 5 lights · 31 furniture pieces
* **Exterior doors:** F1_S6(S side), Wing-1_E0(E side), Wing1_W0(W side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -6.5, 0)
* **Interactions:** cook, open, sit, sleep, use, work
* **Placed on island at:** (-227.5, -82.8, 0.15), rotZ 180° · **Files:** `export/glb/minnan_sanheyuan.glb`, Blender collection `BLD_minnan_sanheyuan`

### 摩洛哥庭園宅 Moroccan Riad House — `moroccan_riad`

![day](renders/moroccan_riad_front_day.png) ![night](renders/moroccan_riad_front.png) ![plan](renders/moroccan_riad_cut_day.png)

* **Style:** 摩洛哥風 / Moroccan Riad · **Tier:** upscale · **Type:** guesthouse · **Floors:** 2
* **Fits game styles:** fantasy, desert, realistic, adventure
* **Description:** Ochre 2-storey riad: carved arch door, mashrabiya grilles, tiled lounge, guest rooms, roof terrace with lanterns.
* **Size:** 17.0 × 17.0 m footprint, 9.5 m tall · 203 objects · ~87348 tris · 15 lights · 51 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E2(E side), PH_W0(W side) · interior doors: 8
* **Spawn points (local m):** front (-2.0, -8.5, 0)
* **Interactions:** cook, open, sit, sleep, use, wash, work
* **Placed on island at:** (105.5, 16.3, 0.15), rotZ 0° · **Files:** `export/glb/moroccan_riad.glb`, Blender collection `BLD_moroccan_riad`

### 紐約褐石排屋 Brooklyn Brownstone — `nyc_brownstone`

![day](renders/nyc_brownstone_front_day.png) ![night](renders/nyc_brownstone_front.png) ![plan](renders/nyc_brownstone_cut_day.png)

* **Style:** 紐約褐石屋 / New York Brownstone · **Tier:** upscale · **Type:** townhouse · **Floors:** 4
* **Fits game styles:** realistic, noir, sitcom, crime, urban
* **Description:** Narrow 4-storey brownstone with raised stoop, double timber door, cornice, sash windows, flat roof with water tank.
* **Size:** 13.0 × 19.5 m footprint, 16.2 m tall · 254 objects · ~93400 tris · 14 lights · 54 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_E2(E side) · interior doors: 8
* **Spawn points (local m):** front (-1.6, -9.0, 0)
* **Interactions:** cook, open, sit, sleep, use, work
* **Placed on island at:** (-212.5, 18.3, 0.15), rotZ 0° · **Files:** `export/glb/nyc_brownstone.glb`, Blender collection `BLD_nyc_brownstone`

### 巴黎奧斯曼公寓 Parisian Haussmann Apartment — `paris_haussmann`

![day](renders/paris_haussmann_front_day.png) ![night](renders/paris_haussmann_front.png) ![plan](renders/paris_haussmann_cut_day.png)

* **Style:** 巴黎奧斯曼式 / Haussmann Parisian · **Tier:** upscale · **Type:** apartment · **Floors:** 4
* **Fits game styles:** realistic, romance, anime, noir, europe
* **Description:** Cream stone 4-storey block: corner café with terrace, wrought-iron balconies, mansard slate roof with dormers, cornice.
* **Size:** 19.0 × 17.5 m footprint, 17.6 m tall · 412 objects · ~136764 tris · 19 lights · 121 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side), F2_S1(S side), F2_S2(S side), F3_S1(S side), F3_S2(S side), F4_S1(S side), F4_S2(S side) · interior doors: 15
* **Spawn points (local m):** front (-4.0, -8.0, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (-229.5, 17.3, 0.15), rotZ 0° · **Files:** `export/glb/paris_haussmann.glb`, Blender collection `BLD_paris_haussmann`

### 未來膠囊陽台公寓 Pod Balcony Apartments — `pod_apartments`

![day](renders/pod_apartments_front_day.png) ![night](renders/pod_apartments_front.png) ![plan](renders/pod_apartments_cut_day.png)

* **Style:** 未來公寓 / Futurist Pod Housing · **Tier:** upscale · **Type:** apartment · **Floors:** 6
* **Fits game styles:** sci-fi, modern, solarpunk, anime
* **Description:** 6-storey white panel block with glass pod balconies on every flat, solar roof terrace.
* **Size:** 17.0 × 16.0 m footprint, 21.3 m tall · 603 objects · ~135164 tris · 29 lights · 152 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side), F2_S1(S side), F2_S3(S side), F3_S1(S side), F3_S3(S side), F4_S1(S side), F4_S3(S side), F5_S1(S side), F5_S3(S side), F6_S1(S side), F6_S3(S side), PH_W0(W side) · interior doors: 22
* **Spawn points (local m):** front (-3.0, -8.0, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (105.5, -133.8, 0.15), rotZ 180° · **Files:** `export/glb/pod_apartments.glb`, Blender collection `BLD_pod_apartments`

### 日光艙屋 Solar Pod Home — `pod_solar`

![day](renders/pod_solar_front_day.png) ![night](renders/pod_solar_front.png) ![plan](renders/pod_solar_cut_day.png)

* **Style:** 科幻離網艙屋 / Sci-Fi Off-Grid Module · **Tier:** upscale · **Type:** house · **Floors:** 2
* **Fits game styles:** sci-fi, solarpunk, post-apocalyptic, anime, realistic
* **Description:** Raised copper module house: pipe-frame base + deck, lower glazed kitchen/lab pod, interior stair to an upper sleeping module with wrap balcony, roof hatch, two large tilting solar panels, antenna mast, hydroponic planters.
* **Size:** 18.0 × 16.0 m footprint, 11.4 m tall · 117 objects · ~75272 tris · 5 lights · 24 furniture pieces
* **Exterior doors:** Lo_S1(S side), Up_S1(S side) · interior doors: 0
* **Spawn points (local m):** deck_stair (1.2, -6.32, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, work
* **Placed on island at:** (56.0, -17.0, 0.15), rotZ 180° · **Files:** `export/glb/pod_solar.glb`, Blender collection `BLD_pod_solar`

### 拉賈斯坦哈維利 Rajasthani Haveli — `rajasthan_haveli`

![day](renders/rajasthan_haveli_front_day.png) ![night](renders/rajasthan_haveli_front.png) ![plan](renders/rajasthan_haveli_cut_day.png)

* **Style:** 印度哈維利 / Indian Haveli · **Tier:** upscale · **Type:** mansion · **Floors:** 3
* **Fits game styles:** historical, fantasy, adventure, realistic
* **Description:** 3-storey sandstone haveli: carved jharokha screens, courtyard-style rooms, roof terrace with domed chhatri pavilions.
* **Size:** 17.0 × 17.0 m footprint, 12.9 m tall · 287 objects · ~88456 tris · 16 lights · 74 furniture pieces
* **Exterior doors:** F1_S3(S side), F1_E2(E side), PH_W0(W side) · interior doors: 12
* **Spawn points (local m):** front (-2.0, -8.5, 0)
* **Interactions:** cook, open, sit, sleep, use, wash, work
* **Placed on island at:** (-62.5, -78.3, 0.15), rotZ 180° · **Files:** `export/glb/rajasthan_haveli.glb`, Blender collection `BLD_rajasthan_haveli`

### 聖托里尼藍頂屋 Santorini Blue-Dome House — `santorini_house`

![day](renders/santorini_house_front_day.png) ![night](renders/santorini_house_front.png) ![plan](renders/santorini_house_cut_day.png)

* **Style:** 希臘聖托里尼 / Cycladic Greek · **Tier:** upscale · **Type:** house · **Floors:** 2
* **Fits game styles:** summer, romance, realistic, anime
* **Description:** Whitewashed cubic 2-storey house with a blue dome, blue doors and shutters, roof terrace edge.
* **Size:** 14.0 × 14.0 m footprint, 10.7 m tall · 143 objects · ~78880 tris · 8 lights · 36 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_E1(E side) · interior doors: 6
* **Spawn points (local m):** front (-1.13, -7.0, 0)
* **Interactions:** cook, open, sit, sleep, use, wash, work
* **Placed on island at:** (-206.0, -103.2, 0.15), rotZ 0° · **Files:** `export/glb/santorini_house.glb`, Blender collection `BLD_santorini_house`

### 舊金山彩繪淑女屋 San Francisco Painted Lady — `sf_painted_lady`

![day](renders/sf_painted_lady_front_day.png) ![night](renders/sf_painted_lady_front.png) ![plan](renders/sf_painted_lady_cut_day.png)

* **Style:** 維多利亞彩屋 / Victorian Painted Lady · **Tier:** upscale · **Type:** townhouse · **Floors:** 3
* **Fits game styles:** realistic, sitcom, romance, americana
* **Description:** 3-storey Victorian with teal clapboard, white trim, bay window, steep front gable, stoop.
* **Size:** 10.6 × 17.0 m footprint, 15.0 m tall · 187 objects · ~90820 tris · 9 lights · 36 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_E2(E side) · interior doors: 6
* **Spawn points (local m):** front (1.6, -8.5, 0)
* **Interactions:** cook, open, sit, sleep, use, wash, work
* **Placed on island at:** (62.3, -101.7, 0.15), rotZ 0° · **Files:** `export/glb/sf_painted_lady.glb`, Blender collection `BLD_sf_painted_lady`

### 西班牙莊園 Spanish Hacienda — `spanish_hacienda`

![day](renders/spanish_hacienda_front_day.png) ![night](renders/spanish_hacienda_front.png) ![plan](renders/spanish_hacienda_cut_day.png)

* **Style:** 西班牙殖民風 / Spanish Colonial · **Tier:** upscale · **Type:** house · **Floors:** 1
* **Fits game styles:** western, realistic, telenovela, rpg-village
* **Description:** Long single-storey stucco ranch house with arched veranda, terracotta roof, living/dining/kitchen/bedrooms.
* **Size:** 21.0 × 18.5 m footprint, 5.6 m tall · 93 objects · ~67922 tris · 6 lights · 30 furniture pieces
* **Exterior doors:** F1_S3(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -8.0, 0)
* **Interactions:** cook, open, sit, sleep, use, work
* **Placed on island at:** (-114.5, 18.3, 0.15), rotZ 0° · **Files:** `export/glb/spanish_hacienda.glb`, Blender collection `BLD_spanish_hacienda`

### 新創科技總部 Startup HQ — `startup_hq`

![day](renders/startup_hq_front_day.png) ![night](renders/startup_hq_front.png) ![plan](renders/startup_hq_cut_day.png)

* **Style:** 科技新創 / Tech Startup Office · **Tier:** upscale · **Type:** office · **Floors:** 3
* **Fits game styles:** modern, corporate, slice-of-life, cyberpunk
* **Description:** 3-storey dark-glass office: lobby café, open-plan desks, meeting rooms, server room, roof terrace.
* **Size:** 21.0 × 19.0 m footprint, 14.1 m tall · 372 objects · ~116308 tris · 16 lights · 163 furniture pieces
* **Exterior doors:** F1_S3(S side), F1_E2(E side), PH_W0(W side) · interior doors: 12
* **Spawn points (local m):** front (-3.6, -9.5, 0)
* **Interactions:** open, shop, sit, use, wash, work
* **Placed on island at:** (-170.5, -135.3, 0.15), rotZ 180° · **Files:** `export/glb/startup_hq.glb`, Blender collection `BLD_startup_hq`

### 阿爾卑斯木屋 Alpine Swiss Chalet — `swiss_chalet`

![day](renders/swiss_chalet_front_day.png) ![night](renders/swiss_chalet_front.png) ![plan](renders/swiss_chalet_cut_day.png)

* **Style:** 瑞士山屋 / Swiss Alpine Chalet · **Tier:** upscale · **Type:** house · **Floors:** 2
* **Fits game styles:** realistic, cozy, winter, anime, europe
* **Description:** Stone base + log upper storey, wide low gable with deep eaves, wrap balcony with flower boxes, red shutters.
* **Size:** 16.0 × 15.0 m footprint, 10.0 m tall · 178 objects · ~76680 tris · 9 lights · 44 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side), F2_S1(S side), F2_S3(S side) · interior doors: 7
* **Spawn points (local m):** front (-1.13, -7.5, 0)
* **Interactions:** cook, open, sit, sleep, use, wash, work
* **Placed on island at:** (-165.0, 15.3, 0.15), rotZ 0° · **Files:** `export/glb/swiss_chalet.glb`, Blender collection `BLD_swiss_chalet`

### 托斯卡尼農舍 Tuscan Farmhouse — `tuscan_farmhouse`

![day](renders/tuscan_farmhouse_front_day.png) ![night](renders/tuscan_farmhouse_front.png) ![plan](renders/tuscan_farmhouse_cut_day.png)

* **Style:** 義大利托斯卡尼 / Tuscan Casale · **Tier:** upscale · **Type:** farmhouse · **Floors:** 2
* **Fits game styles:** europe, romance, farming-sim, realistic
* **Description:** Stone 2-storey casale with a low terracotta hip roof, green shutters, cypress trees, rustic kitchen.
* **Size:** 19.9 × 19.4 m footprint, 9.6 m tall · 179 objects · ~75746 tris · 10 lights · 48 furniture pieces
* **Exterior doors:** F1_S3(S side), F1_E1(E side) · interior doors: 8
* **Spawn points (local m):** front (-1.13, -7.5, 0)
* **Interactions:** cook, open, sit, sleep, use, wash, work
* **Placed on island at:** (-189.5, -102.7, 0.15), rotZ 0° · **Files:** `export/glb/tuscan_farmhouse.glb`, Blender collection `BLD_tuscan_farmhouse`

### 生態巨構塊 Arcology Block — `arcology_block`

![day](renders/arcology_block_front_day.png) ![night](renders/arcology_block_front.png) ![plan](renders/arcology_block_cut_day.png)

* **Style:** 生態巨構 / Arcology Megablock · **Tier:** luxury · **Type:** megablock · **Floors:** 8
* **Fits game styles:** solarpunk, sci-fi, utopia, cyberpunk
* **Description:** 8-storey concrete megablock: market hall, apartments with planted balconies, roof forest and solar canopy.
* **Size:** 21.0 × 21.0 m footprint, 27.8 m tall · 930 objects · ~222374 tris · 41 lights · 270 furniture pieces
* **Exterior doors:** F1_S3(S side), F1_E3(E side), F2_S1(S side), F2_S3(S side), F3_S1(S side), F3_S3(S side), F4_S1(S side), F4_S3(S side), F5_S1(S side), F5_S3(S side), F6_S1(S side), F6_S3(S side), F7_S1(S side), F7_S3(S side), F8_S1(S side), F8_S3(S side), PH_W0(W side) · interior doors: 32
* **Spawn points (local m):** front (-4.0, -10.5, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (213.5, -136.3, 0.15), rotZ 180° · **Files:** `export/glb/arcology_block.glb`, Blender collection `BLD_arcology_block`

### 峇里島茅頂別墅 Bali Thatch Villa — `bali_villa`

![day](renders/bali_villa_front_day.png) ![night](renders/bali_villa_front.png) ![plan](renders/bali_villa_cut_day.png)

* **Style:** 峇里島villa / Balinese Villa · **Tier:** luxury · **Type:** villa · **Floors:** 1
* **Fits game styles:** resort, realistic, romance, tropical
* **Description:** Single-storey stone villa with a steep thatch hip roof and deep eaves, living / bedroom / outdoor-feel spa bath, palms.
* **Size:** 21.9 × 17.1 m footprint, 8.9 m tall · 79 objects · ~54162 tris · 5 lights · 16 furniture pieces
* **Exterior doors:** F1_S3(S side) · interior doors: 0
* **Spawn points (local m):** front (-1.5, -7.5, 0)
* **Interactions:** open, sit, sleep, use, wash, work
* **Placed on island at:** (-81.5, -77.3, 0.15), rotZ 180° · **Files:** `export/glb/bali_villa.glb`, Blender collection `BLD_bali_villa`

### 海港儲蓄銀行 Harbor Savings Bank — `bank_classical`

![day](renders/bank_classical_front_day.png) ![night](renders/bank_classical_front.png) ![plan](renders/bank_classical_cut_day.png)

* **Style:** 新古典銀行 / Neoclassical Bank · **Tier:** luxury · **Type:** bank · **Floors:** 2
* **Fits game styles:** realistic, heist, noir, western, civic
* **Description:** Granite neoclassical bank on a podium: columned portico with pediment, banking hall with teller counter, vault/server room, offices upstairs.
* **Size:** 19.0 × 22.0 m footprint, 10.5 m tall · 171 objects · ~90036 tris · 7 lights · 60 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side) · interior doors: 5
* **Spawn points (local m):** front (-1.0, -9.0, 0)
* **Interactions:** open, shop, sit, use, wash, work
* **Placed on island at:** (-169.5, -20.8, 0.15), rotZ 180° · **Files:** `export/glb/bank_classical.glb`, Blender collection `BLD_bank_classical`

### 懸挑清水宅 Cantilever Concrete House — `cantilever_house`

![day](renders/cantilever_house_front_day.png) ![night](renders/cantilever_house_front.png) ![plan](renders/cantilever_house_cut_day.png)

* **Style:** 懸挑住宅 / Brutalist Cantilever · **Tier:** luxury · **Type:** house · **Floors:** 2
* **Fits game styles:** modern, thriller, architectural, realistic
* **Description:** Concrete 2-storey house whose upper floor projects into a 4.5 m cantilevered terrace with glass rail.
* **Size:** 26.0 × 15.0 m footprint, 7.0 m tall · 170 objects · ~80336 tris · 9 lights · 46 furniture pieces
* **Exterior doors:** F1_S3(S side), F1_E1(E side) · interior doors: 7
* **Spawn points (local m):** front (-1.13, -7.5, 0)
* **Interactions:** cook, open, sit, sleep, use, wash, work
* **Placed on island at:** (190.0, -102.7, 0.15), rotZ 0° · **Files:** `export/glb/cantilever_house.glb`, Blender collection `BLD_cantilever_house`

### 清水模住宅 Fair-faced Concrete House — `concrete_minimal`

![day](renders/concrete_minimal_front_day.png) ![night](renders/concrete_minimal_front.png) ![plan](renders/concrete_minimal_cut_day.png)

* **Style:** 日式清水模 / Japanese Minimalist Concrete · **Tier:** luxury · **Type:** house · **Floors:** 2
* **Fits game styles:** realistic, modern, thriller, zen, architectural
* **Description:** Introverted fair-faced concrete 2-storey house: few deep windows, minimal interior, flat roof, single maple tree.
* **Size:** 16.4 × 17.8 m footprint, 7.0 m tall · 118 objects · ~82238 tris · 7 lights · 31 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_E0(E side) · interior doors: 5
* **Spawn points (local m):** front (-2.4, -8.5, 0)
* **Interactions:** cook, open, sit, sleep, use, wash, work
* **Placed on island at:** (-101.5, -45.7, 0.15), rotZ 0° · **Files:** `export/glb/concrete_minimal.glb`, Blender collection `BLD_concrete_minimal`

### 沙漠蘇丹宮殿 Desert Sultan's Palace — `desert_palace`

![day](renders/desert_palace_front_day.png) ![night](renders/desert_palace_front.png) ![plan](renders/desert_palace_cut_day.png)

* **Style:** 中東宮殿 / Arabian Palace · **Tier:** luxury · **Type:** palace · **Floors:** 2
* **Fits game styles:** fantasy, desert, aladdin, rpg, adventure
* **Description:** 2-storey cream palace under a golden onion-style dome with twin minarets: throne hall, banquet, chambers and library.
* **Size:** 28.0 × 19.0 m footprint, 16.2 m tall · 203 objects · ~96268 tris · 11 lights · 53 furniture pieces
* **Exterior doors:** F1_S6(S side), F1_E2(E side) · interior doors: 9
* **Spawn points (local m):** front (0.0, -9.5, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (-49.0, -187.3, 0.15), rotZ 180° · **Files:** `export/glb/desert_palace.glb`, Blender collection `BLD_desert_palace`

### 血月哥德莊園 Bloodmoon Gothic Manor — `gothic_manor`

![day](renders/gothic_manor_front_day.png) ![night](renders/gothic_manor_front.png) ![plan](renders/gothic_manor_cut_day.png)

* **Style:** 哥德莊園 / Gothic Revival Manor · **Tier:** luxury · **Type:** mansion · **Floors:** 3
* **Fits game styles:** horror, gothic, vampire, mystery, otome
* **Description:** 3-storey black-brick manor: tall lancet windows, steep slate mansard with dormers, iron spike fence, red-lit windows.
* **Size:** 20.1 × 18.5 m footprint, 15.7 m tall · 297 objects · ~107096 tris · 16 lights · 74 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side) · interior doors: 12
* **Spawn points (local m):** front (0.0, -8.0, 0)
* **Interactions:** open, sit, sleep, use, wash, work
* **Placed on island at:** (68.5, -151.7, 0.15), rotZ 0° · **Files:** `export/glb/gothic_manor.glb`, Blender collection `BLD_gothic_manor`

### 裝飾藝術大飯店 Grand Deco Hotel — `hotel_artdeco`

![day](renders/hotel_artdeco_front_day.png) ![night](renders/hotel_artdeco_front.png) ![plan](renders/hotel_artdeco_cut_day.png)

* **Style:** 裝飾藝術風 / Art Deco Hotel · **Tier:** luxury · **Type:** hotel · **Floors:** 6
* **Fits game styles:** noir, 1920s, realistic, mystery, bioshock-like
* **Description:** 6-storey Art Deco hotel: black-marble lobby with reception + bar, restaurant, 24 guest rooms, brass-trimmed stepped crown, vertical fins.
* **Size:** 21.0 × 21.0 m footprint, 28.2 m tall · 609 objects · ~137704 tris · 40 lights · 188 furniture pieces
* **Exterior doors:** F1_S3(S side), F1_E2(E side) · interior doors: 34
* **Spawn points (local m):** front (-3.0, -9.5, 0)
* **Interactions:** open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (199.5, -19.3, 0.15), rotZ 180° · **Files:** `export/glb/hotel_artdeco.glb`, Blender collection `BLD_hotel_artdeco`

### 羅亞爾小城堡 Loire Petit Château — `loire_chateau`

![day](renders/loire_chateau_front_day.png) ![night](renders/loire_chateau_front.png) ![plan](renders/loire_chateau_cut_day.png)

* **Style:** 法式城堡 / French Château · **Tier:** luxury · **Type:** mansion · **Floors:** 3
* **Fits game styles:** europe, romance, fantasy, mystery, otome
* **Description:** 3-storey cream château with slate mansard + dormers and two conical corner turrets, grand salon and bedrooms.
* **Size:** 26.0 × 17.0 m footprint, 16.9 m tall · 328 objects · ~93616 tris · 18 lights · 93 furniture pieces
* **Exterior doors:** F1_S4(S side), F1_E1(E side) · interior doors: 15
* **Spawn points (local m):** front (0.0, -8.5, 0)
* **Interactions:** cook, open, sit, sleep, use, wash, work
* **Placed on island at:** (-166.0, -101.7, 0.15), rotZ 0° · **Files:** `export/glb/loire_chateau.glb`, Blender collection `BLD_loire_chateau`

### 幸運7賭場 Lucky 7 Casino — `lucky7_casino`

![day](renders/lucky7_casino_front_day.png) ![night](renders/lucky7_casino_front.png) ![plan](renders/lucky7_casino_cut_day.png)

* **Style:** 拉斯維加斯賭場 / Las Vegas Casino · **Tier:** luxury · **Type:** casino · **Floors:** 2
* **Fits game styles:** crime, heist, gta-like, neon, retro
* **Description:** 2-storey black-and-gold casino: gaming floor of machines, bar and lounge, upstairs VIP room, huge neon marquee.
* **Size:** 23.0 × 19.0 m footprint, 8.5 m tall · 208 objects · ~83658 tris · 9 lights · 83 furniture pieces
* **Exterior doors:** F1_S3(S side), F1_E2(E side) · interior doors: 7
* **Spawn points (local m):** front (-3.0, -9.5, 0)
* **Interactions:** open, play, shop, sit, use, wash, work
* **Placed on island at:** (130.5, -100.7, 0.15), rotZ 0° · **Files:** `export/glb/lucky7_casino.glb`, Blender collection `BLD_lucky7_casino`

### 馬里布海灘屋 Malibu Beach House — `malibu_beach_house`

![day](renders/malibu_beach_house_front_day.png) ![night](renders/malibu_beach_house_front.png) ![plan](renders/malibu_beach_house_cut_day.png)

* **Style:** 加州海灘屋 / California Beach House · **Tier:** luxury · **Type:** beach house · **Floors:** 2
* **Fits game styles:** summer, realistic, gta-like, modern
* **Description:** Raised 2-storey white beach house: full-height glass, wraparound balcony, shed roof, surfboards.
* **Size:** 17.0 × 15.0 m footprint, 9.0 m tall · 180 objects · ~80284 tris · 9 lights · 42 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side), F2_S1(S side), F2_S3(S side) · interior doors: 7
* **Spawn points (local m):** front (-1.13, -7.5, 0)
* **Interactions:** cook, open, sit, sleep, use, wash, work
* **Placed on island at:** (31.5, -102.7, 0.15), rotZ 0° · **Files:** `export/glb/malibu_beach_house.glb`, Blender collection `BLD_malibu_beach_house`

### 海港金融中心 Harbor Finance Tower — `office_glass_tower`

![day](renders/office_glass_tower_front_day.png) ![night](renders/office_glass_tower_front.png) ![plan](renders/office_glass_tower_cut_day.png)

* **Style:** 現代玻璃帷幕大樓 / Modern Glass High-rise · **Tier:** luxury · **Type:** office high-rise · **Floors:** 10
* **Fits game styles:** realistic, modern, corporate, thriller, cyberpunk
* **Description:** 20x20 m, 10 floors: marble lobby + reception, 2 elevator shafts (car objects with level data) + fire stair, open-plan offices / meeting / pantry / server room, 5 vacant shell floors for custom fit-out, executive suite, roof with helipad and plant.
* **Size:** 26.0 × 25.5 m footprint, 41.9 m tall · 1205 objects · ~290604 tris · 105 lights · 479 furniture pieces
* **Exterior doors:** F1_S1(S side), F1_S2(S side), F1_N1(N side), RoofCore_S0(S side) · interior doors: 23
* **Spawn points (local m):** forecourt (0.0, -14.0, 0)
* **Interactions:** cook, elevator, elevator_call, open, shop, sit, use, wash, work
* **Placed on island at:** (20.0, 20.5, 0.15), rotZ 0° · **Files:** `export/glb/office_glass_tower.glb`, Blender collection `BLD_office_glass_tower`

### 白崖現代豪宅 White Cliff Modern Villa — `villa_luxury_modern`

![day](renders/villa_luxury_modern_front_day.png) ![night](renders/villa_luxury_modern_front.png) ![plan](renders/villa_luxury_modern_cut_day.png)

* **Style:** 奢華現代主義別墅 / Luxury Modernist Villa · **Tier:** luxury · **Type:** villa · **Floors:** 2
* **Fits game styles:** realistic, modern, thriller, life-sim, anime
* **Description:** Glass-walled concrete living pavilion (living/dining/kitchen island), floating stair, cantilevered upper volume with master suite + ensuite, 2nd bedroom, study, garage with car, roof terrace, infinity pool & deck.
* **Size:** 31.8 × 25.3 m footprint, 7.8 m tall · 188 objects · ~92452 tris · 15 lights · 64 furniture pieces
* **Exterior doors:** A_S1(S side), B_S0(S side), B_W0(W side), C_E0(E side) · interior doors: 4
* **Spawn points (local m):** front_gate (1.8, -12.5, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (-82.0, 19.0, 0.15), rotZ 0° · **Files:** `export/glb/villa_luxury_modern.glb`, Blender collection `BLD_villa_luxury_modern`

### 霓光電路別墅 Neon Circuit Villa — `villa_neon_circuit`

![day](renders/villa_neon_circuit_front_day.png) ![night](renders/villa_neon_circuit_front.png) ![plan](renders/villa_neon_circuit_cut_day.png)

* **Style:** 近未來科技別墅 / Near-Future Tech Villa · **Tier:** luxury · **Type:** villa · **Floors:** 2
* **Fits game styles:** cyberpunk, sci-fi, near-future, realistic, anime
* **Description:** Charcoal composite villa with cyan circuit-trace lighting: gated courtyard, glowing steps, G/F lounge + kitchen + game room, 2F suite with balcony, west wing with roof terrace reached by an outside stair.
* **Size:** 24.0 × 23.0 m footprint, 7.3 m tall · 180 objects · ~79276 tris · 15 lights · 45 furniture pieces
* **Exterior doors:** M_S1(S side), M_W0(W side), U_S1(S side), U_W0(W side), Wg_S1(S side) · interior doors: 3
* **Spawn points (local m):** gate (0.0, -11.5, 0)
* **Interactions:** cook, open, play, sit, sleep, use, wash, work
* **Placed on island at:** (26.0, -20.5, 0.15), rotZ 180° · **Files:** `export/glb/villa_neon_circuit.glb`, Blender collection `BLD_villa_neon_circuit`

### 冒險者公會 Adventurers' Guild Hall — `adventurers_guild`

![day](renders/adventurers_guild_front_day.png) ![night](renders/adventurers_guild_front.png) ![plan](renders/adventurers_guild_cut_day.png)

* **Style:** 冒險者公會 / Fantasy Guild Hall · **Tier:** landmark · **Type:** guild · **Floors:** 3
* **Fits game styles:** fantasy, rpg, anime, isekai, dnd
* **Description:** 3-storey stone-and-timber guild: tavern hall with quest board, guild office, upstairs dormitory and library.
* **Size:** 21.0 × 17.0 m footprint, 17.4 m tall · 297 objects · ~110728 tris · 17 lights · 109 furniture pieces
* **Exterior doors:** F1_S4(S side), F1_E1(E side) · interior doors: 12
* **Spawn points (local m):** front (-1.0, -8.5, 0)
* **Interactions:** cook, open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (47.5, -153.7, 0.15), rotZ 0° · **Files:** `export/glb/adventurers_guild.glb`, Blender collection `BLD_adventurers_guild`

### 翠焰煉金塔 Emerald Alchemy Tower — `alchemy_tower`

![day](renders/alchemy_tower_front_day.png) ![night](renders/alchemy_tower_front.png) ![plan](renders/alchemy_tower_cut_day.png)

* **Style:** 煉金塔 / Alchemist Tower · **Tier:** landmark · **Type:** tower · **Floors:** 4
* **Fits game styles:** fantasy, steampunk, rpg, magic-school
* **Description:** 8-sided dark-brick tower with a copper cone: brewing floors with green-glowing flasks, spiral stair, observatory top.
* **Size:** 14.0 × 16.0 m footprint, 19.3 m tall · 236 objects · ~72228 tris · 8 lights · 5 furniture pieces
* **Exterior doors:** F1_5_0(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -6.1, 0)
* **Interactions:** cook, open, use
* **Placed on island at:** (-20.0, -153.7, 0.15), rotZ 0° · **Files:** `export/glb/alchemy_tower.glb`, Blender collection `BLD_alchemy_tower`

### 獅鷲城堡塔 Griffin Castle Keep — `castle_keep`

![day](renders/castle_keep_front_day.png) ![night](renders/castle_keep_front.png) ![plan](renders/castle_keep_cut_day.png)

* **Style:** 中世紀城堡 / Medieval Castle Keep · **Tier:** landmark · **Type:** castle · **Floors:** 4
* **Fits game styles:** fantasy, medieval, rpg, strategy, realistic
* **Description:** 4-storey square stone keep with corner turrets: great hall, armoury/storage, lord's chamber + library, crenellated roof walk with banners.
* **Size:** 22.0 × 17.0 m footprint, 21.3 m tall · 370 objects · ~131540 tris · 17 lights · 92 furniture pieces
* **Exterior doors:** F1_S3(S side), F1_E2(E side), PH_W0(W side) · interior doors: 12
* **Spawn points (local m):** front (-2.0, -8.5, 0)
* **Interactions:** open, shop, sit, sleep, use, work
* **Placed on island at:** (170.0, -45.7, 0.15), rotZ 0° · **Files:** `export/glb/castle_keep.glb`, Blender collection `BLD_castle_keep`

### 尼羅神殿 Temple of the Nile — `egyptian_temple`

![day](renders/egyptian_temple_front_day.png) ![night](renders/egyptian_temple_front.png) ![plan](renders/egyptian_temple_cut_day.png)

* **Style:** 埃及神殿 / Ancient Egyptian Temple · **Tier:** landmark · **Type:** temple · **Floors:** 1
* **Fits game styles:** historical, fantasy, adventure, mummy
* **Description:** Sandstone temple: battered pylon gateway, columned portico, sanctuary hall with altar, obelisk.
* **Size:** 22.0 × 23.0 m footprint, 9.8 m tall · 66 objects · ~57290 tris · 1 lights · 21 furniture pieces
* **Exterior doors:** F1_S4(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -9.5, 0)
* **Interactions:** open, sit, use
* **Placed on island at:** (28.0, -191.3, 0.15), rotZ 180° · **Files:** `export/glb/egyptian_temple.glb`, Blender collection `BLD_egyptian_temple`

### 海港水族館 Harbor Aquarium — `harbor_aquarium`

![day](renders/harbor_aquarium_front_day.png) ![night](renders/harbor_aquarium_front.png) ![plan](renders/harbor_aquarium_cut_day.png)

* **Style:** 水族館 / Public Aquarium · **Tier:** landmark · **Type:** aquarium · **Floors:** 1
* **Fits game styles:** family, modern, slice-of-life, anime
* **Description:** Low dark hall of glowing fish tanks and benches under a big glass dome.
* **Size:** 23.0 × 19.0 m footprint, 9.2 m tall · 43 objects · ~63136 tris · 4 lights · 8 furniture pieces
* **Exterior doors:** F1_S4(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -9.5, 0)
* **Interactions:** open, sit, use
* **Placed on island at:** (146.5, -135.3, 0.15), rotZ 180° · **Files:** `export/glb/harbor_aquarium.glb`, Blender collection `BLD_harbor_aquarium`

### 超迴路列車站 Hyperloop Station — `hyperloop_station`

![day](renders/hyperloop_station_front_day.png) ![night](renders/hyperloop_station_front.png) ![plan](renders/hyperloop_station_cut_day.png)

* **Style:** 超迴路車站 / Hyperloop Terminal · **Tier:** landmark · **Type:** station · **Floors:** 1
* **Fits game styles:** sci-fi, modern, cyberpunk
* **Description:** Single-storey steel-and-glass terminal hall with ticket lobby, behind it a transparent hyperloop tube with a waiting pod.
* **Size:** 34.6 × 18.0 m footprint, 6.2 m tall · 110 objects · ~74576 tris · 2 lights · 68 furniture pieces
* **Exterior doors:** F1_S3(S side) · interior doors: 0
* **Spawn points (local m):** front (-4.0, -7.5, 0)
* **Interactions:** open, shop, sit, use
* **Placed on island at:** (-172.0, -154.7, 0.15), rotZ 0° · **Files:** `export/glb/hyperloop_station.glb`, Blender collection `BLD_hyperloop_station`

### 白鷺天守閣 White Heron Castle Keep — `japanese_castle`

![day](renders/japanese_castle_front_day.png) ![night](renders/japanese_castle_front.png) ![plan](renders/japanese_castle_cut_day.png)

* **Style:** 日式天守閣 / Japanese Castle Tenshu · **Tier:** landmark · **Type:** castle · **Floors:** 3
* **Fits game styles:** japan, samurai, anime, historical, strategy
* **Description:** 3-storey white tenshu on a 3 m battered stone base: tiered curled roofs at every floor, golden shachihoko, samurai hall inside.
* **Size:** 20.0 × 20.0 m footprint, 18.0 m tall · 230 objects · ~101966 tris · 12 lights · 56 furniture pieces
* **Exterior doors:** F1_S2(S side), F1_E1(E side) · interior doors: 9
* **Spawn points (local m):** front (0.0, -7.5, 0)
* **Interactions:** open, shop, sit, sleep, use, work
* **Placed on island at:** (-73.0, -190.3, 0.15), rotZ 180° · **Files:** `export/glb/japanese_castle.glb`, Blender collection `BLD_japanese_castle`

### 元宵燈籠塔 Lantern Festival Tower — `lantern_festival_tower`

![day](renders/lantern_festival_tower_front_day.png) ![night](renders/lantern_festival_tower_front.png) ![plan](renders/lantern_festival_tower_cut_day.png)

* **Style:** 燈籠塔 / Chinese Lantern Tower · **Tier:** landmark · **Type:** tower · **Floors:** 3
* **Fits game styles:** wuxia, festival, anime, fantasy
* **Description:** 8-sided vermilion tower hung with dozens of red lanterns, tile cone roof, spiral stair to a lookout.
* **Size:** 14.0 × 16.0 m footprint, 14.7 m tall · 211 objects · ~87312 tris · 27 lights · 0 furniture pieces
* **Exterior doors:** F1_5_0(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -5.7, 0)
* **Interactions:** open
* **Placed on island at:** (134.0, -153.7, 0.15), rotZ 0° · **Files:** `export/glb/lantern_festival_tower.glb`, Blender collection `BLD_lantern_festival_tower`

### 海角燈塔 Cape Lighthouse — `lighthouse_cape`

![day](renders/lighthouse_cape_front_day.png) ![night](renders/lighthouse_cape_front.png) ![plan](renders/lighthouse_cape_cut_day.png)

* **Style:** 海事燈塔 / Maritime Lighthouse · **Tier:** landmark · **Type:** lighthouse · **Floors:** 5
* **Fits game styles:** realistic, horror, mystery, adventure, ghibli
* **Description:** Red/white striped 5-storey round tower with spiral stair, gallery deck, glazed lantern room with glowing lens; keeper's cottage.
* **Size:** 18.4 × 20.0 m footprint, 21.1 m tall · 418 objects · ~95048 tris · 7 lights · 7 furniture pieces
* **Exterior doors:** F1_8_0(S side), Lantern_8_0(S side), Cottage_S0(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -5.7, 0)
* **Interactions:** open, sit, sleep, use
* **Placed on island at:** (124.0, -43.7, 0.15), rotZ 0° · **Files:** `export/glb/lighthouse_cape.glb`, Blender collection `BLD_lighthouse_cape`

### 星輝魔法學院 Astral Mage Academy — `mage_academy`

![day](renders/mage_academy_front_day.png) ![night](renders/mage_academy_front.png) ![plan](renders/mage_academy_cut_day.png)

* **Style:** 魔法學院 / Fantasy Magic Academy · **Tier:** landmark · **Type:** academy · **Floors:** 3
* **Fits game styles:** fantasy, anime, magic-school, rpg
* **Description:** 3-storey stone academy: lecture halls, grand library, slate gable, twin conical towers flanking the front.
* **Size:** 28.0 × 19.0 m footprint, 18.5 m tall · 503 objects · ~157704 tris · 20 lights · 276 furniture pieces
* **Exterior doors:** F1_S6(S side), F1_E2(E side) · interior doors: 15
* **Spawn points (local m):** front (0.0, -9.5, 0)
* **Interactions:** open, shop, sit, sleep, use, wash, work
* **Placed on island at:** (23.0, -152.7, 0.15), rotZ 0° · **Files:** `export/glb/mage_academy.glb`, Blender collection `BLD_mage_academy`

### 羽蛇金字塔 Feathered Serpent Pyramid — `maya_pyramid`

![day](renders/maya_pyramid_front_day.png) ![night](renders/maya_pyramid_front.png) ![plan](renders/maya_pyramid_cut_day.png)

* **Style:** 馬雅金字塔 / Mesoamerican Step Pyramid · **Tier:** landmark · **Type:** pyramid · **Floors:** 2
* **Fits game styles:** adventure, historical, fantasy, tomb-raider
* **Description:** Nine-tier stepped stone pyramid with a central stair to a summit temple room (altar, torches).
* **Size:** 30.0 × 31.5 m footprint, 14.2 m tall · 47 objects · ~73952 tris · 2 lights · 1 furniture pieces
* **Exterior doors:** - · interior doors: 0
* **Spawn points (local m):** front (0.0, -14.5, 0)
* **Interactions:** use
* **Placed on island at:** (-224.0, 74.8, 0.15), rotZ 0° · **Files:** `export/glb/maya_pyramid.glb`, Blender collection `BLD_maya_pyramid`

### 星穹天文台 Starvault Observatory — `observatory_dome`

![day](renders/observatory_dome_front_day.png) ![night](renders/observatory_dome_front.png) ![plan](renders/observatory_dome_cut_day.png)

* **Style:** 圓頂天文台 / Domed Observatory · **Tier:** landmark · **Type:** observatory · **Floors:** 2
* **Fits game styles:** sci-fi, realistic, mystery, anime, academy
* **Description:** 12-sided white drum: visitor/lab floor, control room, telescope floor under a copper dome with an opening slit and a large telescope.
* **Size:** 14.0 × 16.0 m footprint, 12.8 m tall · 168 objects · ~75716 tris · 3 lights · 14 furniture pieces
* **Exterior doors:** F1_8_0(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -7.5, 0)
* **Interactions:** open, sit, use, work
* **Placed on island at:** (108.0, -45.7, 0.15), rotZ 0° · **Files:** `export/glb/observatory_dome.glb`, Blender collection `BLD_observatory_dome`

### 海港科學館 Harbor Science Museum — `science_museum`

![day](renders/science_museum_front_day.png) ![night](renders/science_museum_front.png) ![plan](renders/science_museum_cut_day.png)

* **Style:** 科學館 / Science Museum · **Tier:** landmark · **Type:** museum · **Floors:** 2
* **Fits game styles:** family, sci-fi, mystery, realistic
* **Description:** 2-storey concrete museum with a glazed sawtooth roof: exhibit halls of consoles and models, library and meeting room.
* **Size:** 25.0 × 19.0 m footprint, 10.4 m tall · 183 objects · ~124388 tris · 9 lights · 57 furniture pieces
* **Exterior doors:** F1_S5(S side), F1_E2(E side) · interior doors: 7
* **Spawn points (local m):** front (-4.0, -9.5, 0)
* **Interactions:** open, shop, sit, use, wash, work
* **Placed on island at:** (171.5, -135.3, 0.15), rotZ 180° · **Files:** `export/glb/science_museum.glb`, Blender collection `BLD_science_museum`

### 朱鳥神社 Vermilion Bird Shrine — `shinto_shrine`

![day](renders/shinto_shrine_front_day.png) ![night](renders/shinto_shrine_front.png) ![plan](renders/shinto_shrine_cut_day.png)

* **Style:** 日式神社 / Japanese Shinto Shrine · **Tier:** landmark · **Type:** shrine · **Floors:** 1
* **Fits game styles:** anime, japan, fantasy, horror, realistic
* **Description:** Vermilion shrine hall on a stone plinth with sliding paper doors and a curved slate gable; torii gate, stone lanterns, offering box, bell, sacred tree.
* **Size:** 20.3 × 20.0 m footprint, 6.8 m tall · 69 objects · ~60756 tris · 1 lights · 12 furniture pieces
* **Exterior doors:** F1_S2(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -6.5, 0)
* **Interactions:** open, sit, use
* **Placed on island at:** (227.0, -40.7, 0.15), rotZ 0° · **Files:** `export/glb/shinto_shrine.glb`, Blender collection `BLD_shinto_shrine`

### 火星殖民穹頂 Mars Colony Dome — `space_colony_dome`

![day](renders/space_colony_dome_front_day.png) ![night](renders/space_colony_dome_front.png) ![plan](renders/space_colony_dome_cut_day.png)

* **Style:** 太空殖民地 / Sci-Fi Habitat Dome · **Tier:** landmark · **Type:** habitat · **Floors:** 1
* **Fits game styles:** sci-fi, survival, mars, solarpunk
* **Description:** 16-sided habitat ring under a big glass dome: hydroponic farm racks, crew lounge, consoles; airlock entrance.
* **Size:** 20.0 × 22.0 m footprint, 8.7 m tall · 62 objects · ~62652 tris · 1 lights · 8 furniture pieces
* **Exterior doors:** F1_11_0(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -9.5, 0)
* **Interactions:** open, sit, use, work
* **Placed on island at:** (49.0, -189.3, 0.15), rotZ 180° · **Files:** `export/glb/space_colony_dome.glb`, Blender collection `BLD_space_colony_dome`

### 海角石砌教堂 Cape Stone Chapel — `stone_chapel`

![day](renders/stone_chapel_front_day.png) ![night](renders/stone_chapel_front.png) ![plan](renders/stone_chapel_cut_day.png)

* **Style:** 哥德復興教堂 / Gothic Revival Chapel · **Tier:** landmark · **Type:** chapel · **Floors:** 1
* **Fits game styles:** realistic, horror, romance, fantasy, wedding
* **Description:** Stone nave with tall lancet windows, rows of pews and altar, steep slate gable, square bell tower with brass bell and spire.
* **Size:** 21.2 × 22.9 m footprint, 19.7 m tall · 74 objects · ~67556 tris · 1 lights · 27 furniture pieces
* **Exterior doors:** F1_S2(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -11.0, 0)
* **Interactions:** open, sit, use
* **Placed on island at:** (-131.0, -18.8, 0.15), rotZ 180° · **Files:** `export/glb/stone_chapel.glb`, Blender collection `BLD_stone_chapel`

### 紫霄道觀 Purple Cloud Taoist Temple — `taoist_temple`

![day](renders/taoist_temple_front_day.png) ![night](renders/taoist_temple_front.png) ![plan](renders/taoist_temple_cut_day.png)

* **Style:** 道觀 / Taoist Temple · **Tier:** landmark · **Type:** temple · **Floors:** 1
* **Fits game styles:** wuxia, fantasy, xianxia, realistic
* **Description:** Vermilion hall on a tall stone plinth with sweeping curled roof and ornaments, altar inside, censer and bagua courtyard.
* **Size:** 17.0 × 20.0 m footprint, 9.9 m tall · 60 objects · ~63410 tris · 3 lights · 14 furniture pieces
* **Exterior doors:** F1_S2(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -7.5, 0)
* **Interactions:** open, sit, use
* **Placed on island at:** (-142.5, -190.3, 0.15), rotZ 180° · **Files:** `export/glb/taoist_temple.glb`, Blender collection `BLD_taoist_temple`

### 天界樓閣 Heaven Gate Pavilion — `temple_pagoda`

![day](renders/temple_pagoda_front_day.png) ![night](renders/temple_pagoda_front.png) ![plan](renders/temple_pagoda_cut_day.png)

* **Style:** 中式樓閣廟宇 / Chinese Pagoda Temple (neo-oriental) · **Tier:** landmark · **Type:** temple / landmark · **Floors:** 3
* **Fits game styles:** wuxia, fantasy, cyberpunk-oriental, anime, realistic
* **Description:** Stone podium with front stair, 3-storey timber pavilion (altar hall / scripture library / lookout) linked by interior stairs, verandas with red columns, triple curled hip roofs, neon-lit paifang gate and red lantern strings.
* **Size:** 24.0 × 30.0 m footprint, 20.5 m tall · 243 objects · ~133392 tris · 11 lights · 18 furniture pieces
* **Exterior doors:** T1_S6(S side), T2_S4(S side), T2_N4(N side), T2_W2(W side) · interior doors: 0
* **Spawn points (local m):** gate (0.0, -18.0, 0)
* **Interactions:** open, sit, use
* **Placed on island at:** (-28.0, -27.0, 0.15), rotZ 180° · **Files:** `export/glb/temple_pagoda.glb`, Blender collection `BLD_temple_pagoda`

### 福德宮 Fude Folk Temple — `tw_folk_temple`

![day](renders/tw_folk_temple_front_day.png) ![night](renders/tw_folk_temple_front.png) ![plan](renders/tw_folk_temple_cut_day.png)

* **Style:** 台灣廟宇 / Taiwanese Folk Temple · **Tier:** landmark · **Type:** temple · **Floors:** 1
* **Fits game styles:** taiwan, wuxia, fantasy, horror, realistic
* **Description:** Red temple hall on a stone plinth: dragon-wrapped columns, swallow-tail curled roof with ornaments, altar inside, incense burner.
* **Size:** 17.0 × 21.0 m footprint, 9.6 m tall · 67 objects · ~53842 tris · 5 lights · 18 furniture pieces
* **Exterior doors:** F1_S2(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -8.5, 0)
* **Interactions:** open, sit, use
* **Placed on island at:** (17.5, -82.3, 0.15), rotZ 180° · **Files:** `export/glb/tw_folk_temple.glb`, Blender collection `BLD_tw_folk_temple`

### 風車磨坊 Old Dutch Windmill — `windmill_dutch`

![day](renders/windmill_dutch_front_day.png) ![night](renders/windmill_dutch_front.png) ![plan](renders/windmill_dutch_cut_day.png)

* **Style:** 荷蘭風車 / Dutch Tower Windmill · **Tier:** landmark · **Type:** windmill · **Floors:** 3
* **Fits game styles:** rpg-village, fantasy, cozy, farming-sim, realistic
* **Description:** 8-sided brick windmill: grain store, millstone floor with reefing gallery, miller's loft; timber cap with four lattice sails (rotate prop).
* **Size:** 15.2 × 16.0 m footprint, 17.2 m tall · 201 objects · ~64816 tris · 4 lights · 9 furniture pieces
* **Exterior doors:** F1_5_0(S side), F2_5_0(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -5.9, 0)
* **Interactions:** open, sleep, use
* **Placed on island at:** (94.0, -45.7, 0.15), rotZ 0° · **Files:** `export/glb/windmill_dutch.glb`, Blender collection `BLD_windmill_dutch`

### 星辰法師塔 Starlight Wizard Tower — `wizard_tower`

![day](renders/wizard_tower_front_day.png) ![night](renders/wizard_tower_front.png) ![plan](renders/wizard_tower_cut_day.png)

* **Style:** 奇幻法師塔 / High-Fantasy Wizard Tower · **Tier:** landmark · **Type:** tower · **Floors:** 4
* **Fits game styles:** fantasy, rpg, anime, magic-school, ghibli
* **Description:** 12-sided stone tower: library, alchemy lab, bedchamber and star-gazing study linked by a spiral stair; tall blue cone roof, glowing crystals.
* **Size:** 14.0 × 16.0 m footprint, 22.1 m tall · 294 objects · ~91672 tris · 6 lights · 17 furniture pieces
* **Exterior doors:** F1_8_0(S side) · interior doors: 0
* **Spawn points (local m):** front (0.0, -6.7, 0)
* **Interactions:** cook, open, sleep, use
* **Placed on island at:** (80.0, -45.7, 0.15), rotZ 0° · **Files:** `export/glb/wizard_tower.glb`, Blender collection `BLD_wizard_tower`

## 環境 Environment — `island_town`

Island ~300×225 m: town flats, two crossing streets with sidewalks, curbs, lane markings, zebra crossings, street lamps, beach palms, snowy north hill (polar station plateau, z = 7 m), sea plane at z = −0.6 m. File: `export/glb/island_town.glb`.
