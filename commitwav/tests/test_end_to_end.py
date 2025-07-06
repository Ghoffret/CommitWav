import pathlib, json, subprocess


def test_smoke():
    repo = pathlib.Path(__file__).parent
    out = repo / "smoke.wav"
    subprocess.check_call(["python", "-m", "commitwav", str(repo), "--out", str(out)])
    assert out.exists() and out.stat().st_size > 10_000
    meta = json.loads((repo/"analysis.json").read_text())
    assert len(meta["commits"]) > 0
