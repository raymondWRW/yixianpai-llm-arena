"""Helper: record the ONE decisive lesson + a reusable check reminder.
Usage: run_program('tan_key_sim.py') — prints the recipe and the merge-priority.
This is a REFERENCE note, not a sim driver (sim needs the harness)."""
RECIPE = ["众星拱月(+1)", "梅开二度", "星弈·断+1", "静气心法+2", "静气心法+1", "星罗棋布+1", "巽卦+1", "星弈·断"]
LESSON = (
    "vs 小布(pid3 气势体修): my R18 board LOSES 11t; upgrading ONLY 静气心法->+2 WINS 11t (he pays 21命).\n"
    "=> MERGE 静气心法 FIRST. It is the single card that decides the pid3 1v1.\n"
    "=> Always sim the EXACT board I will field (not upgraded levels).\n"
    "=> I beat every rival 100% EXCEPT pid3; the whole game hinges on upgrading enough to beat pid3."
)
if __name__ == "__main__":
    print("RECIPE:", " | ".join(RECIPE))
    print(LESSON)
