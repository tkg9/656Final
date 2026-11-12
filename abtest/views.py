import random

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from .models import Visit

SESSION_KEY = "abtest_visit_id"


def _current_visit(request):
    visit_id = request.session.get(SESSION_KEY)
    if visit_id:
        visit = Visit.objects.filter(pk=visit_id).first()
        if visit:
            return visit
    visit = Visit.objects.create(variant=random.choice(["kudos", "thanks"]))
    request.session[SESSION_KEY] = visit.pk
    return visit


def page(request):
    visit = _current_visit(request)
    return render(request, "abtest/page.html", {
        "variant": visit.variant,
        "members": settings.TEAM_MEMBERS,
        "team": settings.TEAM_NICKNAME,
    })


@require_POST
def click(request):
    visit = get_object_or_404(Visit, pk=request.session.get(SESSION_KEY, 0))
    if visit.clicked_at is None:
        visit.clicked_at = timezone.now()
        visit.save(update_fields=["clicked_at"])
    return redirect("abtest-page")


def stats(request):
    counts = {}
    for variant in ("kudos", "thanks"):
        visits = Visit.objects.filter(variant=variant)
        counts[variant] = {
            "impressions": visits.count(),
            "clicks": visits.filter(clicked_at__isnull=False).count(),
        }

    def rate(v):
        c = counts[v]
        return c["clicks"] / c["impressions"] if c["impressions"] else 0.0

    preferred = "thanks" if rate("thanks") > rate("kudos") else "kudos"
    return JsonResponse({"preferred": preferred, **counts})
