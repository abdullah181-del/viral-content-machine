import unittest

from engine import (
    HOOK_STYLES,
    build_prompt,
    get_hook_by_id,
    get_hook_by_name,
    get_hook_names,
    is_generic,
    parse_post_sections,
)


class EngineTests(unittest.TestCase):
    def test_hook_lookup_round_trip(self):
        hook = get_hook_by_id("curiosity")
        self.assertEqual(hook["id"], "curiosity")
        self.assertEqual(get_hook_by_name(hook["name"]), hook)
        self.assertIn(hook["name"], get_hook_names())
        self.assertGreaterEqual(len(HOOK_STYLES), 12)

    def test_prompt_contains_language_and_variation(self):
        prompt = build_prompt("AI & Tech", HOOK_STYLES[0], "Educational", 6, language="Hinglish")
        self.assertIn("Hinglish", prompt)
        self.assertIn("Educational", prompt)

    def test_generic_filter_rejects_weak_openers(self):
        self.assertTrue(is_generic("Most people don't realize this simple trick."))
        self.assertTrue(is_generic("The truth is you can do it."))
        self.assertFalse(is_generic("A quiet inbox can expose a broken offer."))

    def test_parse_post_sections(self):
        sections = parse_post_sections("Hook line\n\nValue line\n\nCTA line")
        self.assertEqual(sections["hook"], "Hook line")
        self.assertEqual(sections["body"], "Value line")
        self.assertEqual(sections["cta"], "CTA line")


if __name__ == "__main__":
    unittest.main()
