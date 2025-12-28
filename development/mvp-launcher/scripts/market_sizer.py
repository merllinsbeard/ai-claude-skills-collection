#!/usr/bin/env python3
"""
Market Sizing Calculator (TAM/SAM/SOM)

Calculates Total Addressable Market, Serviceable Addressable Market, 
and Serviceable Obtainable Market.
"""

import argparse
import sys


def calculate_market_size(
    total_market: float,
    addressable_percent: float,
    obtainable_percent: float,
    avg_revenue_per_customer: float = None
) -> dict:
    """Calculate TAM/SAM/SOM metrics"""
    
    if not (0 <= addressable_percent <= 100):
        raise ValueError("Addressable percent must be between 0 and 100")
    if not (0 <= obtainable_percent <= 100):
        raise ValueError("Obtainable percent must be between 0 and 100")
    
    sam = total_market * (addressable_percent / 100)
    som = sam * (obtainable_percent / 100)
    
    result = {
        'tam': total_market,
        'sam': sam,
        'som': som,
        'sam_percent': addressable_percent,
        'som_percent': obtainable_percent
    }
    
    if avg_revenue_per_customer:
        result['tam_customers'] = total_market / avg_revenue_per_customer
        result['sam_customers'] = sam / avg_revenue_per_customer
        result['som_customers'] = som / avg_revenue_per_customer
    
    return result


def format_number(num: float) -> str:
    """Format large numbers with K/M/B suffixes"""
    if num >= 1_000_000_000:
        return f"${num/1_000_000_000:.1f}B"
    elif num >= 1_000_000:
        return f"${num/1_000_000:.1f}M"
    elif num >= 1_000:
        return f"${num/1_000:.1f}K"
    else:
        return f"${num:,.0f}"


def main():
    parser = argparse.ArgumentParser(
        description='Calculate TAM/SAM/SOM market sizing',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python market_sizer.py --total-market 10000000000 --addressable-percent 15 --obtainable-percent 3
  python market_sizer.py --total-market 5000000000 --addressable-percent 20 --obtainable-percent 5 --arpu 1200

TAM: Total Addressable Market (entire market size)
SAM: Serviceable Addressable Market (portion you can serve)
SOM: Serviceable Obtainable Market (realistic near-term capture)
        '''
    )
    
    parser.add_argument('--total-market', type=float, required=True,
                       help='Total Addressable Market (TAM) in $')
    parser.add_argument('--addressable-percent', type=float, required=True,
                       help='Percent of TAM you can address (0-100)')
    parser.add_argument('--obtainable-percent', type=float, required=True,
                       help='Percent of SAM you can obtain (0-100)')
    parser.add_argument('--arpu', type=float, default=None,
                       help='Average revenue per customer (optional, for customer count)')
    
    args = parser.parse_args()
    
    try:
        results = calculate_market_size(
            args.total_market,
            args.addressable_percent,
            args.obtainable_percent,
            args.arpu
        )
        
        # Market size assessments
        tam_assessment = (
            "✅ Venture scale" if results['tam'] >= 1_000_000_000
            else "⚠️  Small market" if results['tam'] >= 100_000_000
            else "❌ Too small for VC"
        )
        
        sam_assessment = (
            "✅ Large opportunity" if results['sam'] >= 100_000_000
            else "✅ Good opportunity" if results['sam'] >= 10_000_000
            else "⚠️  Niche market"
        )
        
        som_assessment = (
            "✅ Strong first-year target" if results['som'] >= 1_000_000
            else "✅ Realistic" if results['som'] >= 100_000
            else "⚠️  May need to increase obtainable %"
        )
        
        # Output
        print("\n" + "="*60)
        print("MARKET SIZING ANALYSIS")
        print("="*60)
        
        print("\n📊 INPUTS:")
        print(f"  Total Market (TAM):            {format_number(args.total_market)}")
        print(f"  Addressable Segment:           {args.addressable_percent}% of TAM")
        print(f"  Obtainable (Year 1-3):         {args.obtainable_percent}% of SAM")
        if args.arpu:
            print(f"  Avg Revenue per Customer:      ${args.arpu:,.2f}")
        
        print("\n💰 MARKET SIZES:")
        print(f"  TAM (Total Addressable):       {format_number(results['tam'])}")
        print(f"    → {tam_assessment}")
        print(f"\n  SAM (Serviceable Addressable): {format_number(results['sam'])}")
        print(f"    → {args.addressable_percent}% of TAM")
        print(f"    → {sam_assessment}")
        print(f"\n  SOM (Serviceable Obtainable):  {format_number(results['som'])}")
        print(f"    → {args.obtainable_percent}% of SAM")
        print(f"    → {som_assessment}")
        
        if args.arpu:
            print("\n👥 CUSTOMER COUNTS:")
            print(f"  TAM Customers:                 {results['tam_customers']:,.0f}")
            print(f"  SAM Customers:                 {results['sam_customers']:,.0f}")
            print(f"  SOM Customers (Year 1-3):      {results['som_customers']:,.0f}")
        
        print("\n🎯 STRATEGIC ASSESSMENT:")
        
        # TAM analysis
        if results['tam'] >= 1_000_000_000:
            print("\n  ✅ TAM supports venture-scale business")
            print("     • Large enough for VC funding")
            print("     • Room for multiple players")
        elif results['tam'] >= 100_000_000:
            print("\n  ⚠️  TAM is smallish for traditional VC")
            print("     • Consider bootstrapping or focused VC")
            print("     • May need to expand TAM definition")
        else:
            print("\n  ❌ TAM likely too small for VC model")
            print("     • Bootstrap or find adjacent markets")
            print("     • Expand TAM definition if possible")
        
        # SAM analysis
        if results['sam'] >= 100_000_000:
            print("\n  ✅ Strong serviceable market")
            print("     • Enough room to build significant business")
        elif results['sam'] >= 10_000_000:
            print("\n  ⚠️  Moderate serviceable market")
            print("     • Validate obtainable % is realistic")
            print("     • Consider expanding addressable segment")
        else:
            print("\n  ⚠️  Small serviceable market")
            print("     • Increase addressable % or expand definition")
            print("     • Verify market sizing assumptions")
        
        # SOM analysis
        som_percent_of_sam = args.obtainable_percent
        if som_percent_of_sam > 10:
            print("\n  ⚠️  Obtainable % seems high (>10% of SAM)")
            print("     • Be more conservative in projections")
            print("     • Typical first 3 years: 1-5% of SAM")
        elif som_percent_of_sam >= 1:
            print("\n  ✅ Obtainable % looks realistic")
            print("     • Focus on execution to capture SOM")
        else:
            print("\n  ⚠️  Obtainable % very conservative")
            print("     • Possibly too pessimistic")
            print("     • Or SAM definition too broad")
        
        print("\n📈 NEXT STEPS:")
        print("  1. Validate TAM assumptions with research")
        print("  2. Identify specific SAM segments to target")
        print("  3. Build bottom-up model for SOM")
        print("  4. Test pricing and unit economics")
        print("  5. Define 12-month customer acquisition plan")
        
        print("\n" + "="*60)
        print("\nBENCHMARKS:")
        print("  TAM:  >$1B = venture scale, >$100M = viable")
        print("  SAM:  >$100M = large opportunity")
        print("  SOM:  1-5% of SAM realistic for Year 1-3")
        print("  Reality check: Build bottom-up model to verify")
        print("="*60 + "\n")
        
    except ValueError as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
