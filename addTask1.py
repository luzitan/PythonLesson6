"""
Допзадание - вывод в консоль таблицы умножения через генераторы списков.
"""

multiplication_table_half = [[f"{i} * {j} = {i * j}" for i in range(2, 6)] for j in range(2, 10)]
multiplication_table_second_half = [[f"{i} * {j} = {i * j}" for i in range(6, 10)] for j in range(2, 10)]

print("\n".join(["\t".join(el) for el in multiplication_table_half]))
print()
print("\n".join(["\t".join(el) for el in multiplication_table_second_half]))

