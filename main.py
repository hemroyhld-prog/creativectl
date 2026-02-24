import sys
import os
import json
from validators import ScriptValidator
from security import lock_file, verify_lock
from emotional_nlp import EmotionalAnalyzer


def load_script(file_path):
    if not os.path.exists(file_path):
        print("File not found.")
        sys.exit(1)

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def enforce_integrity(file_path):
    if not verify_lock(file_path):
        print("Locked file modified. Validation blocked.")
        sys.exit(1)


def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <command> <scriptfile>")
        sys.exit(1)

    command = sys.argv[1]
    script_file = sys.argv[2]

    script_text = load_script(script_file)
    enforce_integrity(script_file)

    validator = ScriptValidator(script_text)

    if command == "validate":
        report = validator.basic_structure_report()
        print(json.dumps(report, indent=2))
        if report["status"] == "FAIL":
            sys.exit(1)

    elif command == "motif-report":
        motifs = ["cross", "names", "ledger", "fracture"]
        report = validator.count_motifs(motifs)
        print(json.dumps(report, indent=2))

    elif command == "emotion-report":
        analyzer = EmotionalAnalyzer(script_text)
        report = analyzer.analyze_sentiment_density()
        print(json.dumps(report, indent=2))

    elif command == "lock":
        lock_file(script_file)

    elif command == "verify":
        if verify_lock(script_file):
            print("Integrity verified.")
        else:
            sys.exit(1)

    else:
        print("Unknown command.")
        sys.exit(1)


if __name__ == "__main__":
    main()