# Emerald (J) TAS info
ID: cd74d187
Mudkip: 8752 89613c19 rash    30, 31, 16, 28,  1, 10
trainer: そ  v EA00000F B+15
glitch id: 0x3110 targets 02330000 (Box 12 slot 13-14)

## Addresses
| Symbol | Address |
| ------ | ------- |
| gTrainerId | 02020000 |
| party | 02024190 |
| enemy party | 020243E8 |
| RNG | 03005ae0 |
| RNG cycles | 02024664 |
| gSaveBlock1Ptr | 03005aec |
| gSaveBlock2Ptr | 03005af0 |
| animation loaded at | 080A3420 |
| RunAnimScriptCommand | 080a35ac |
| sBattleAnimScriptPtr | 02038090 |
| gAnimFramesToWait    | 0203809c |
| SetCallback2AfterHallOfFameDisplay | 08173F68 |
| gTasks | 03005b60 |
| gRandomTurnNumber | 02023FD4 |
| gBattleMons | 02023D28 |
| gBattleMoveDamage | 02023E94 |
| tileTransitionState | 02037233  |
| gCritMultiplier | 02023EB5 |
| gMoveResultFlags | 02023F20 |
| gBattleStruct | 02024140 | 0x6d offset
| gMain | 03002360
| inBattle | 03002799
| CreateBoxMon | 080677A0 |
| CreateMon | 08067730 |
| GetSpeciesName | 0806B3DC |
| SetSaveBlocksPointers | 080765E4 |
| save block offset | 080765F6 |
| GetBoxMonData | 0806A1B4 |
| gPokemonStoragePtr | 03005AF4 |
| gMapHeader | 02036FB8 |
| CB2_LoadMap2 | 08085964 |
| gEventObjects | 02036FF0 |
| Scott | 081db9f0 |
| Common_Movement_ExclamationMark | 0824361b |
| BattlePutTextOnWindow | 0814FA04 | Mislabeled!
| gActiveBattler | 02023D08 |
| gBattleBufferA | 02022D08 |
| gCurrentMove | 02023E8E |
| gBattlerTarget | 02023EB0 |
| gBattleMons | 02023D28 | 0x58 large, 0xC is moves
| ZeroMonData: | 08067670 |
| daycare | +0x2F9C |
| step counter | daycare+0x1b0 |

## New Route:
- Mudkip: TBD
- (10, 13, 10, 17, 0, 26) with accuracy, defense, strength rooms
- Target EVs: 21 HP 6 AT (HP Up, Kelpsy Berry, Wurmple, Solrock, Poochyena)
- Early Verdanturf
- Meteor Falls: Solrock
- Route 102/103: Poochyena, Wurmple, capture, teach Surf, Facade, use HP Up on Abra
- Route 111: Order as Any Abra Marshtomp, use Surf
- Rose fight: KO Any, bring Abra to 1, switch in Marshtomp (this updates slot to 3)
- Manip Berry Master for Pomeg, Kelpsy
- Teleport to Petalburg, apply HP Ups, Kelpsy Berry
- Name Box 1, scroll back to box 2 in reverse, deposit Marshtomp Box 2 Slot 24
- Corrupt PID & Withdraw Egg
- Hatch. Win.
- alternate routes: Which HP Up, Verdanturf early/late
- move switching tech

## Glitzer Popping
- Target: 0202A52C (-100 each time)
- 1st corruption at 0202a574

## Trash bytes
- Set at 0806789A
- target byte: 03007cef
- Can be manipulated by opening and closing the menu (lol)

## Mudkip
- ~6018 cycles from ID generation
- 3c/2f after A press
- (0, 0, 0, 0, 0, 1)

## Brendan 1
- !Tackle, !Tackle
- (0, 0, 0, 0, 0, 2)

## Youngster Calvin
- Tackle, !Tackle
- (0, 1, 0, 0, 0, 2)

## Wally Tutorial
- Run in the grass near the spinner to advance RNG quickly
1. PutZigzagoonInPlayerParty (just after exiting gym)
  - Generated via method 1
2. StartWallyTutorialBattle (just after message)
   1. CreateMaleMon (loops otId & personality until it's male)
      1. CreateMon fixed personality, generates IV

## Aqua Grunt
- !Tackle, !Tackle, !Tackle
- Poochyena outspeeds if Mudkip is Brave, Relaxed, Quiet or Sassy, or has less than 6 Speed IVs
- (0, 2, 0, 0, 0, 2)

## Youngster Josh
- !Mud Slap, !Mud Slap, !Mud Slap
- (0, 2, 1, 0, 0, 2)

## Roxanne
- Water Gun, Water Gun, Water Gun, !Water Gun
- (0, 2, 4, 0, 0, 2)

## Catch Abra
- Must have at least 7-8,16,23-24 HP IVs
- Abra: 707FE208 Adamant (15, 2, 26, 21, 21, 5)

## Hiker Devan
- Water Gun x2
- (0, 2, 6, 0, 0, 2)

## Aqua Grunt
- !Water Gun
- (0, 3, 6, 0, 0, 2)

## Brawly
- Mudkip is level 14 and levels up on Machop
- Machop 16 Quiet (0)/(12) !Water Gun, Low Kick, !Water Gun
- Meditite 16 Docile (0)/(12) !Water Gun!, !Water Gun, Focus Punch vs 15
- Makuhita 19 Adamant (0)/(24) !Water Gun, Vital Throw, !Water Gun
- Teach Mud Shot over Growl?
- +1HP, +1 AT, +1SP
- (1, 4, 6, 0, 0, 3)

## Aqua Grunts
- Last heal of the run
- (1, 6, 6, 0, 0, 4)
- Tackle: 35 Water Gun: 25 Mud Shot: 15

## Pokefan Isabel
- Mud Shot, Mud Shot
- (1, 6, 6, 0, 0, 6)
- Tackle: 35 Water Gun: 25 Mud Shot: 13

## Pokefan Kaleb
- Mud Shot, Mud Shot
- (1, 6, 6, 0, 0, 8)
- Tackle: 35 Water Gun: 25 Mud Shot: 11

## Brendan 3
- Marshtomp is 19 at start
- Slugma Mud Shot
- Grovyle 20 Jolly (0)/(12) Absorb, Tackle!/Mud Shot!, !Mud Shot/!Tackle
- Wingull !Tackle
- Need [18,] after at level 19
- (1, 6, 6, 1, 0, 11)
- Tackle: 33 Water Gun: 25 Mud Shot: 9

## Triathlon Alyssa
- Mud Slap
- (1, 6, 6, 2, 0, 11)
- Tackle: 33 Water Gun: 25 Mud Shot: 9

## Psychic Edward
- Tackle
- (1, 6, 6, 3, 0, 11)
- Tackle: 32 Water Gun: 25 Mud Shot: 9

## Wally
- Mud Shot
- (1, 6, 6, 4, 0, 11)
- Tackle: 32 Water Gun: 25 Mud Shot: 8

## Youngster Ben
- Water Gun!, Mud Shot
- (2, 6, 6, 4, 0, 12)
- Tackle: 32 Water Gun: 24 Mud Shot: 7

## Wattson
- Mud Shot x3, Mud Shot!
- (2, 6, 6, 6, 0, 16)
- Tackle: 32 Water Gun: 24 Mud Shot: 3

## Hiker Lucas
- Water Gun, Water Gun
- (2, 6, 7, 7, 0, 16)
- Tackle: 32 Water Gun: 22 Mud Shot: 3

# Solrock
- Water Gun
- (2, 8, 7, 7, 0, 16)
- Tackle: 32 Water Gun: 21 Mud Shot: 3

## Verdanturf
- Fluffy Tail, 2-3 X-Special, Super Potion
- HP Up 1

## Magma Grunts
- Mud Shot, Tackle!
- +1 SA, +1 SP
- (2, 8, 7, 8, 0, 17)
- Tackle: 31 Water Gun: 21 Mud Shot: 2

## Tabitha
- Water Gun, Water Gun!, Water Gun!/Tackle!, Water Gun
- +1 AT, +2 SA, +1 SP
- (2, 9, 7, 10, 0, 18)
- Tackle: 31 Water Gun: 17 Mud Shot: 2

## Maxie
- Mightyena 24 Rash (0)/(18) (Bite)
- Water Gun x 3
- +3 AT, +1 SA, +1 SP
- (2, 12, 7, 11, 0, 19)
- 13+17, 13+21, 22+17, 22+21
- Take 21 damage from Mightyena
- Tackle: 30 Water Gun: 14 Mud Shot: 2

## Flannery
- Water Gun x2, Water Gun!
- +1 AT, +2 DE, +3 SA
- pick up 2nd protein
- (2, 13, 9, 14, 0, 19)
- Need [21,] after at level 28
- Tackle: 30 Water Gun: 10 Mud Shot: 2

- (2, 13, 9, 14, 0, 19) 1 solrock
- (3, 13, 9, 14, 0, 20) accuracy
- (6, 13, 9, 14, 0, 20) defense
- (6, 15, 9, 14, 0, 20) strength
- (9, 15, 9, 15, 0, 24) norman
- (10, 15, 10, 17, 0, 26) r&d
- (10, 16, 10, 17, 0, 26) poochyena
- (11, 16, 10, 17, 0, 26) wurmple
- (21, 6, 10, 17, 0, 26) hp up & kelpsy

## Accuracy Room
- Marshtomp is level 28
- Delcatty 26 Serious (0)/(31) Water Gun!, Feint Attack, Water Gun!/Mud Shot!
- Take 14-15 damage
- +1HP, +1SP
- (3, 13, 9, 14, 0, 20)
- Tackle: 30 Water Gun: 8 Mud Shot: 2

## Defense Room
- Marshtomp is level 28
- Wigglytuff 26 Hardy (0)/(31) Tackle!, Defense Curl, Mud Shot!
- +3HP
- (6, 13, 9, 14, 0, 20)
- Tackle: 29 Water Gun: 8 Mud Shot: 1

## Strength Room
- Tackle, Mud Shot!
- +2 AT
- (2, 15, 9, 15, 0, 21)
- Tackle: 28 Water Gun: 8 Mud Shot: 0

## Norman
- Spinda 27 Bashful (0)/(24) (Facade x2)
- Vigoroth 27 Sassy (0)/(24)
- Linoone 29 Lax (0)/(24)
- Slaking 31 Bashful (0)/(30) (Feint Attack)
- Need 28 health at Slaking at level 29
- 2 X. SpAttack, Water Gun!x3, Water Gun, Water Gun!
- +3 HP, +1 SA, +4 SP
- (9, 15, 9, 15, 0, 24)
- Tackle: 28 Water Gun: 3 Mud Shot: 0

# Patch EVs
- Fight 1 Wurmple, 1 Poochyena, catch one Poochyena
- (11, 15, 9, 15, 0, 24)
- Teach Surf, use HP Up (Abra)
- Reorder party as: Poochyena Abra Marshtomp

## Mauville City Redux
- HP Up 2 Route 111
- Head east to Route 119

## Rose & Deandre
- Roselia 14 Bashful (0)/(0) Absorb/Growth/Poison Sting/Stun Spore
- Absorb 10,11,12,20
- Poison String 8,9,10,16,18,20
- Zigzagoon 14 Modest (0)/(0) Growl/Tail Whip/Headbutt/Sand Attack
- Headbutt 18,19,20,21
- Roselia 14 Rash (0)/(0) Absorb/Growth/Poison Sting/Stun Spore
- Aron 14 Hasty (0)/(0) Harden/Mud Slap/Headbutt/Metal Claw
- Shroomish 14 Gentle (0)/(0) Absorb/Tackle/Stun Spore/Leech Seed
- Tackle 6,7,8,12,14,16
- Absorb 5,6,7,10,12,14
- Electrike 14 Quiet (0)/(0) Tackle/Thunder Wave/Leer/Howl
- Tackle 6,7,8,12,14,16
- +1 HP, +1 DE, +2 SA, +2 SP
- Abra gains 9 HP
- 21 HP at level 7
- Electrike 8-10
- 15, good for 56 steps
- (6, 19, 10, 18, 0, 27)
- 7, 8, 9, 13, 15, 17
- 4, 6, 8
- 17, 15, 13 damage
- Absorb
- 6, 7, 8, 11, 13, 15
- 2, 4, 6
- 19, 17, 15 damage
- Electrike
- 7, 8, 9, 13, 15, 17
- 4, 6, 8
- 17, 15, 13 damage
- 12
- Abra: 1 HP EVs

## Hatching
- Slateport HP Up adds 198 steps
- Verdanturf Late adds 321 steps
- Route 111 adds 120 steps
- ends on 0x36
- without verdanturf: f5

## EV Target
AT-HP SP-DE SD-SA
3110 1b0a 0012
- (16, 49, 10, 18, 0, 27)

## PC Visit
- Name Box 1-2
- Marshtomp: Box 2 Slot 24

## Glitzer Popping
- Use Pomeg Berry on Abra
- Corrupt PID at: 0202a574

## ACE Prep
- Lift & replace Egg, place in party
- Name Boxes 1-5
- Hatch Egg

## Move ACE
1. Glitch move `0x3110` targets 02330000 (Box 12 slot 14).
- Bootstrap: 1f zz yy xx ww ff targets address wwxxyyzz
- Bootstrap: 1f 50 00 33 02 ff (Box 12 slot 14/15) (まっ ぉい)  
2. +1 pokemon jumps (B+15) are possible and minimal.
3. ARM instructions fit 1 instruction per pokemon.
4. Use the high registers to avoid clobbering. (DO NOT use r0)

## TODO
- Faster alignment
- Code improvements

## Box Name Input
- Bootstrap: 1F 09 18 03 02 FF (Box 1 name; THUMB) (まけねうい)
- Short prelude to overwrite instructions
- PokemonStorage+0x8344
- When bootstrap is at 02330000, start at 02031808
r0: 0 r1: 080a5113 r2: ffffffff r3: 03005b88
r4: 020382bc r6: jump address
r8: 0
1. Setup key input
2. Write lower 8 bits
3. Loop unless L&R pressed
```
Box1: @ 02 4D 34 1D 05 DF 04 E0 (いぷゃへおkえl)
LDR r5,[pc,#8]  4D02 @ r5=REG_KEY_INPUT
ADD r4,r6,#4    1D34 @ r4=start of loop (SWI)
SWI #5          DF05
B Box3          E004
Box2: @ xx xx xx 30 01 00 04 (ぃぃぃぃあ え)
.space 3
.4byte 0x04000130 @ REG_KEYINPUT
Box3: @ 29 68 71 77 01 4B 04 E0 (るネムラ ゥぽ えl)
LDR r1,[r5]     6829 @ r1=keys
STRB r1,[r6]    7031 @ write keys
LDR r3,[pc,#4]  4B01 @ r3=0x300
B Box5          E004
Box4: @ xx 00 03 (  う)
.space 1
.2byte 0x300
Box5: @ 01 36 19 42 00 D0 20 47 (あょのぢ Vみび)
ADD r6,#1       3601
TST r1,r3       4219 @ Z=L&R
BEQ target      D000
BX r4           4720 @ loop to SWI
target:
```

## Credits Warp (ARM)
1. set task func to SetCallback2AfterHallOfFameDisplay
2. hang animation
3. return
```
ADD r12,r1,0x56     e281c056 # r1=080a5169
ADD r12,r12,0xee    E28ccCEE # r1=080B3F69
ADD r12,r12,0xc0    E28cc80C # r1=08173f69
STR r12,[r3-0x28]   E503c028 # set task
STR r1,[r4-0x22c]   E504122C # hang animation
STB r2,[r4-0x220]   E5442220 # set sound count to ff
BX r1               e12fff1e
```

## Map group (ARM)
1. set map group
2. end animation
3. return
```
LDR r11,[r3-0x9c]   E513B09C # r11=saveBlock1
MOV r12,16          E3A0C010
STB r12,[r11+4]     E5CBC004 # store map
STB r0,[r4-543]     E544021F # make inactive
STB r2,[r4-541]     E544221d # set sound count to ff
BX lr               e12fff1e
```

## Input Bootstrap (ARM)
1. setup key input
2. write lower 8 bits consecutively
3. loop until L&R pressed
```
STREQ r0,[r0]       04000130 # REG_KEYINPUT
LDR r5,[r6]         E5965000 # r5=REG_KEYINPUT
SWILS #5            9F050000 # C=0 or Z=1
LDR r1,[r5]         E5951000 # R1=keys
STB r1,[r6+0x280]   E5C61280 # store at next
ADD r6,#1           E2866001
AND r1,#0x3f        E2110C3F # Z=L&R
LDRNE r0,[pc-0x198] 143F0198 # pseudo-BNE
```

## 7 instruction bootstrap (ARM)
```
LDRT r5,[r6,#0x190]   E5B65190 # r5=REG_KEYINPUT
SWILS #5              9F050000 # C=0 or Z=1
LDR r1,[r5]           E5951000 # R1=keys
STB r1,[r6+1]         E4C61001 # write keys
AND r1,#0x300         E2110C03 # Z=L&R
STREQ r0,[r0]         04000130 # REG_KEYINPUT
LDRNET r0,[pc-0x148]  143F0148 # pseudo-BNE
```

## ARM Box Names (5 Boxes) (Used in TAS)
- Box names start around 02071800
- ACE Vector is 0206FEFE
```
box_01: @ (そタッmダみっ♀q)
mov r6,pc             91A0600F
ldr! r5, [r6,#32]     E5B65020 @ r5=REG_KEYINPUT, r6+=0x20
box_02: @ (おおポ たドド)
swils #5              9F0505FF @ C=0 or Z=1
ldr r1,[r5]           95951000 @ r1=keys
box_03: @ (いいあたLp)
                      0202FFFF
stb! r1, [r6,#1]      E4C61001 @ write keys, r6+=1
box_04: @ (あぃせちて)
                      01FFFFFF
tsts r1,#0x300        13110E30 @ Z=L&R
                      FFFFFFFF
box_05: @ (や ぜとぃあ え)
ldrne! r0,[pc-#28]    143F0024 @ pseudo-BNE to swi
                      04000130 @ REG_KEYINPUT
```

## 0x615 Warp Code (JPN)
- For species 0x615 (21 HP 6 AT)
- r1: 0206FEFE
- r14: 080066FF
- Replace first * with the character for map group
- Replace second * with the character for map ID
- [Character map](https://bulbapedia.bulbagarden.net/wiki/Character_encoding_in_Generation_III#Japanese)
- Hall of Fame: Group:ID: 16:11 or 0x10:0x0B, characters: た and さ
- Faraway Island Group:ID 26:56 or 0x1A:0x38
- Birth Island Group:ID 26:58 or 0x1A:0x3A
- Navel Rock Group:ID 26:66 or 0x1A:0X42
- Southern Island Group:ID 26:09 or 0x1A:0x09
```
box_01: (り ポqし♂…o)
ldr r0,[pc+0x30]    E59F0028 @ r0=CB2_LoadMap2+1
movs r11,0x3000000  E3B0B50C
box_02: ( ?』お/ゴn ) @ first and last are spaces
                    B2AC00FF
add r11,0x5000      E28BBA05
box_03: (?』x/パq  )
                    B2ACFF00
ldr r11,[r11+0xaec] E59BBAEC @ r11=&saveBlock1
box_04: (E*Fッo   )
                    BFFF0000
mov r12,xx          E3A0C0xx @ r12=map group
                    FF000000
box_05: (*Rザn」FQm)
add r12,xx00        E28CCCxx @ r12=group:id
strh r12,[r11+4]    E1CBC0B4
box_06: ( ?』ナケくくた) @ first is space
                    B2AC00FF
                    08085965 @ CB2_LoadMap2+1
box_07: (ぁm) @ small ぁ on blue screen
                    E12FFF10
```

## JPN Sprite ACE
- Ralts must be level 4
- Give Exp. Share to DOTS
- 24 28 (5) 28 22 (6) 22 22 (7) (Growth) 22 10 10 16 10 10 (8) (320 total EXP)
- Marill Poochyena (5) Poochyena Poochyena (6) Wurmple Wurmple (7) Poochyena Poochyena Poochyena Wurmple Poochyena Poochyena
- Marill: 2 HP, Poochyena x8: 8 AT, Wurmple x3: 3 HP
- Take Exp. Share from DOTS
- Use 9 HP Ups on DOTS
- HP: 95 AT: 8
- CreatedHatchedMon -> CreateMon -> CreateBoxMon 0x080677A0 -> GetSpeciesName, GiveBoxMonInitialMoveset (0x08068DB0)
- 08068E36 (possible hang in GiveBoxMonInitialMoveset)
- 080066FC (call_via_r1)l
- 0206fffe+1 (jump target)
- 0817F398 callback read
- 0806E85A (tAnimId selection)
- tAnimId = byte at sMonFrontAnimIdsTable[species - 1] = 082FA374[species - 1]
- 0817F398 callback set
  - target = sMonAnimFunctions[tAnimId] = 085D34E8[4*tAnimId]
  - target = 085D34E8[4*082FA374[species - 1]] & 0703FFFF
- gLevelUpLearnsets[4*species][i] -- Note that this reads from invalid addresses
```
Box1: @ 00 48 00 47 3D 55 17 08 ( ぶ びじオぬく)
LDR r0, [pc]
BX r0 @ Call 0817553D (Credits CB2, used in SetCallback2AfterHallOfFameDisplay)
.4byte 0817553D
```
- Place DOTS in Box 2 Slot 24

```
Species Address   EVs
03CE =  0202FFFF (206 HP 003 AT) Y
03FE =  0202FFFF (254 HP 003 AT) X
059D =  0202FEFE (157 HP 005 AT)
0615 =  0202FEFE (021 HP 006 AT) x
079D =  0202FEFE (157 HP 007 AT)
085F =  0202FFFF (095 HP 008 AT) Y -- Used in the video, summary-stable
08BB =  0202FFFF (187 HP 008 AT) Y
0A3F =  0202FEFE (063 HP 010 AT) x
0A62 =  0202FEFE (098 HP 010 AT)
0A90 =  0202FFFF (144 HP 010 AT) Y
0B5D =  0202FEFE (093 HP 011 AT)
672D =  0202FFFF (045 HP 103 AT) X
6789 =  0202FEFE (137 HP 103 AT)
69D7 =  0202FFFF (215 HP 105 AT) Y
BC35 =  0202FFFF (053 HP 188 AT) X
C185 =  0202FFFF (133 HP 193 AT)
C195 =  0202FFFF (149 HP 193 AT)
CC1F =  0202FEFE (031 HP 204 AT)
CC26 =  0202FEFE (038 HP 204 AT)
```

## Back Sprite ACE
- GetSpeciesBackAnimSet: 0817F320
- LaunchAnimationTaskForBackSprite: 0817F440
- after GetNature: 0817F47C
- store tAnimId at 0817F496
- read tAnimId at 0817F3A0 (Task_HandleMonAnimation)
- backAnimSet = sSpeciesToBackAnimSet[species] - 1 (only if not equal to zero)
- animId = 3 * backAnimSet + sBackAnimNatureModTable[nature]
- tAnimId = data[3] = sBackAnimationIds[animId]
- target = sMonAnimFunctions[tAnimId]

- u8 backAnimSet = 085D3328[species] - 1
- u8 animId = 3 * backAnimSet + 085D378F[nature]
- u8 tAnimId = 085D3744[animId]
- u32 target = 085D34E8[4*tAnimId]
