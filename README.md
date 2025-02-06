# playwright_python_owasp_zap_black_licorice
Playwright-Python Test Automation Framework ready for cloud and ci/cd. Security Analyst Framework using OWASP ZAP.

# To Integrate OWASP ZAP with Playwright
You’ll need to start ZAP proxy and configure Playwright to use it:
Start ZAP Proxy (Manually or via API)

* Command: zap.sh -daemon -port 8080

Or start it in Python:
  from zapv2 import ZAPv2

  zap = ZAPv2(proxies={'http': 'http://localhost:8080', 'https': 'http://localhost:8080'})
  zap.core.new_session(name='playwright_zap', overwrite=True)


# Modify Playwright to Use ZAP Proxy
  Configure Playwright to route traffic through ZAP:
  browser = p.chromium.launch(proxy={"server": "http://localhost:8080"})


# To Run Playwright Tests  
pytest --headed  # Run with UI
pytest --browser=chromium  # Specify browser

# Run ZAP Active Scan (Optional)
After running Playwright tests, you can initiate an active scan:
zap.ascan.scan(target_url)
print(f"Scan status: {zap.ascan.status()}")

# Key Differences:
✅ Use Python instead of JavaScript (pip install playwright)
✅ Install OWASP ZAP Python API (pip install python-owasp-zap-v2.4)
✅ Configure Playwright to use ZAP Proxy
✅ Use pytest for running tests
