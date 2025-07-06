"""Command line interface for CommitWav."""
import json
import pathlib
import argparse
from .analysis import analyze_repo
from .composer import render_audio


def main(argv=None):
    parser = argparse.ArgumentParser(prog="commitwav")
    parser.add_argument("repo")
    parser.add_argument("--out", default="out.wav")
    args = parser.parse_args(argv)
    repo_path = pathlib.Path(args.repo)
    out_path = pathlib.Path(args.out)
    data = analyze_repo(repo_path)
    audio = render_audio(data)
    out_path.write_bytes(audio)
    (repo_path / "analysis.json").write_text(json.dumps(data, indent=2))
    print(f"Wrote {out_path}")

if __name__ == "__main__":
    main()
