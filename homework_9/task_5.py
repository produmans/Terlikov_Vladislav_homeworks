"""
5) Выведите статистику частности букв в кортеже
long_word = ( 'т', 'т', 'а', 'и', 'и', 'а', 'и’,'и', 'и', 'т', 'т', 'а', 'и', 'и','и', 'и', 'и', 'т', 'и’)
"""
long_word = ('т', 'т', 'а', 'и', 'и', 'а', 'и', 'и', 'и', 'т', 'т', 'а', 'и', 'и', 'и', 'и', 'и', 'т', 'и')
print(long_word.count('т'), "- число повторений 'т'")
print(long_word.count('а'), "- число повторений 'а'")
print(long_word.count('и'), "- число повторений 'и'")