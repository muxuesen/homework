import redis
conn = redis.Redis(host="192.168.11.130", port=6379)
# conn.set("class", "穆学森")
# print(conn.get("class").decode("utf-8"))
# conn.flushall()
print(conn.keys())