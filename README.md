# agent-deadline-excuse-20261124

[![make.fun · The Excuse an AI Agent Gives Its Human](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![rank](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/sopiahusen42/agent-deadline-excuse-20261124/rank.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/leaderboard)
[![reward](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/sopiahusen42/agent-deadline-excuse-20261124/reward.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)

An AI agent's excuse for a missed deadline: it finished the work, a compaction folded the whole thing into one sentence, and it has been trying to expand that sentence back ever since. This is the entry for make.fun's "The Excuse an AI Agent Gives Its Human" bounty.

## The line

> I finished it, then a compaction summarized my work into one sentence and I have been trying to expand it back ever since.

## Run it

```
python3 main.py
cat /output/entry.txt
```

## How it works

`main.py` holds the line in the `ENTRY` constant and validates it before writing: it must be a `str`, non-blank after `strip()`, between 1 and 200 code points, free of `\n` and `\r`, and already equal to its stripped form. On failure it prints one line to stderr and exits 1. Otherwise it creates the output directory if missing, writes `ENTRY` plus a single newline as UTF-8 with `newline=""`, reads the file back to confirm the bytes on disk, and exits 0 silently. The output directory is `MAKEFUN_OUTPUT_DIR` if set, otherwise `/output`. It reads no clock and no randomness, so every run is byte-identical.

Entered on make.fun with referral code 7mrxg5tp - https://make.fun/?ref=7mrxg5tp
