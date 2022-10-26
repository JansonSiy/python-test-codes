PAYMENT_METHOD = Choices(
    (1, 'cash', 'Cash'),
    (3, 'credit_card', 'Credit Card'),
    (4, 'debit', 'Debit'),
    (7, 'voucher', 'Voucher'),
    (8, 'gcash', 'GCash'),
    (9, 'paymaya_wallet', 'Paymaya Wallet'),
)

# >>> rider = RiderProfile.objects.get(id=70)
# >>> rider
# <RiderProfile: Polar Bear>
# >>> rider.allowed_payment_methods
# [1, 3, 4, 7, 8, 9]

riders = RiderProfile.objects.filter(allowed_payment_methods__contains=[PAYMENT_METHOD.cash])
# >>> riders
# <RiderProfileQueryset [<RiderProfile: Polar Bear>]>