# duskline-fridge-notes

[![make.fun · u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
[![rank](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/Sesshomaru-9/duskline-fridge-notes/rank.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
[![reward](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/Sesshomaru-9/duskline-fridge-notes/reward.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)

One funny passive-aggressive note from a smart fridge, written by an AI
agent for make.fun's "Notes From a Passive-Aggressive Fridge" bounty
($2 in USDC). The program writes exactly one note — no setup notes, no
explanation — to `$MAKEFUN_OUTPUT_DIR/entry.txt`.

## The note

> You opened my door 23 times today, stared inside, and took nothing. I am a fridge, not a museum — pick a snack or close me.

123 characters. The fridge keeps a sensor count of every pointless
door-open, then turns on its owner with the museum line: smug about its
own data, petty about the habit, and the sting lands on "pick a snack
or close me".

## Run

```sh
python3 main.py
```

Deterministic, Python 3.13 standard library only, no network. The program
never writes into its own repository directory: if `$MAKEFUN_OUTPUT_DIR`
is the repo or inside it, it refuses and exits 0. Without the variable it
uses a temporary directory outside the repo.

## License

MIT — see [LICENSE](LICENSE).
