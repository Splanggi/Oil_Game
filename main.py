#hello

print("hello")


def test():
    print("running test")


def fart():
    print("running fart")


def shit():
    print("running shit")


for func in (test, fart, shit):
    try:
        func()
    except Exception as exc:
        print(f"{func.__name__} failed: {exc}")
            
