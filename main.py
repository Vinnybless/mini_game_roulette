# MINI-GAME SHOWDOWN
import time
from random import randint


def correct_guess(guess):
    print("2")
    time.sleep(0.2)
    print("7")
    time.sleep(0.2)
    print("5")
    time.sleep(0.2)
    print("1")
    time.sleep(0.2)
    print("9")
    time.sleep(0.2)
    print("0")
    time.sleep(0.4)
    print("3")
    time.sleep(0.6)
    print("6")
    time.sleep(0.8)
    print("4")
    time.sleep(1)
    print(f"=== WINNER ===|{guess}|=== WINNER ===")


def wrong_guess():
    print("2")
    time.sleep(0.2)
    print("7")
    time.sleep(0.2)
    print("5")
    time.sleep(0.2)
    print("1")
    time.sleep(0.2)
    print("9")
    time.sleep(0.2)
    print("0")
    time.sleep(0.4)
    print("3")
    time.sleep(0.6)
    print("6")
    time.sleep(0.8)
    print("4")
    time.sleep(1)
    print(f"---|YOU SUCK|---")


def rng(player, cpu, list_of_enemies):
    guess = int(input("Guess a number between 1-5, if you win, all enemies die "))
    answer = randint(1, 5)
    
    while guess not in [1, 2, 3, 4, 5]:
        guess = int(input("Guess a number between 1-5, if you win, all enemies die "))
    
    if guess != answer:
        wrong_guess()
        player.take_dmg()
        time.sleep(1)
        player.display_hp()
    else:
        correct_guess(guess)
        for i in range(len(list_of_enemies)):
            print(f"{list_of_enemies[-1].name} DIES")
            list_of_enemies.pop()
            time.sleep(1)


def death_flip(player, cpu, list_of_enemies):
    print(f"{cpu.name} APPEARS, READY TO FUCK YOU UP")
    time.sleep(1)
    flip = randint(1, 2)
    guess = int(input("1. HEADS  2. TAILS "))
    
    while guess not in [1, 2]:
        guess = int(input("1. HEADS  2. TAILS "))
    
    time.sleep(1)
    if guess == flip:
        print("YOU WIN")
        time.sleep(1)
        cpu.death()
        list_of_enemies.pop()
        time.sleep(1)
        print(f"There are {len(list_of_enemies)} mfs left")
    else:
        print("YOU LOSE")
        player.take_dmg()
        player.display_hp()


def rps(player, cpu, list_of_enemies):
    print(f"{cpu.name} APPEARS, READY TO FUCK YOU UP")
    time.sleep(1)
    cpu_move = randint(0, 2)
    player_move = input("r/p/s ")
    
    while player_move not in ["r", "p", "s"]:
        player_move = input("r/p/s ")
        
    if cpu_move == 0 and player_move == "r":
        print("DRAW")
        rps(player, cpu, list_of_enemies)
    if cpu_move == 1 and player_move == "p":
        print("DRAW")
        rps(player, cpu, list_of_enemies)
    if cpu_move == 2 and player_move == "s":
        print("DRAW")
        rps(player, cpu, list_of_enemies)
    
    if cpu_move == 0 and player_move == "p":
        print(f"{cpu.name} CHOOSES ROCK")
        time.sleep(1)
        print(f"{player.name} CHOOSES PAPER")
        time.sleep(1.5)
        print(f"{player.name} WINS")
        time.sleep(1)
        cpu.death()
        list_of_enemies.pop()
        time.sleep(1)
        print(f"There are {len(list_of_enemies)} mfs left")
    if cpu_move == 0 and player_move == "s":
        print(f"{cpu.name} CHOOSES ROCK")
        time.sleep(1)
        print(f"{player.name} CHOOSES SCISSORS")
        time.sleep(1.5)
        print(f"{cpu.name} WINS")
        time.sleep(1)
        player.take_dmg()
        player.display_hp()
    
    if cpu_move == 1 and player_move == "r":
        print(f"{cpu.name} CHOOSES PAPER")
        time.sleep(1)
        print(f"{player.name} CHOOSES ROCK")
        time.sleep(1.5)
        print(f"{cpu.name} WINS")
        time.sleep(1)
        player.take_dmg()
        player.display_hp()
    if cpu_move == 1 and player_move == "s":
        print(f"{cpu.name} CHOOSES PAPER")
        time.sleep(1)
        print(f"{player.name} CHOOSES SCISSORS")
        time.sleep(1.5)
        print(f"{player.name} WINS")
        time.sleep(1)
        cpu.death()
        list_of_enemies.pop()
        time.sleep(1)
        print(f"There are {len(list_of_enemies)} mfs left")
        
    if cpu_move == 2 and player_move == "r":
        print(f"{cpu.name} CHOOSES SCISSORS")
        time.sleep(1)
        print(f"{player.name} CHOOSES ROCK")
        time.sleep(1.5)
        print(f"{player.name} WINS")
        time.sleep(1)
        cpu.death()
        list_of_enemies.pop()
        time.sleep(1)
        print(f"There are {len(list_of_enemies)} mfs left")
    if cpu_move == 2 and player_move == "p":
        print(f"{cpu.name} CHOOSES SCISSORS")
        time.sleep(1)
        print(f"{player.name} CHOOSES PAPER")
        time.sleep(1.5)
        print(f"{cpu.name} WINS")
        time.sleep(1)
        player.take_dmg()
        player.display_hp()
        
        
def spawn_enemies():
    num = int(input("How many mfs do you want to fight? "))
    dudes = []
    for i in range(0, num):
        dudes.append(Enemies())
    return dudes


class Enemies:
    def __init__(self):
        self.names = ["Kermit The Frog", "Datboi", "Bobby Hill", "The Real Dirty Dan", "Dale Gribble", "Bubbles", "Biggus Dickus"]
        self.name = self.names[randint(0, len(self.names)-1)]
        
    def death(self):
        print(f"{self.name} dies a horrible death")


class Hero:
    def __init__(self):
        self.name = input("Enter name: ")
        self.hp = 100
        
    def choose_game(self, target, list_of_enemies):
        game = input("CHOOSE GAME  1: R/P/S  2: Death Flip  3: RNG ROULETTE ")
        
        while game not in ["1", "2", "3"]:
            game = input("CHOOSE GAME  1: R/P/S  2: Death Flip  3: RNG ROULETTE ")
        
        if game == "1":
            rps(self, target, list_of_enemies)
        if game == "2":
            death_flip(self, target, list_of_enemies)
        if game == "3":
            rng(self, target, list_of_enemies)
        
    def display_hp(self):
        print(f"{self.name} has {self.hp}HP now")
        
    def take_dmg(self):
        self.hp -= 20


def main():
    enemies = spawn_enemies()
    player = Hero()
    
    while player.hp > 0 and len(enemies) > 0:
        player.choose_game(enemies[-1], enemies)
    
    if player.hp <= 0:
        print("YOU DIED")
        
    if len(enemies) == 0:
        print("YOU KILLED EVERY MF")


main()
