import numpy as np

products_ids = np.array([101, 102, 103, 104, 105, 200, 150, 120, 130, 190, 125, 159])
prices = np.array([10.99, 20.99, 35.25, 50.99, 38.10, 50.99, 29.99, 49.99, 99.99, 64.59, 80.29, 25.99])
quantities = np.array([10, 30, 5, 25, 13, 100, 50, 200, 150, 90, 120, 155])
dates = np.array([
    '2024-07-20', '2024-08-03', '2024-08-07', '2024-08-08', '2024-08-09',
    '2024-08-10', '2024-08-13', '2024-08-15', '2024-08-16', '2024-08-17'
])

total_sales = prices * quantities
print(f"Скидки: {total_sales}")

total_revenue = np.sum(total_sales)
print(f"Total revenue: {total_revenue}$")

average_check = np.mean(total_sales)
print(f"Average check: {average_check:.2f}")

#Лучший и худший продукт
best_product_index = np.argmax(total_sales)
worst_product_index = np.argmin(total_sales)
print(f"Лучший тавар (ID: {products_ids[best_product_index]} sales amount: {total_sales[best_product_index]:.2f}$")

print(f"Худший тавар (ID: {products_ids[worst_product_index]} sales amount: {total_sales[worst_product_index]:.2f}$")

#Pandas
import pandas as pd
dates_pd = pd.to_datetime(dates)
days_of_week = dates_pd.day_name()
print(f"Sales per week: {days_of_week}")

sales_by_day = dict()
for day, sale in zip(days_of_week, total_sales):
    if day in sales_by_day:
        sales_by_day[day] +=sale
    else:
        sales_by_day[day] = sale

print(f"Sales per days: {sales_by_day}")


#Визуолизация данных
import matplotlib.pyplot as plt
import seaborn as sns
import mplcyberpunk

plt.figure(figsize=(10, 6))
sns.barplot(x=products_ids, y=total_sales, palette='Oranges_d')
plt.xlabel('ID Продукта')
plt.ylabel('Общие продажи в доларах')
plt.title('Общие продажи по продуктам')
# plt.show()

plt.figure(figsize=(10, 7))
sns.barplot(x=sales_by_day.keys(), y=sales_by_day.values(), palette='Reds_d')
plt.xlabel('День недели')
plt.ylabel('Общие продажи в доларах')
plt.title('Общие продажи по дням недели')
plt.show()





# categories = ['A', 'B', 'C', 'D']
#
# data = {
#     'Category': categories,
#     'Value1': np.random.randint(0, 20, 4),
#     'Value2': np.random.randint(0, 20, 4),
#     'Value3': np.random.randint(0, 20, 4),
# }
#
# df = pd.DataFrame(data)
#
# with plt.style.context('cyberpunk'):
#     df.plot(x='Category', kind='line',
#             lw=3, marker='.', ms=20,
#             figsize=(8, 5))
#     mplcyberpunk.add_gradient_fill(alpha_gradientglow=0.4)
# plt.show()

