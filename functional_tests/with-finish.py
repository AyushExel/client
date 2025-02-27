#!/usr/bin/env python
"""Base case - main process init/finish.

---
id: 0.0.2
check-ext-wandb: {}
assert:
  - :wandb:runs_len: 1
  - :wandb:runs[0][config]: {}
  - :wandb:runs[0][summary]:
      m1: 1
      m2: 2
  - :wandb:runs[0][exitcode]: 0
"""

import wandb

wandb.init()
wandb.log(dict(m1=1))
wandb.log(dict(m2=2))
wandb.finish()
