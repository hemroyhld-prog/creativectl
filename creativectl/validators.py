import re

class ScriptValidator:
    def __init__(self, script_text):
        self.script_text = script_text

    def extract_scenes(self):
        scene_blocks = re.split(r"(INT\.|EXT\.)", self.script_text)
        scenes = []
        scene_counter = 1

        for i in range(1, len(scene_blocks), 2):
            if i + 1 >= len(scene_blocks):
                break

            header = scene_blocks[i]
            body = scene_blocks[i + 1]

            scenes.append({
                "scene_number": scene_counter,
                "content": header + body.strip()
            })

            scene_counter += 1

        return scenes

    def count_motifs(self, motif_keywords):
        results = {}
        text_lower = self.script_text.lower()

        for motif in motif_keywords:
            results[motif] = text_lower.count(motif.lower())

        return results

    def basic_structure_report(self):
        scenes = self.extract_scenes()

        return {
            "scene_count": len(scenes),
            "has_int": bool(re.search(r"\bINT\.", self.script_text)),
            "has_ext": bool(re.search(r"\bEXT\.", self.script_text)),
            "status": "PASS" if len(scenes) > 0 else "FAIL"
        }
