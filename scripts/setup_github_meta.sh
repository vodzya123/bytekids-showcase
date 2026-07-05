#!/usr/bin/env bash
# Установка description, homepage и topics через GitHub API.
# Нужен GH_TOKEN или gh auth login (repo scope).
set -euo pipefail

REPO="${GITHUB_SHOWCASE_REPO:-vodzya123/bytekids-showcase}"
DESCRIPTION="ByteKids — платформа для школ программирования: демо, скриншоты, описание функций. SaaS / white-label."
HOMEPAGE="https://bytekids.online"
TOPICS='["bytekids","coding-school","education","flask","python","saas","school-management","demo","edtech","learning-management-system"]'

if ! gh auth status >/dev/null 2>&1; then
  if [[ -n "${GH_TOKEN:-}" ]]; then
    echo "$GH_TOKEN" | gh auth login --with-token
  else
    echo "Нужен GH_TOKEN или gh auth login" >&2
    exit 1
  fi
fi

gh repo edit "$REPO" --description "$DESCRIPTION" --homepage "$HOMEPAGE"

gh api --method PUT "repos/${REPO}/topics" \
  -H "Accept: application/vnd.github.mercy-preview+json" \
  -f "names=${TOPICS}"

echo "Метаданные обновлены: https://github.com/${REPO}"
