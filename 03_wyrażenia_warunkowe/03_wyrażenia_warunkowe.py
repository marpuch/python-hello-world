import random

niespodzianka = random.randint(0, 100)
if niespodzianka > 50:
    print(f'Liczba {niespodzianka} jest większa niż 50. Przegrałeś!')
else:
    print(f'{niespodzianka} to za mało. Przegrałeś!')