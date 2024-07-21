from pyspark.sql import SparkSession
from pyspark.sql.functions import col, coalesce, lit

# Инициализация SparkSession
spark = SparkSession.builder.appName("ProductCategory").getOrCreate()

# Пример данных для продуктов
products_data = [
    (1, "Product A"),
    (2, "Product B"),
    (3, "Product C"),
    (4, "Product D")
]
products_df = spark.createDataFrame(products_data, ["product_id", "product_name"])

# Пример данных для категорий
categories_data = [
    (1, "Category 1"),
    (2, "Category 2"),
    (3, "Category 3")
]
categories_df = spark.createDataFrame(categories_data, ["category_id", "category_name"])

# Пример данных для связей продуктов и категорий
product_categories_data = [
    (1, 1),
    (1, 2),
    (2, 3),
    (3, 1)
]
product_categories_df = spark.createDataFrame(product_categories_data, ["product_id", "category_id"])

def get_product_category_pairs_and_orphans(products_df, categories_df, product_categories_df):
    # Объединяем таблицы для получения пар «Имя продукта – Имя категории»
    product_category_pairs_df = products_df \
        .join(product_categories_df, "product_id", "left") \
        .join(categories_df, "category_id", "left") \
        .select("product_name", "category_name")

    # Добавляем пары «Имя продукта – Имя категории» и оставляем значения None для продуктов без категорий
    product_category_pairs_with_none_df = product_category_pairs_df \
        .select("product_name", coalesce(col("category_name"), lit(None)).alias("category_name"))

    # Продукты без категорий
    orphan_products_df = product_category_pairs_df \
        .filter(col("category_name").isNull()) \
        .select("product_name") \
        .distinct()

    return product_category_pairs_with_none_df, orphan_products_df

# Получение пар и продуктов без категорий
product_category_pairs_with_none_df, orphan_products_df = get_product_category_pairs_and_orphans(
    products_df, categories_df, product_categories_df
)

# Вывод результатов
print("Пары «Имя продукта – Имя категории»:")
product_category_pairs_with_none_df.show()

print("Продукты без категорий:")
orphan_products_df.show()

# Остановка SparkSession
spark.stop()
