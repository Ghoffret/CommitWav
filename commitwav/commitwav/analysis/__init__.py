"""Repository analysis utilities."""
import subprocess
import pathlib
from datetime import datetime


def analyze_repo(repo_path: pathlib.Path):
    """Return simple commit metadata for repo."""
    try:
        result = subprocess.run(
            ["git", "-C", str(repo_path), "log", "--pretty=%H %ct"],
            capture_output=True, text=True, check=True
        )
        lines = result.stdout.strip().splitlines()
    except subprocess.CalledProcessError:
        lines = []
    commits = []
    if not lines:
        commits.append({"sha": "0" * 40, "timestamp": int(datetime.utcnow().timestamp())})
    else:
        for line in lines:
            sha, ts = line.split()
            commits.append({"sha": sha, "timestamp": int(ts)})
    return {"commits": commits, "generated": datetime.utcnow().isoformat()}
