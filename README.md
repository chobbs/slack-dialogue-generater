# Slack Dialogue Generater
generate fake conversation in Slack channels

# Usage

## From the Command Line
You can also run specific scenes directly from the command line with parameters:

### Setup Virtual Environment
Before running the script, set up a Python virtual environment to manage dependencies:

```bash
# Cloned the repository, and navigate to the newly created directory
git clone https://github.com/chobbs/slack-dialogue-generater.git
cd ./slack-dialogue-generater/

# Create a virtual environment (only needs to be done once)
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install required packages
pip install slack_bolt
```

### Running the Script

```bash
# List all available scenes
# Option 1: After activating the virtual environment
python list_scenes.py

# Option 2: Using the virtual environment's Python directly
./.venv/bin/python list_scenes.py
```

```bash
# Run available scenes
# Option 1: Run a scene using Python directly (after activating the virtual environment)
python crowd.py --scene the-matrix --channel SLACK_CHANNEL_ID --delay 2 --speed 1.0

# Option 2: Run without activating (using the virtual environment's Python directly)
./.venv/bin/python crowd.py --scene the-matrix --channel SLACK_CHANNEL_ID --delay 2 --speed 1.0

# Option 3: Use the convenience shell script
./run_scene.sh the-matrix SLACK_CHANNEL_ID 2 1.0
```

### Command-line Arguments
- `--scene`: The scene key to play (required)
- `--channel`: The Slack channel ID to post in (required)
- `--delay`: Wait time in seconds before starting the scene (default: 0)
- `--speed`: Playback speed multiplier (default: 1.0)

Note: You still need to set up the Slack API tokens as environment variables:
```bash
export SLACK_APP_TOKEN=xapp-***
export SLACK_BOT_TOKEN=xoxb-***
```

# Scripts

- [The Fellowship of the Ring](#the-fellowship-of-the-ring)
- [Revenge of the Sith](#revenge-of-the-sith)
- [The Matrix](#the-matrix)
- and more!

## The Fellowship of the Ring

<img width="596" alt="image" src="https://github.com/nicwaller/crowd/assets/2850248/fd8e28cc-63d2-42cb-8da6-95b1adf369b0">
<img width="593" alt="image" src="https://github.com/nicwaller/crowd/assets/2850248/390bbc78-4cfc-4cf0-88b9-406909d33f2e">

## Revenge of the Sith

<img width="669" alt="image" src="https://github.com/nicwaller/crowd/assets/2850248/203eb253-6fc5-4277-a7b2-cc71fd9e437e">
<img width="585" alt="image" src="https://github.com/nicwaller/crowd/assets/2850248/f42f91e7-b924-4ece-979b-280e2f3b93a1">

## The Matrix

<img width="626" alt="image" src="https://github.com/nicwaller/crowd/assets/2850248/77ad3e2d-729b-4ad2-bd58-850ce127da2d">

---

## Acknowledgments

This repository is a fork of [nicwaller/crowd](https://github.com/nicwaller/crowd), with additional virtual environment setup instructions and other improvements. Full credit for the original implementation goes to [Nic Waller](https://github.com/nicwaller).
