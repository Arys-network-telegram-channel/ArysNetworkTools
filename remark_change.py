import base64
import re

# تابع برای رمزگشایی base64
def decode_base64(data):
    return base64.b64decode(data).decode('utf-8')

# تابع برای رمزگذاری به base64
def encode_base64(data):
    return base64.b64encode(data.encode('utf-8')).decode('utf-8')

# تابع برای تغییر نام سرور
def change_server_names_from_base64(input_base64, new_name):
    # رمزگشایی ورودی از base64
    decoded_servers = decode_base64(input_base64).splitlines()

    # تغییر نام سرورها
    updated_servers = []
    for server in decoded_servers:
        # تغییر بخش بعد از # با new_name
        updated_server = re.sub(r'#[^#]+', f'#{new_name}', server.strip())
        
        # بررسی نوع پروتکل (trojan یا vless) و اضافه کردن security مناسب
        if 'trojan' in updated_server:
            if 'security=tls' not in updated_server:
                updated_server = updated_server.split('?')[0] + '?security=tls&' + updated_server.split('?')[1] if '?' in updated_server else updated_server + '?security=tls'
        elif 'vless' in updated_server:
            if 'security=' not in updated_server:
                updated_server = updated_server.split('?')[0] + '?security=none&' + updated_server.split('?')[1] if '?' in updated_server else updated_server + '?security=None'

        updated_servers.append(updated_server)
    
    # رمزگذاری خروجی به base64
    updated_servers_str = '\n'.join(updated_servers)
    return encode_base64(updated_servers_str)

# ورودی base64 (تغییر دهید)
input_base64 = 'dmxlc3M6Ly9iODRkY2JlZS1lNTlhLTQxMDgtYWU5Zi0wZGU2NDIwNjRhYWRAZnJpZW5kcy1uZXdzLTE4MjEucGFnZXMuZGV2OjQ0Mz9wYXRoPS9QSEN1S29TSENqZ0NsSTNVJTNGZWQlM0QyNTYwJmVuY3J5cHRpb249bm9uZSZob3N0PWZyaWVuZHMtbmV3cy0xODIxLnBhZ2VzLmRldiZ0eXBlPXdzJnNlY3VyaXR5PXRscyZzbmk9RnJJRU5Ecy1OZVdzLTE4MjEucEFHZXMuZGVWJmZwPXJhbmRvbWl6ZWQmYWxwbj1oMixodHRwLzEuMSMlRjAlOUYlOTIlQTYlMjAxJTIwLSUyMFZMRVNTJTIwLSUyMERvbWFpbiUyMCUzQSUyMDQ0Mwp2bGVzczovL2I4NGRjYmVlLWU1OWEtNDEwOC1hZTlmLTBkZTY0MjA2NGFhZEB3d3cuc3BlZWR0ZXN0Lm5ldDo0NDM/cGF0aD0vRGVnMWJvTTdFcXVhckp1TyUzRmVkJTNEMjU2MCZlbmNyeXB0aW9uPW5vbmUmaG9zdD1mcmllbmRzLW5ld3MtMTgyMS5wYWdlcy5kZXYmdHlwZT13cyZzZWN1cml0eT10bHMmc25pPWZSSWVOZHMtbmVXcy0xODIxLlBhZ2VzLmRldiZmcD1yYW5kb21pemVkJmFscG49aDIsaHR0cC8xLjEjJUYwJTlGJTkyJUE2JTIwMiUyMC0lMjBWTEVTUyUyMC0lMjBEb21haW4lMjAlM0ElMjA0NDMKdmxlc3M6Ly9iODRkY2JlZS1lNTlhLTQxMDgtYWU5Zi0wZGU2NDIwNjRhYWRAMTcyLjY2LjQ3Ljg3OjQ0Mz9wYXRoPS9KMkNhY1R4MW1TcW83dlFtJTNGZWQlM0QyNTYwJmVuY3J5cHRpb249bm9uZSZob3N0PWZyaWVuZHMtbmV3cy0xODIxLnBhZ2VzLmRldiZ0eXBlPXdzJnNlY3VyaXR5PXRscyZzbmk9RlJpRU5kUy1uRVdTLTE4MjEucGFHRVMuRGVWJmZwPXJhbmRvbWl6ZWQmYWxwbj1oMixodHRwLzEuMSMlRjAlOUYlOTIlQTYlMjAzJTIwLSUyMFZMRVNTJTIwLSUyMElQdjQlMjAlM0ElMjA0NDMKdmxlc3M6Ly9iODRkY2JlZS1lNTlhLTQxMDgtYWU5Zi0wZGU2NDIwNjRhYWRAMTcyLjY2LjQ0LjE2OTo0NDM/cGF0aD0vQkJabzZiYTJraHd1dkVIZCUzRmVkJTNEMjU2MCZlbmNyeXB0aW9uPW5vbmUmaG9zdD1mcmllbmRzLW5ld3MtMTgyMS5wYWdlcy5kZXYmdHlwZT13cyZzZWN1cml0eT10bHMmc25pPWZSaWVuRFMtTmV3Uy0xODIxLnBBR0VzLkRFdiZmcD1yYW5kb21pemVkJmFscG49aDIsaHR0cC8xLjEjJUYwJTlGJTkyJUE2JTIwNCUyMC0lMjBWTEVTUyUyMC0lMjBJUHY0JTIwJTNBJTIwNDQzCnZsZXNzOi8vYjg0ZGNiZWUtZTU5YS00MTA4LWFlOWYtMGRlNjQyMDY0YWFkQFsyNjA2OjQ3MDA6MzEwYzo6YWM0MjoyZjU3XTo0NDM/cGF0aD0vOFV3akNaaUtvWmgxdWdldCUzRmVkJTNEMjU2MCZlbmNyeXB0aW9uPW5vbmUmaG9zdD1mcmllbmRzLW5ld3MtMTgyMS5wYWdlcy5kZXYmdHlwZT13cyZzZWN1cml0eT10bHMmc25pPWZSaWVOZFMtbkVXcy0xODIxLlBhR0VTLmRFViZmcD1yYW5kb21pemVkJmFscG49aDIsaHR0cC8xLjEjJUYwJTlGJTkyJUE2JTIwNSUyMC0lMjBWTEVTUyUyMC0lMjBJUHY2JTIwJTNBJTIwNDQzCnZsZXNzOi8vYjg0ZGNiZWUtZTU5YS00MTA4LWFlOWYtMGRlNjQyMDY0YWFkQFsyNjA2OjQ3MDA6MzEwYzo6YWM0MjoyY2E5XTo0NDM/cGF0aD0vNUVFdWJmMFlIVHhUdTUwRyUzRmVkJTNEMjU2MCZlbmNyeXB0aW9uPW5vbmUmaG9zdD1mcmllbmRzLW5ld3MtMTgyMS5wYWdlcy5kZXYmdHlwZT13cyZzZWN1cml0eT10bHMmc25pPWZySUVOZFMtTmV3cy0xODIxLnBBR0VzLkRldiZmcD1yYW5kb21pemVkJmFscG49aDIsaHR0cC8xLjEjJUYwJTlGJTkyJUE2JTIwNiUyMC0lMjBWTEVTUyUyMC0lMjBJUHY2JTIwJTNBJTIwNDQzCnZsZXNzOi8vYjg0ZGNiZWUtZTU5YS00MTA4LWFlOWYtMGRlNjQyMDY0YWFkQDEwNC4yNS4xMDYuMjc6NDQzP3BhdGg9L1R0cU1wRkhtN3FIZzVZUlQlM0ZlZCUzRDI1NjAmZW5jcnlwdGlvbj1ub25lJmhvc3Q9ZnJpZW5kcy1uZXdzLTE4MjEucGFnZXMuZGV2JnR5cGU9d3Mmc2VjdXJpdHk9dGxzJnNuaT1mckllTmRTLU5lV3MtMTgyMS5wYUdlUy5ERXYmZnA9cmFuZG9taXplZCZhbHBuPWgyLGh0dHAvMS4xIyVGMCU5RiU5MiVBNiUyMDclMjAtJTIwVkxFU1MlMjAtJTIwQ2xlYW4lMjBJUCUyMCUzQSUyMDQ0Mwp0cm9qYW46Ly9EY0JiVWVQKEclNUVIWDBCQnNAZnJpZW5kcy1uZXdzLTE4MjEucGFnZXMuZGV2OjQ0Mz9wYXRoPS90clBIQ3VLb1NIQ2pnQ2xJM1UlM0ZlZCUzRDI1NjAmaG9zdD1mcmllbmRzLW5ld3MtMTgyMS5wYWdlcy5kZXYmdHlwZT13cyZzZWN1cml0eT10bHMmc25pPUZySUVORHMtTmVXcy0xODIxLnBBR2VzLmRlViZmcD1yYW5kb21pemVkJmFscG49aDIsaHR0cC8xLjEjJUYwJTlGJTkyJUE2JTIwMSUyMC0lMjBUcm9qYW4lMjAtJTIwRG9tYWluJTIwJTNBJTIwNDQzCnRyb2phbjovL0RjQmJVZVAoRyU1RUhYMEJCc0B3d3cuc3BlZWR0ZXN0Lm5ldDo0NDM/cGF0aD0vdHJEZWcxYm9NN0VxdWFySnVPJTNGZWQlM0QyNTYwJmhvc3Q9ZnJpZW5kcy1uZXdzLTE4MjEucGFnZXMuZGV2JnR5cGU9d3Mmc2VjdXJpdHk9dGxzJnNuaT1mUkllTmRzLW5lV3MtMTgyMS5QYWdlcy5kZXYmZnA9cmFuZG9taXplZCZhbHBuPWgyLGh0dHAvMS4xIyVGMCU5RiU5MiVBNiUyMDIlMjAtJTIwVHJvamFuJTIwLSUyMERvbWFpbiUyMCUzQSUyMDQ0Mwp0cm9qYW46Ly9EY0JiVWVQKEclNUVIWDBCQnNAMTcyLjY2LjQ3Ljg3OjQ0Mz9wYXRoPS90ckoyQ2FjVHgxbVNxbzd2UW0lM0ZlZCUzRDI1NjAmaG9zdD1mcmllbmRzLW5ld3MtMTgyMS5wYWdlcy5kZXYmdHlwZT13cyZzZWN1cml0eT10bHMmc25pPUZSaUVOZFMtbkVXUy0xODIxLnBhR0VTLkRlViZmcD1yYW5kb21pemVkJmFscG49aDIsaHR0cC8xLjEjJUYwJTlGJTkyJUE2JTIwMyUyMC0lMjBUcm9qYW4lMjAtJTIwSVB2NCUyMCUzQSUyMDQ0Mwp0cm9qYW46Ly9EY0JiVWVQKEclNUVIWDBCQnNAMTcyLjY2LjQ0LjE2OTo0NDM/cGF0aD0vdHJCQlpvNmJhMmtod3V2RUhkJTNGZWQlM0QyNTYwJmhvc3Q9ZnJpZW5kcy1uZXdzLTE4MjEucGFnZXMuZGV2JnR5cGU9d3Mmc2VjdXJpdHk9dGxzJnNuaT1mUmllbkRTLU5ld1MtMTgyMS5wQUdFcy5ERXYmZnA9cmFuZG9taXplZCZhbHBuPWgyLGh0dHAvMS4xIyVGMCU5RiU5MiVBNiUyMDQlMjAtJTIwVHJvamFuJTIwLSUyMElQdjQlMjAlM0ElMjA0NDMKdHJvamFuOi8vRGNCYlVlUChHJTVFSFgwQkJzQFsyNjA2OjQ3MDA6MzEwYzo6YWM0MjoyZjU3XTo0NDM/cGF0aD0vdHI4VXdqQ1ppS29aaDF1Z2V0JTNGZWQlM0QyNTYwJmhvc3Q9ZnJpZW5kcy1uZXdzLTE4MjEucGFnZXMuZGV2JnR5cGU9d3Mmc2VjdXJpdHk9dGxzJnNuaT1mUmllTmRTLW5FV3MtMTgyMS5QYUdFUy5kRVYmZnA9cmFuZG9taXplZCZhbHBuPWgyLGh0dHAvMS4xIyVGMCU5RiU5MiVBNiUyMDUlMjAtJTIwVHJvamFuJTIwLSUyMElQdjYlMjAlM0ElMjA0NDMKdHJvamFuOi8vRGNCYlVlUChHJTVFSFgwQkJzQFsyNjA2OjQ3MDA6MzEwYzo6YWM0MjoyY2E5XTo0NDM/cGF0aD0vdHI1RUV1YmYwWUhUeFR1NTBHJTNGZWQlM0QyNTYwJmhvc3Q9ZnJpZW5kcy1uZXdzLTE4MjEucGFnZXMuZGV2JnR5cGU9d3Mmc2VjdXJpdHk9dGxzJnNuaT1mcklFTmRTLU5ld3MtMTgyMS5wQUdFcy5EZXYmZnA9cmFuZG9taXplZCZhbHBuPWgyLGh0dHAvMS4xIyVGMCU5RiU5MiVBNiUyMDYlMjAtJTIwVHJvamFuJTIwLSUyMElQdjYlMjAlM0ElMjA0NDMKdHJvamFuOi8vRGNCYlVlUChHJTVFSFgwQkJzQDEwNC4yNS4xMDYuMjc6NDQzP3BhdGg9L3RyVHRxTXBGSG03cUhnNVlSVCUzRmVkJTNEMjU2MCZob3N0PWZyaWVuZHMtbmV3cy0xODIxLnBhZ2VzLmRldiZ0eXBlPXdzJnNlY3VyaXR5PXRscyZzbmk9ZnJJZU5kUy1OZVdzLTE4MjEucGFHZVMuREV2JmZwPXJhbmRvbWl6ZWQmYWxwbj1oMixodHRwLzEuMSMlRjAlOUYlOTIlQTYlMjA3JTIwLSUyMFRyb2phbiUyMC0lMjBDbGVhbiUyMElQJTIwJTNBJTIwNDQzCg=='
 # نام جدید برای جایگزینی
new_name = 'ArysNetwork-TelramChannel'
# تغییر نام سرورها و گرفتن خروجی base64
output_base64 = change_server_names_from_base64(input_base64, new_name)

print("خروجی base64 سرورها تغییر یافت:")
print(output_base64)
