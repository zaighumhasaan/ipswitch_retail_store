from .models import Cart


def cart_context(request):
    cart_items_count = 0

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items_count = cart.get_total_items()
    elif request.session.session_key:
        cart = Cart.objects.filter(session_key=request.session.session_key).first()
        if cart:
            cart_items_count = cart.get_total_items()

    return {
        'cart_items_count': cart_items_count
    }
