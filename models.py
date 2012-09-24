# Add User.get_subscription() method
def __user_get_subscription(user):
    '''
    Returns latest valid subscription or expired subscription with on hold.
    If no subscription is available adds a free subscription.
    '''
    today = datetime.date.today()
    institution = user.get_profile().institution
    susriptions = InstitutionSubscription.objects.filter(institution=institution, on_hold=False, expires__gte=today)
    if not subscriptions.exists():
        free_subscription = Subscription.objects.get(name='Free')
        institution_subscription = InstitutionSubscription.objects.create(
            institution=institution,
            subscription=free_subscription
        )
    else:
        institution_subscription = subscriptions.order_by('-subscription__priority')[0]
    return institution_subscription


User.add_to_class('get_subscription', __user_get_subscription)
