def select_products_by_category(products, category):
    return [x for x in products if x.category == category]
