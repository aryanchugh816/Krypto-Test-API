from celery import shared_task
from celery.utils.log import get_task_logger
import requests
from django.apps import apps
from django.core.mail import send_mail

logger = get_task_logger(__name__)

EMAIL_MESSAGE = "Congratulations !!! Your crypto currency is at the optimum price of {} as required by you, all because of Krypto"

@shared_task
def get_prices():
    logger.info("tasks.py - get_prices() ran.")
    response = requests.get(
        'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false')

    if response.status_code == 200:

        EventsModel = apps.get_model('events', 'Events')

        response = response.json()
        
        for res in response:
            objs = EventsModel.objects.filter(coin_id=res['id'], target_price=res['current_price'])
            emails = []
            for events in objs:
                emails.append(events.owner.email)

            send_mail(subject="Krypto - Your {} is at the right price".format(res['id']), message=EMAIL_MESSAGE.format(res['current_price']), from_email=None, recipient_list=emails, fail_silently=False)
