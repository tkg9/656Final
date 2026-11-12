import re
from datetime import datetime, timezone as dt_tz

from django.core.management import call_command
from django.contrib.auth import get_user_model
from django.test import TestCase

from abtest.models import Visit

PAGE = "/bdcabb0"


def buttons(html):
    return re.findall(r'<button id="abtest"[^>]*>\s*(.*?)\s*</button>', html, re.S)


class AbPageTests(TestCase):
    def test_page_is_public_with_one_button(self):
        r = self.client.get(PAGE)
        self.assertEqual(r.status_code, 200)
        found = buttons(r.content.decode())
        self.assertEqual(len(found), 1)
        self.assertIn(found[0], ("kudos", "thanks"))
        self.assertContains(r, "quaint-chinchilla")

    def test_reload_keeps_variant_and_one_impression(self):
        first = buttons(self.client.get(PAGE).content.decode())[0]
        for _ in range(3):
            self.assertEqual(buttons(self.client.get(PAGE).content.decode())[0], first)
        self.assertEqual(Visit.objects.count(), 1)

    def test_new_visitors_get_both_variants(self):
        variants = set()
        for _ in range(40):
            self.client.cookies.clear()
            variants.add(buttons(self.client.get(PAGE).content.decode())[0])
        self.assertEqual(variants, {"kudos", "thanks"})
        self.assertEqual(Visit.objects.count(), 40)

    def test_click_counts_once_and_redirect_is_not_an_impression(self):
        variant = buttons(self.client.get(PAGE).content.decode())[0]
        r = self.client.post(f"{PAGE}/click", follow=True)
        self.assertEqual(buttons(r.content.decode())[0], variant)
        self.client.post(f"{PAGE}/click", follow=True)
        visit = Visit.objects.get()
        self.assertIsNotNone(visit.clicked_at)
        self.assertEqual(Visit.objects.count(), 1)

    def test_click_without_visit_is_rejected(self):
        self.assertEqual(self.client.post(f"{PAGE}/click").status_code, 404)


class StatsTests(TestCase):
    def make(self, variant, impressions, clicks):
        now = datetime.now(dt_tz.utc)
        for i in range(impressions):
            Visit.objects.create(variant=variant, clicked_at=now if i < clicks else None)

    def test_preferred_is_higher_click_rate(self):
        self.make("kudos", 10, 2)
        self.make("thanks", 4, 2)
        data = self.client.get(f"{PAGE}/stats").json()
        self.assertEqual(data["preferred"], "thanks")
        self.assertEqual(data["kudos"], {"impressions": 10, "clicks": 2})

    def test_empty_database_still_answers(self):
        self.assertIn(self.client.get(f"{PAGE}/stats").json()["preferred"], ("kudos", "thanks"))


class SeedTests(TestCase):
    def test_seed_creates_loginable_accounts_and_is_rerunnable(self):
        call_command("seed")
        call_command("seed")
        self.assertEqual(get_user_model().objects.count(), 2)
        self.assertTrue(self.client.login(username="admin@example.com", password="stage-door-lantern"))
        self.assertTrue(self.client.login(username="member@example.com", password="curtain-call-rope"))

    def test_login_page_loads(self):
        self.assertEqual(self.client.get("/login/").status_code, 200)
