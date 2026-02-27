"""
verify_production_security.py
Verifies that QA security and stability fixes are live on Hugging Face.
"""
import requests
import io
import sys

BASE_URL = "https://bhishaj-merchflow-ai.hf.space"

PASS = "✅ PASS"
FAIL = "❌ FAIL"

def test_safety_check():
    """
    Negative Test: Send a malformed payload (text file pretending to be an image)
    to /generate-catalog. Expect a generic error, NOT a raw stack trace.
    """
    print("\n" + "=" * 60)
    print("TEST 1: Safety Check (Negative Test)")
    print("=" * 60)

    url = f"{BASE_URL}/generate-catalog"
    
    # Create a fake text file disguised with a .jpg extension
    fake_file = io.BytesIO(b"This is not an image. It is a malicious text payload.")
    files = {"file": ("malicious_payload.jpg", fake_file, "image/jpeg")}
    
    try:
        response = requests.post(url, files=files, timeout=60)
        status = response.status_code
        body = response.text
        
        print(f"  Status Code : {status}")
        print(f"  Response Body (first 300 chars):\n    {body[:300]}")
        
        # Check for stack trace indicators
        trace_keywords = ["Traceback", "File \"", "line ", "traceback", "format_exc", ".py\""]
        has_trace = any(kw in body for kw in trace_keywords)
        
        has_generic_msg = "An internal server error occurred" in body
        
        if has_trace:
            print(f"\n  Result: {FAIL}")
            print("  Server LEAKED a raw Python stack trace to the client!")
            return False
        elif status == 500 and has_generic_msg:
            print(f"\n  Result: {PASS}")
            print("  Server returned a sanitized generic error. No stack trace leaked.")
            return True
        elif status == 200:
            print(f"\n  Result: {PASS}")
            print("  Server handled malformed input gracefully via agent fallback (200 OK, no crash).")
            return True
        else:
            print(f"\n  Result: {FAIL}")
            print(f"  Unexpected response. Status={status}. Generic message present={has_generic_msg}.")
            return False
    except requests.exceptions.Timeout:
        print(f"\n  Result: {FAIL}")
        print("  Request timed out after 60s.")
        return False
    except Exception as e:
        print(f"\n  Result: {FAIL}")
        print(f"  Connection error: {e}")
        return False


def test_live_pulse():
    """
    Positive Test: Ping the root endpoint / and check that the
    Dashboard HTML loads with 'Bhishaj Technologies' branding.
    """
    print("\n" + "=" * 60)
    print("TEST 2: Live Pulse (Positive Test)")
    print("=" * 60)
    
    url = f"{BASE_URL}/"
    
    try:
        response = requests.get(url, timeout=30)
        status = response.status_code
        body = response.text
        
        print(f"  Status Code : {status}")
        print(f"  Content Length : {len(body)} chars")
        
        has_branding = "Bhishaj" in body
        is_html = "<html" in body.lower() or "<!doctype" in body.lower()
        
        print(f"  Contains HTML  : {is_html}")
        print(f"  Contains 'Bhishaj' branding : {has_branding}")
        
        if status == 200 and is_html and has_branding:
            print(f"\n  Result: {PASS}")
            print("  Dashboard loaded successfully with Bhishaj Technologies branding.")
            return True
        else:
            print(f"\n  Result: {FAIL}")
            if not is_html:
                print("  Response is not HTML.")
            if not has_branding:
                print("  'Bhishaj' branding not found in response.")
            return False
    except requests.exceptions.Timeout:
        print(f"\n  Result: {FAIL}")
        print("  Request timed out after 30s.")
        return False
    except Exception as e:
        print(f"\n  Result: {FAIL}")
        print(f"  Connection error: {e}")
        return False


if __name__ == "__main__":
    print("=" * 60)
    print("  MerchFlow AI — Production Security Verification")
    print(f"  Target: {BASE_URL}")
    print("=" * 60)
    
    r1 = test_safety_check()
    r2 = test_live_pulse()
    
    print("\n" + "=" * 60)
    print("  SUMMARY")
    print("=" * 60)
    print(f"  Test 1 (Safety Check) : {PASS if r1 else FAIL}")
    print(f"  Test 2 (Live Pulse)   : {PASS if r2 else FAIL}")
    print("=" * 60)
    
    if r1 and r2:
        print("\n🎉 All production security checks PASSED.")
        sys.exit(0)
    else:
        print("\n⚠️  Some checks FAILED. Review output above.")
        sys.exit(1)
