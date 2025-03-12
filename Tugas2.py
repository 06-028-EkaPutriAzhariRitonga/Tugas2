import random

class Robot:
    def __init__(self, name, attack, hp):
        self.name = name
        self.attack = attack
        self.hp = hp

    def attack_enemy(self, enemy):
        # Menggunakan attack_accuracy untuk menentukan apakah serangan berhasil
        attack_accuracy = random.randint(1, 100)
        if attack_accuracy <= 80:  # 80% chance to hit
            damage = self.attack
            enemy.hp -= damage
            print(f"{self.name} menyerang {enemy.name} dan memberikan {damage} damage!")
        else:
            print(f"{self.name} menyerang {enemy.name} tetapi meleset!")

    def regen_health(self):
        regen_amount = random.randint(5, 15)
        self.hp += regen_amount
        print(f"{self.name} meregenerasi {regen_amount} HP!")

    def is_alive(self):
        return self.hp > 0

class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.round = 1

    def start_game(self):
        print("Permainan dimulai!")
        while self.robot1.is_alive() and self.robot2.is_alive():
            print(f"\n--- Ronde {self.round} ---")
            self.robot1.attack_enemy(self.robot2)
            if self.robot2.is_alive():
                self.robot2.attack_enemy(self.robot1)
            else:
                print(f"{self.robot2.name} telah kalah!")
                break

            # Mungkin menambahkan regenerasi kesehatan setelah setiap ronde
            self.robot1.regen_health()
            self.robot2.regen_health()

            print(f"{self.robot1.name} HP: {self.robot1.hp}")
            print(f"{self.robot2.name} HP: {self.robot2.hp}")

            self.round += 1

        print("Permainan selesai!")

# Contoh penggunaan
robot1 = Robot("Robot A", attack=20, hp=100)
robot2 = Robot("Robot B", attack=15, hp=100)

game = Game(robot1, robot2)
game.start_game()
