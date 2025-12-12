
class GardenManager:
    count = 0
    def __init__(self):
        self.gardens = ()

    def create_garden(self, name):
        garden = Garden(name)
        self.gardens = self.gardens + (garden, )
        return garden

    class GardenStats:
        def __init__ (self, gardens):
            self.gardens = gardens

        def total_plants(self):
            total = 0 
            for g in self.gardens:
                count = 0
                for p in g.plants:
                    count += 1 
                total = total + count
            return total

        def total_gardens(self):
            total = 0
            for g in self.gardens:
                total += 1  
            return total

    @classmethod
    def  create_garden_network(cls):
        total = 0 
        for g in self.gardens:
            total += 1 
        return total



class Garden:
    def __init__(self, name):
        self.name = name
        self.plants = ()
        self.score = 0

    def add_plant(self, plant):
        self.plants = self.plants + (plant,)
        print(f"Added {plant.name} to {self.name}'s garden")


    def show_plants(self, name):
        print(f"\n=== {self.name}'s Garden Report ===")
        print("Plants in garden:")

        total_plants = 0
        total_growth = 0
        reg_count = 0
        fl_count = 0
        pr_count = 0
        gard_score = 0
        height_check = 0

        for plant in self.plants:
            if type(plant).__name__  == "FloweringPlant":
                print(f"- {plant.name}: {plant.height}cm, {plant.color} flowers (blooming)")
                fl_count += 1
                total_plants += 1
            elif type(plant).__name__  == "PrizeFlower":
                print(f"- {plant.name}: {plant.height}cm, {plant.color} flowers (blooming), Prize points: {plant.points}")
                pr_count += 1
                total_plants += 1
            else:
                 print(f"- {plant.name}: {plant.height}cm")
                reg_count += 1
                total_plants += 1

            gard_score = gard_score + plant.height
            if type(plant).__name__ == "PrizeFlower":
                gard_score = gard_score + plant.height + plant.points

            for plant in self.plants:
                if plant.height > 0:
                    height_check = 1
            print("Plants added:", total_plants, ", Total growth:", total_growth, "cm")
            print("Plant types:", regular_count, "regular,", flowering_count, "flowering,", prize_count, "prize flowers")
            print("Height validation test:", height_ok)
            print("Garden scores -", self.name + ":", garden_score)

    def grow_plants(self, name):
        print(f"\n{self.name} is helping all plants grow...")
        for plant in self.plants:
            growth = 1 
            plant.height += growth
            print(f"{plant.name} grew {growth}cm ")
 
class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = int(height)

class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color

    @classmethod
    def ft_create(cls, n, h, c):
        return cls(n, h, c)
           
class PrizeFlower(FloweringPlant): 
    def __init__(self, name, height, color, points):
        super().__init__(name, height, color)
        self.name = name
        self.points = points;

    @classmethod
    def ft_create(cls, n, h, c, points):
        return cls(n, h, c, points)

class Tree(Plant):
    def __init__(self, name, height):
        super().__init__(name, height)
    
    @classmethod
    def ft_create(cls, n, h):
        return cls(n, h)
      

if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    manager = GardenManager()
    g1 = manager.create_garden("Alice")
    g2 = manager.create_garden("Bob")

    fl1 = FloweringPlant.ft_create("Rose", 15, "red")
    tr1 = Tree.ft_create("Oak", 101)
    pf1 = PrizeFlower.ft_create("Sunflower", 51, "yellow", 10)

    g1.add_plant(tr1)
    g1.add_plant(fl1)
    g1.add_plant(pf1)

    g1.grow_plants("Alice")

    g1.show_plants("Alice")

    stats = GardenManager.GardenStats(manager.gardens)
    print("Total gardens:", stats.total_gardens())
    print("Total plants:", stats.total_plants())

    
    


    


    


