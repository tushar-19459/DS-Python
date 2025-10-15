from product import All_Product
class test:
    product = All_Product()
    product.place_order(1,13,'tushar',199)
    product.place_order(2,2,'raj',200)
    product.place_order(3,7,'kunjoor',300)
    product.place_order(1,11,'tushar',140)
    product.place_order(2,13,'kunjoor',800)
    product.place_order(3,3,'raj',90)
    print(product.get_top_selling_product())
    print(product.count_unique_products())
    # print(product.topselling[1])

test()