#!/bin/bash

# Usage check
if [ "$1" == "-h" ] || [ "$1" == "--help" ] || [ -z "$1" ] || [ -z "$2" ]; then
  echo "Usage: $0 <scene-key> <channel-id> [delay] [speed]"
  echo "Run 'python list_scenes.py' to see available scenes"
  exit 1
fi

SCENE=$1
CHANNEL=$2
DELAY=${3:-0}
SPEED=${4:-1.0}

# Check if SLACK_BOT_TOKEN and SLACK_APP_TOKEN are set
if [ -z "$SLACK_BOT_TOKEN" ] || [ -z "$SLACK_APP_TOKEN" ]; then
  echo "ERROR: Slack tokens not set. Please set the following environment variables:"
  echo "export SLACK_BOT_TOKEN=xoxb-***"
  echo "export SLACK_APP_TOKEN=xapp-***"
  exit 1
fi

# Run the scene
python crowd.py --scene "$SCENE" --channel "$CHANNEL" --delay "$DELAY" --speed "$SPEED"
