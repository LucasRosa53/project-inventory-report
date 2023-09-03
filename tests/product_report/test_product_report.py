from inventory_report.product import Product

def test_product_report() -> None:
    product = Product(
        "1",
        "Nicotine Polacrilex",
        "Target Corporation",
        "2021-02-18",
        "2023-09-17",
        "CR25 1551 4467 2549 4402 1",
        "instrucao 1",
    )
    except_output = (
            f"The product {product.id} - {product.product_name} "
            f"with serial number {product.serial_number} "
            f"manufactured on {product.manufacturing_date} "
            f"by the company {product.company_name} "
            f"valid until {product.expiration_date} "
            "must be stored according to the following instructions: "
            f"{product.storage_instructions}."
    )

    assert str(product) == except_output
