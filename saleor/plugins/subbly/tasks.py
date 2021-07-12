from urllib.parse import urlencode

from templated_email import send_templated_mail

from ...celeryconf import app
from ...core.emails import get_email_context
from ...core.utils.url import prepare_url


@app.task
def send_customer_invitation_email(onboarding_url, customer_email):
    params = urlencode({"email": customer_email})
    onboarding_url = prepare_url(params, onboarding_url)
    send_kwargs, ctx = get_email_context()
    ctx["onboarding_url"] = onboarding_url
    send_templated_mail(
        template_name="account/onboarding",
        recipient_list=[customer_email],
        context=ctx,
        **send_kwargs,
    )
