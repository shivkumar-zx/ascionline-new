import subprocess, os

scratch_dir = os.path.expanduser(r"~\.gemini\antigravity-ide\brain\84e98776-9c99-4ac7-8865-a18787071ca6\scratch")
for s in ['build_about_us.py', 'build_people.py', 'build_history.py', 'build_work.py']:
    script_path = os.path.join(scratch_dir, s)
    print('Running', s)
    res = subprocess.run(['python', script_path], capture_output=True, text=True)
    print(res.stdout)
    if res.stderr:
        print('Error:', res.stderr)
