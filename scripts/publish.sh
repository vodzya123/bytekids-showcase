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

PROFILE_REPO="${GITHUB_PROFILE_REPO:-vodzya123/vodzya123}"
PROFILE_DIR="${GITHUB_PROFILE_DIR:-../vodzya123-profile}"
if [[ -d "${PROFILE_DIR}/.git" ]] && [[ -f "${PROFILE_DIR}/README.md" ]]; then
  echo "Публикация README профиля: ${PROFILE_REPO}"
  git -C "${PROFILE_DIR}" push origin main 2>/dev/null || git -C "${PROFILE_DIR}" push -u origin main
fi
