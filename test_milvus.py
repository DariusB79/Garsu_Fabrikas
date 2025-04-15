from pymilvus import connections

# Prisijungimas prie Milvus
connections.connect("default", host="localhost", port="19530")

print("✅ Prisijungta prie Milvus sėkmingai!")