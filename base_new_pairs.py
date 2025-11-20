import requests, time

def monitor_base():
    print("Мониторинг новых пулов на Base (DexScreener)...")
    seen = set()
    while True:
        r = requests.get("https://api.dexscreener.com/latest/dex/pairs/base")
        for p in r.json().get("pairs", []):
            addr = p["pairAddress"]
            if addr in seen: continue
            if p.get("pairCreatedAt", 0) > time.time() - 120:  # < 2 мин
                seen.add(addr)
                print(f"НОВАЯ ПАРА!\n"
                      f"{p['baseToken']['symbol']}/{p['quoteToken']['symbol']}\n"
                      f"Цена: ${float(p['priceUsd']):.12f}\n"
                      f"Ликвидность: ${p['liquidity']['usd']:,.0f}\n"
                      f"https://dexscreamer.com/base/{addr}\n"
                      f"{'-'*50}")
        time.sleep(6)

if __name__ == "__main__":
    monitor_base()
