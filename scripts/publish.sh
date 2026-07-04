#!/usr/bin/env bash
# Публикация витрины на GitHub (нужен gh auth или GH_TOKEN).
set -euo pipefail
cd "$(dirname "$0")/.."

REPO="${GITHUB_SHOWCASE_REPO:-vodzya123/bytekids-showcase}"
REMOTE="git@github.com:${REPO}.git"

if ! gh auth status >/dev/null 2>&1; then
  if [[ -n "${GH_TOKEN:-}" ]]; then
    echo "$GH_TOKEN" | gh auth login --with-token
  else
    echo "GitHub CLI не авторизован. Выполните один раз:"
    echo "  gh auth login"
    echo "или:"
    echo "  GH_TOKEN=ghp_... bash scripts/publish.sh"
    exit 1
  fi
fi

if ! gh repo view "$REPO" >/dev/null 2>&1; then
  gh repo create "$REPO" \
    --public \
    --description "ByteKids — витрина платформы (демо, скрины, без исходников)" \
    --source=. \
    --remote=origin \
    --push
else
  git remote remove origin 2>/dev/null || true
  git remote add origin "$REMOTE"
  git push -u origin main
fi

echo "Готово: https://github.com/${REPO}"
