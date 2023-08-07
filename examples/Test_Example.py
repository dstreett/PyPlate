from PyPlate import Substance, Container, Recipe, Plate

water = Substance.liquid('H2O', mol_weight=18.0153, density=1)
salt = Substance.solid('NaCl', 58.4428)

recipe = Recipe()
recipe.create_container('halfM salt water', 1000, ((water, '100 mL'), (salt, '50 mmol')))
salt_water_halfM, = recipe.bake()

triethylamine = Substance.liquid("triethylamine", mol_weight=101.19, density=0.726)
triethylamine_halfM = Container.create_stock_solution(triethylamine, 0.5, water, 10)
print(triethylamine_halfM)

salt_water_oneM = Container('oneM salt water', 1000)
recipe2 = Recipe().uses(water, salt, salt_water_oneM)
recipe2.transfer(water, salt_water_oneM, '100 mL')
recipe2.transfer(salt, salt_water_oneM, '100 mmol')
salt_water_oneM, = recipe2.bake()

recipe3 = Recipe().uses(salt_water_halfM, salt_water_oneM)
recipe3.transfer(salt_water_halfM, salt_water_oneM, '5 mL')
salt_water_halfM, salt_water_oneM = recipe3.bake()

plate = Plate('plate', 50_000.0)
recipe4 = Recipe().uses(plate, salt_water_oneM, salt_water_halfM)
recipe4.transfer(salt_water_oneM, plate[:4], '0.5 mL')
recipe4.transfer(salt_water_halfM, plate, '0.5 mL')
plate, salt_water_oneM, salt_water_halfM = recipe4.bake()

recipe5 = Recipe().uses(plate, salt_water_oneM)
for sub_plate, volume in {plate[1, 1]: 1.0, plate['A', 2]: 2.0, plate[1, 3]: 3.0,
                          plate[3, 3]: 7.0, plate['D', 3]: 10.0, plate[5, '3']: 9.0}.items():
    recipe5.transfer(salt_water_oneM, sub_plate, f"{volume} uL")
plate, salt_water_oneM = recipe5.bake()

print(plate.volumes())
print(plate.substances())
print(salt_water_halfM)
print(salt_water_oneM)
