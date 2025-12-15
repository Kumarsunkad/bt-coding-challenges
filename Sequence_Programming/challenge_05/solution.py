# solution.py

def calculate_overall_sales():
    """
    Calculate overall sales and sales from chemical-free farming.
    Returns a tuple: (total_sales, chemical_free_sales)
    """
    # Land distribution
    total_land = 80  # acres
    segment_land = total_land / 5  # each crop segment

    # Crop yields and prices
    # Tomatoes
    tomato_land_30 = segment_land * 0.3
    tomato_land_70 = segment_land * 0.7
    tomato_yield_30 = 10  # tonnes/acre
    tomato_yield_70 = 12  # tonnes/acre
    tomato_price = 7  # Rs/kg

    # Potatoes
    potato_yield = 10  # tonnes/acre
    potato_price = 20  # Rs/kg

    # Cabbage
    cabbage_yield = 14  # tonnes/acre
    cabbage_price = 24  # Rs/kg

    # Sunflower
    sunflower_yield = 0.7  # tonnes/acre
    sunflower_price = 200  # Rs/kg

    # Sugarcane
    sugarcane_yield = 45  # tonnes/acre
    sugarcane_price = 4000  # Rs/tonne

    # Calculate total sales
    total_sales = 0

    # Tomatoes
    total_sales += (tomato_land_30 * tomato_yield_30 * 1000) * tomato_price
    total_sales += (tomato_land_70 * tomato_yield_70 * 1000) * tomato_price

    # Potatoes
    total_sales += (segment_land * potato_yield * 1000) * potato_price

    # Cabbage
    total_sales += (segment_land * cabbage_yield * 1000) * cabbage_price

    # Sunflower
    total_sales += (segment_land * sunflower_yield * 1000) * sunflower_price

    # Sugarcane
    total_sales += (segment_land * sugarcane_yield) * sugarcane_price  # price in Rs/tonne

    # Calculate chemical-free sales at end of 11 months
    # Vegetables: tomatoes, potatoes, cabbage (first 6 months)
    chemical_free_sales = 0
    chemical_free_sales += (tomato_land_30 * tomato_yield_30 * 1000) * tomato_price
    chemical_free_sales += (tomato_land_70 * tomato_yield_70 * 1000) * tomato_price
    chemical_free_sales += (segment_land * potato_yield * 1000) * potato_price
    chemical_free_sales += (segment_land * cabbage_yield * 1000) * cabbage_price

    # Sunflower: next 4 months (added after 10 months, but included in 11th month)
    chemical_free_sales += (segment_land * sunflower_yield * 1000) * sunflower_price

    # Sugarcane not yet chemical-free by 11 months (final 4 months needed after sunflower)

    return total_sales, chemical_free_sales

# Example usage
if __name__ == "__main__":
    total, chemical_free = calculate_overall_sales()
    print(f"Overall Sales: Rs {total:,.2f}")
    print(f"Sales from Chemical-Free Farming at 11 months: Rs {chemical_free:,.2f}")
