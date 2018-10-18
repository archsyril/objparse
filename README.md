# objparse
This small library includes the functions `understand` and `understand_with`.

### understand_with(filename|configparser, class, *section_name)
_weapons.ini_
```ini
[Wooden Sword]
min_hit=2
max_hit=10
[Dagger]
min_hit=7
max_hit=9
```
_weapons.py_
```python
class Weapon:
  def __init__(self, *, name, min_hit, max_hit):
    self.name = name
    self.min_hit = int(min_hit)
    self.max_hit = int(max_hit)
weapons = understand_with('weapons.ini', Weapon, 'name')
#section_name is set to name, it will pull the value within the square brackets and use that as the class's name init parameter.
```

### understand(filename, methods...)
_armor.ini_
```ini
[CLASS]
__name__=Armor #Name of the new class
__section__=name #Name of the init keyword to set to the value of the section name
defence=int({})
[Leather Gloves]
defence=5
[Iron Chestplate]
defence=32
```
_armour.py_
```python
def __repr__(self):
  return self.name
Armor, armors = understand('armor.ini', __repr__) # method is added to the class
print(armors[0]) # prints Leather Gloves
```
