# Backrooms World Simulation

A text-based life simulation in Python. Humans are placed into the levels of a
Backrooms-style world, where they grow older, fall in love, have children, migrate
between levels, and eventually die — from the dangers of the level itself or from
the creatures that inhabit it.

Every run is different: each level gets a random threat rating, and every human and
creature is generated with random stats.

## Features

- **Levels with random threat ratings (0–5)**: from safe zones to levels where few survive
- **Humans** with a name, age, sex, strength, HP, and a hidden *love code*
- **Creatures** that you name yourself, with their own strength and HP
- **Reproduction**: compatible adults (aged 16–41) may have a child, with a chance
  based on how close their love codes are
- **Combat**: humans and creatures fight until one (or both) of them falls
- **Migration**: groups of humans move from one level to another
- **Turn-based world clock**: you advance time one tick at a time

## Requirements

- Python 3: no external libraries, only the standard `random` module

## Getting started

```bash
git clone https://github.com/Cuman000Q/own-simulations-AI-related-simulations.git
cd own-simulations-AI-related-simulations
python Simulation_world_10.py
```

The world starts with three levels (`Level-1` to `Level-3`), each populated with three
humans. You will be asked to name one creature for each level, after which the
simulation menu appears.

## Commands

| Key | Action |
|-----|--------|
| `1` | Advance the world by one tick |
| `2` | Show the humans on every level |
| `3` | Show the creatures on every level |
| `4` | List all levels |
| `5` | Add a new level |
| `6` | Add a new creature (placed on the most recently created starting level) |
| `0` | Exit the simulation |

## How a tick works

On each tick, for every level:

1. Every human ages by one year.
2. Couples of opposite sex aged 16–41 may have a child. The closer their love codes,
   the higher the chance. Couples who don't match grow slightly more compatible over time.
3. The level's threat is applied:

   | Threat | Description | Chance a human dies |
   |--------|-------------|---------------------|
   | 0 | Safe level, no threats | 0% |
   | 1–3 | Minor creatures, still survivable | 10% |
   | 4 | Dangerous, average creatures | 50% |
   | 5 | Very dangerous, low chance to survive | 85% |

4. A random human fights a random creature until one (or both) of them dies.

After all levels are processed, there is a 50% chance that a group of humans migrates
to another level.

## Example output

```
World Time: 1
Level-1: Minor creatures, still survivable
Smiler defeated Corvian
Baby born from Lioraen and Selmira. Name: Althira, Sex: M
Level-2: Safe level, no threats detected
Hound defeated Selmira
Level-3: Very dangerous, low chance to survive
Thalise died due to level danger
Facelings defeated Tavrik
```

## Project structure

```
Simulation_world_10.py   # the whole simulation
├── Human                # a person: stats, ageing, love code
├── Creature             # a monster with strength and HP
├── Levels               # one level: population, threat, reproduction, fights
└── Backrooms_World      # the world: levels, time, migration
```

## Roadmap

- [ ] Improve the levels and give each one its own character
- [ ] Make creatures unique to each level
- [ ] Add new creature types
- [ ] Death from old age (natural causes)
- [ ] Save and load a world

## Author

Made by [Cuman000Q](https://github.com/Cuman000Q).
