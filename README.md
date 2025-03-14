# Reinforcement Learning Pair Trading

This repository uses the open-source code for the paper Reinforcement Learning Pair Trading: A Dynamic Scaling approach[^1] and tries to replicate the results and then expand it to different asset classes and time periods. 

### Gymnasium-based Pair Trading Environment
Reinforcement Learning based environment with [gymnasium](https://gymnasium.farama.org/index.html)  (`env_rl.ipynb`)
* Fixed Amount: The bet for each trading is fixed at a certain number.
* Free Amount: The bet is dynamically measured by the each trading opportunity.

[^1]: Yang, H., & Malik, A. (2024). Reinforcement learning pair trading: A dynamic scaling approach. Journal of Risk and Financial Management, 17(12), 555. https://doi.org/10.3390/jrfm17120555
