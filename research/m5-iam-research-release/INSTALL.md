# Installation

## From the release ZIP (members of the public)

1. Download `m5-iam-free-v0.2.0.zip` and its `.sha256` file from the release.
2. Check the download: `shasum -a 256 -c m5-iam-free-v0.2.0.zip.sha256`
3. Unzip it and check every file: `shasum -a 256 -c PACKAGE-CHECKSUMS.sha256`
4. Open `reference-implementation/m5-iam-free/` and double-click
   **Start M5 IAM.command** (macOS) or **Start M5 IAM.bat** (Windows).
   On macOS, the first time, right-click the launcher and choose **Open**.
5. The app opens in your browser at `http://127.0.0.1:8756/`. Your pod is
   created in `~/M5POD-IAM` when you attest.

Requirement: Python 3.9 or later. Nothing else is installed.

## From source (researchers and reviewers)

```bash
git clone https://github.com/TitleChain-Foundation/M5-AI-Sovereign-Commons.git
cd M5-AI-Sovereign-Commons
python3 -m pip install -r requirements-dev.txt     # pytest and schema tools, for the tests only
python3 -m pytest tests/test_m5_iam_free.py -q
python3 reference-implementation/m5-iam-free/demo/reproduce.py
python3 reference-implementation/m5-iam-free/m5_iam_app.py --pod /tmp/iam-trial
```

Use `--pod` to keep trial pods out of your home folder. To remove a pod, delete
its folder.
