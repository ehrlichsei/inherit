from animal import Animal, Dog, Cat

# to test parent init partical argument(which is child class) from child
class PetOwner:
    def __init__(self, pet: Animal):
        self.pet = pet

class DogOwner(PetOwner):
    def __init__(self, dog: Dog):
        super().__init__(dog)

class CatOwner(PetOwner):
    def __init__(self, cat: Cat):
        super().__init__(cat) # child pass child class arguments to parent

if __name__ == "__main__":
    # 创建一个狗对象
    my_dog = Dog("Buddy", "Golden Retriever")
    # 使用 DogOwner 初始化
    dog_owner = DogOwner(my_dog)

    # 创建一个猫对象
    my_cat = Cat("Whiskers", "Gray")
    # 使用 CatOwner 初始化
    cat_owner = CatOwner(my_cat)

    # 打印狗主人的狗的名字和品种
    print(f"Dog Owner - Dog Name: {dog_owner.pet.name}, Breed: {dog_owner.pet.breed}")

    # 打印猫主人的猫的名字和颜色
    print(f"Cat Owner - Cat Name: {cat_owner.pet.name}, Color: {cat_owner.pet.color}")
