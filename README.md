# quakemash

level design project aiming to merge all quake levels together into a singular map.

## possible qc features

Basic Features - getting vanilla quake working in a single level

* zoned gravity areas (for e1m8)
* dynamic difficulty modifications (for when you switch the difficulty level in start)
* key pickup is removed on pickup, but when a player dies every key they're carrying respawns at their original location

Extended Features - experimental gameplay that tries new things 

* using entity spawn positions as markers for randomly spawning within a certain radius
* having monsters change behaviour based on either location, proximity to player, proximity to other monsters, or other data
* better pathfinding for monsters so that they will always chase the player (so the player can start to herd monsters)
* ability for player to create linked teleporters , on creation of teleporter , player would create a name for teleporter and optionally a destination teleporter. all teleporters can be linked to other teleporters
* ability for player to create different types of monsters, weapon, ammo, powerups, level elements from "crafting stations" 
* combination of sven coop and risk of rain game mode
* survival coop mode 
* faction warfare mode 
* collecting runes could be a type of powerup or unlocking of certain abilities (grapple hook for instance)

Zany Crazy Time Ideas - this section is for completely off the wall ideas that we put out there to be implemented or not and might be out the scope of pure qc programming into actual engine modifications

* 3d tile based player bases - based on http://oskarstalberg.com/game/house/index.html giving the player a type of tool that would allow them to essentially shoot a base that would seamlessly integrate itself into the surrounding geometry, the player would have an alternate shot that would also create or pack up bases. 
* allow weapons to be a digging tool that would allow people to dig holes into certain types of level geometry
* research procedural methods to feed the entire quakemash data set into a wave-collapse procedural generation algorithim that would expand the quakemash world further

*notes*

*recommended engine is latest build of darkplaces http://icculus.org/twilight/darkplaces/files/darkplacesengineautobuild.zip
*latest version of fteqw has been tested, loads the map but has an odd audio echo bug, make sure to type sv_bigcoords 1 to set fteqw to render the level properly
*version of quakespasm that should work with quakemash http://triptohell.info/moodles/qss/quakespasm-spike-r7.zip , make sure to type sv_protocol 999 to force quakespasm to render the level properly
*pixelated textures:
*gl_texturemode gl_nearest_mipmap_linear in console

pixelated shadows:
r_shadow_shadowmapping_useshadowsampler 0
r_shadow_shadowmapping_filterquality 0
r_shadow_shadowmapping_bordersize 0 (can also use the default of 4)
