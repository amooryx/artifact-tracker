import contextlib
import io
import unittest
from unittest.mock import patch

import artifact_tracker


class AuthorisationTests(unittest.TestCase):
    def test_end_of_file_fails_closed_with_clear_message(self):
        output = io.StringIO()
        with patch("builtins.input", side_effect=EOFError), contextlib.redirect_stdout(output):
            result = artifact_tracker.authorised(assume_yes=False)

        self.assertFalse(result)
        self.assertIn("authorisation input unavailable; refusing to run.", output.getvalue())

    def test_yes_option_skips_prompt(self):
        with patch("builtins.input") as mocked_input:
            self.assertTrue(artifact_tracker.authorised(assume_yes=True))

        mocked_input.assert_not_called()

    def test_denial_does_not_run_workflow(self):
        output = io.StringIO()
        with patch("builtins.input", side_effect=EOFError), patch(
            "artifact_tracker.run"
        ) as mocked_run, contextlib.redirect_stdout(output):
            result = artifact_tracker.main(["example.test"])

        self.assertEqual(result, 1)
        mocked_run.assert_not_called()
        self.assertIn("authorisation not confirmed; nothing was done.", output.getvalue())

    def test_confirmed_authorisation_runs_workflow(self):
        with patch("builtins.input", return_value="y"), patch(
            "artifact_tracker.run", return_value=0
        ) as mocked_run, contextlib.redirect_stdout(io.StringIO()):
            result = artifact_tracker.main(["example.test"])

        self.assertEqual(result, 0)
        mocked_run.assert_called_once()


if __name__ == "__main__":
    unittest.main()
