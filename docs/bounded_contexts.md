# Bounded Contexts

1. Catalog — управление каталогом тортов (Cake, Flavor, Size, Decoration, Ingredient, base Price).
   Ubiquitous Language: фокус на описании продуктов.

2. Ordering — оформление и управление заказами (Order, OrderLine, Quantity, Customer, DeliveryAddress, OrderStatus, TotalAmount).
   Ubiquitous Language: фокус на процессе покупки.

3. Pricing — расчёт цены (доплаты, скидки) — интегрируется с Catalog и Ordering.

(Позже: Payment, BakeryProduction)