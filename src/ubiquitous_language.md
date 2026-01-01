# Ubiquitous Language — Tortik Shop (Core Domain: Custom Cake Ordering)

- **Cake** — кастомный торт, определяемый вкусом, размером, количеством коржей, декором и ингредиентами.
- **Name** — у основных позиций есть наименования тортиков
- **CakeId** — уникальный идентификатор торта в каталоге (UUID или str).
- **Flavor** — базовый вкус (Chocolate, Vanilla, Strawberry, Red Velvet и т.д.).
- **Size** — размер торта (Small — 1 кг, Medium — 2 кг, Large — 3 кг).
- **LayersCount** — количество коржей (от 1 до 5).
- **Decoration** — декор (CreamFlowers, Fruits, ChocolateFigures и т.д.).
- **Ingredient** — дополнительный ингредиент (Nuts, Berries — с возможной доплатой).
- **Money** — денежная сумма в рублях (с копейками, всегда RUB).
- **Quantity** — количество одинаковых тортов в заказе (целое положительное число).
- **Order** — заказ клиента, содержащий одну или несколько строк (OrderLines), общую сумму и статус.
- **OrderId** — уникальный идентификатор заказа.
- **OrderLine** — строка заказа: конкретный Cake + Quantity + цена за строку.
- **Customer** — клиент с именем, телефоном, email, месенджерами и адресом доставки.
- **DeliveryAddress** — адрес доставки (строка с городом, улицей и т.д.).
- **DeliveryMethod** — способ доставки
- **OrderStatus** — статус заказа: Pending, Confirmed, InProduction, ReadyForPickup, Delivered, Cancelled.