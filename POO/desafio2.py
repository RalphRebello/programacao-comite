# ====================================
#     SISTEMA DE RPG COM HERANÇA
# ====================================

# Classe base Personagem
class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self):
        """Método genérico de ataque. Classes filhas podem sobrescrever."""
        return self.ataque

    def batalhar(self, inimigo):
        print(f"\n⚔️ BATALHA: {self.nome} VS {inimigo.nome}\n")

        turno = 1
        while self.vida > 0 and inimigo.vida > 0:
            print(f"----- TURNO {turno} -----")

            # Ataque do personagem
            dano = self.atacar()
            inimigo.vida -= dano
            print(f"{self.nome} atacou {inimigo.nome} causando {dano} de dano.")
            print(f"Vida de {inimigo.nome}: {max(inimigo.vida, 0)}")

            if inimigo.vida <= 0:
                print(f"\n🏆 {self.nome} venceu a batalha!")
                return self

            # Ataque do inimigo
            dano_inimigo = inimigo.atacar()
            self.vida -= dano_inimigo
            print(f"{inimigo.nome} atacou {self.nome} causando {dano_inimigo} de dano.")
            print(f"Vida de {self.nome}: {max(self.vida, 0)}")

            if self.vida <= 0:
                print(f"\n🏆 {inimigo.nome} venceu a batalha!")
                return inimigo

            turno += 1


# Classe Guerreiro
class Guerreiro(Personagem):
    def atacar(self):
        # Guerreiro tem ataque físico forte
        dano = self.ataque + 5
        return dano


# Classe Mago
class Mago(Personagem):
    def atacar(self):
        # Mago tem ataque mágico variável
        from random import randint
        dano = self.ataque + randint(0, 10)
        return dano


# ====================================
#       SIMULAÇÃO DO SISTEMA
# ====================================
def main():
    # Criando personagens
    guerreiro = Guerreiro("Thor", vida=100, ataque=12)
    mago = Mago("Gandalf", vida=80, ataque=15)

    # Iniciar batalha
    vencedor = mago.batalhar(guerreiro)

    print("\n===============================")
    print(f"🔥 VENCEDOR FINAL: {vencedor.nome}")
    print("===============================\n")

main()