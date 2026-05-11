"""
HOWLING MUNE — Stripe Payment Link Creator
==========================================
Run this ONCE from your terminal:
  python3 create_payment_links.py

You need your SECRET key (sk_live_...) — never share this publicly.
The script creates 3 Payment Links and prints the URLs.
Paste those URLs into your payment page.

Stripe API version: 2026-04-22.dahlia
"""

import sys
import os

import stripe

# Set this in your shell before running:
#   export STRIPE_SECRET_KEY="sk_live_..."
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY", "")

if not STRIPE_SECRET_KEY:
    print("\n❌  Set STRIPE_SECRET_KEY in your environment before running this script.\n")
    sys.exit(1)

stripe.api_key = STRIPE_SECRET_KEY
stripe.api_version = "2026-04-22.dahlia"

stages = [
    {
        "name": "HOWLING MUNE — Stage 1: Foundation + Clarity",
        "amount": 250000,   # in cents = $2,500.00 USD
        "description": (
            "Foundation + Clarity phase. Includes: doctrine extraction, "
            "first offer + audience decision, collective positioning map, "
            "system architecture, required asset list, 30-day action map."
        ),
        "metadata": {
            "client":  "Theo / HOWLING MUNE",
            "stage":   "1",
            "project": "Foundation + Front Door",
            "trigger": "Due to begin upon agreement",
        }
    },
    {
        "name": "HOWLING MUNE — Stage 2: Build",
        "amount": 200000,   # $2,000.00 USD
        "description": (
            "Build phase. Includes: landing page / entry page, intake form, "
            "CRM / lead tracker, routing logic, lead source tracking."
        ),
        "metadata": {
            "client":  "Theo / HOWLING MUNE",
            "stage":   "2",
            "project": "Foundation + Front Door",
            "trigger": "Due before build phase",
        }
    },
    {
        "name": "HOWLING MUNE — Stage 3: Activate",
        "amount": 200000,   # $2,000.00 USD
        "description": (
            "Activate phase. Includes: lead flow plan, referral + partnership "
            "pathways, WhatsApp / voice-note close structure, first optimization "
            "pass, handoff documentation."
        ),
        "metadata": {
            "client":  "Theo / HOWLING MUNE",
            "stage":   "3",
            "project": "Foundation + Front Door",
            "trigger": "Due before activation / handoff",
        }
    },
]

print("\n🔗  Creating HOWLING MUNE Payment Links on Stripe...\n")

links = {}

for stage in stages:
    # 1. Create a Price (one-time, USD)
    price = stripe.Price.create(
        currency="usd",
        unit_amount=stage["amount"],
        product_data={
            "name": stage["name"],
            "statement_descriptor": "AMA SOLUTIONS",  # appears on bank statement (max 22 chars)
        },
    )

    # 2. Create a Payment Link using CheckoutSessions under the hood
    link = stripe.PaymentLink.create(
        line_items=[{"price": price.id, "quantity": 1}],
        payment_method_types=["card"],
        currency="usd",
        after_completion={
            "type": "hosted_confirmation",
            "hosted_confirmation": {
                "custom_message": (
                    f"Payment received. {stage['name'].split('—')[1].strip()} "
                    "confirmed. Major Dream Williams will be in touch within 24 hours."
                )
            }
        },
        metadata=stage["metadata"],
        custom_text={
            "submit": {"message": "Your payment goes to AMA Solutions Corporation via Brex (ACH)."},
        },
        billing_address_collection="auto",
        phone_number_collection={"enabled": False},
    )

    stage_num = stage["metadata"]["stage"]
    links[stage_num] = link.url
    amt = stage["amount"] / 100
    print(f"  ✅  Stage {stage_num}  ${amt:,.0f}  →  {link.url}")

print("\n" + "─" * 60)
print("COPY THESE INTO howling_mune_payment.html")
print("─" * 60)
for num, url in links.items():
    print(f'  STAGE_{num}_LINK = "{url}"')
print("─" * 60 + "\n")
