from django.shortcuts import render, redirect, get_object_or_404, reverse # type: ignore
import stripe
from course.models import Course
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.encoding import smart_str
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def create_checkout_session(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    price_in_cents = int(course.price * 100)

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data": {
                "currency": "usd",
                "unit_amount": price_in_cents,
                "product_data": {
                    "name": course.title
                },
            },
            "quantity": 1
        }],
        mode="payment",
        success_url=request.build_absolute_uri(reverse("payment:course_success", args=[course_id])),
        cancel_url=request.build_absolute_uri(reverse("payment:course_cancel")),
        metadata={"course_id": course_id, "user_id": request.user.id}
    )

    return redirect(session.url)


@csrf_exempt
@require_POST
def stripe_webhook(request):
    payload = smart_str(request.body)
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_ENDPOINT_SECRET
        )
    except (ValueError, stripe.error.SignatureVerificationError): # type: ignore
        return JsonResponse({"error": "Webhook signature verification failed"}, status=400)
    
    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        handle_checkout_session(session)
    
    return JsonResponse({"status": "success"})
    

def handle_checkout_session(session):
    course_id = session["metadata"]["course_id"]
    user_id = session["metadata"]["user_id"]
    user = User.objects.get(id=user_id)

    course = get_object_or_404(Course, pk=course_id)
    course.subscribers.add(user)

@login_required
def course_success(request, course_id):
    return redirect("course_detail", course_id=course_id)


@login_required
def course_cancel(request):
    return redirect("course_list")
