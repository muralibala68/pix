from threading import Lock, Thread, current_thread


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
            return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    @classmethod
    def get_instance(cls):
        return Singleton("INS")

    def __init__(self, value) -> None:
        self.value = value

    def get_value(self) -> str:
        return self.value


def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(f"\n{current_thread().name}: Singleton value: {singleton.get_value()}")


def main():
    o1 = Singleton.get_instance()
    o2 = Singleton.get_instance()
    if o1 != o2:
        print("Singleton pattern is broken ;(")

    thread1 = Thread(target=test_singleton, name="T-01", args=("ABC",))
    thread2 = Thread(target=test_singleton, name="T-02", args=("XYZ",))

    thread1.start()
    thread2.start()


if __name__ == "__main__":
    main()
