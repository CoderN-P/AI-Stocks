from pathlib import Path

def get_parent_path():
    current_dir = Path(__file__).parent
    return [p for p in current_dir.parents if p.parts[-1] == "AI-Stocks"][0]