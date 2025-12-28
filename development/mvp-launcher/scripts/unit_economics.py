#!/usr/bin/env python3
"""
Unit Economics Calculator

Calculates key SaaS metrics: LTV, CAC, payback period, and ratios.
"""

import argparse
import sys


def calculate_ltv(arpu: float, gross_margin: float, monthly_churn: float) -> dict:
    """Calculate Customer Lifetime Value"""
    if monthly_churn <= 0 or monthly_churn >= 100:
        raise ValueError("Monthly churn must be between 0 and 100")
    
    churn_rate = monthly_churn / 100
    customer_lifetime_months = 1 / churn_rate
    
    # LTV = ARPU × Gross Margin × Customer Lifetime
    ltv = arpu * (gross_margin / 100) * customer_lifetime_months
    
    return {
        'ltv': ltv,
        'lifetime_months': customer_lifetime_months
    }


def calculate_payback_period(cac: float, arpu: float, gross_margin: float) -> float:
    """Calculate CAC Payback Period in months"""
    monthly_gross_profit = arpu * (gross_margin / 100)
    if monthly_gross_profit <= 0:
        raise ValueError("Monthly gross profit must be positive")
    
    payback_months = cac / monthly_gross_profit
    return payback_months


def main():
    parser = argparse.ArgumentParser(
        description='Calculate SaaS unit economics',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python unit_economics.py --arpu 100 --cac 300 --churn-rate 5 --margin 80
  python unit_economics.py --arpu 50 --cac 150 --churn-rate 8 --margin 70
  
Output explains:
  - LTV (Lifetime Value)
  - LTV:CAC ratio (target: ≥3:1)
  - CAC Payback Period (target: ≤12 months)
  - Customer Lifetime in months
        '''
    )
    
    parser.add_argument('--arpu', type=float, required=True,
                       help='Average Revenue Per User (monthly, in $)')
    parser.add_argument('--cac', type=float, required=True,
                       help='Customer Acquisition Cost (in $)')
    parser.add_argument('--churn-rate', type=float, required=True,
                       help='Monthly churn rate (in %, e.g., 5 for 5%%)')
    parser.add_argument('--margin', type=float, default=80,
                       help='Gross margin (in %%, default: 80)')
    
    args = parser.parse_args()
    
    try:
        # Calculate LTV
        ltv_data = calculate_ltv(args.arpu, args.margin, args.churn_rate)
        ltv = ltv_data['ltv']
        lifetime_months = ltv_data['lifetime_months']
        
        # Calculate ratios
        ltv_cac_ratio = ltv / args.cac if args.cac > 0 else 0
        payback_months = calculate_payback_period(args.cac, args.arpu, args.margin)
        
        # Assessments
        ltv_cac_assessment = (
            "✅ Excellent" if ltv_cac_ratio >= 5
            else "✅ Good" if ltv_cac_ratio >= 3
            else "⚠️  Marginal" if ltv_cac_ratio >= 1
            else "❌ Broken"
        )
        
        payback_assessment = (
            "✅ Excellent" if payback_months <= 6
            else "✅ Good" if payback_months <= 12
            else "⚠️  Marginal" if payback_months <= 18
            else "❌ Too long"
        )
        
        churn_assessment = (
            "✅ Excellent" if args.churn_rate <= 3
            else "✅ Good" if args.churn_rate <= 5
            else "⚠️  High" if args.churn_rate <= 10
            else "❌ Critical"
        )
        
        # Output results
        print("\n" + "="*60)
        print("UNIT ECONOMICS ANALYSIS")
        print("="*60)
        
        print("\n📊 INPUTS:")
        print(f"  ARPU (Monthly):        ${args.arpu:,.2f}")
        print(f"  CAC:                   ${args.cac:,.2f}")
        print(f"  Monthly Churn Rate:    {args.churn_rate}%")
        print(f"  Gross Margin:          {args.margin}%")
        
        print("\n💰 KEY METRICS:")
        print(f"  LTV:                   ${ltv:,.2f}")
        print(f"  Customer Lifetime:     {lifetime_months:.1f} months")
        print(f"  LTV:CAC Ratio:         {ltv_cac_ratio:.2f}:1  {ltv_cac_assessment}")
        print(f"  CAC Payback Period:    {payback_months:.1f} months  {payback_assessment}")
        
        print("\n🎯 ASSESSMENT:")
        print(f"  LTV:CAC Ratio:         {ltv_cac_assessment}")
        print(f"  Payback Period:        {payback_assessment}")
        print(f"  Churn Rate:            {churn_assessment}")
        
        print("\n📈 IMPROVEMENT LEVERS:")
        
        if ltv_cac_ratio < 3:
            print("  ⚠️  LTV:CAC below 3:1 - Options:")
            print("     • Reduce CAC (optimize channels, improve conversion)")
            print("     • Increase ARPU (pricing, upsells, cross-sells)")
            print("     • Reduce churn (improve retention, product value)")
        
        if payback_months > 12:
            print("  ⚠️  Payback > 12 months - Options:")
            print("     • Annual billing (get cash upfront)")
            print("     • Reduce CAC (more efficient channels)")
            print("     • Increase ARPU (higher pricing)")
        
        if args.churn_rate > 5:
            print("  ⚠️  High churn - Focus on:")
            print("     • Onboarding improvements")
            print("     • Product stickiness features")
            print("     • Customer success programs")
            print("     • Better customer targeting")
        
        if ltv_cac_ratio >= 3 and payback_months <= 12 and args.churn_rate <= 5:
            print("  ✅ Unit economics look healthy!")
            print("     • Focus on scaling customer acquisition")
            print("     • Maintain or improve these ratios at scale")
        
        print("\n" + "="*60)
        print("\nBENCHMARKS (B2B SaaS):")
        print("  LTV:CAC Ratio:   ≥3:1 minimum, ≥5:1 excellent")
        print("  Payback Period:  ≤12 months good, ≤6 months excellent")
        print("  Monthly Churn:   ≤5% good, ≤3% excellent")
        print("="*60 + "\n")
        
    except ValueError as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
