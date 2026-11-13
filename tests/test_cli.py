import os
import tempfile
import unittest

from cardgen.cli import main


class CliTest(unittest.TestCase):
    def test_missing_file_returns_2(self):
        self.assertEqual(main(["no_such_file.md"]), 2)

    def test_existing_file_returns_0(self):
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
            f.write("## Вопрос\nОтвет\n")
        try:
            self.assertEqual(main([f.name]), 0)
        finally:
            os.remove(f.name)


if __name__ == "__main__":
    unittest.main()
