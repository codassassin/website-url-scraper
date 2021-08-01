from colorama import init
import requests


class bColors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'


def banner():
    print(bColors.GREEN + '<<< IP-TRACKER v2.0>>>')
    print(bColors.RED + r'''
  _
 | |
 | |___
 |  _  \   _   _
 | |_)  | | (_) |
  \____/   \__, |
            __/ |
           |___/
                                        _                                                         _
                                       | |                                                       (_)
                  ____     ____     ___| |   ___ _   ______   ______    ___ _   ______   ______   _   _ ____
                 / ___\   /    \   /  _  |  / _ | | /  ____| /  ____|  / _ | | /  ____| /  ____| | | | |   | \
                | |____  |  ()  | |  (_| | | (_|| | \_____ \ \_____ \ | (_|| | \_____ \ \_____ \ | | | |   | |
                 \____/   \____/   \____/   \___|_| |______/ |______/  \___|_| |______/ |______/ |_| |_|   |_|
        ''')


init(autoreset=True)


def auto(nig, url, l, time):
    try:
        obj2 = requests.get(url + "/" + nig, timeout=time, allow_redirects=False)
        by = len(obj2.text)
        if l == 20:
            print(bColors.BLUE + "[" + bColors.YELLOW + "?" + bColors.BLUE + "] - (" + bColors.YELLOW + f"{l}" +
                  bColors.BLUE + ") REQS, this might take a while ")
        if obj2.status_code == 302:
            print(bColors.BLUE + "[" + bColors.GREEN + "+" + bColors.BLUE + f"] Code (" + bColors.YELLOW +
                  f"{obj2.status_code}" + bColors.BLUE + f") | REQS (" + bColors.YELLOW + f"{l}" + bColors.BLUE +
                  f") | BYTES (" + bColors.YELLOW + f"{by}" + bColors.BLUE + f") - " + obj2.url + bColors.GREEN +
                  f" >> " + bColors.YELLOW + f"{obj2.headers['location']}")
            return
        if l == 100 and obj2.status_code == 302:
            print(bColors.BLUE + f"[" + bColors.RED + "!" + bColors.BLUE +
                  "] - 404, might just be just going back to home ")
        if obj2.status_code == 404:
            pass
        else:
            if "admin portal" in obj2.text:
                print(bColors.BLUE + "[" + bColors.GREEN + "+" + bColors.BLUE + "] Code (" + bColors.YELLOW +
                      f"{obj2.status_code}" + bColors.BLUE + ") | REQS (" + bColors.YELLOW + f"{l}" + bColors.BLUE +
                      ") | BYTES (" + bColors.YELLOW + f"{by}" + bColors.BLUE + ") - " + obj2.url + " (" +
                      bColors.GREEN + f"FOUND admin panel" + bColors.BLUE + ")")
                return
            elif "admin" in obj2.text:
                print(bColors.BLUE + "[" + bColors.GREEN + "+" + bColors.BLUE + "] Code (" + bColors.YELLOW +
                      f"{obj2.status_code}" + bColors.BLUE + ") | REQS (" + bColors.YELLOW + f"{l}" + bColors.BLUE +
                      ") | BYTES (" + bColors.YELLOW + f"{by}" + bColors.BLUE + ") - " + obj2.url + " (" +
                      bColors.GREEN + "FOUND admin panel" + bColors.BLUE + ")")
                return
            elif "admin login" in obj2.text:
                print(bColors.BLUE + f"[" + bColors.GREEN + "+" + bColors.BLUE + "] Code (" + bColors.YELLOW +
                      f"{obj2.status_code}" + bColors.BLUE + ") | REQS (" + bColors.YELLOW + f"{l}" + bColors.BLUE +
                      ") | BYTES (" + bColors.YELLOW + f"{by}" + bColors.BLUE + ") - " + obj2.url + " (" + bColors.GREEN
                      + "FOUND admin panel" + bColors.BLUE + f")")
                return
            elif "portal manager" in obj2.text:
                print(bColors.BLUE + "[" + bColors.GREEN + "+" + bColors.BLUE + "] Code (" + bColors.YELLOW +
                      f"{obj2.status_code}" + bColors.BLUE + ") | REQS (" + bColors.YELLOW + f"{l}" + bColors.BLUE +
                      ") | BYTES (" + bColors.YELLOW + f"{by}" + bColors.BLUE + ") - " + obj2.url + " (" + bColors.GREEN
                      + "FOUND admin panel" + bColors.BLUE + f")")
                return

            elif "admin manager" in obj2.text:
                print(bColors.BLUE + "[" + bColors.GREEN + "+" + bColors.BLUE + "] Code (" + bColors.YELLOW +
                      f"{obj2.status_code}" + bColors.BLUE + ") | REQS (" + bColors.YELLOW + f"{l}" + bColors.BLUE +
                      ") | BYTES (" + bColors.YELLOW + f"{by}" + bColors.BLUE + ") - " + obj2.url + " (" + bColors.GREEN
                      + "FOUND admin panel" + bColors.BLUE + ")")
                return
            print(bColors.BLUE + "[" + bColors.GREEN + "+" + bColors.BLUE + "] Code (" + bColors.YELLOW +
                  f"{obj2.status_code}" + bColors.BLUE + ") | REQS (" + bColors.YELLOW + f"{l}" + bColors.BLUE +
                  ") | BYTES (" + bColors.YELLOW + f"{by}" + bColors.BLUE + ") - " + obj2.url + "/")
    except requests.exceptions.ReadTimeout:
        # request timeout
        print(bColors.BLUE + "[" + bColors.RED + "!" + bColors.BLUE + "] - Connection timeout ")
        return


def status(url):
    # checks the status of input url
    try:
        obj = requests.get(url, timeout=5)
        if obj.status_code == 404:
            print(bColors.BLUE + "[" + bColors.RED + "!" + bColors.BLUE +
                  "] - Look's like site is responding with a 404? ")
            exit(0)
        return
    except requests.exceptions.ReadTimeout:
        # request timeout
        print(bColors.BLUE + "[" + bColors.RED + "!" + bColors.BLUE + "] - Look's like site is not responding ")
        return


def searcher(url, time):
    # checks if it is a valid url
    if "https://" in url or "http://" in url:
        pass
    else:
        print(bColors.BLUE + "[" + bColors.RED + "!" + bColors.BLUE + "] - Not a valid url")
        return

    # checks if site responds with a valid status code
    status(url)
    print(bColors.BLUE + "[" + bColors.GREEN + "+" + bColors.BLUE + "] Site - seems to be online")
    with open("pathFinder.txt", 'r') as f:
        buf = f.readlines()
        if buf[-1] == '\n':
            buf = buf[:-1]
        urls = [x[:-1] for x in buf]
        l = 0
        for nig in urls:
            l += 1
            by = len(f.read())
            auto(nig, url, l, time)
        print(bColors.BLUE + "[" + bColors.GREEN + "+" + bColors.BLUE + "] Total Requests - " + str(l))


if __name__ == '__main__':
    url = input(f"url -> ")
    time = int(input("timeouts -> "))

    searcher(url, time)
