from core.calculator import PricingCalculator

def run_compliance_tests():
    cases = [
        {"input": "Back to the Future 1\nBack to the Future 2\nBack to the Future 3", "expected": 36.0},
        {"input": "Back to the Future 1\nBack to the Future 2\nBack to the Future 3\nBack to the Future 2", "expected": 48.0},
        {"input": "Back to the Future 1\nBack to the Future 2\nBack to the Future 3\nLa chèvre", "expected": 56.0},
    ]

    print("--- DÉBUT DES TESTS ---")
    for i, case in enumerate(cases, 1):
        result = PricingCalculator.calculate_total(case["input"])
        status = "✅ OK" if result == case["expected"] else "❌ ERREUR"
        print(f"Test {i}: {status} (Attendu: {case['expected']}€, Obtenu: {result}€)")

if __name__ == "__main__":
    run_compliance_tests()