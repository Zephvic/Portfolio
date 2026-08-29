import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
DATA_PATH = PROJECT_ROOT / "data" / "biscuit_sales_2024.csv"

def load_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    # Parse dates
    df["Transaction Date"] = pd.to_datetime(df["Transaction Date"], errors="coerce")
    # Numeric columns
    for col in ["Quantity Purchased", "Cost", "Unit Price", "Revenue", "Total Cost of Goods", "Profit", "Age"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["Transaction Date", "Revenue", "Profit"])
    return df

def kpis(df: pd.DataFrame) -> dict:
    total_orders = len(df)
    total_units = int(df["Quantity Purchased"].sum())
    total_revenue = float(df["Revenue"].sum())
    total_profit = float(df["Profit"].sum())
    profit_margin = total_profit / total_revenue if total_revenue else 0.0

    return {
        "total_orders": total_orders,
        "total_units": total_units,
        "total_revenue": total_revenue,
        "total_profit": total_profit,
        "profit_margin": profit_margin,
    }

def save_bar(series: pd.Series, title: str, xlabel: str, ylabel: str, filename: str) -> None:
    plt.figure()
    series.plot(kind="bar")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(PROJECT_ROOT / filename)
    plt.close()

def main() -> None:
    df = load_data(DATA_PATH)

    # KPIs
    metrics = kpis(df)
    print("=== Biscuit Sales & Profitability Summary (2024) ===")
    print(f"Total orders: {metrics['total_orders']:,}")
    print(f"Total units sold: {metrics['total_units']:,}")
    print(f"Total revenue: {metrics['total_revenue']:,.0f}")
    print(f"Total profit: {metrics['total_profit']:,.0f}")
    print(f"Overall profit margin: {metrics['profit_margin']*100:.1f}%\n")

    # Monthly trend
    monthly = (
        df.groupby(df["Transaction Date"].dt.to_period("M"))
          .agg(Revenue=("Revenue","sum"), Profit=("Profit","sum"))
          .reset_index()
    )
    monthly["Month"] = monthly["Transaction Date"].dt.to_timestamp()

    plt.figure()
    plt.plot(monthly["Month"], monthly["Revenue"])
    plt.title("Monthly Revenue (2024)")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig(PROJECT_ROOT / "monthly_revenue.png")
    plt.close()

    # Top brands
    top_brands = df.groupby("Biscuit Brand")["Revenue"].sum().sort_values(ascending=False).head(10)
    save_bar(top_brands, "Top Biscuit Brands by Revenue", "Biscuit Brand", "Revenue", "top_brands_revenue.png")

    # Top locations
    top_locations = df.groupby("Buyer Location")["Revenue"].sum().sort_values(ascending=False).head(10)
    save_bar(top_locations, "Top Buyer Locations by Revenue", "Location", "Revenue", "top_locations_revenue.png")

    # Payment method
    pay = df.groupby("Payment Method")["Revenue"].sum().sort_values(ascending=False)
    save_bar(pay, "Revenue by Payment Method", "Payment Method", "Revenue", "revenue_by_payment.png")

    # Sales reps
    reps = df.groupby("Sales Representative")["Revenue"].sum().sort_values(ascending=False)
    save_bar(reps, "Revenue by Sales Representative", "Sales Representative", "Revenue", "revenue_by_sales_rep.png")

    # Profit margin by brand (top by revenue)
    brand_perf = df.groupby("Biscuit Brand").agg(Revenue=("Revenue","sum"), Profit=("Profit","sum"))
    brand_perf["Profit Margin"] = brand_perf["Profit"] / brand_perf["Revenue"]
    brand_perf = brand_perf.loc[top_brands.index].sort_values("Profit Margin", ascending=False)
    save_bar(brand_perf["Profit Margin"], "Profit Margin by Top Brands", "Biscuit Brand", "Profit Margin", "profit_margin_by_brand.png")

    # Save summary tables
    (PROJECT_ROOT / "outputs").mkdir(exist_ok=True)
    top_brands.to_frame("Revenue").to_csv(PROJECT_ROOT / "outputs" / "top_brands_by_revenue.csv")
    top_locations.to_frame("Revenue").to_csv(PROJECT_ROOT / "outputs" / "top_locations_by_revenue.csv")
    reps.to_frame("Revenue").to_csv(PROJECT_ROOT / "outputs" / "revenue_by_sales_rep.csv")
    monthly[["Month", "Revenue", "Profit"]].to_csv(PROJECT_ROOT / "outputs" / "monthly_revenue_profit.csv", index=False)

    print("Saved charts and summary tables to the project folder.")

if __name__ == "__main__":
    main()
