import base64

def base64_decode(data, n):
    for i in range(n):
        data = base64.b64decode(data).decode() 
    return data

text = 'Vm0wd2QyUXlVWGxXYTJoV1YwZG9WVll3WkRSV1JsbDNXa1JTVjAxV2JETlhhMUpUVmpGYWRHVkVRbUZTVjJoeVZtMTRTMk15VGtWUmJVWlhWakpvZVZadE1UUlRNazE1Vkd0V1VtSlZXbGhXYWtaTFUxWmFkR05GWkZwV01ERTFWa2QwYzJGV1NuUlZhemxhWWxob1NGUlVSbUZqVms1eFZXeHdWMDFFUlRCV2EyTXhWREpHVjFOWVpGaGlSMmhZV1ZkMGQyUnNXbGRYYlVacVlrWmFlVnBGV2xOVWJGcFZWbXRzVjJKVVFYaFdha3BIVmpGT2RWVnNXbWxTTW1oWFZtMTBWMlF5VWxkalJtaHNVakJhY1ZscmFFTlRiR3QzV2tSU1ZrMXJjRmhWTW5oelZqRmFObEZZYUZabGExcHlWVEJhVDJOc2NFaGpSazVwVmpKb2RsWnRNWGRVTVZWNFYxaG9hbEpXV2xSWmJGWmhZMVpzY21GRlRsTmlSbkJaV2xWak5XRkdXbk5qU0d4WFRWZG9NMVpxUmt0ak1rNUhZVVp3YkdFelFrbFdiWEJIVkRKU1YxVnVUbWhTTW5oWVZXcE9iMkl4V25STlZFSlhZWHBHV0ZVeWRHdFhSbVJJWVVac1dtSkhhRlJXTVZwWFkxWktjbVJHVWxOaVIzY3hWMVJPZDFJeFdYZE5WVlpUWVRGd1dGbHNhRzlsYkZweFUydGFiRlpzV2xaVlYzaHJZVWRGZUdOSGFGaGlSbkJvVlhwS1QxWXhjRWxVYlVaVFRXNW9XVlpYY0U5aU1rbDRWMWhvV0dKRk5WUlVWM2hIVGtaa2NsWnRkRmRpVlhCNVdUQmFjMWR0U2tkWGJXaFhZa1p3V0ZsNlJsZGpNWEJIWVVkc1UwMVZiekZXYWtvd1lqSkZlVkpyWkZSWFIyaFpXVzB4TkZkR1VsaE9WVTVvVW14c00xWXllSGRpUjBwSFYycEdWMDF1YUdoWlZXUkdaVWRPU1dKR1pGZE5NRXBKVjFaU1MxUXlUWGhhU0ZaVllrWktjRlZxUmt0V1ZscEhWV3RLYTAxRVJsTlZSbEYzVUZFOVBRPT18MTE='
data = base64.b64decode(text).decode()
n = int(data.split('|')[1])

d_text = base64_decode(data, n)
print(type(d_text))
