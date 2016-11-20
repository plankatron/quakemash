# quakemash

level design project aiming to merge all quake levels together into a singular map.

## possible qc features

Basic Features - getting vanilla quake working in a single level

* zoned gravity areas (for e1m8)
* dynamic difficulty modifications (for when you switch the difficulty level in start)

Extended Features - experimental gameplay that tries new things 

* using entity spawn positions as markers for randomly spawning within a certain radius
* having monsters change behaviour based on either location, proximity to player, proximity to other monsters, or other data
* better pathfinding for monsters so that they will always chase the player (so the player can start to herd monsters)
* survival coop mode 
* faction warfare mode 

Zany Crazy Time Ideas - this section is for completely off the wall ideas that we put out there to be implemented or not

* 3d tile based player bases - based on http://oskarstalberg.com/game/house/index.html giving the player a type of tool that would allow them to essentially shoot a base that would seamlessly integrate itself into the surrounding geometry, the player would have an alternate shot that would also create or pack up bases. 
* allow the axe to be a digging tool that would allow people to dig holes into certain types of level geometry
* research procedural methods to feed the entire quakemash data set into a wave-collapse procedural generation algorithim that would expand the quakemash world further

*notes*
pixelated textures:
gl_texturemode gl_nearest_mipmap_linear in console

pixelated shadows:
r_shadow_shadowmapping_useshadowsampler 0
r_shadow_shadowmapping_filterquality 0
r_shadow_shadowmapping_bordersize 0 (can also use the default of 4)
