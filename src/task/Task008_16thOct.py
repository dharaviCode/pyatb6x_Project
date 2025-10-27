# You want to check whether a web page loads within 3 seconds (performance test condition).
#
# load_time = 4.2
# ⚠️ Page load too slow: 4.2 seconds

load_time = float(input("Enter load time: ").strip())

if load_time >= 3.01:
    print(f"⚠️ Page load too slow: {load_time} seconds")
else:
    print(f"✅ Page loaded successfully in {load_time} seconds")
