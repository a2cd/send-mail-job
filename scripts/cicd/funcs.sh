#!/bin/sh

setup_ssh() {
  mkdir -p ~/.ssh/
  echo "$SSH_PRIVATE_KEY" > ~/.ssh/github_actions.pri.key
  chmod 600 ~/.ssh/github_actions.pri.key
  cat >> ~/.ssh/config <<END
Host remote-server
  HostName $SSH_HOST
  User $SSH_USER
  IdentityFile ~/.ssh/github_actions.pri.key
  StrictHostKeyChecking no
END
}

cicd() {
  ssh remote-server <<EOF
bash -c 'set -x; \
cd /usr/local/repo/send-mail-job/ && \
git pull origin main && \
uv sync && \
(pids=$(pgrep -f "python3 main.py"); if [ -n "$pids" ]; then kill -9 "$pids"; fi) && \
(nohup uv run main.py > /dev/null 2>&1 < /dev/null & disown)'
EOF
}