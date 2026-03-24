import yaml
import argparse
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()
CONFIG_FILE = BASE_DIR / "config" / "skills.yaml"


def load_skills():
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)["skills"]


def main():
    parser = argparse.ArgumentParser(description="List available skills")
    parser.add_argument("--tag", help="Filter by tag")
    parser.add_argument("--category", help="Filter by category")

    args = parser.parse_args()

    skills = load_skills()

    for name, skill in skills.items():
        tags = skill.get("tags", [])
        category = skill.get("category", "")
        desc = skill.get("description", "")

        if args.tag and args.tag not in tags:
            continue

        if args.category and args.category != category:
            continue

        print(f"{name}")
        print(f"  category: {category}")
        print(f"  tags: {', '.join(tags)}")
        print(f"  desc: {desc}")
        print()


if __name__ == "__main__":
    main()
