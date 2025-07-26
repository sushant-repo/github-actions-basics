import subprocess

def test_hello_script_runs():
    result = subprocess.run(["python", "scripts/hello.py"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Hello" in result.stdout
