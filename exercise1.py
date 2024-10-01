from dataclasses import dataclass
import queue

@dataclass
class Application:
    id: int
    name: str


class Service:
    def __init__(self):
        self.last_id = 0
        self.q = queue.Queue()

    def generate_request(self, name: str) -> int:
        self.q.put(Application(id=self.last_id+1, name=name))
        self.last_id += 1
        return self.last_id

    def process_request(self) -> bool:
        if not self.q.empty():
            item = self.q.get()
            print(f"Користувач {item.name}, номер заявки {item.id}, ви для нас пріоритет номер 1, залишайтесь будь ласка на звʼязку")
            return True
        else:
            print(f"Хух, здається, все на сьогодні, заявок оброблено {self.last_id}.")

        return False

if __name__ == "__main__":
    user_quit = False
    empty_queue = False
    service = Service()
    while not user_quit and not empty_queue:
        lastname = input("Будь ласка, введіть своє прізвище, або quit для виходу")
        user_quit = lastname == 'quit'
        if user_quit:
            continue

        if len(lastname) > 0:
            service.generate_request(lastname)

        empty_queue = not service.process_request()
