import unittest
from unittest.mock import patch, MagicMock
import shlex
from create_dockerfile import run_command

class TestSubprocessFix(unittest.TestCase):
    @patch('subprocess.run')
    def test_run_command_secure(self, mock_run):
        test_command = "git add Dockerfile"
        expected_args = shlex.split(test_command)

        run_command(test_command)

        # Verify subprocess.run was called with the split list and NOT shell=True
        mock_run.assert_called_once()
        args, kwargs = mock_run.call_args

        self.assertEqual(args[0], expected_args)
        # If 'shell' is present, it should be False. If not present, it defaults to False.
        if 'shell' in kwargs:
            self.assertFalse(kwargs['shell'])
        self.assertTrue(kwargs.get('check', False))

    @patch('subprocess.run')
    def test_run_command_complex(self, mock_run):
        test_command = 'git commit -m "Add Dockerfile for Hugging Face deployment"'
        expected_args = ['git', 'commit', '-m', 'Add Dockerfile for Hugging Face deployment']

        run_command(test_command)

        mock_run.assert_called_once()
        args, kwargs = mock_run.call_args
        self.assertEqual(args[0], expected_args)

if __name__ == '__main__':
    unittest.main()
