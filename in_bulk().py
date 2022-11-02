promotion_banner_ids = (4,5,6,7)
# >>> promotion_banner_ids
# (4, 5, 6, 7)

# in_bulk() returns a dictionary
promotion_banners = PromotionBanner.objects.in_bulk(promotion_banner_ids)
# >>> promotion_banners
# {7: <PromotionBanner: PromotionBanner object (7)>, 4: <PromotionBanner: PromotionBanner object (4)>,
#  5: <PromotionBanner: PromotionBanner object (5)>, 6: <PromotionBanner: PromotionBanner object (6)>}

# can be used for searching via key
test_num = 3
if test_num not in promotion_banners:
    msg = f'Promotion Banner "{test_num}" does not exist in the database'
    print(msg)
else:
    msg = f'Promotion Banner "{test_num}" exist in the database'
    print(msg)


# can also target specific fields
store_slugs = ('test-store', 'not-existing')
stores = Store.objects.in_bulk(store_slugs, field_name='slug')
# >>> stores
# {'test-store': <Store: Stamps Office>}
