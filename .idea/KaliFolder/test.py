class Worker:
    def __init__(self, kneaden):
        self.kneaden = kneaden
        
    def info(self):
        return f"Я умею мести: {self.kneaden}"
    
    
    
class Mason(Worker):
    def __init__(self, kneaden, stone):
        super().__init__(kneaden)
        self.stone = stone
        
    def info(self):
        return f"{super().info()} а еще я умею {self.stone} класть и делать облицовку домов"
    

class Foreman(Mason):
    def __init__(self, kneaden, stone, calcul):
        super().__init__(kneaden, stone)
        self.calcul = calcul
        
    def info(self):
        return f"{super().info()} по мимо этого я еще провожу {self.calcul} на стройке."
    
    
class Arch(Foreman):
    def __init__(self, kneaden, stone, calcul, design):
        super().__init__(kneaden, stone, calcul)
        self.design = design

    def info(self):
        return f"{super().info()} так еще я умею самое важное это делать {self.design} правильно" 
    
    
mason = Mason("раствор", "кирпичь")
foreman = Foreman("раствор", "кирпичь", "расчеты")
arch = Arch("раствор", "кирпичь", "расчеты", "проекты")   


print(mason.info())
print(foreman.info())
print(arch.info())
    