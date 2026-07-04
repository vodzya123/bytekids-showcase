#!/usr/bin/env python3
"""Capture showcase screenshots from the live demo (fictional data only)."""
from __future__ import annotations

import os
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote

import requests
from playwright.sync_api import sync_playwright

BASE_URL = os.environ.get("BYTEKIDS_BASE_URL", "https://bytekids.online").rstrip("/")
OUT_DIR = Path(__file__).resolve().parent.parent / "screenshots"
VIEWPORT = {"width": 1440, "height": 900}
LOGIN_PATHS = {
    "admin": "/login_admin",
    "teacher": "/login_teacher",
    "student": "/login_student",
}
DEMO_GROUP = "Python Junior — Демо A"
DEMO_STUDENT = "demostu_alisa001"


@dataclass(frozen=True)
class Shot:
    role: str
    path: str
    outfile: str
    wait_ms: int = 2800
    hide_notifications: bool = True
    click_selector: str | None = None
    run_js: str | None = None


HIDE_SPLASH_JS = "document.getElementById('splashLottie')?.classList.add('hidden');"


def build_student_shots(username: str) -> list[Shot]:
    q = "demo_embed=1"
    eq = f"embed=1&{q}"
    base = f"/modules/junior?{q}"
    open_stats_js = HIDE_SPLASH_JS + """
(function(){
  var n = 0;
  var timer = setInterval(function () {
    if (window.ModulesStatsSpa && typeof window.ModulesStatsSpa.open === 'function') {
      window.ModulesStatsSpa.open({ fromRouter: true });
      clearInterval(timer);
    } else if (++n > 50) {
      clearInterval(timer);
    }
  }, 200);
})();
"""
    return [
        Shot("student", base, "student/01-modules-overview.png", wait_ms=5000, run_js=HIDE_SPLASH_JS),
        Shot(
            "student",
            base,
            "student/02-module-python.png",
            wait_ms=2500,
            run_js=HIDE_SPLASH_JS + "document.getElementById('m1')?.scrollIntoView({block:'center'});",
        ),
        Shot(
            "student",
            base,
            "student/03-module-turtle.png",
            wait_ms=2500,
            run_js=HIDE_SPLASH_JS + "document.getElementById('m2')?.scrollIntoView({block:'center'});",
        ),
        Shot(
            "student",
            base,
            "student/04-module-pygame.png",
            wait_ms=2500,
            run_js=HIDE_SPLASH_JS + "document.getElementById('m4')?.scrollIntoView({block:'center'});",
        ),
        Shot("student", f"/homework?{eq}", "student/05-homework.png", wait_ms=4000),
        Shot("student", f"/shop?{eq}", "student/06-shop.png", wait_ms=4000),
        Shot("student", f"/student_page/{username}?{eq}", "student/07-profile.png", wait_ms=4000),
        Shot("student", base, "student/08-stats.png", wait_ms=8000, run_js=open_stats_js),
        Shot("student", f"/project?{eq}", "student/09-projects.png", wait_ms=5000),
        Shot("student", f"/my_lab?{eq}", "student/10-portfolio.png", wait_ms=5000),
        Shot("student", f"/dopka_gallery?discipline=word&{eq}", "student/11-extra-lessons-word.png", wait_ms=4000),
        Shot("student", f"/dopka_gallery?discipline=python&{eq}", "student/12-extra-lessons-python.png", wait_ms=4000),
        Shot("student", f"/task1?{q}", "student/13-task-hello-world.png", wait_ms=3000),
        Shot("student", f"/task1_turtle?{q}", "student/14-task-turtle.png", wait_ms=3000),
    ]


SHOTS: list[Shot] = [
    # Demo
    Shot("public", "/demo", "demo/01-registration.png", wait_ms=1200, hide_notifications=False),
    Shot("public", "/login?demo_embed=1", "demo/02-login.png", wait_ms=1500, hide_notifications=False),
    # Admin
    Shot("admin", "/admin_full?demo_embed=1", "admin/01-dashboard.png"),
    Shot("admin", "/schedule?demo_embed=1", "admin/02-schedule.png", wait_ms=3500),
    Shot("admin", "/payments_control?demo_embed=1", "admin/03-payments.png", wait_ms=3500),
    Shot("admin", "/analytics_tailwind?demo_embed=1", "admin/04-analytics.png", wait_ms=3500),
    Shot("admin", "/booking_orders?demo_embed=1", "admin/05-booking-orders.png"),
    Shot("admin", "/remarks?demo_embed=1", "admin/06-remarks.png"),
    Shot("admin", "/show_attendance?demo_embed=1", "admin/07-attendance.png", wait_ms=3500),
    Shot("admin", "/forms?embed=1&demo_embed=1", "admin/08-forms.png"),
    Shot("admin", "/homework_manager?demo_embed=1", "admin/09-homework.png"),
    Shot("admin", "/student_monthly_reports?demo_embed=1", "admin/10-student-reports.png"),
    Shot(
        "admin",
        f"/student_page/{DEMO_STUDENT}?embed=1&demo_embed=1",
        "admin/11-student-card.png",
    ),
    Shot(
        "admin",
        f"/group/{quote(DEMO_GROUP, safe='')}?embed=1&demo_embed=1",
        "admin/12-group.png",
    ),
    Shot("admin", "/assigned_projects?demo_embed=1", "admin/13-assigned-projects.png"),
    Shot("admin", "/admin_full?demo_embed=1", "admin/14-notifications.png", wait_ms=4000, hide_notifications=False),
    # Teacher
    Shot("teacher", "/teacher?demo_embed=1", "teacher/01-dashboard.png"),
    Shot("teacher", "/schedule?demo_embed=1", "teacher/02-schedule.png", wait_ms=3500),
    Shot("teacher", "/teacher/income?embed=1&demo_embed=1", "teacher/03-income.png", wait_ms=3500),
    Shot("teacher", "/remarks?demo_embed=1", "teacher/04-remarks.png"),
    Shot(
        "teacher",
        f"/student_page/{DEMO_STUDENT}?embed=1&demo_embed=1",
        "teacher/05-student-card.png",
    ),
    Shot(
        "teacher",
        f"/group/{quote(DEMO_GROUP, safe='')}?embed=1&demo_embed=1",
        "teacher/06-group.png",
    ),
    Shot("teacher", "/booking_orders?demo_embed=1", "teacher/07-booking-orders.png"),
]


def register_demo() -> dict:
    sys.path.insert(0, "/root")
    from demo_platform import register_demo_access

    return register_demo_access(
        contact_name="Витрина GitHub",
        contact_email="showcase@bytekids.online",
        contact_company="ByteKids Showcase",
        ip="127.0.0.1",
    )


def credentials_for_role(result: dict, role: str) -> tuple[str, str]:
    for account in result["accounts"]:
        if account["role"] == role:
            return account["username"], account["password"]
    raise KeyError(f"role not found: {role}")


def http_login(role: str, username: str, password: str) -> requests.Session:
    session = requests.Session()
    login_path = LOGIN_PATHS[role]
    response = session.post(
        f"{BASE_URL}{login_path}",
        params={"demo_embed": "1"},
        data={"username": username, "password": password, "demo_embed": "1"},
        allow_redirects=True,
        timeout=60,
    )
    if response.status_code >= 400:
        raise RuntimeError(f"login failed for {role}: HTTP {response.status_code}")
    if "session=" not in str(session.cookies):
        raise RuntimeError(f"login failed for {role}: no session cookie")
    return session


def playwright_context_with_cookies(browser, http_session: requests.Session | None):
    context = browser.new_context(viewport=VIEWPORT, locale="ru-RU")
    if not http_session:
        return context
    cookies = []
    for cookie in http_session.cookies:
        cookies.append(
            {
                "name": cookie.name,
                "value": cookie.value,
                "domain": cookie.domain or "bytekids.online",
                "path": cookie.path or "/",
            }
        )
    if cookies:
        context.add_cookies(cookies)
    return context


def prepare_page(page, hide_notifications: bool) -> None:
    if hide_notifications:
        page.add_init_script(
            """
            window.addEventListener('DOMContentLoaded', () => {
              const el = document.getElementById('formNotifications');
              if (el) el.remove();
            });
            """
        )


def screenshot(page, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    page.screenshot(path=str(path), full_page=False)
    print(f"saved {path.relative_to(OUT_DIR.parent)}")


def capture_demo_registration() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport=VIEWPORT, locale="ru-RU")
        page = context.new_page()
        page.goto(f"{BASE_URL}/demo", wait_until="networkidle")
        page.locator('input[name="contact_name"]').fill("Витрина GitHub")
        page.locator('input[name="contact_email"]').fill("showcase@bytekids.online")
        page.locator('input[name="contact_company"]').fill("ByteKids Showcase")
        page.locator('button[type="submit"]').click()
        page.wait_for_load_state("networkidle")
        time.sleep(1.2)
        screenshot(page, OUT_DIR / "demo/01-registration.png")
        browser.close()


def capture_page(page, shot: Shot) -> None:
    wait_until = "domcontentloaded" if shot.role == "student" else "networkidle"
    timeout = 60000 if shot.role == "student" else 30000
    page.goto(f"{BASE_URL}{shot.path}", wait_until=wait_until, timeout=timeout)
    if shot.run_js:
        try:
            page.evaluate(shot.run_js)
        except Exception as exc:
            print(f"warn js {shot.outfile}: {exc}")
    if shot.click_selector:
        try:
            page.wait_for_selector(shot.click_selector, timeout=20000, state="visible")
            page.locator(shot.click_selector).first.click(timeout=5000)
        except Exception as exc:
            print(f"warn click {shot.outfile}: {exc}")
    time.sleep(shot.wait_ms / 1000)


def capture_shots(result: dict, only_role: str | None = None) -> None:
    sessions: dict[str, requests.Session] = {}
    student_username, _ = credentials_for_role(result, "student")
    all_shots = SHOTS + build_student_shots(student_username)
    if only_role:
        all_shots = [s for s in all_shots if s.role == only_role]
    for role in ("admin", "teacher", "student"):
        username, password = credentials_for_role(result, role)
        sessions[role] = http_login(role, username, password)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for shot in all_shots:
            if shot.outfile == "demo/01-registration.png":
                continue
            http_session = None if shot.role == "public" else sessions[shot.role]
            context = playwright_context_with_cookies(browser, http_session)
            page = context.new_page()
            prepare_page(page, shot.hide_notifications)
            capture_page(page, shot)
            screenshot(page, OUT_DIR / shot.outfile)
            context.close()
        browser.close()


def cleanup_legacy_files() -> None:
    legacy = [
        "demo-access.png",
        "admin.png",
        "teacher.png",
        "schedule.png",
        "student/01-modules.png",
        "student/02-extra-lessons.png",
    ]
    for name in legacy:
        path = OUT_DIR / name
        if path.exists():
            path.unlink()
            print(f"removed legacy {name}")


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Capture ByteKids showcase screenshots from demo.")
    parser.add_argument("--only-role", choices=("admin", "teacher", "student", "public"))
    args = parser.parse_args()

    print(f"base url: {BASE_URL}")
    result = register_demo()
    print(f"batch: {result['batch_id']}")
    cleanup_legacy_files()
    if not args.only_role or args.only_role == "public":
        capture_demo_registration()
    capture_shots(result, only_role=args.only_role)
    total = sum(1 for _ in OUT_DIR.rglob("*.png"))
    print(f"done: {total} screenshots in {OUT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
